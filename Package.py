import csv

class Package: 
    delivery_statuses = ["AtHub", "EnRoute", "Delivered"]
    def __init__(self, package_id, address, city, state, zip, delivery_deadline, weight, truck=None, delivery_status=0):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.delivery_status = 0 
        self.truck = None
        
        
        
        
