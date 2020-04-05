import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("files/newsafr.xml", parser)
titles = []
root = tree.getroot()
xml_items = root.findall("channel/item/description")
#print(len(xml_items))
stroka = "" 
for xmli in xml_items:
  stroka =stroka +xmli.text


def sortByLength(inputStr):
   return len(inputStr)    
    
list_data = stroka.strip().split()
word_data = {}
for i in range(len(list_data)):
  list_data1 = sortByLength(list_data[i])
  
  if list_data1 > 6:
     count = word_data.get(list_data[i],0)
     word_data[list_data[i]] = count+1 
list_data_new=list(word_data.items())
list_data_new.sort(key=lambda i: i[1])
dlina = int(len(list_data_new))
print(list_data_new[dlina-10:dlina])