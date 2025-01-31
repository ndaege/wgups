from distance_lookup import distance_lookup

class Truck:
    def __init__(self, truck_number, current_address):
        self.truck_number = truck_number
        self.hub_address = "4001 South 700 East"
        self.current_address = current_address
        self.next_address = None
        self.miles_travelled = 0.0
        self.loaded_packages = []
        self.packages_delivered = []
        self.addresses_visited = []
        self.deliver_time = 0.0
        self.speed = 18
        
    def __str__(self):
        return f"Truck{self.truck_number}, is currently at {self.current_address}, has travelled {self.miles_travelled}, and has delivered {self.packages_delivered} packages."
        
    def load_packages(self, package_ids, package_hashmap):
        for package_id in package_ids:
            package = package_hashmap.get(str(package_id))
            if package:
                self.loaded_packages.append(package)
            
    def return_to_hub(self, current_address, hub_address):
        if self.loaded_packages == []:
            self.miles_travelled += distance_lookup.distance_lookup(current_address, hub_address)
            self.current_address = hub_address
            
    def start_delivery(self, current_address, all_addresses):
        while self.loaded_packages:
            
            if current_address == '':
                continue
            else:
                current_address = self.current_address
                nearest_address = None
                nearest_distance = 140.0
        
            for address in all_addresses:
                if address == '':
                    continue
                if address in self.addresses_visited:
                    continue
                distance = float(distance_lookup(current_address, address))
                print(f"Distance from {current_address} to {address}: {distance}")
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_address = address
                    
                    
            if nearest_address:
                delivered_packages = [package for package in self.loaded_packages if package.address == nearest_address]
                
                self.current_address = nearest_address
                self.miles_travelled += nearest_distance
                self.deliver_time += (nearest_distance / self.speed)
                self.addresses_visited.append(nearest_address)

                print(f"Delivering to {nearest_address}.")
                for package in delivered_packages:
                    package.delivery_status = 2
                    package.delivered_at = self.deliver_time
                    self.packages_delivered.append(package)
                    self.loaded_packages.remove(package)
                    

                    
                print(f"Truck {self.truck_number} delivered to {nearest_address}.")
            else:
                print(f"No more valid addresses for Truck {self.truck_number}. Returning to hub.")
                return
                
                    
            
             

            
    
        