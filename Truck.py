'''
Trucks store truck information and packages
'''

import datetime
import csv
from Truck import distance_lookup

# read distance table data for extraction
with open('distance_table.csv', 'r') as file:
    filtered_line = (line.replace('\n', '') for line in file)
    reader = csv.reader(filtered_line)
    distance_table = list(reader)
            
    addresses = [address for address in distance_table[0][2:]]
    distances = [row[1:] for row in distance_table[1:]]
    
# extract distance from addresses
def distance_lookup(truck_current_address, next_address, addresses):
    for x_index, address in enumerate(addresses):
        if address == next_address:
            x_position = x_index
            break

    for y_index, address in enumerate(addresses):
        if address == truck_current_address:
            y_position = y_index
            break
        
    if x_position > y_position:
        return distances[x_position][y_position + 1]
    elif x_position < y_position:
        return distances[y_position][x_position + 1]

class Truck:
    def __init__(self, truck_number, current_address, manifest, start_time):
        self.truck_number = truck_number
        self.current_address = current_address
        self.hub_address = "4001 South 700 East"
        self.loaded_packages = manifest
        self.miles_travelled = 0
        self.packages_delivered = []
        self.speed = 18
        self.start_time = start_time
        self.previous_address = current_address
        
    def find_nearest_neighbor(self):
        # for package in manifest: 
        # if get package address is equal to current address, skip
        # otherwise, loop through and find nearest address
        # when that address is found, return the nearest address
        for package in self.loaded_packages:
            distance_lookup(self.current_address, )
        
    def update_current_address(self, nearest_neighbor):
        None
        
    def update_miles_travelled(self, nearest_neighbor):
        None