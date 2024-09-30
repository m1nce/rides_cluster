import csv

class CoordsAssign():
    """
    A class to handle coordinate assignment for locations using a CSV file.
    
    Attributes:
        coords (dict): A dictionary to store the location and their coordinates.
    """

    def __init__(self):
        """
        Initializes the CoordsAssign object and reads the coordinates from a CSV file.
        """
        reader = csv.reader(open('rides_cluster/location_coords.csv', 'r'))
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

    def get_coords(self):
        """
        Retrieves the dictionary of location coordinates.
        
        Returns:
            dict: The dictionary containing locations and their coordinates.
        """
        return self.coords
    
    def push_csv(self):
        """
        Writes the updated coordinates to the CSV file.
        """
        with open("location_coords.csv", "w") as f:
            w = csv.writer(f)
            w.writerows(self.coords.items())