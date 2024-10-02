import pandas as pd
import numpy as np

class Cluster():

    def __init__(self, riders_file):
        self.riders = pd.read_csv(riders_file)
        self.riders = self.riders.assign(cluster=np.nan)

        if 'coord' not in '\t'.join(self.riders.columns):
            print('No coordinates found in the riders file. Attempting to assign coordinates...')
            self.riders = self.coords_column(riders_file)

    def preliminary_cluster(self):
        """
        Assigns riders to clusters based on their coordinates.

        Returns:
            pd.DataFrame: DataFrame with riders and their assigned clusters.
        """
        location_counts = self.riders['location'].value_counts()
        location_counts = location_counts[location_counts >= 4]

        riders_copy = self.riders.copy()
        riders_copy = riders_copy[riders_copy['location'].isin(location_counts.index.tolist())]
        