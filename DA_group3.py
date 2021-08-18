print('testing')
print("this better work or im gonna cry")
#it works
#but it only works if changes are made in github n not in pycharm if my theory isn't wrong
#go to the git option in the top and click 'update project' and 'merge...'
#by doing this, ur updating the pycharm to this current one
#we chould do updates everytime we gotta test this so yeah
#once yalls have seen this imma erase this

#ill be following lab 10a word for word and see if it works pls work
import socket;
import requests
url = "http://localhost:8080/"
url_used = print("url:", url) #this will be the url of the website we will be using
# uh ignore these^ for a sec

#testing to see if lab 10b works for this
testing = "https://www.youtube.com/"
t = requests.get(testing)
print(t.text)

print("Status Code: ")
print("\t *", t.status_code)
if t.status_code == 200:
  print("Translation: 200 = OK")
  
h = requests.head(url)
print("HEADER:")
print("*******************************************")
for x in h.headers:
  print("\t *", x, ":", h.headers[x])
print("*******************************************")
