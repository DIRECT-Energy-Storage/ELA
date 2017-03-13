from ipywidgets import widgets
from IPython.display import display
from IPython.display import clear_output

import ela


def interact_html():
    """
    A wrapper function that display the output as HTML

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    None
    """
    # widgets.Checkbox(
    #     value=False,
    #     description='Storage Data'
    # )

    widgets.HTML(
        value=interact(),
        placeholder='energy breakdown HTML',
        description='energy breakdown HTML',
        disabled=False
    )
    return


def interact():
    """
    A function that interactively ask the user for a zip code and
    display the energy break down of that location

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    None
    """

    # Make a text box
    zipcode = widgets.Text()

    # Display the text box
    display(zipcode)

    # Set some initial text to be displayed in the box
    zipcode.value = 'Enter your zip code here'

    # Define a function to run when someone presses Enter
    # text.value refers to whatever is in the box
    # Here, we are using int(text.value) to change the string to an integer
    #     because ela.get_state_from_zip takes in an integer.

    # On submit (user presses Enter), the text box will call handle_submit
    zipcode.on_submit(handle_submit)
    return


def handle_submit(zipcode):
    """
    Given the zip code in the text box and
    plot the energy break down of that location

    Parameters
    ----------
    zipcode: widget text
    a text contains the input zip code

    Returns
    -------
    None

    Raises
    ------
    None
    """

    clear_output()
    zipcode = int(zipcode.value)
    latlon = ela.get_latlon_from_zip(zipcode)
    predict_gen = ela.get_predicted_type(latlon, 'gen')
    predict_store = ela.get_predicted_type(latlon, 'stor')
    print("Predicted local generation energy type: %s"
          % (predict_gen))
    print("Predicted local storage energy type: %s"
          % (predict_store))
    print("Energy generation breakdown of your state %s:" %
          (ela.get_state_from_zip(zipcode)))
    ela.graph_state_breakdown(ela.get_state_from_zip(zipcode), ela.gen_data)
    print("Energy storage breakdown of your state %s:" %
          (ela.get_state_from_zip(zipcode)))
    ela.graph_state_breakdown(ela.get_state_from_zip(zipcode), ela.stor_data)
    return
