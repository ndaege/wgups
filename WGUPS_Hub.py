'''
The WGUPS Hub will manage and dispatch the trucks. It will also predetermine the routes 
for the trucks, so they know where to go before dispatch. 
'''

import csv
from HashMap import HashMap
from HashMap import Pair
from Truck import Truck
from Package import Package
import datetime
        
class WGUPS_Hub:
    def __init__(self):
        self.package_hashmap = HashMap()
        # loop through packages in package hashmap instead
        self.addresses = []
        self.distances = []
        self.package_array = []
        self.truck1_manifest = [1, 7, 8, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 39]
        self.truck2_manifest = [3, 4, 5, 6, 10, 11, 18, 25, 28, 32, 36, 38, 40]
        self.truck3_manifest = [2, 9, 12, 17, 19, 21, 22, 23, 24, 26, 27, 33, 35]
        # might have to remove the addresses and distances from the Truck objects
        self.truck1 = Truck(1, "4001 South 700 East", self.addresses, self.distances)
        self.truck2 = Truck(2, "4001 South 700 East", self.addresses, self.distances)
        self.truck3 = Truck(3, "4001 South 700 East", self.addresses, self.distances)
        self.time = datetime.timedelta(hours=(8), minutes=(0))
        
        # hub is passing empty addresses to objects
        # loop through manifest, check for what has been delivered(remove what has been delivered), 
        # for packages not delivered, calc distance
        
        for key in self.truck1_manifest:
            if key in self.package_hashmap.map:
                print(self.package_hashmap.get(key.key))
        
    
    # open and read file containing package data    
    def read_package_data(self):    
        with open('package_data.csv', 'r') as file:
            filtered_line = (line.replace('\n', '') for line in file)
            reader = csv.reader(filtered_line)
            self.package_array = list(reader)
            
            return self.package_array[1:]
            
    # open and read file containing distance data
    def read_distance_data(self):
        with open('distance_table.csv', 'r') as file:
            filtered_line = (line.replace('\n', '') for line in file)
            reader = csv.reader(filtered_line)
            distance_table = list(reader)
            
            self.addresses = [address for address in distance_table[0][2:]]
            self.distances = [row[1:] for row in distance_table[1:]]
            
            return self.addresses, self.distances
        
        
    # instantiate packages
    def instantiate_packages(self):
        for row in self.read_package_data():
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
            
    def all_packages_delivered(self):
        for key in self.package_hashmap.map:
            if key is None:
                continue
            # make sure package status is added to the hashmap
            if key and self.package_hashmap.get(key.key)[5] < 2:
                return False
        return True
    
    def change_delivery_status(self, delivery_status):
        for truck in [self.truck1, self.truck2, self.truck3]:
            for package in truck.loaded_packages:
                package = self.package_hashmap.get(str(package))
                
                if package is not None:
                    package[5] = delivery_status
    # main loop
    def start_delivery_program(self):
        # Greet user
        print("________________________________________________________________________________________________")
        print('''
 ____      ____   ______  _____  _____  _______    ______   
|_  _|    |_  _|.' ___  ||_   _||_   _||_   __ \ .' ____ \  
  \ \  /\  / / / .'   \_|  | |    | |    | |__) || (___ \_| 
   \ \/  \/ /  | |   ____  | '    ' |    |  ___/  _.____`.  
    \  /\  /   \ `.___]  |  \ \__/ /    _| |_    | \____) | 
     \/  \/     `._____.'    `.__.'    |_____|    \______.'                                             
''')
        print('''
              
                   __              __
                   \ `-._......_.-` /
                    `.  '.    .'  .'
                     //  _`\/`_  \\\\
                    ||  /\O||O/\  ||
                    |\  \_/||\_/  /|
                    \ '.   \/   .' /
                    / ^ `'~  ~'`   \\
                   /  _-^_~ -^_ ~-  \\
                   | / ^_ -^_- ~_^\ |
                   | |~_ ^- _-^_ -| |
                   | \  ^-~_ ~-_^ / |
                   \_/;-.,____,.-;\_/
            ==========(_(_(==)_)_)=========
''')
        print("________________________________________________________________________________________________")
        print(" ")
        print("This is the WGPUPS delivery service program.")
        start = input("Type 'start' to being the program. ")
        start = start.lower()
        if start == "start": 
            # read addresses and distance data
            self.read_package_data()
            self.read_distance_data()
            
            # load packages onto trucks
            for package in self.truck1_manifest:
                self.truck1.loaded_packages.append(package)
            for package in self.truck2_manifest:
                self.truck2.loaded_packages.append(package)
            for package in self.truck3_manifest:
                self.truck3.loaded_packages.append(package)
            print("Packages loaded onto trucks")
            
            for key in self.truck1_manifest:
                print(str(key))
                
            for package in self.package_hashmap.map:
                if package == None:
                    continue
                print(package)
            
            while self.all_packages_delivered():
                print("Delivering packages now...")
                self.change_delivery_status(1)
                
                
                trucks = [self.truck1, self.truck2, self.truck3]
                
                for truck in trucks:
                    print("Finding nearest neighbor")
                    nearest_address, nearest_distance = truck.find_nearest_neighbor()
                    print(f"Nearest address: {nearest_address} + Nearest distance: {nearest_distance}")
                    self.change_delivery_status(2)
                    truck.update_address_and_deliver_packages(nearest_distance, nearest_address)
                    print(f"Truck{truck.truck_number} delivered {truck.packages_delivered}")
                    
                    
                print("Deliveries complete")

                
        else: 
            print("Incorrect user input, please try again")
          
          

            
wgups_delivery_service = WGUPS_Hub()
wgups_delivery_service.instantiate_packages()
wgups_delivery_service.start_delivery_program()
            
    