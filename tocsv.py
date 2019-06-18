import csv
import datetime
csv_columns = ['date_time','value']

dict_data = [
{'date_time': datetime.datetime(2019,6,18), 'value': 0.02},
{'date_time': datetime.datetime(2019,6,1), 'value': 0.3},
{'date_time': datetime.datetime(2019,5,18), 'value': 2.9},
{'date_time': datetime.datetime(2019,5,1), 'value': 0.5},
{'date_time': datetime.datetime(2019,4,18), 'value': 0.37},
{'date_time': datetime.datetime(2019,4,1), 'value': -0.02},
{'date_time': datetime.datetime(2019,3,18), 'value': 0.95},
{'date_time': datetime.datetime(2019,3,1), 'value': 0.06},
{'date_time': datetime.datetime(2019,2,18), 'value':0.87},
{'date_time': datetime.datetime(2019,2,1), 'value': 0.05},
{'date_time': datetime.datetime(2019,1,18), 'value':0.34},
{'date_time': datetime.datetime(2019,1,1), 'value': 1.2},
{'date_time': datetime.datetime(2018,12,18), 'value':0.78},
{'date_time': datetime.datetime(2018,12,1), 'value': 3.8},
{'date_time': datetime.datetime(2018,11,18), 'value': 0.23},
{'date_time': datetime.datetime(2018,11,1), 'value': 0.69},
{'date_time': datetime.datetime(2018,10,18), 'value': -0.34},
{'date_time': datetime.datetime(2018,10,1), 'value': -0.26}
]

csv_file = "index_data2.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error") 
