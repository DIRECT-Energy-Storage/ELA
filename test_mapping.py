import ela
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
