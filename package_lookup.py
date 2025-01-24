import csv 

def package_lookup(package_id):
    
    with open('package_data.csv', 'r') as file:
        filtered_line = (line.replace('\n', '') for line in file)
        reader = csv.reader(filtered_line)
        for row in reader:
            return row[package_id]
            
print(package_lookup(1))