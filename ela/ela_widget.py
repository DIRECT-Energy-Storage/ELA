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
