from time import sleep as s
import urllib.request as u
import re
print("\t -------------- Today's Weather Forecast in India --------------")
flag=1
while flag == 1:
    url = "https://www.weathercity.com/in/"
    s(1)
    name = input("\nEnter the City: ")
    name=name.replace(" ","_")
    url = url + name #The url to be crawled
    try:
        data = u.urlopen(url).read()
        try:
            newdata = data.decode("utf") #trying to decode to utf-8 format
        except:
            print('\n')
        try:
            newdata = data.decode('windows-1252') #if utf-8 format fails
        except:
            print('\n')
            
        m = re.search('b1',newdata)
        start = m.start()
        end = m.end() + 31
        s(1)
        print("Today's temperature ")
        start = end - 3
        end = end -1
        print("\nHigh: " + newdata[start:end] + ' degree'+'\n')
        n = re.search('Detailed',newdata)
        head = n.end() +500
        tail = head + 322
        Newdata = newdata[head:tail]
        n = re.search('nowrap>Temperature:&nbsp;',Newdata)
        head = n.end()
        tail = n.end()+2
        print("\nLow: " + Newdata[head:tail] + ' degree')
    except:
        print("\nSorry. No match found !")
    s(1)    
    choice = input("\nDo you need one more chance? y/n : ")
    if choice.lower()=='y':
        flag = 1
    else:
        flag = 0
