import pandas as pd
import numpy as np
from scipy.spatial import distance as dist
from sklearn.neighbors import KNeighborsClassifier

# Load in the data
zip_data = pd.read_csv('./ela/data/zipcode_data.csv')
gen_data = pd.read_csv('./ela/data/generation_data.csv')
stor_data = pd.read_csv('./ela/data/storage_data.csv')


# Some imports and data loading may be moved to __init__.py

def get_latlon_from_zip(zipcode):
    """
    Given a zip code, return its latitude and longitude as a tuple.

    Parameters
    ----------
    zipcode : int
        Zipcode to look up.

    Returns
    -------
    (lat, lon) : tuple
        Latitude and longitude values corresponding to the center of the given
        zipcode.

    Raises
    ------
    TypeError : if the input zipcode is not an integer
    ValueError : if the input zipcode is not in the zipcode database

    """

    if not np.issubdtype(type(zipcode), np.integer):
        raise TypeError("Not a numeric zipcode.")
    row = zip_data[zip_data.zip == zipcode]
    if len(row) == 1:
        return row.lat.iloc[0], row.lon.iloc[0]
    else:
        raise ValueError("Zipcode not in database.")


def get_state_from_zip(zipcode):
    """
    Given a zip code, return its state's two-letter abbreviation.

    Parameters
    ----------
    zipcode : int
        Zipcode to look up.

    Returns
    -------
    string:
        Two-letter abbreviation for the state containing the input zipcode.

    Raises
    ------
    TypeError : if the input zipcode is not an integer
    ValueError : if the input zipcode is not in the zipcode database

    """

    if not np.issubdtype(type(zipcode), np.integer):
        raise TypeError("Not a numeric zipcode.")
    row = zip_data[zip_data.zip == zipcode]
    if len(row) == 1:
        return row.state.iloc[0]
    else:
        raise ValueError("Zipcode not in database.")


def get_distances(latlon, facility_data):
    """
    Calculate the distance between a location and all input energy facilities.

    Parameters
    ----------
    latlon : tuple of floats
        Latitude and longitude values for the desired location.
        This is returned by get_latlon_from_zip.

    facility_data : Pandas dataframe
        Dataframe containing, at minimum, latitude and longitude values. These
        values should be in columns entitled 'lat' and 'lon'.
        This can be the imported gen_data or stor_data dataframes.

    Returns
    -------
    None.

    Side Effects
    ------------
    If the input dataframe does not contain a 'zip_dist' column, this column is
    added.
    If the input dataframe has a 'zip_dist' column and this column does not
    contain the distances to the input location, the values in this column are
    modified.

    Notes
    -----
    Distances are in latitude-longitude units.

    """

    row0 = facility_data.iloc[0]
    if 'zip_dist' in facility_data.columns and np.isclose(
            dist.euclidean(latlon, (row0.lat, row0.lon)), row0.zip_dist):
        return

    distances = []
    for index, row in facility_data.iterrows():
        facility_latlon = (row.lat, row.lon)
        distances.append(dist.euclidean(latlon, facility_latlon))
    facility_data['zip_dist'] = distances


def get_closest_facility(latlon, facility_data):
    """
    Find the closest energy facility to the input location, from the facilities
    in the input dataframe.

    Parameters
    ----------
    latlon : tuple of floats
        Latitude and longitude values for the desired location.
        This is returned by get_latlon_from_zip.

    facility_data : Pandas dataframe
        Dataframe containing, at minimum, latitude and longitude values. These
        values should be in columns entitled 'lat' and 'lon'.
        This can be the imported gen_data or stor_data dataframes.

    Returns
    -------
    Pandas series (dataframe row)
        Entire row from the dataframe, containing information about the energy
        facility closest to the input location.

    Side Effects
    ------------
    If the input dataframe does not contain a 'zip_dist' column, this column is
    added.
    If the input dataframe has a 'zip_dist' column and this column does not
    contain the distances to the input location, the values in this column are
    modified.

    Notes
    -----
    Distances are in latitude-longitude units.

    """

    row0 = facility_data.iloc[0]
    if 'zip_dist' not in facility_data.columns or not np.isclose(
            dist.euclidean(latlon, (row0.lat, row0.lon)), row0.zip_dist):
        get_distances(latlon, facility_data)
    return facility_data.iloc[facility_data.zip_dist.idxmin()]


def get_state_breakdown(state, facility_data):
    """
    Given a state and facility data either generation or storage
    and break it down into different storage types.

    Parameters
    ----------
    state: string
        State abbreviation in two letters.
        This can be returned by get_state_from_zip.

    facility_data: Pandas Dataframe
        Dataframe containing, at minimum, latitude and longitude values. These
        values should be in columns entitled 'lat' and 'lon'.
        This can be the imported gen_data or stor_data dataframes.

    Returns
    -------
    Pandas dataframe
        Dataframe contains information about the energy types
        and the ratio of that type in given state.

    Side Effects
    ------------


    Notes
    -----
    Energy types break down are in percentage

    """

    state_data = facility_data.loc[facility_data['state'] == state]
    return get_energy_breakdown(state_data)


def get_energy_breakdown(facility_data):
    """
    Given a facility data either generation or storage
    and break it down into different storage types.

    Parameters
    ----------
    facility_data: Pandas Dataframe
        Dataframe containing, at minimum, latitude and longitude values. These
        values should be in columns entitled 'lat' and 'lon'.
        This can be the imported gen_data or stor_data dataframes.

    Returns
    -------
    Pandas dataframe
        Dataframe contains information about the energy types
        and the ratio of that type in given state.

    Side Effects
    ------------


    Notes
    -----
    Energy types break down are in percentage

    """

    facility_data_type = pd.Series.to_frame(pd.Series.value_counts
                                            (facility_data['type'].
                                                replace('0', 'OTHER')))
    ratio = []
    for i in range(len(facility_data_type)):
        ratio_percent = str(int(100 * facility_data_type.iloc[i][0] /
                                facility_data_type.sum())) + "%"
        ratio.append(ratio_percent)
    facility_data_type['ratio'] = ratio
    return pd.Series.to_frame(facility_data_type['ratio'])


def split_data_by_state(facility_data, facility_type):
    """
    Given a facility data either generation or storage,
    break it down by states and store it in csv.

    Parameters
    ----------
    facility_data: Pandas Dataframe
        Dataframe containing, at minimum, latitude and longitude values. These
        values should be in columns entitled 'lat' and 'lon'.
        This can be the imported gen_data or stor_data dataframes.

    facility_type: string
    A string contains the types of facility, either generation or storage

    Returns
    -------
    None

    Side Effects
    ------------


    Notes
    -----
    Store state energy data in csv.
    """
    states = pd.Series.unique(facility_data['state'])
    for state in states:
        state_data = facility_data.loc[facility_data['state'] == state]
        filepath = './ela/data/' + state + '_' + facility_type + '.csv'
        state_data.to_csv(filepath)
    return None
