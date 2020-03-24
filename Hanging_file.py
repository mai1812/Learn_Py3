#created file csv from url

import requests

def save_file_url():
    r = requests.get(url, allow_redirects=True)
    open('post.csv', 'wb').write(r.content) #created file csv dạng nhị phân "wb"

url = 'https://jsonplaceholder.typicode.com/posts/1'
f= open("post.csv", "r")
print(f.read())


def main():
    f= open("guru99.txt","w+") #created new file
    #f=open("guru99.txt","a+") #append 
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    f.close()   

     #Open the file back and read the contents
f= open("guru99.txt","rt")
print(f.read())
     #or, readlines reads the individual line into a list
     #fl =f.readlines()
     #for x in fl:
     #print x
if __name__== "__main__":
  main()





