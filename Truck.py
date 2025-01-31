'''
Trucks store truck information and package objects
'''
import datetime 

class Truck:
    def __init__(self, truck_number, current_address, addresses, distances):
        self.truck_number = truck_number
        self.hub_address = "4001 South 700 East"
        self.current_address = current_address
        self.next_address = None
        self.miles_travelled = 0.0
        self.loaded_packages = []
        self.packages_delivered = []
        self.addresses_visited = []
        self.speed = 18
        self.addresses = addresses
        self.distances = distances
        
    def __str__(self):
        return f"Truck{self.truck_number}, is currently at {self.current_address}, has travelled {self.miles_travelled}, and has delivered {len({self.packages_delivered})} packages."
    
    # define distance lookup algorithm
    def distance_lookup(self, current_address, next_address):
        for x_index, address in enumerate(self.addresses):
            if address == next_address:
                x_position = x_index
                break
    
        for y_index, address in enumerate(self.addresses):
            if address == current_address:
                y_position = y_index
                break
            
        if x_position > y_position:
            return self.distances[x_position][y_position + 1]
        elif x_position < y_position:
            return self.distances[y_position][x_position + 1]
        
    # define nearest neighbor algorithm
    def find_nearest_neighbor(self):
        nearest_distance = 140.00
        for address in self.addresses:
            if address == self.current_address:
                continue
            distance = self.distance_lookup(self.current_address, address)
            if float(distance) < nearest_distance:
                nearest_distance = float(distance)
                nearest_address = address
        return [nearest_address, nearest_distance]
    
    # move truck to address 
    def update_address_and_deliver_packages(self, time, nearest_distance, nearest_address):
        self.miles_travelled += nearest_distance
        self.current_address = nearest_address
        self.addresses_visited.append(nearest_address)
        for package in self.loaded_packages:
            self.packages_delivered.append([package, self.deliver_time])
            self.loaded_packages.remove(package)
        time_packages_delivered = self.miles_travelled / 18
        time += datetime.timedelta(hours=float(time_packages_delivered))
        
        return time
        
    
    
    
    # return truck to hub   
    def return_to_hub(self, miles_travelled):
        self.current_address = self.hub_address
        self.miles_travelled += miles_travelled