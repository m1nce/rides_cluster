import csv

class CoordsAssign():

    def __init__(self):
        reader = csv.reader(open('rides_cluster/location_coords.csv', 'r'))
        self.coords = {}
        for row in reader:
            k, v = row
            self.coords[k] = v

    def update_coords(self, location, coords):
        self.coords[location] = coords

    def get_coords(self):
        return self.coords
    
    def push_csv(self):
        with open("location_coords.csv", "w") as f:
            w = csv.writer(f)
            w.writerows(self.coords.items())
    
coords = CoordsAssign()
print(coords.get_coords())