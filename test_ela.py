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
    "Test for predicting the closest energy generation facility"
    assert len(ela.get_closest_facility( ela.get_latlon_from_zip(98105),'gen').state)==2,"The state name is a stirng of 2 characters"
    assert type(ela.get_closest_facility( ela.get_latlon_from_zip(98105),'gen').lat)==np.float64,"The latitude data is not precise"
    assert ela.get_closest_facility( ela.get_latlon_from_zip(98105),'gen').capacity_MW> ela.get_closest_facility( ela.get_latlon_from_zip(98034),'gen').production_GWh, "Production is less than capacity"
    return



def test_get_predicted_type():
    "Test for predicting the type of generation and storage facilities"
    assert type(ela.get_predicted_type(ela.get_latlon_from_zip(98105),'stor'))==str ,"Output is not a string"
    assert len(ela.get_predicted_type( ela.get_latlon_from_zip(98033), 'gen'))==3,"The energy resource of the plant is not oil or gas"
    assert len(ela.get_predicted_type( ela.get_latlon_from_zip(98105), 'stor'))==16, "The storage facility is not electro-chemical"
    return


def test_get_state_breakdown():
    "Test for giving out the type of energy generation for particular state in US"
    gen_data = pd.DataFrame(gen_data)
    A=ela.get_state_breakdown(ela.get_state_from_zip(98033),gen_data).HYDRO
    B=ela.get_state_breakdown(ela.get_state_from_zip(98033),gen_data).WIND
    C=ela.get_state_breakdown(ela.get_state_from_zip(98033),gen_data).GAS
    D=ela.get_state_breakdown(ela.get_state_from_zip(98033),gen_data).NUCLEAR
    assert A>B, "Energy generated from wind is more than hydro in WA"
    assert D==0,"Energy is generated from nuclear resourcesin WA"
    assert C<B, "Energy generated from gas is more then wind in WA"
    return


def test_get_energy_breakdwon():
    "Test for giving out data on the type of energy generation resources across US"
    gen_data = pd.DataFrame(gen_data)
    assert ela.get_energy_breakdown(gen_data, location='US').SOLAR==ela.get_energy_breakdown(gen_data, location='US').HYDRO,"energy generated from hydro and solar are different"
    assert len(list(ela.get_energy_breakdown(gen_data, location='US')))==12,"total number of resources considered are incorrect"
    assert ela.get_energy_breakdown(gen_data, location='US').GAS>ela.get_energy_breakdown(gen_data, location='US').COAL,"energy generated from coal is more than gas"
    return



def test_state_type():
    "Test for a state wise break down in the type of energy generation resources in US"
    gen_data = pd.DataFrame(gen_data)
    assert ela.state_type(gen_data).OIL[0]>ela.state_type(gen_data).OIL[1],"energy generated using oil as resource is greater in alabama than arkansas"
    assert ela.state_type(gen_data).HYDRO.WA>ela.state_type(gen_data).SOLAR.WA,"energy geneeration from hydro plants is less than solar plants in WA "
    assert len(ela.state_type(gen_data))==51," incorrect number of states"
    return
