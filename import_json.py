import json
from pprint import pprint
with open(r"files/newsafr.json") as datafile:
  json_data = json.load(datafile)
list_data=[]
json_data1 = json_data["rss"]["channel"]["items"] 
stroka = "" 
for descriptions in json_data1:
    stroka = stroka + descriptions['description']

def sortByLength(inputStr):
        
        return len(inputStr)    
    
list_data = stroka.strip().split()
#list_data.sort()
#list_data_new = []
word_data = {}
for i in range(len(list_data)):
  list_data1 = sortByLength(list_data[i])
  
  if list_data1 > 6:
     #list_data_new.append(list_data[i])
     count = word_data.get(list_data[i],0)
     #print(count)
     word_data[list_data[i]] = count+1 
list_data_new=list(word_data.items())
list_data_new.sort(key=lambda i: i[1])
dlina = int(len(list_data_new))
print(list_data_new[dlina-10:dlina])