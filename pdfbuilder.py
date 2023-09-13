import requests 
import json
import base64

url = "https://api.doppio.sh/v1/render/pdf/sync"
html = open("yourhtmlfile.html", "r").read()
b = base64.b64encode(bytes(html, 'utf-8')).decode('utf-8')

                
payload = json.dumps({
  "page": {
    "setContent": {
      "html":b, 
    },
    "pdf": {
      "printBackground": True,
      "format": "A4"
    }
  }
})
headers = {
  'Authorization': 'Bearer a0d86f6aa8586757856b9ce9',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

res = response.text 
parsedRes = json.loads(res)
newUrl = parsedRes['documentUrl']
r = requests.get(newUrl).content
output = base64.b64decode(r)
with open("output.pdf",'wb') as f:
    f.write(r)
