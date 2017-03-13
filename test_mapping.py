import ela
import mapping
import folium
import pandas as pd
import json
import numpy as np
import IPython.display



def test_geojson_to_df():
   assert ela.geojson_to_df(states).polygon[0] == ela.geojson_to_df(states).polygon[3], "Geometry types are not similar for given locations in Alabama and Arizona"


def test_gen_statewise():
    assert len(vars(ela.gen_statewise('WA')))==len(vars(ela.gen_statewise('NY'))), "The number of the items in the dictionaries not equal "
    assert type(ela.gen_statewise('WA'))==type(ela.gen_statewise('WA')), "Error!, type of objects are not similar"
    assert repr(ela.gen_statewise('AL'))== repr(ela.gen_statewise('WA')), "Representations of the objects are not similar"


def test_stor_statewise():
    assert len(vars(ela.gen_statewise('WA')))==len(vars(ela.gen_statewise('NY'))), "The number of the items in the dictionaries not equal "
    assert type(ela.gen_statewise('WA'))==type(ela.gen_statewise('WA')), "Error!, type of objects are not similar"
    assert repr(ela.gen_statewise('AL'))== repr(ela.gen_statewise('WA')), "Representations of the objects are not similar"
