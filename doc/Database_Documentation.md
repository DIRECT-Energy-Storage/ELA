# Datasets for ELA: Energy by Location in America

## Energy generation facilities

This dataset is from the U.S. Environmental Protection Agency (EPA), specifically the Emissions & Generation Resource Integrated Database (eGRID). The original dataset can be found [here](https://www.epa.gov/energy/emissions-generation-resource-integrated-database-egrid) and includes information about U.S. power plants, their emissions, and their energy sources. The data is from 2014 but was released in January 2017; eGRID data from previous years is also available.

Our condensed dataset focuses on the plant-level data from 2014 and on energy generation types. We have removed facilities with no specified energy generation type. This dataset contains 8462 facilities.

For each facility, the dataset includes:
* The state where each facility is located
* The name of the facility
* Latitude and longitude
* Primary energy type (Gas, Oil, Coal, Biomass, Nuclear, Geothermal, Solar, Wind, Hydro, Other)
* Rated capacity in MW
* Actual production in GWh

## Energy storage facilities

This dataset is from the U.S. Department of Energy (DOE), specifically the DOE Global Energy Storage Database. The original database can be found [here](http://www.energystorageexchange.org/projects) and includes information about 1628 energy storage facilities around the world.

Our condensed dataset is limited to facilities in the U.S. and contains 678 facilities.

For each facility, the dataset includes:
* The name of each facility
* Latitude and longitude
* Type of energy technology (`type` is the general category, which includes Electro-mechanical, Pumped Hydro Storage, Electro-chemical, or Thermal Storage; `type2` is a more specific description)
* Power in kW
* Energy storage duration
* Status of the facility
* Primary use case
* City and state where the facility is located

