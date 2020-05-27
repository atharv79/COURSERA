'''Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract 
the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and 
the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553) 

Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.'''

import urllib.request as urll
import json

json_url = input("Enter URL : ")
print("Retrieving: ", json_url)
data = urll.urlopen(json_url).read().decode('utf-8')
print('Retrieved: ', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total_number = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total_number += 1

print('Count: ', total_number)
print('Sum: ', sum)
