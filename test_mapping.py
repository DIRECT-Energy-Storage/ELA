import ela
<<<<<<< HEAD
from ela import *
import ela.mapping as mapping
import folium
import pandas as pd
import json
import numpy as np
import IPython.display



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
=======
import ela.mapping as mapping



# def test_geojson_to_df():
#     gen_data = ela.gen_data
#     assert mapping.geojson_to_df(gen_data.to_json()).polygon[0] == mapping.geojson_to_df(gen_data).polygon[3], "Geometry types are not similar for given locations in Alabama and Arizona"


# def test_gen_statewise():
#     assert len(vars(ela.gen_statewise('WA')))==len(vars(ela.gen_statewise('NY'))), "The number of the items in the dictionaries not equal "
#     assert type(ela.gen_statewise('WA'))==type(ela.gen_statewise('WA')), "Error!, type of objects are not similar"
#     assert repr(ela.gen_statewise('AL'))== repr(ela.gen_statewise('WA')), "Representations of the objects are not similar"


# def test_stor_statewise():
#     assert len(vars(ela.gen_statewise('WA')))==len(vars(ela.gen_statewise('NY'))), "The number of the items in the dictionaries not equal "
#     assert type(ela.gen_statewise('WA'))==type(ela.gen_statewise('WA')), "Error!, type of objects are not similar"
#     assert repr(ela.gen_statewise('AL'))== repr(ela.gen_statewise('WA')), "Representations of the objects are not similar"
>>>>>>> 29361885547a59c2d5a83151c9f4de14150c3a35
