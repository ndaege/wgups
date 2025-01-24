import csv

class Package: 
    def __init__(self, package_id, ):
        self.package_id = 0
        
        
        
    def package_lookup(package_id):
    
        with open('package_data.csv', 'r') as file:
            filtered_line = (line.replace('\n', '') for line in file)
            reader = csv.reader(filtered_line)
            two_dimensional_array = list(reader)
            indexes = [(package_id, 1), (package_id, 2), (package_id, 3), (package_id, 4), (package_id, 6)]
            package_info = [two_dimensional_array[row][column] for row, column in indexes]
            return package_info

for i in range(1, 10):
    print(Package.package_lookup(i))