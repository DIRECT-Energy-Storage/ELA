import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Load in the data and set up KNN
ela_dir, ela_filename = os.path.split(__file__)
data_dir = os.path.join(ela_dir, "data")
zip_data = pd.read_csv(os.path.join(data_dir, 'zipcode_data.csv'))
gen_data = pd.read_csv(os.path.join(data_dir, 'generation_data.csv'))
stor_data = pd.read_csv(os.path.join(data_dir, 'storage_data.csv'))
gen_clf = KNeighborsClassifier(n_neighbors=1, weights='distance')
gen_clf.fit(gen_data[['lat', 'lon']], np.ravel(gen_data.type))
stor_clf = KNeighborsClassifier(n_neighbors=1, weights='distance')
stor_clf.fit(stor_data[['lat', 'lon']], np.ravel(stor_data.type))


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


def get_closest_facility(latlon, gen_or_stor):
    """
    Find the closest energy facility to the input location, from the facilities
    in the input classifier.

    Parameters
    ----------
    latlon : tuple of floats
        Latitude and longitude values for the desired location.
        This is returned by get_latlon_from_zip.

    gen_or_stor : string, either 'gen' or 'stor'
        Specify whether to return a generation or storage facility.

    Returns
    -------
    Pandas series (dataframe row)
        Entire row from the dataframe, containing information about the energy
        facility closest to the input location.

    Raises
    ------
    ValueError if gen_or_stor is not either 'gen' or 'stor'.

    Notes
    -----
    Distances are in latitude-longitude units.

    """

    if gen_or_stor == 'gen':
        clf = gen_clf
        data = gen_data
    elif gen_or_stor == 'stor':
        clf = stor_clf
        data = stor_data
    else:
        raise ValueError("Enter either 'gen' or 'stor'.")

    return data.iloc[clf.kneighbors(np.asarray(latlon).reshape(1, 2),
                                    1, False)[0][0]]


def get_predicted_type(latlon, gen_or_stor):
    """
    Get the predicted energy generation or storage type for the input
    location, based on the KNN classifier. (Note that for KNN with K = 1, this
    is the same as the type of the facility returned by get_closest_facility.)

    Parameters
    ----------
    latlon : tuple of floats
        Latitude and longitude values for the desired location.
        This is returned by get_latlon_from_zip.

    gen_or_stor : string, either 'gen' or 'stor'
        Specify whether to return a generation or storage type.

    Returns
    -------
    type : string
        Predicted energy type based on the KNN model.

    Raises
    ------
    ValueError if gen_or_stor is not either 'gen' or 'stor'.

    """

    if gen_or_stor == 'gen':
        clf = gen_clf
        data = gen_data
    elif gen_or_stor == 'stor':
        clf = stor_clf
        data = stor_data
    else:
        raise ValueError("Enter either 'gen' or 'stor'.")

    return clf.predict(np.asarray(latlon).reshape(1, 2))[0]


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
    return get_energy_breakdown(state_data, location=state)


def get_energy_breakdown(facility_data, location='US'):
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
    facility_data_type[location] = ratio
    return pd.Series.to_frame(facility_data_type[location]).transpose()


def state_type(facility_data):
    """
    Given a facility data either generation or storage,
    break it down by states and store it in a csv.

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
    state_types: Pandas Dataframe
        A data frame contains all the state energy break down
        for a given facility data

    Side Effects
    ------------


    Notes
    -----
    """

    states = pd.Series.unique(facility_data['state'])
    state_types = pd.DataFrame()
    for state in states:
        state_info = get_state_breakdown(state, facility_data)
        state_types = state_types.append(state_info).fillna('0%')
    return state_types


def graph_state_breakdown(state, gen_or_stor):
    """
    Given a state and a facility data either generation or storage
    plot the energy breakdown in a pie chart

    Parameters
    ----------
    state: String
        A string contains the state abbreviation

    gen_or_stor : string, either 'gen' or 'stor'
        Specify whether to map generation or storage facilities.

    Returns
    -------

    Side Effects
    ------------


    Notes
    -----
    Plot a pie chart which break down in percentage of each energy type
    """
    type_colors = {'Solar': '#f6cc0a', 'Hydro': '#2B90F5',
                   'Nuclear': '#b9341b',
                   'Biomass': '#55b64e', 'Oil': '#ff6700',
                   'Coal': '#fe7b89',
                   'Gas': '#283b1a', 'Geothermal': '#d400ee',
                   'Wind': '#d9ffd8',
                   'Other': '#000000',
                   'Electro-mechanical': '#f6cc0a',
                   'Electro-chemical': '#2B90F5',
                   'Pumped Hydro Storage': '#b9341b',
                   'Thermal Storage': '#55b64e'}

    if gen_or_stor == 'gen':
        facility_data = gen_data[gen_data.state == state]
    elif gen_or_stor == 'stor':
        facility_data = stor_data[stor_data.state == state]
    else:
        raise ValueError("Enter either 'gen' or 'stor'.")

    breakdown_df = get_state_breakdown(state, facility_data)
    breakdown_df = breakdown_df.loc[:, (breakdown_df != '0%').any(axis=0)]
    label = breakdown_df.columns
    sizes = []
    colors = []
    for i in range(len(breakdown_df.transpose())):
        ratio = int(breakdown_df.transpose().iloc[i][0].split('%')[0])
        sizes.append(ratio)
        colors.append(type_colors[label[i]])
    plt.pie(sizes, labels=label, autopct='%1.1f%%', shadow=True,
            startangle=140, pctdistance=1.2, labeldistance=1.4, colors=colors)
    plt.axis('equal')
    plt.show()
    return None
