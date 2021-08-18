print('testing')
print("this better work or im gonna cry")
#it works
#but it only works if changes are made in github n not in pycharm if my theory isn't wrong
#go to the git option in the top and click 'update project' and 'merge...'
#by doing this, ur updating the pycharm to this current one
#we chould do updates everytime we gotta test this so yeah
#once yalls have seen this imma erase this


#First HTTP Server 

import socket; 

#Define the host as a tuple 

HOST, PORT = "", 8080; 

 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); 

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1); 

s.bind((HOST,PORT)); 

s.listen(True); 

 

print("Serving HTTP on port %s...." %PORT); 

 

while True: 

    client_connection, client_address = s.accept(); 

    request = client_connection.recv(1024); #Buffer Size 

    print(request.decode("utf-8")); #Display the HTTP request 

    #Define the Web response message 

    http_reponse = """\ 

HTTP/1.1 200 OK 

Content-Type: text/html; charset=UTF-8 

Welcome This is my first webpage, GREAT! 

""" 

    client_connection.sendall(bytes(http_reponse, "utf-8")); 

    client_connection.close(); 
