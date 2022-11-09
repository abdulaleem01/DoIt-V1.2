import requests

#from newup import hhh




y1 = ""
tcnum1 = ""
tcname1 = ""

def hhh(*args):
    global y1,tcname1,tcnum1
    if args[0] == 0:
        y = args[1]
        if args[2] == "image":
            y1 += y+"~"
        else:
            y1 += y+"^"
    
    if args[0] == 1:
        tcnum1 = args[1]
    if args[0] == 2:
        tcname1 = args[1]
    if args[0] == 3:
        file1 = open("myfile.txt","w")
        file1.write(f"TCNUM - {tcnum1}\n TCNAME - {tcname1}\n TCDATA - {y1}")
        myobj = {'tcnum':tcnum1,'tcname':tcname1,'tcdata':y1}
        url = 'http://127.0.0.1:8000/api/add/'
        x = requests.post(url, json = myobj)


"""
import requests

url = 'http://127.0.0.1:8000/add/'
h = "hrfcnjkdmxchvjnfckmlscjhvfjnkdslcnhfjnkdm"
myobj = {'name': h}

x = requests.post(url, json = myobj)

print(x.text)


################

hhh(0,"open the text box ","")
hhh(0,"now click the right bar","")
hhh(0,"/Users/abdulaleem/Desktop/api_test/csvwrite.py","image")
hhh(0,"/Users/abdulaleem/Desktop/api_test/csvwrite.py","image")
hhh(0,"/Users/abdulaleem/Desktop/api_test/csvwrite.py","image")

hhh(1,"C123456")
hhh(2,"IA CHARTS AND DOCUMENTS")
hhh(3)
#hhh(1)
"""




"""
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
  
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()
"""