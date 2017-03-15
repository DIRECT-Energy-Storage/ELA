# Energy by Location in America (ELA)


[![Build Status](https://travis-ci.org/DIRECT-Energy-Storage/ELA.svg?branch=master)](https://travis-ci.org/DIRECT-Energy-Storage/ELA)
___
ELA is a tool for learning about the distribution of U.S. energy generation and storage facilities by energy type. The user can enter a U.S. zip code to access information about energy facilities in their area, as well as visualizing the distribution and type of energy facilities in any U.S. state.

---

### Features
#### List of things ELA can do
* By giving a two letter abbreviation for each state in the United States of America, `ela` can visualize the energy generation facilities for that state.
* By giving a two letter abbreviation for each state in the United States of America, `ela` can visualize the energy storage facilities for that state.


An example Jupyter notebook illustrating these features is available here. (will link to demo notebook when finished)

---

### Data

ELA uses the U.S. EPA's eGRID dataset for energy generation facilities and the U.S. Department of Energy's ... for energy storage facilities. More information about both datasets can be found here. (will link to the data documentation file)

---
### Installation and Compatibility

ELA is designed to be used in a Jupyter notebook, and also requires the following:

* [Numpy](http://www.numpy.org)
* [Scikit-learn](http://scikit-learn.org/stable/)
* [Pandas](http://pandas.pydata.org)
* [Folium](https://github.com/python-visualization/folium)
* [Ipywidgets](https://github.com/ipython/ipywidgets)

 __The visualization component of ELA does not work in Jupyter notebooks in Internet Explorer.__

---

#### MIT License
We chose MIT License because it is a short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.
