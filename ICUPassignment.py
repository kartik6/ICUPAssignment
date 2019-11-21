#Splitting data and finding frequency
import re
f=open("sport.txt",'r')#opening file to read and then split
dictionary={}
Words=[]
for line in f:
    line=line.strip()
    words=re.split('[.,\-();\s\'\"]',line)
    words=list(filter(lambda x:len(x)!=0,words))
    Words+=words
        
for word in Words:              #frequency of words
    if word not in dictionary:
        dictionary[word]=0
    dictionary[word]+=1
print(dictionary)
for i in range(8):
    print()
#Removing stopwords
import nltk
from nltk.corpus import stopwords
stop=set(stopwords.words('english'))
dictset=set(dictionary.keys())
Filtered=list(dictset-stop)
f1=open("Filtered.txt","w+")
for i in Filtered:
    f1.write(i+" ")#appending filtered data in file
dict2={}
f1.seek(0)#finding frequency
for data in f1:
    words=data.split(' ')
    for word in words:
        if word not in dict2:
            dict2[word]=0
        dict2[word]+=1
print(dict2)
f.close()
f1.close()
#graph of the 2 files sizes
import os
count1= os.path.getsize("C:\Python\Python37\sport.txt")
count2= os.path.getsize("C:\Python\Python37\Filtered.txt")
import matplotlib.pyplot as plt 
x = ["File1","File2"]  
y = [count1,count2] 
plt.plot(x, y)  
plt.xlabel('Files checked') 
plt.ylabel('Size of files') 
plt.title('Size comparison') 
plt.show()

    

        
