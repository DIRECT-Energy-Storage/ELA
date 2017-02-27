The primary dataset is the information extracted for United States from **DOE Global Energy Storage Database**.
The data set contains **1629 rows** (representing 1629 U.S. energy storage facilities) and **106 columns**.
The columns of primary importance in the data set are listed below:


* Project name
* Technology
* Technology type
* Rated Power in kW
* Duration
* Longitude and Longitude

The complete data set can be obtained from DOE Global Energy Storage Database at `http://www.energystorageexchange.org`.
It is possible to create subsets for the dataset for unit tests using integer or label based indexing in a python dataframe.

The other dataset is of the **United States EPA** (Environmental Protection Agency).
The complete dataset contains information at the level of power generators, power plants, states, grid regions, and more. Our project will focus on the power plant data and potentially also incorporate the state-level data.  
The power plant dataset contains **8505 rows** (representing 8505 U.S. power plants) and **120 columns**
The columns of primary importance in the data set are listed below:

* Plant name
* Plant Latitude and Longitude
* Plant capacity factor
* Plant annual net generation for oil,coal,gas,nuclear power,hydropower,biomass,wind,solar,geothermal and other fossil fuels

From the plant annual net generation columns, we will extract the primary energy type for each plant to be used in our classification model.  
The link for the above dataset is `https://www.epa.gov/energy/emissions-generation-resource-integrated-database-egrid`
It is possible to generate subsets for the dataset for unit tests by using integer or label based indexing in python dataframe
