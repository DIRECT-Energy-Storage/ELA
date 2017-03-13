import ela
from ipywidgets import widgets
from IPython.display import display
from IPython.display import clear_output


def interact():
    # Make a text box
    text = widgets.Text()

    # Display the text box
    display(text)

    # Set some initial text to be displayed in the box
    text.value = 'Enter your zipcode here'

    # Define a function to run when someone presses Enter
    # text.value refers to whatever is in the box
    # Here, we are using int(text.value) to change the string to an integer
    #     because ela.get_state_from_zip takes in an integer.
    def handle_submit(sender):
        clear_output()
        zipcode = int(text.value)
        latlon = ela.get_latlon_from_zip(zipcode)
        predict_gen = ela.get_predicted_type(latlon, 'gen')
        predict_store = ela.get_predicted_type(latlon, 'stor')
        print("Your predicted local generation energy type is %s"
              % (predict_gen))
        print("Your predicted local storage energy type is %s"
              % (predict_store))
        ela.graph_state_breakdown(ela.get_state_from_zip(zipcode), ela.gen_data)


    # On submit (user presses Enter), the text box will call handle_submit
    text.on_submit(handle_submit)
    return


def map_widget():
    """
    IPywidgets for generating and displaying Folium maps of energy types.

    """

    state_box = widgets.Dropdown(options=['AK', 'AL', 'AR', 'AS', 'AZ', 'CA',
                                          'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
                                          'HI', 'IA', 'ID', 'IL', 'IN', 'KS',
                                          'KY', 'LA', 'MA', 'MD', 'ME', 'MI',
                                          'MN', 'MO', 'MS', 'MT', 'NC', 'ND',
                                          'NE', 'NH', 'NJ', 'NM', 'NV', 'NY',
                                          'OH', 'OK', 'OR', 'PA', 'PR', 'RI',
                                          'SC', 'SD', 'TN', 'TX', 'UT', 'VA',
                                          'VT', 'WA', 'WI', 'WV', 'WY'],
                                 description='State:',
                                 )

    gen_fac = widgets.Checkbox(layout=widgets.Layout(width='20px'))
    gen_fac_label = widgets.Label(value='Generation facilities')
    gen_fac_box = widgets.HBox([gen_fac, gen_fac_label])

    stor_fac = widgets.Checkbox(layout=widgets.Layout(width='20px'))
    stor_fac_label = widgets.Label(value='Storage facilities')
    stor_fac_box = widgets.HBox([stor_fac, stor_fac_label])

    gen_pred = widgets.Checkbox(layout=widgets.Layout(width='20px'))
    gen_pred_label = widgets.Label(value='Generation prediction')
    gen_pred_box = widgets.HBox([gen_pred, gen_pred_label])

    stor_pred = widgets.Checkbox(layout=widgets.Layout(width='20px'))
    stor_pred_label = widgets.Label(value='Storage prediction')
    stor_pred_box = widgets.HBox([stor_pred, stor_pred_label])

    go_button = widgets.Button(description='Generate map')

    display(state_box)
    display(gen_fac_box, stor_fac_box, gen_pred_box, stor_pred_box)
    display(go_button)

    def generate_map(sender):
        clear_output()
        state = state_box.value
        m = ela.state_map(state)
        if (gen_fac.value is True):
            m.add_child(ela.facility_map(state, 'gen'))
        if (stor_fac.value is True):
            m.add_child(ela.facility_map(state, 'stor'))
        if (gen_pred.value is True):
            m.add_child(ela.prediction_map(ela.counties, 'gen'))
        if (stor_pred.value is True):
            m.add_child(ela.prediction_map(ela.counties, 'stor'))
        display(m)

    go_button.on_click(generate_map)