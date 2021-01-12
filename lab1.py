import requests
#Make a Python script that prints out the version of the requests library.
print(requests.__version__)

#Modify your Python script to GET the Google homepage.
google = requests.get('http://www.google.com')
print(google)

