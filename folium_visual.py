"""
This module provides the `FoliumVisual` class for visualizing locations on a map using Folium.

The `FoliumVisual` class allows loading location data from a CSV file, optionally assigning coordinates
using the `CoordsAssign` class if not already present, and creating an interactive map using Folium.
The class provides methods to generate the map and save it as an HTML file.

Usage Example:
    visual = FoliumVisual('path/to/data.csv', coord_path='path/to/location_coords.csv')
    map_object = visual.create_map()
    visual.save_map(map_object, 'output_map.html')

Attributes:
    None

Todo:
    * Add error handling for invalid coordinate formats.
"""

import folium
import pandas as pd
import coords_assign

class FoliumVisual:
    """
    A class to create and visualize a map using location data with Folium.
    
    Attributes:
        data (pd.DataFrame): DataFrame containing location data.
        location (list): Default center coordinates for the map.
        zoom_start (int): Initial zoom level for the map.
        coords (dict): A dictionary of coordinates for locations.
    """

    def __init__(self, file_path, location=[32.8788, -117.2359], zoom_start=14, coord_path='location_coords.csv'):
        """
        Initializes the FoliumVisual object and reads the location data from a CSV file.

        Args:
            file_path (str): The path to the CSV file containing location data.
            location (list, optional): The default center coordinates for the map. Defaults to [32.8788, -117.2359] (UCSD).
            zoom_start (int, optional): The initial zoom level for the map. Defaults to 14.
            coord_path (str, optional): The path to the CSV file containing coordinates. Defaults to 'location_coords.csv'.
        """
        self.data = pd.read_csv(file_path)
        self.location = location
        self.zoom_start = zoom_start

        # Initialize the CoordsAssign object to read location coordinates
        coords = coords_assign.CoordsAssign(coord_path)
        self.coords = coords.get_coords()

        # Check if 'coord' column exists in the data
        if 'coord' not in '\t'.join(self.data.columns):
            print('No coordinates found in the data file. Attempting to assign coordinates from the CSV file...')
            self.data = coords.coords_column(file_path)

    def create_map(self):
        """
        Creates a Folium map with markers for each location in the data.

        Returns:
            folium.Map: A Folium map object with location markers.
        """
        # Create a map with default location and zoom level
        map = folium.Map(location=self.location, zoom_start=self.zoom_start)
        for _, row in self.data.iterrows():
            location_name = row['location'].lower()

            # Check if the location has coordinates assigned and adds a marker
            if location_name in self.coords:
                coordinates = eval(self.coords[location_name])
                folium.Marker(location=coordinates, popup=row['name'], tooltip=location_name.title()).add_to(map)
        return map

    def save_map(self, map, file_name):
        """
        Saves the generated Folium map to an HTML file.

        Args:
            map_object (folium.Map): The Folium map object to be saved.
            file_name (str): The name of the file to save the map as.
        """
        map.save(file_name)

