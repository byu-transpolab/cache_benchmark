import pandas as pd
from simpledbf import Dbf5
import geopandas as gpd
import os
 
# Function to read a DBF file and convert it to a DataFrame
def read_dbf(dbf_file):
    dbf = Dbf5(dbf_file)
    return dbf.to_dataframe()
 
# Function to save the DataFrame to CSV
def save_to_csv(df, csv_file):
    df.to_csv(csv_file, index=False)

#This will remove any duplicate links.
def remove_duplicate_pairs(df):
    return df.drop_duplicates(subset=['A', 'B'], keep='first')

#This is to be used when the facility_type column uses integers rather than strings.
    #If the values in the facility_type column are integers, use this function to convert them to strings based on your data.
#def factype_to_string(factype_value):
    #if isinstance(factype_value, int):
        #factype_dict = {
            #1: 'Type 1', 
            #2: 'Type 2', 
            #3: 'Type 3', 
        #}
        #return factype_dict.get(factype_value, f'Unknown Type {factype_value}')
    #return 'Invalid FACTYPE'
 
# Function to process and convert DBF links to CSV
def dbflinks_to_csv(dbf_file, shp_file, csv_file):
     # Check if the shapefile exists
    if not os.path.exists(shp_file):
        print(f"Error: The file {shp_file} does not exist.")
        return
    # Read the DBF and shapefile
    df = read_dbf(dbf_file)
    shapefile = gpd.read_file(shp_file)
 

    # Merge geometry based on the from node and to node columns.
    if {'A', 'B'}.issubset(shapefile.columns) and {'A', 'B'}.issubset(df.columns):
        # Select only the 'A', 'B', and 'geometry' columns from the shapefile
        shapefile_geometry = shapefile[['A', 'B', 'geometry']]

        # Merge shapefile GeoDataFrame and DBF DataFrame based on 'A' and 'B'
        merged = pd.merge(df, shapefile_geometry, on=['A', 'B'], how='left')

        # Remove duplicates
        merged = remove_duplicate_pairs(merged)

        # Log after duplicates are removed
        print(f"After duplicate removal, {len(merged)} rows remain.")

    #This is to be used when the facility_type column uses integers rather than strings.
        # Ensure the 'FACTYPE' column is in integer format before applying conversion
        #merged['FACTYPE'] = merged['FACTYPE'].astype('Int64', errors='ignore')

        # Apply the factype_to_string function to the 'FACTYPE' column
        #merged['FACTYPE'] = merged['FACTYPE'].apply(factype_to_string) 


        # Rename columns and reorder them
        merged.rename(columns={
            'LINKID': 'link_id',
            'STREET': 'name',
            'A': 'from_node_id',
            'B': 'to_node_id',
            'DISTANCE': 'length',
            'UDOT_FC': 'facility_type',
            'ONEWAY': 'lanes',
            'BIKE_FAC': 'bike_facility'
        }, inplace=True)
 
         # List the columns to keep (those that are renamed)
        columns_to_keep = ['link_id', 'name', 'from_node_id', 'to_node_id', 
                            'length', 'facility_type', 
                           'bike_facility', 'geometry']
        
        # Drop columns that are not in the 'columns_to_keep' list
        merged = merged[columns_to_keep]

        # Save the merged DataFrame to CSV
        save_to_csv(merged, csv_file)
    else:
        print("Error: 'ID' column is missing from either the shapefile or DBF data.")

#Only if zone_id column previously existed in the nodes file
def dbfnodes_to_csv(dbf_file, csv_file):
    # Read the DBF file
    dbf = Dbf5(dbf_file)
    df = dbf.to_dataframe()

    # Define the columns you want to keep
    new_order = ['N', 'X', 'Y', 'TAZID']  # Replace with your desired columns

    # Drop columns that are not in the new order
    df = df[new_order]
    df.rename(columns={'N': 'node_id', 'X': 'x_coord', 'Y': 'y_coord', 'TAZID': 'zone_id'}, inplace=True)


    # Write to CSV file
    df.to_csv(csv_file, index=False)

#Alternative: Use if the zone_id column does not exist in you nodes file
# Function to process and convert DBF nodes to CSV
#def dbfnodes_to_csv(dbf_file, csv_file):
   # df = read_dbf(dbf_file)
    # Rename columns for clarity
    #df.rename(columns={'Old_name': 'New_name'}, inplace=True)
   
    # Save to CSV
    #save_to_csv(df, csv_file)


# This is only if the zone_id column does not exist in your nodes files
# Function to merge zones with nodes data
#def merge_zones_with_nodes(nodes_csv, zones_csv, output_csv):
    #nodes_df = pd.read_csv(nodes_csv)
    #zones_df = pd.read_csv(zones_csv)
   
    #Merge based on 'ID' column and save the result
   #merged_df = pd.merge(nodes_df, zones_df[['ID', 'Z']], on='ID', how='left')
    #save_to_csv(merged_df, output_csv)



if __name__ == "__main__":
    try:
        # Convert links DBF to CSV
        dbflinks_to_csv('hwy/src/links.dbf', 'hwy/src/links_shape.shp', 'hwy/link.csv')
        print("Converted links 'links.dbf' to 'links.csv' successfully.")
       
        # Convert nodes DBF to CSV
        dbfnodes_to_csv('hwy/src/nodes.dbf', 'hwy/node.csv')
        print("Converted nodes 'nodes.dbf' to 'nodes.csv' successfully.")

        #Alternative: Use if the zone_id column does not exist in you nodes file
        # Merge zones with nodes
        #merge_zones_with_nodes('nodes_from_cube.csv', 'zones.csv', 'nodes.csv')
        #print("Merged zones data into 'nodes_from_cube.csv' and saved to 'nodes.csv'.")

    except Exception as e:
        print(f"An error occurred: {e}")
   
   

