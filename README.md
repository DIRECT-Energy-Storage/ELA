# Energy by Location in America (ELA)

[![Build Status](https://travis-ci.org/DIRECT-Energy-Storage/ELA.svg?branch=master)](https://travis-ci.org/DIRECT-Energy-Storage/ELA)

ELA is a tool for learning about the distribution of U.S. energy generation and storage facilities by energy type. The user can enter a U.S. zip code to access information about energy facilities in their area, as well as visualizing the distribution and type of energy facilities in any U.S. state.

---

### Features
#### List of things ELA can do
##### Zipcode lookup
* The user can enter a zip code to find the closest energy generation and storage facilities, predicted energy types based on nearby facilities, and compare the distribution of energy facilities in their state and in the U.S.

##### Map Visualization
* The user can visualize energy generation or storage facilities in any state, or the predicted energy generation or storage types across the entire U.S. based on the KNN model.



An example Jupyter notebook illustrating these features is available here. (will link to demo notebook when finished)

---

### Data

ELA uses the U.S. EPA's eGRID dataset for energy generation facilities and the U.S. Department of Energy's data for energy storage facilities. More information about both datasets can be found here. (will link to the data documentation file)

---
### Installation and Compatibility

ELA is designed to be used in a Jupyter notebook, and also requires the following:

<<<<<<< HEAD
* pandas==0.19.2  
* scikit-learn==0.18.1  
* matplotlib==1.5.3  
* numpy==1.12.0  
* scipy==0.19.0  
* folium==0.3.0  
* ipywidgets==6.0  
* IPython==5.3.0
* json==2.0.9
* 
The visualization component of ELA does not work in Jupyter notebooks in Internet Explorer.
=======
* [Numpy](http://www.numpy.org)
* [Scikit-learn](http://scikit-learn.org/stable/)
* [Pandas](http://pandas.pydata.org)
* [Folium](https://github.com/python-visualization/folium)
* [Ipywidgets](https://github.com/ipython/ipywidgets)

 __The visualization component of ELA does not work in Jupyter notebooks in Internet Explorer.__
>>>>>>> e1d7482c771d649310a316f394b91fd4db6855be

---

#### MIT License
We chose MIT License because it is a short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.
