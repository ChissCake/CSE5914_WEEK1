import requests
import sys

base_uri = "https://api.nationalize.io/?"

countries_url = "https://flagsapi.com/"

# Creating an HTML file
Func = open("output.html","w")

Func.write("<html>\n<head>\n<title> \nOutput Data in an HTML file</title>\n</head>\n")

while True:
    name = input("Enter a name: ")
    params = {"name": f"{name}"}
    
    if name == 'exit':
        print("quiting...")
        sys.exit(0)
    r = requests.get(base_uri, params=params)

    print("Server Response: " + str(r.status_code))
    Func.write("\n<p>"+name+"</p>\n")
    for i in r.json()["country"]:
        print(i["country_id"] + " : " + str(i["probability"]))
        flag = countries_url + i["country_id"] + "/flat/64.png"
        #flag_img = requests.get(flag)
        #Func.write("<img src=" + flag + "/>")
        Func.write("<p> <img src=" + flag + "/> " + i["country_id"] + " : " + str(i["probability"]) + "</p>\n")
    
    # Saving the data into the HTML file
Func.write("</html>")    
Func.close()
#Func.write("<img src=" + flag_img + "/>")