# Energy by Location in America (ELA)


[![Build Status](https://travis-ci.org/DIRECT-Energy-Storage/ELA.svg?branch=master)](https://travis-ci.org/DIRECT-Energy-Storage/ELA)
___
ELA is a tool for learning about the distribution of U.S. energy generation and storage facilities by energy type, designed to run in a Jupyter notebook. The user can enter a U.S. zip code to access information about energy facilities in their area, as well as visualizing the distribution and type of energy facilities in any U.S. state. ELA uses a K-nearest neighbors (KNN) classification model to investigate the distribution of energy facilities in the U.S.

---

### Features
#### List of things ELA can do
##### Zipcode lookup
* The user can enter a zip code to find the closest energy generation and storage facilities, predicted energy types based on nearby facilities, and compare the distribution of energy facilities in their state and in the U.S.

##### Map Visualization
* The user can visualize energy generation or storage facilities in any state, or the predicted energy generation or storage types across the entire U.S. based on the KNN model.


Sample Jupyter notebooks demonstrating ELA's [user interface](https://github.com/DIRECT-Energy-Storage/ELA/blob/master/examples/demo_ELA_interface.ipynb) and [selected functions](https://github.com/DIRECT-Energy-Storage/ELA/blob/master/examples/demo_ELA_functions.ipynb) are available.

---

### Data

ELA uses the U.S. EPA's eGRID dataset for energy generation facilities and the U.S. Department of Energy's data for energy storage facilities. More information about both datasets can be found [here](https://github.com/UWDIRECT/cohort1-datasets/blob/master/ELA_EnergyByLocationInAmerica/data.md).

---
### Installation and Compatibility

ELA is designed to be used in a Jupyter notebook, and also requires the following:

* [IPython](http://ipython.org)
* [Matplotlib](http://matplotlib.org)
* [Scipy](https://scipy.org)
* [Numpy](http://www.numpy.org)
* [Scikit-learn](http://scikit-learn.org/stable/)
* [Pandas](http://pandas.pydata.org)
* [Folium](https://github.com/python-visualization/folium)
* [Ipywidgets](https://github.com/ipython/ipywidgets)

 __The visualization component of ELA does not work in Jupyter notebooks in Internet Explorer.__

---

#### MIT License
We chose MIT License because it is a short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.
