import requests

url = "https://api.sandbox.transferwise.tech/v1/rates?source=EUR&target=USD&from=2019-02-13T14:53:01&to=2019-03-13T14:53:01&group=day"

payload={}
headers = {
  'Authorization': 'Bearer eb66daa3-6474-49bd-910c-294d5f7be5c6',
  'Cookie': '__cf_bm=ADynNO3g2RwUmJv26lbMNyYkID_4mgXKyBS6ry.fnIA-1666434726-0-Ae0cMZVP50r6PrfUQwsSaSANMcH8ZVfoaHn/ZSuB7YYe8t26YDVDIDFNVoGoksn25nzeU/CUUW4Nq9aWASsE7Ok='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())