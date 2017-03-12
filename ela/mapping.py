import folium
import branca
import ela
import pandas as pd
import IPython.display

IPython.display.Image(filename='Legend_Gen.png')

def gen_statewise(state):
    """
    Given a state, it identifies the generation facilities of that
    state and plots them in a color code based on the type of the
    facility using folium as a mapping tool.

    Parameters
    ----------
    state : str

    Returns
    -------
    map

    """

    gen_df = ela.gen_data
    gen_df = gen_df[gen_df.state==state]
    m=folium.Map()
    for index,rows in gen_df.iterrows():
        f = folium.map.FeatureGroup()
        if rows[5]=='Solar':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#f6cc0a')) #YELLOW
            m.add_child(f)
        elif rows[5]=='Hydro':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#2B90F5')) #BLUE
            m.add_child(f)
        elif rows[5]=='Nuclear':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#b9341b')) #RED
            m.add_child(f)
        elif rows[5]=='Biomass':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#55b64e')) #GREEN
            m.add_child(f)
        elif rows[5]=='Oil':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#ff6700')) #ORANGE
            m.add_child(f)
        elif rows[5]=='Coal':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#fe7b89')) #PINK
            m.add_child(f)
        elif rows[5]=='Geothermal':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#d400ee')) #PURPLE
            m.add_child(f)
        elif rows[5]=='Wind':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#b9eeb7')) #MINT
            m.add_child(f)
        elif rows[5]=='Other':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#000000')) #BLACK
            m.add_child(f)
        elif rows[5]=='Gas':
            f.add_child(folium.features.CircleMarker([rows[3],rows[4]],radius=3,fill_color='#283b1a')) #DARKGREEN
            m.add_child(f)

        else:
            pass
    return m

IPython.display.Image(filename='Legend_Stor.png')

def stor_statewise(state):
    """
    Given a state, it identifies the storage facilities of that
    state and plots them in a color code based on the type of the
    facility using folium as a mapping tool.

    Parameters
    ----------
    state : str

    Returns
    -------
    map

    """

    stor_df = ela.stor_data
    stor_df = stor_df[stor_df.state==state]
    m=folium.Map()
    for index,rows in stor_df.iterrows():
        f = folium.map.FeatureGroup()
        if rows[5]=='Electro-mechanical':
            f.add_child(folium.features.CircleMarker([rows[2],rows[3]],radius=3,fill_color='#f6cc0a')) #YELLOW
            m.add_child(f)
        elif rows[5]=='Electro-chemical':
            f.add_child(folium.features.CircleMarker([rows[2],rows[3]],radius=3,fill_color='#2B90F5')) #BLUE
            m.add_child(f)
        elif rows[5]=='Pumped Hydro Storage':
            f.add_child(folium.features.CircleMarker([rows[2],rows[3]],radius=3,fill_color='#b9341b')) #RED
            m.add_child(f)
        elif rows[5]=='Thermal Storage':
            f.add_child(folium.features.CircleMarker([rows[2],rows[3]],radius=3,fill_color='#55b64e')) #GREEN
            m.add_child(f)
    return m
