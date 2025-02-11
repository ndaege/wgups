'''
The WGUPS Hub will manage and dispatch the trucks. It will also predetermine the routes 
for the trucks, so they know where to go before dispatch. 
'''

import csv
from HashMap import HashMap
from HashMap import Pair
from old_Truck import Truck
from Package import Package
import datetime
        
class WGUPS_Hub:
    def __init__(self):
        self.package_hashmap = HashMap()
        self.extracted_package_data = []
        self.addresses = []
        self.distances = []
        self.truck1 = Truck(1, "4001 South 700 East", [1, 7, 8, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 39])
        self.truck2 = Truck(2, "4001 South 700 East", [3, 4, 5, 6, 10, 11, 18, 25, 28, 32, 36, 38, 40])
        self.truck3 = Truck(3, "4001 South 700 East", [2, 9, 12, 17, 19, 21, 22, 23, 24, 26, 27, 33, 35])
        self.time = datetime.timedelta(hours=(8), minutes=(0))
        
        # hub is passing empty addresses to objects
        # loop through manifest, check for what has been delivered(remove what has been delivered), 
        # for packages not delivered, calc distance
        
    
    # open and read file containing package data    
    def read_package_data(self):    
        with open('package_data.csv', 'r') as file:
            filtered_line = (line.replace('\n', '') for line in file)
            reader = csv.reader(filtered_line)
            self.extracted_package_data = list(reader)
            
            return self.extracted_package_data[1:]
            
    # open and read file containing distance data
    def read_distance_data(self):
        with open('distance_table.csv', 'r') as file:
            filtered_line = (line.replace('\n', '') for line in file)
            reader = csv.reader(filtered_line)
            distance_table = list(reader)
            
            self.addresses = [address for address in distance_table[0][2:]]
            self.distances = [row[1:] for row in distance_table[1:]]
            
            return self.addresses, self.distances
        
    # gather package information
    def gather_package_information(self):
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
                
        # define distance lookup algorithm
    def distance_lookup(self, truck_current_address, next_address, addresses):
        for x_index, address in enumerate(addresses):
            if address == next_address:
                x_position = x_index
                break
    
        for y_index, address in enumerate(addresses):
            if address == truck_current_address:
                y_position = y_index
                break
            
        if x_position > y_position:
            return self.distances[x_position][y_position + 1]
        elif x_position < y_position:
            return self.distances[y_position][x_position + 1]
        
    # define nearest neighbor algorithm
    def find_nearest_neighbor(self, truck, addresses):
        nearest_distance = 140.00
        for package in truck.loaded_packages:
            break
        
        # for address in addresses:
        #     if address == self.current_address:
        #         continue
        #     distance = self.distance_lookup(truck_current_address, address, addresses)
        #     if float(distance) < nearest_distance:
        #         nearest_distance = float(distance)
        #         nearest_address = address
        # return [nearest_address, nearest_distance]
            
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
            
            # for key in self.truck1_manifest:
            #     print(str(key))
                
            # for key in self.truck1_manifest:
            #     print(self.package_hashmap.get(str(key)))
            
            while not self.all_packages_delivered():
                print("Delivering packages now...")
                self.change_delivery_status(1)
                
                
                trucks = [self.truck1, self.truck2, self.truck3]

                
                for truck in trucks:
                    print(f"Truck{truck.truck_number} has the following packages: ")
                    for package in truck.loaded_packages:
                        print(f"{package} : {self.package_hashmap.get(str(package))}")
                        
                    print("Finding nearest neighbor")
                    nearest_address, nearest_distance = self.find_nearest_neighbor(truck, self.read_distance_data()[0])
                    print(f"Nearest address: {nearest_address} + Nearest distance: {nearest_distance}")
                    self.change_delivery_status(2)
                    truck.update_address_and_deliver_packages(nearest_distance, nearest_address)
                    print(f"Truck{truck.truck_number} delivered {truck.packages_delivered}")
                    
                    
                print("Deliveries complete")

                
        else: 
            print("Incorrect user input, please try again")
          
          

            
wgups_delivery_service = WGUPS_Hub()
print("Packages loaded onto trucks")
wgups_delivery_service.gather_package_information()
wgups_delivery_service.start_delivery_program()
            
    