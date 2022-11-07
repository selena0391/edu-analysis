import csv



with open ('states_all.csv', 'r') as data:
    reader = csv.DictReader(data)
    list_data = list(reader)

print(list_data)
