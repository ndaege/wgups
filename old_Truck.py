'''
Trucks store truck information and package objects
'''
import datetime

class Truck:
    def __init__(self, truck_number, current_address, manifest):
        self.truck_number = truck_number
        self.hub_address = "4001 South 700 East"
        self.current_address = current_address
        self.next_address = None
        self.miles_travelled = 0.0
        self.loaded_packages = manifest 
        self.packages_delivered = []
        self.addresses_visited = []
        self.speed = 18
        
    def __str__(self):
        return f"Truck{self.truck_number}, is currently at {self.current_address}, has travelled {self.miles_travelled}, and has delivered {len({self.packages_delivered})} packages."
    
    # move truck to address 
    def update_address_and_deliver_packages(self, time, nearest_distance, nearest_address):
        None
    
    def set_manifest(self, manifest):
        self.loaded_packages = manifest
    
    # return truck to hub   
    def return_to_hub(self, miles_travelled):
        self.current_address = self.hub_address
        self.miles_travelled += miles_travelled