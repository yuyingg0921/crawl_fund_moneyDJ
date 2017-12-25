import requests
from bs4 import BeautifulSoup
import sys
fund_id = []
fund_name = ["name"]
others = []

fund_price = ["price"]
change = ["change"]
change_p = ["change%"]
highest = ["high"]
lowest = ["low"]

res = requests.get('https://www.moneydj.com/funddj/ya/YP081000List.djhtm?a=1')
soup = BeautifulSoup(res.text, "lxml")


for a in soup.find_all('a', href=True):
    if "/funddj/ya/yp081000.djhtm?a=ET00" in a['href']:
        fund_id.append(a['href'].lstrip('/funddj/ya/yp081000.djhtm?a='))

for i in fund_id:
    try:
        print (i)
        res = requests.get('https://www.moneydj.com/funddj/ya/yp081000.djhtm?a='+str(i))
        soup = BeautifulSoup(res.text, "lxml")

        for a in soup.find_all('td',{"class":['t3t1c1','t3t1c1_rev']}):
            fund_name.append(a.text)

        for each_fund in soup.find_all('td',{"class":['t3n1','t3n1_rev']}):
            others.append(each_fund.text)

        for i in range(len(others)):
            if i%5 == 0:
                fund_price.append(others[i])
            elif i%5 == 1:    
                change.append(others[i])
            elif i%5 == 2:    
                change_p.append(others[i])
            elif i%5 == 3:    
                highest.append(others[i])
            elif i%5 == 4:    
                lowest.append(others[i])      

    except:
        pass



import csv

with open('fund_moneydj.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in zip(fund_name,fund_price,change,change_p,highest,lowest):
        writer.writerow(row)