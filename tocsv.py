import csv
csv_columns = ['date_time','value']
'''
dict_data = [
{'date_time': 1, 'value': 2.3},
{'date_time': 2, 'value': 2.3}

]
'''
csv_file = "index_data.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error") 