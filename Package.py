'''
Each package has its own information, it is stored in the package object
'''

class Package: 
    def __init__(self, package_id, package_info):
        self.package_id = package_id
        self.address = package_info[0]
        self.city = package_info[1]
        self.zip = package_info[2]
        self.delivery_deadline = package_info[3]
        self.weight = package_info[4]
        self.delivery_statuses = ["AtHub", "EnRoute", "Delivered"]
        self.delivery_status = 0
        self.delivered_at = None
        self.truck = None
        
    def __str__(self):
        return f""    
        
        
        
