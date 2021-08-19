# testing to see if lab 10b works for this
# performing get request
import requests

# testing my option system
while True:
    print("Welcome to DA_group3")
    print("\t *", "Option 1) Perform the get request on website")
    print("\t *", "Option 2) View the status code")
    print("\t *", "Option 3) View website header")
    print("\t *", "Option 4) View modified header User-Agent")
    answer = input("What would you like to see? Option: ")
    if answer == "1":
        testing = "https://www.youtube.com/"
        t = requests.get(testing)
        print(t.text)
        
        if t.text == t.text:
            n1 = input("Would you like to view anything else?(Y/N): ")
            if n1 == "y" and "Y":
                pass
            if n1 == "n" and "N":
                break
          

# testinng for OK return status
    if answer == "2":
        testing = "https://www.youtube.com/"
        t = requests.get(testing)
        print("Status Code: ")
        print("\t *", t.status_code)
        if t.status_code == 200:
            print("Translation: 200 = OK")
            
            if t.status_code == t.status_code:
                n1 = input("Would you like to view anything else?(Y/N): ")
                if n1 == "y" and "Y":
                    pass
                if n1 == "n" and "N":
                    break

            
# testing for website header
    if answer == "3":
        testing = "https://www.youtube.com/"
        t = requests.get(testing)
        h = requests.head(testing)
        print("HEADER:")
        print("*******************************************")
        for x in h.headers:
            print("\t *", x, ":", h.headers[x])
        print("*******************************************")
        
        n1 = input("Would you like to view anything else?(Y/N): ")
           if n1 == "y" and "Y":
               pass
           if n1 == "n" and "N":
               break
        
  
   

        
# testing for mobile for header user-agent
    if answer == "4":
        headers = {
            "User-Agent": "Mobile"
        }
        testing2 = "http://httpbin.org/headers"
        rh = requests.get(testing2, headers=headers)
        print(rh.text)
        n1 = input("Would you like to view anything else?(Y/N): ")
           if n1 == "y" and "Y":
               pass
           if n1 == "n" and "N":
               break

        
    else:
        if answer != "1" and answer != "2" and answer != "3" and answer != "4":
            print("answer undefined. please try again.")


