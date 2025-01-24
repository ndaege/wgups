# keep track of the amount of drivers available
import csv 
import datetime
import HashMap
import Package

# Read csv data files
package_data = []
with open('package_data.csv', 'r') as file:
        filtered_line = (line.replace('\n', '') for line in file)
        reader = csv.reader(filtered_line)
        package_array = list(reader)
            
def package_lookup(package_id):
    indexes = [(package_id, 1), (package_id, 2), (package_id, 3), (package_id, 4), (package_id, 6)]
    package_info = [package_array[row][column] for row, column in indexes]
        
    return package_id,package_info
    
# Create the package objects
packages = [" "]
for i in range(1, len(package_array)):
    package_object = Package(package_lookup(i))
    packages.append(package_object)
    
    print(packages)
    
    
# Create hashmap and load package objects
    
# Create Truck objects and load packages with a loading algorithm
    
# Start delivering packages using nearest neighbor algorithm

# Define Main class
# class Main:
