import pandas as pd
from simpledbf import Dbf5

# read the link dbf to a csv and export
def dbflinks_to_csv(dbf_file, csv_file):
    # Read the DBF file
    dbf = Dbf5(dbf_file)
    df = dbf.to_dataframe()

   # Define the columns you want to keep
    new_order = ['LINKID', 'STREET', 'A', 'B', 'ONEWAY', 'DISTANCE', 'TYPE', 'CFAC']  # Replace with your desired columns

    # Drop columns that are not in the new order
    df = df[new_order]

    # Save the modified DataFrame back to the same links CSV file
    df.to_csv('links.csv', index=False)

    # RENAME
    df = pd.read_csv('links.csv')

    # Step 2: Rename the columns
    # For example, if you want to rename 'old_name1' to 'new_name1' and 'old_name2' to 'new_name2':
    df.rename(columns={'LINKID': 'link_id', 'STREET': 'name', 'A': 'from_node_id', 'B': 'to_node_id', 'ONEWAY': 'directed', 'DISTANCE': 'length', 'TYPE': 'facility_type', 'CFAC': 'capacity'}, inplace=True)

    # Step 3: Save the modified DataFrame back to a CSV file
    df.to_csv('links.csv', index=False)


    # Write to CSV file
    df.to_csv(csv_file, index=False)


def dbfnodes_to_csv(dbf_file, csv_file):
    # Read the DBF file
    dbf = Dbf5(dbf_file)
    df = dbf.to_dataframe()

    # Define the columns you want to keep
    new_order = ['N', 'X', 'Y', 'TAZID']  # Replace with your desired columns

    # Drop columns that are not in the new order
    df = df[new_order]

    # Save the modified DataFrame back to the same node CSV file
    df.to_csv('nodes.csv', index=False)

    # Read the nodes CSV file
    df = pd.read_csv('nodes.csv')

    # Step 2: Rename the columns
    df.rename(columns={'N': 'node_id', 'X': 'x_coord', 'Y': 'y_coord', 'TAZID': 'zone_id'}, inplace=True)


    # Write to CSV file
    df.to_csv(csv_file, index=False)


if __name__ == "__main__":
    
    # read in highway network and write out csv file
    input_dbf = 'links.dbf'  # Replace with your DBF file path
    output_csv = 'links.csv'  # Replace with your desired CSV file path

    dbflinks_to_csv(input_dbf, output_csv)
    print(f"Converted links '{input_dbf}' to '{output_csv}' successfully.")

    # read in nodes and write out CSV file
    inputn_dbf = 'nodes.dbf'  # Replace with your DBF file path
    outputn_csv = 'nodes.csv'  # Replace with your desired CSV file path

    dbfnodes_to_csv(inputn_dbf, outputn_csv)
    print(f"Converted nodes '{inputn_dbf}' to '{outputn_csv}' successfully.")
   
   

