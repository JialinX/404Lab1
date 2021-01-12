import requests
#Make a Python script that prints out the version of the requests library.
print(requests.__version__)

#Modify your Python script to GET the Google homepage.
google = requests.get('http://www.google.com')
print(google)

#Modify your Python script so that it downloads itself from GitHub and prints out its own source code from GitHub.
lab1 = requests.get('https://raw.githubusercontent.com/JialinX/404Lab1/main/lab1.py')
print(lab1.text)