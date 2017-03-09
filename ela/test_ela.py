import pandas as pd
import numpy as np

import ela


def test_get_latlon_from_zip():
    """Tests for checking the latitude-longitude for the entered zip code"""
    assert ela.get_latlon_from_zip(98105)== (47.66377, -122.30118), "Zipcode entered incorrectly!"
    assert type(ela.get_latlon_from_zip(81059))==tuple, "Lat-Lon is not in the expected format"
    assert len(ela.get_latlon_from_zip(81059))==2 , "The length of the tuple is incorrect"
    return


def test_get_state_from_zip():
    """Test for checking the state for the entered zipcode"""
    assert type(ela.get_state_from_zip(11206))==str,"Output is not a string"
    assert ela.get_state_from_zip(98105)=='WA', "Zipcode does not match the state"
    assert len(ela.get_state_from_zip(98105))==2 ,"The length of the string is incorrect"
    return


def test_get_closest_facility():
    test_df = pd.DataFrame()
    return


def test_get_predicted_type():
     assert type(ela.get_predicted_type(ela.get_latlon_from_zip(98105),'stor'))==str ,"Output is not a string"
    return


def test_get_state_breakdown():
    test_df = pd.DataFrame()
    return


def test_get_energy_breakdwon():
    test_df = pd.DataFrame()
    return


def test_split_data_by_state():
    test_df = pd.DataFrame()
    return
