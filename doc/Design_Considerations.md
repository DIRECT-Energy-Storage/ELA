## Design considerations

### Use cases
1. User enters a zip code and receives data about the locally dominant forms of energy generation and storage
2. User can choose to generate and display maps of energy generation or storage

Components for both use cases: `user_interface`, `knn_generator`, `knn_predictor`, Tkinter (for GUI)  
Components for use case 1 only: `zipcode_selector`, `zipcode_to_latlong`, `facility_lookup`, `state_lookup`  
Components for use case 2 only: `map_selector`, `knn_mapper`, `data_mapper`, Matplotlib basemap toolkit (for visualizing maps)  

### Diagram of primary interactions of components


![Diagram of primary interactions of components](ELA/img/Process_Flow.png)







### Components

#### `user_interface`
What it does: top-level component for both use cases, allows user to look up energy data by zip code or visualize maps of energy data  
Inputs: user interaction including zip code entry and map selection  
Outputs: display information about energy generation and storage in that zip code, or display map  
Interactions: user interaction with `map_selector` or `zipcode_selector` results in display being created/returned, GUI constructed using [Tkinter](https://wiki.python.org/moin/TkInter)


#### `zipcode_selector`
What it does: enables the user to choose a location (zip code) for creating an energy data report  
Inputs: zip code (via GUI)  
Outputs: prints predicted energy generation and storage type for that zip code; locations, types, and capacities of the nearest energy generation and storage facilities; and breakdown of energy generation and storage by type at the state and national level  
Interactions: calls `zipcode_to_latlong`, `knn_generator`, `knn_predictor`, `facility_lookup`, and `state_lookup`

#### `zipcode_to_latlong`
What it does: verifies that the entered zip code is valid and finds the latitude and longitude for that zip code  
Inputs: zip code  
Outputs: raises exception if zip code is not a valid US zip code, otherwise returns latitude and longitude as a tuple    
Interactions: uses zip code database  

#### `facility_lookup`
What it does: finds the nearest energy generation or storage facilities for a given location  
Inputs: latitude and longitude, dataframe (generation or storage facilities)  
Outputs: string or list containing the name, type, location, and capacity of the nearest facility to the input location  
#### `state_lookup`
What it does: finds the energy generation and storage breakdown by type for a given location  
Inputs: latitude and longitude, dataframe (generation or storage state-level breakdown)  
Outputs: dictionary (or similar) containing energy types and percentages  


#### `map_selector`
What it does: enables the user to choose a type of map to display  
Inputs: type of map (via GUI) including data or prediction and generation or storage  
Outputs: displays a map of the specified type  
Interactions: calls either `knn_mapper` or `data_mapper`  

#### `knn_mapper`
What it does: creates a map of the KNN decision boundary for energy generation or storage  
Inputs: dataframe    
Outputs: displays a map with regions colored by predicted energy generation or storage type    
Interactions: calls `knn_generator` on the specified dataset to create the KNN classifier object, calls `knn_predictor` on all points in the map, uses `basemap` to create the actual map  

#### `knn_generator`
What it does: generates a KNN classifier object  
Inputs: dataframe, value of K   
Outputs: KNN classifier object

#### `knn_predictor`
What it does: makes a prediction based on a KNN model  
Inputs: latitude and longitude values, KNN classifier object  
Outputs: type of energy generation or storage (string)  

#### `data_mapper`
What it does: generates a map of the input dataset
Inputs: dataframe  
Outputs: displays a scatter plot on a map with points representing electricity generation or storage facilities, colored by type of energy and sized by capacity  
Interactions: uses `basemap` to create and plot the actual map

#### `matplotlib basemap toolkit`
What it does: draws maps and can plot data in many different forms ([link](http://matplotlib.org/basemap/))



### Notes
* We are still looking into how to build a GUI and how it will interact with other functions
* This will ultimately be structured such that the datasets are loaded and the KNN classifier objects are generated only once, not every time the user does something
* Most functions will be designed to be able to operate on both data sets (energy generation and energy storage)
* Datasets include:
 * energy generation facilities (type, lat, long, name, capacity)
 * energy storage facilities (type, lat, long, name, capacity)
 * energy generation by state (state, capacities of each type)
 * energy storage by state (state, capacities of each type)
 * zip code to latitude-longitude

