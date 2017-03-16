from ela import *


def test_geojson_to_df():
    """
    Test for a function that reads
    a geojson file into a pandas dataframe.
    """

    state_df = ela.geojson_to_df(states)
    assert state_df.polygon[0] == state_df.polygon[3], \
        "Geometry types are not similar for \
            given locations in Alabama and Arizona"
    return


def test_prediction_map():
    """
    Test for a function that creates a Folium map layer
    with features colored by predicted energy type
    """

    map_gen = ela.prediction_map(states, 'gen')
    map_stor = ela.prediction_map(states, 'stor')
    vars_gen = vars(map_gen)
    vars_stor = vars(map_stor)
    assert len(vars_gen) == len(vars_stor), \
        "The number of the items in the dictionaries not equal"
    assert type(map_gen) == type(map_stor), \
        "Error!, type of objects are not similar"
    return


def test_facility_map():
    """
    Test for a function that plots generation facilities
    in one state on a map, colored by energy type.
    """
    map_wa_gen = ela.facility_map('WA', 'gen')
    map_wa_stor = ela.facility_map('WA', 'stor')
    map_ny_stor = ela.facility_map('NY', 'stor')
    assert len(vars(map_wa_gen)) == len(vars(map_ny_stor)), \
        "The number of the items in the dictionaries are not equal "
    assert type(map_wa_gen) == type(map_wa_stor), \
        "Error!, type of objects are not similar"
    return


def test_state_map():
    """
    Test for a function that generates
    blank folium map centered at the input state
    """

    map_wa = ela.state_map('WA')
    map_ny = ela.state_map('NY')
    map_az = ela.state_map('AZ')
    assert len(vars(map_wa)) == len(vars(map_ny)), \
        "The number of the items in the dictionaries are not equal "
    assert type(map_wa) == type(map_az), \
        "Error!, type of objects are not similar"
    return
