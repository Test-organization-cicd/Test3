import requests
import sys

if __name__== "__main__":
  try:
    response = requests.get("https://api.github.com")
  except requests.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
    sys.exit(1)
  except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
    sys.exit(1) 
  status_code = response.status_code
  print("Request sent")
  print("Status Code:" + str(status_code))
  print(response.text)
  if status_code == 200:
    sys.exit(1)
  sys.exit(1)    