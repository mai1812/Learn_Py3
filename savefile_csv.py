
import csv
import requests 
import json 

#created file names.csv from url file
def url1_csv(api_url): 
    response = requests.get(api_url) 
    if response.status_code == 200:  
        data = json.loads(response.content.decode('utf-8')) 
        data_list = []
        for i in range(len(data)):
            data_list.append(data[i])
    try:
        #csv_name = 'Name_1.csv'
        with open('Names.csv', 'w') as f:
            csv_columns = ['postId', 'id', 'name', 'email', 'body']
            writer = csv.DictWriter(f, fieldnames = csv_columns)
            writer.writeheader()
            for i in data_list:
                writer.writerow(i)
    except IOError:
        print("I/O error")
url1_csv("https://jsonplaceholder.typicode.com/posts/1/comments")

'''
import csv
csv_columns = ['No','Name','Country']
dict_data = [
{'No': 1, 'Name': 'Alex', 'Country': 'India'},
{'No': 2, 'Name': 'Ben', 'Country': 'USA'},
{'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
{'No': 4, 'Name': 'Smith', 'Country': 'USA'},
{'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
]
csv_file = "Names.csv"
try:
    with open(csv_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
'''
#Created file out.csv
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&apikey=demo&datatype=csv'
response = requests.get(url)        

with open('out.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))

#created file innovators.csv
data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data_list)
