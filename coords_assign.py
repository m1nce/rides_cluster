"""
This module provides the `CoordsAssign` class for managing location coordinates.

The `CoordsAssign` class allows reading, updating, and saving location coordinates
from a CSV file. It can also integrate these coordinates into a DataFrame. The class
maintains a dictionary of location coordinates and provides methods to update this
dictionary, add coordinates as a DataFrame column, and push changes back to the CSV.

Usage Example:
    coords = CoordsAssign('path/to/location_coords.csv')
    coords.update_coords('New Location', '123.45, 67.89')
    df_with_coords = coords.coords_column('path/to/other_file.csv')
    coords.push_csv()

Attributes:
    None

Todo:
    * Add error handling for missing or malformed CSV files.
    * Implement a method to delete coordinates for a location.
"""

import csv
import pandas as pd

class CoordsAssign():
    """
    A class to handle coordinate assignment for locations using a CSV file.
    
    Attributes:
        coords (dict): A dictionary to store the location and their coordinates.
    """

    def __init__(self, file_path='rides_cluster/location_coords.csv'):
        """
        Initializes the CoordsAssign object and reads the coordinates from a CSV file.
        """
        reader = csv.reader(open(file_path, 'r'))
        self.coords = {}
        for row in reader:
            k, v = row
            self.coords[k] = v

    def update_coords(self, location, coords):
        """
        Updates the coordinates for a given location.
        
        Args:
            location (str): The name of the location.
            coords (str): The coordinates to assign to the location.
        """
        self.coords[location] = coords

    def coords_column(self, file_path):
        """
        Adds a column of coordinates to the DataFrame.
        
        Args:
            file_name (str): The name of the CSV file to read.
        """
        df = pd.read_csv(file_path)
        return df.assign(coordinates=df['location'].map(self.coords))

    def get_coords(self):
        """
        Retrieves the dictionary of location coordinates.
        
        Returns:
            dict: The dictionary containing locations and their coordinates.
        """
        return self.coords
    
    def push_csv(self, file_path='rides_cluster/location_coords.csv'):
        """
        Writes the updated coordinates to the CSV file.
        """
        with open(file_path, "w") as f:
            w = csv.writer(f)
            w.writerows(self.coords.items())