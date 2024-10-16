import pandas as pd
from simpledbf import Dbf5

# read the link dbf to a csv and export
def dbflinks_to_csv(dbf_file, csv_file):
    # Read the DBF file
    dbf = Dbf5(dbf_file)
    df = dbf.to_dataframe()

    #process link information

    # Write to CSV file
    df.to_csv(csv_file, index=False)


def dbfnodes_to_csv(dbf_file, csv_file):
    # Read the DBF file
    dbf = Dbf5(dbf_file)
    df = dbf.to_dataframe()

    # process the node information

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