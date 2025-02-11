'''
The WGUPS Hub will manage and dispatch the trucks. It will also predetermine the routes 
for the trucks, so they know where to go before dispatch. 
'''

import csv
from HashMap import HashMap
from HashMap import Pair
import datetime
import Truck

# read package data for extraction
with open('package_data.csv', 'r') as file:
    filtered_line = (line.replace('\n', '') for line in file)
    reader = csv.reader(filtered_line)
    extracted_package_data = list(reader)

class WGUPS_Hub:
    def __init__(self):
        self.package_hashmap = HashMap()
        self.time = datetime.timedelta(hours=8, minutes=0)
        
    # gather package information and put it into the package hashmap
    def gather_package_information(self):
        for row in extracted_package_data:
            package_id = str(row[0])
            address = row[1].strip()
            city = row[2].strip()
            zip_code = row[4].strip()
            delivery_deadline = row[5].strip()
            weight = row[6].strip()
            delivery_status = 0
            package_info = [address, city, zip_code, delivery_deadline, weight, delivery_status]
            package_pair = Pair(package_id, package_info)
            self.package_hashmap.put(package_pair.key, package_pair.val)
    
# find nearest neighbor with extracted distance

# when nearest neighbor is found, update truck with new neighbor, have them update current address to the neighbor - truck

# have truck update loaded packages to delivered packages, make sure truck appends timestamp for each package delivered
# also have truck keep track of the distance travelled - truck

# def start_delivery(self, truck):
#     # while loaded packages is not empty, look for the nearest neighbor. When the nearest neighbor is found, 
#     # set current_address to the nearest_neighbor address, take nearest distance and add it to miles travelled. 
#     # deliver packages associated with that address by removing them from loaded packages and adding them to 
#     # delivered packages. Add timestamp to packages. Loop back to beginning
    
#     while not truck.loaded_packages:
#         nearest_neighbor = truck.find_nearest_neighbor()
        
#         # how do the miles travelled get updated from here?
#         truck.update_miles_travelled(nearest_neighbor)
        
#         # how to the packages get delivered from here?
#         truck.deliver_packages(nearest_neighbor)
#         truck.update_address(nearest_neighbor)    
        


# tests
wgups_hub = WGUPS_Hub()
wgups_hub.gather_package_information()
# wgups_hub.package_hashmap.remove("PackageID")
counter = 0
for package in wgups_hub.package_hashmap.map:
    if package == None:
        continue
    counter += 1
    # how to append the time to a package
    wgups_hub.package_hashmap.get(package.key).append(wgups_hub.time)
    # how to print the time from a package
    print(wgups_hub.package_hashmap.get(package.key)[-1])
    print(package)
# print(counter)
