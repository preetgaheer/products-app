# importing the requests library
import requests

# api-endpoint
URL = "http://127.0.0.1:8000/products/popluar/daily"

# location given here
# location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'time':"all"}

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()
print(data)
