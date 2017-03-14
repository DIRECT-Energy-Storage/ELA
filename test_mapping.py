from ela import *


def test_geojson_to_df():
   assert ela.geojson_to_df(states).polygon[0] == ela.geojson_to_df(states).polygon[3], "Geometry types are not similar for given locations in Alabama and Arizona"
   return


def test_prediction_map():
    assert len(vars(ela.prediction_map(states,'gen')))==len(vars(ela.prediction_map(states, 'stor'))), "The number of the items in both the dictionaries not equal "
    assert type(ela.prediction_map(states,'gen'))==type(ela.prediction_map(states,'stor')), "Error!, type of objects are not similar"
    return



def test_facility_map():
    assert len(vars(ela.facility_map('WA', 'gen')))==len(vars(ela.facility_map('NY', 'stor'))), "The number of the items in the dictionaries not equal "
    assert type(ela.facility_map('WA', 'gen'))==type(ela.facility_map('WA','stor')), "Error!, type of objects are not similar"
    return


def test_state_map():
    assert len(vars(ela.state_map('WA')))==len(vars(ela.state_map('NY'))), "The number of the items in the dictionaries not equal "
    assert type(ela.state_map('AZ'))==type(ela.state_map('AZ')), "Error!, type of objects are not similar"
    return