# keep track of the amount of drivers available
import csv 
import datetime
import HashMap
import Package
import old_Truck

# Read csv data files

with open('package_data.csv', 'r') as file:
        filtered_line = (line.replace('\n', '') for line in file)
        reader = csv.reader(filtered_line)
        package_array = list(reader)
            
def package_lookup(package_id):
    indexes = [(package_id, 1), (package_id, 2), (package_id, 4), (package_id, 5), (package_id, 6)]
    package_info = [package_array[row][column] for row, column in indexes]
        
    return package_info

def find_special_instructions(package_id):
    for row in package_array:
        if row[0] == str(package_id):
            special_instructions = row[7]
            break
    return special_instructions
    
# Create the package objects
package_hashmap = HashMap.HashMap()
for i in range(1, len(package_array)):
    package_number = f"{i}"
    package = Package.Package(package_number, package_lookup(i))
    package_values = [package.address, package.city, package.zip, package.delivery_deadline, package.weight]
    package_hashmap.put(package_number, package)
    

      
# Create Truck objects and manifests
truck1 = old_Truck.Truck(1, "4001 South 700 East")
truck2 = old_Truck.Truck(2, "4001 South 700 East")
truck3 = old_Truck.Truck(3, "4001 South 700 East")

truck1_manifest = [1, 7, 8, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 39]
truck2_manifest = [3, 4, 5, 6, 10, 11, 18, 25, 28, 32, 36, 38, 40]
truck3_manifest = [2, 9, 12, 17, 19, 21, 22, 23, 24, 26, 27, 33, 35]
all_addresses = []
for row in package_array:
    all_addresses.append(row[1])
del all_addresses[0]

# Define Main class
class Main:
    while True:
        drivers = 2
        trucks = 3
        total_mileage = 0
        
        print("Welcome to the WGUPS Delivery Service!")
        start_time = datetime.timedelta(hours = int(8), minutes = int(0))
        begin = input("The time becomes 8:00 AM and deliveries start when you type 'begin'. ")
        begin = begin.lower()
        if begin == "begin":
            truck1.load_packages(truck1_manifest, package_hashmap)
            print(f"Packages {truck1.loaded_packages} loaded onto truck {truck1.truck_number}")
        
        truck1.start_delivery(truck1.current_address, all_addresses)
        
        break
    
    
    