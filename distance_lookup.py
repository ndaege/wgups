import csv

def distance_lookup(current_address, next_address): 
    with open('distance_table.csv', 'r') as file:
            filtered_line = (line.replace('\n', '') for line in file)
            reader = csv.reader(filtered_line)
            distance_table = list(reader)
            
            top_row = distance_table[0]
            
            for i, row in enumerate(distance_table):
                if next_address in row[1]:
                    next_index = i
                    break
                    
            for j, address in enumerate(top_row):
                if address == current_address:
                    return distance_table[next_index][j] 
                
print(distance_lookup("4001 South 700 East", "2530 S 500 E"))