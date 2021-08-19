# testing to see if lab 10b works for this
# performing get request
import requests


#testing my option system
print("Welcome to DA_group3", "\t *", "Option 1) Perform the get request on website", "\t *", "Option 2) View the status code", "\t *", "Option 3) View website header", "\t *", "Option 4) View modified header User-Agent")
answer = input("What would you like to see? Option: ")
if answer == "1":
    testing = "https://www.youtube.com/"
    t = requests.get(testing)
    print(t.text)

# testinng for OK return status
if answer == "2":
    print("Status Code: ")
    print("\t *", t.status_code)
    if t.status_code == 200:
        print("Translation: 200 = OK")

# testing for website header
if answer == "3":
    h = requests.head(testing)
    print("HEADER:")
    print("*******************************************")
    for x in h.headers:
        print("\t *", x, ":", h.headers[x])
    print("*******************************************")

# testing for mobile for header user-agent
if answer == "4":
    headers = {
        "User-Agent": "Mobile"
    }
    testing2 = "http://httpbin.org/headers"
    rh = requests.get(testing2, headers=headers)
    print(rh.text)

else:
    if answer != "1" and answer != "2" and answer != "3" and answer != "4":
        print("answer undefined. please try again.")




