#Tinh tong 1 den n
def sumN(n):
    return (n/2)*(n-1)
s=sumN(20)
print(s)

#tim max
def fmax(a,b,c):
    if a>b and a>c:
        print("max is a")
    elif b>a and b>c:
        print("max is b")
    else: 
        print("max is c")
fmax(11,30,9)

#Find N
def findN(n):
    for i in range(n):
        i+=1
        total = (i/2)*(i-1)
        if(total > 10000):
            print(i-1)
            break       
findN(10000)
#chương trình in tam giác vuông cân
for i in range(1,5):
        s = '* '*i
        print(s)

#chương trình in tam giác cân
n = 5
for i in range(1, n):
    s = n - i
    k = s * " "
    print(k, end='')
    print(((2 * i) - 1) * '*')

import requests #ipmort package
import json #ipmort package/thu vien
def url1(api_url): #tao ham
  response = requests.get(api_url) #gan ham
  if response.status_code == 200:  #dieu kien
    data = json.loads(response.content.decode('utf-8')) #format lai kqua tra ve
    for i in range(len(data)):
      print(data[i])
  else:
    print("error")
url1("https://jsonplaceholder.typicode.com/posts/1/comments")

import requests
def url2(api_url):
    res = requests.get(api_url)
    print(res.text)

url2('https://jsonplaceholder.typicode.com/posts/1')