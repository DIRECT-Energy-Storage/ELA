## Component specification for map visualization

### Use case: generate and display maps of energy generation and storage

### Diagram of interactions of components





### Components

#### `user_interface`
What it does: allows user to look up energy data by zip code or visualize maps of energy data  
Inputs: user interaction including zip code entry and map selection  
Outputs: display information about energy generation and storage in that zip code, or display map
Interactions: user interaction with `map_selector` or `zipcode_selector` results in display being created/returned


#### `map_selector`
What it does: enables the user to choose a type of map to display  
Inputs: type of map (via GUI) including data or prediction and generation or storage  
Outputs: displays a map of the specified type  
Interactions: calls either `knn_mapper` or `data_mapper`  

#### `knn_mapper`
What it does: generates a map of the KNN decision boundary for energy generation or storage  
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
What it does: draws maps and can plot data in many different forms



### Notes


