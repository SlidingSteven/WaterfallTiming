import urllib
import time
import urllib.request
list_of_ips = ['http://final-java-attempt.appspot.com/', 'http://34.82.94.25/examples/servlets/servlet/HelloWorldExample', 'https://helloworldpython-252906.appspot.com/']
list_of_names = ["Java On App-Engine", "Java on VM", "Python on App-Engine"]
def pool_requests (list_of_ips):
    i = 0
    for ip in list_of_ips:
        start = time.time()

        urllib.request.urlopen(ip) 
        end = time.time()
        #print(ip)
        string = "\n" + list_of_names[i] +  "," +  str(end - start) 
        f.write(str(string))
        i = i+1
with open("timing.csv", "w") as f: 
    f.write("Name,Time\n")
    for i in range(0, 300):
        pool_requests(list_of_ips)
        print("running: ", i)
