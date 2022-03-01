#Trying to see my swyftx profile
import urllib.request
import requests
values = """
  {
    "apiKey": "7r4hTa2Yb..."
  }
"""

headers = {
  'Content-Type': 'application/json'
}
request = requests.post('https://api.swyftx.com.au/auth/refresh/', data=values, headers=headers)

response_body = urllib.request.urlopen(request).read()
print(response_body)