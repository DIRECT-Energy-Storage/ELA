import ela

import folium
import pandas as pd
import json
import numpy as np

# Set up color scheme.
colors = {'Solar': '#f6cc0a', 'Hydro': '#2B90F5', 'Nuclear': '#b9341b',
          'Biomass': '#55b64e', 'Oil': '#ff6700', 'Coal': '#fe7b89',
          'Gas': '#ffffff', 'Geothermal': '#d400ee', 'Wind': '#d9ffd8',
          'Other': '#ffffff',
          'Electro-mechanical': '#f6cc0a', 'Electro-chemical': '#2B90F5',
          'Pumped Hydro Storage': '#b9341b', 'Thermal Storage': '#55b64e'}

# Load state and county boundaries.
with open('us-states.json') as f:
    states = json.load(f)
with open('us-counties.json') as f:
    counties = json.load(f)


def geojson_to_df(geoj):
    """
    Read a geojson file into a pandas dataframe.

    Parameters
    ----------
    geoj : GeoJSON object (loaded from us-states.json or us-counties.json)

    Returns
    -------
    Pandas dataframe :
        containing columns for the feature ID, geometry type (Polygon or
        MultiPolygon) and geometry (coordinates)

    """
    geometry, geo_id, poly = [], [], []
    for feature in geoj['features']:
        geometry.append(feature['geometry']['coordinates'])
        geo_id.append(feature['id'])
        poly.append(feature['geometry']['type'])
    return pd.DataFrame(np.c_[geo_id, geometry, poly],
                        columns=['id', 'geometry', 'polygon'])


def geojson_centers(df):
    """
    Find the average coordinates of geojson features in a dataframe.

    Parameters
    ----------
    df : Pandas dataframe
        dataframe containing the output of geojson_to_df, with columns
        including 'polygon' and 'geometry'

    Returns
    -------
    None

    Side Effects
    ------------
    Adds a column 'centers' to the input dataframe, containing (latitude,
    longitude) tuples representing the average coordinates of all vertices
    in the GeoJSON geometry specification for each feature

    """
    centers = []
    for i in range(0, len(df)):
        row = df.iloc[i]
        poly = row.polygon

        if poly == 'MultiPolygon':
            geom = []
            for poly in row.geometry:
                geom = geom + poly[0]
        else:
            geom = row.geometry[0]

        lon, lat = list(zip(*geom))
        c_lon = (np.asarray(lon)).mean()
        c_lat = (np.asarray(lat)).mean()
        centers.append((c_lat, c_lon))
    df['centers'] = centers


def geojson_predict(df):
    """
    Predict generation and storage types for all features in a dataframe.

    Parameters
    ----------
    df : Pandas dataframe
        dataframe containing geographic features, with a column 'centers'
        which has (latitude, longitude) tuples
        This should be the output of geojson_to_df after modification by
        geojson_centers.

    Returns
    -------
    None

    Side Effects
    ------------
    Adds two columns 'pred_gen' and 'pred_stor' to the input dataframe,
    containing the predicted energy generation and storage types for each
    feature, based on ela.get_predicted_type() for the latitude and longitude
    in the 'centers' column.

    """

    gens = []
    stors = []
    for index, row in df.iterrows():
        latlon = row.centers
        gens.append(ela.get_predicted_type(latlon, 'gen'))
        stors.append(ela.get_predicted_type(latlon, 'stor'))
    df['pred_gen'] = gens
    df['pred_stor'] = stors


def pred_gen_to_colors(df):
    """
    Generate a dictionary mapping geographic feature ID to energy type color.

    Parameters
    ----------
    df : Pandas dataframe
        Dataframe containing geographic features in an 'id' column and
        predicted energy generation types in a 'pred_gen' column.

    Returns
    -------
    dictionary :
        keys : strings representing feature IDs from input dataframe
        values : strings representing colors (as hex codes) corresponding to
            the predicted energy generation type for each feature

    """
    return {df.iloc[i].id: colors[df.iloc[i].pred_gen] for i in df.index}


def pred_stor_to_colors(df):
    """
    Generate a dictionary mapping geographic feature ID to energy type color.

    Parameters
    ----------
    df : Pandas dataframe
        Dataframe containing geographic features in an 'id' column and
        predicted energy storage types in a 'pred_stor' column.

    Returns
    -------
    dictionary :
        keys : strings representing feature IDs from input dataframe
        values : strings representing colors (as hex codes) corresponding to
            the predicted energy storage type for each feature

    """
    return {df.iloc[i].id: colors[df.iloc[i].pred_stor] for i in df.index}


def pred_layer(geoj, gen_or_stor):
    """
    Create a Folium map layer with features colored by predicted energy type.

    Parameters
    ----------
    geoj : GeoJSON object
        Contains state or county boundaries

    gen_or_stor : string, either 'gen' or 'stor'
        Specify whether to map predicted generation or storage types.

    Returns
    -------
    Folium GeoJson layer
        Map layer showing the input geographic features colored according to
        their predicted energy types

    """

    df = geojson_to_df(geoj)
    geojson_centers(df)
    geojson_predict(df)

    if gen_or_stor == 'gen':
        colors = pred_gen_to_colors(df)
    elif gen_or_stor == 'stor':
        colors = pred_stor_to_colors(df)
    else:
        raise ValueError("Enter either 'gen' or 'stor'.")

    return folium.GeoJson(geoj,
                          style_function=lambda feature: {
                              'fillColor': colors[feature['id']],
                              'weight': 0})
