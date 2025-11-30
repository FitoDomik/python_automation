def f():
    s = "DevOps course."
    print(s)
s = "Python Data"
f()
print(s)
tuple1 = (("cicd", "Jenkins"), ("security", "fortify"))
print(tuple1)
list_data = [9, 2.9, [-3, 5], ["jenkins", "Jira"]]
print(list_data)
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_letters = str(letters)
lists_letters = list(letters)
tuples_letters = tuple(letters)
sets_letters = set(letters)
print("String: ", string_letters)
print() 
print("Lists: ", lists_letters)
print() 
print("Tuples: ", tuples_letters)
print() 
print("Sets: ", sets_letters)
dict1 = {"name":"Devops", "batch":1.0, "canVote":True,"name":"test"}
print(dict1)
print(dict1["name"])
x = 13
if(x>=13):
    print("Met the condition")
else:
    print("Didn't met the condition")
print("Zero:",bool(0))
print("Integer:",bool(23))
print("Float:",bool(3.142))
print("Complex:",bool(5+2j))
Tool = "SONAR"
len1 = len(Tool)
print(len1)
print("Code analysis tool is", Tool, ".Its part of devops")
IAAS = "TERRAFORM"
print(IAAS[:5])      
print(IAAS[5:])      
print(IAAS[2:6])     
Name = "AMAZON WEB SERVICES"
for i in Name:
    print(i)
ToolsData = ["Maven", "Ansible", "Jenkins", "Sonar"] 
if "Maven" in ToolsData:
    print("Maven is present.")
else:
    print("Maven is absent.")
ToolsData.append("Fortify")
del ToolsData[3]
print(ToolsData)
ToolsData = ["Maven","Ansible","Jenkins","Sonar"] 
ToolsData.sort()
print(ToolsData)
applePrice = 180
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1kg Apples to the cart.")
VERSION = 18
if (VERSION < 0):
    print("Version is negative.")
elif (VERSION > 0):
    if (VERSION <= 10):
        print("Version is between 1-10")
    elif (VERSION > 10 and VERSION <= 20):
        print("Version is between 11-20")
    else:
        print("Version is greater than 20")
else:
    print("Version is zero")
name = 'SINGAM'
for i in name:
    print(i)
tools = ("Maven", "Jenkins", "sonar", "jira")
for x in tools:
    print(x)
count = 5
while (count > 0):
    print(count)
    count = count - 1
i=1
while (i<=3):
    for k in range(1, 4):
        print(i, "*", k, "=", (i*k))
    i = i + 1
    print()
for i in range(1, 4):
    k = 1
    while (k<=3):
        print(i, "*", k, "=", (i*k))
        k = k + 1
    print()
def toolname(security, analysis):
    print("Tools,", security, analysis)
toolname("Fortify", "Sonar")
def name(fname, mtame = "Jenkins", boardname = "Jira"):
    print("Hello,", fname, mtame, boardname)
name("Sonar")
def name(firsttool, secondtool, thirdtool):
    print("Hello,", firsttool, secondtool, thirdtool)
name(thirdtool = "Ansible", firsttool = "Terraform", secondtool = "Jmeter")
def name(firsttool, secondtool, thirdtool):
    print("Hello,", firsttool, secondtool, thirdtool)
name("Ansible", "Terraform", "Jmeter")
def name(*name):
    print("Hello,", name[0], name[1], name[2])
name("Ansible", "Terraform", "Jmeter")
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))   
num = 7; 
print("number: ",num)
print("Factorial: ",factorial(num))
from math import *
print(pi)
print(factorial(6))
class Tools:
    name = "Jenkins"
    version = 20
T1 = Tools()
print(T1.name)
print(T1.version)
class Tools:
    name = "Jenkins"
    version = 20
    def toolsdes(self):
        print(self.version, self.name + "\tTOOLS")
T1 = Tools()
T1.toolsdes()
print(T1.name)
print(T1.version)
class Data:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)
p = Data('PowerBI')
p.say_hi()
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something
class B(A):
    def __init__(self, something):
        A.__init__(self, something)
        print("B init called")
        self.something = something
obj = B("Something")
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something
class B(A):
    def __init__(self, something):
        print("B init called")
        self.something = something
        A.__init__(self, something)
obj = B("Something")
import json
tools =  '["Maven", "Jira", "Kubernetes", "Docker"]'
lst1 = json.loads(tools)
print(lst1)
import json
lst1 = ['Maven', 'Jira', 'Kubernetes', 'Docker']
jsonObj = json.dumps(lst1)
print(jsonObj)
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")