

import requests

#testing to see if lab 10b works for this
#performing get request 
testing = "https://www.youtube.com/" 
t = requests.get(testing)
print(t.text)

#testinng for OK return status
print("Status Code: ")
print("\t *", t.status_code)
if t.status_code == 200:
  print("Translation: 200 = OK")
  
#testing for website header
h = requests.head(testing)
print("HEADER:")
print("*******************************************")
for x in h.headers:
  print("\t *", x, ":", h.headers[x])
print("*******************************************")

#testing for mobile for header user-agent
headers = {
  "User-Agent" : "Mobile"
}
testing2 = "http://httpbin.org/headers"
rh = requests.get(testing2, headers=headers)
print(rh.text)


