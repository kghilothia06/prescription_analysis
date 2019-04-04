# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:49:23 2019

@author: Lenovo
"""
import urllib.request
A=[]
for i in range(43):
    media = "http://www.medguideindia.com/npp_price_list.php?nav_link=&pageNum_rr={}&nav_link=&selectme={}".format(i,i)
    print(media)
    page=urllib.request.urlopen(media)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page)
    a_tag=soup.find_all('td',{'class':'mosttext'})
    for a in a_tag:
        if a.text=='\n':
            A.append('Tablet')
        else:
            A.append(a.text)
print(A)
for i in range(2500):
    A.remove('\n\n')
print(A)
for i in range(100):
    A.remove('For Next or Back Page Click on Number in Scroll Box \xa01234567891011121314151617181920212223242526272829303132333435363738394041  of\xa041\xa0Pages')
Sno=[]
for i in range(0,10301,5):
    Sno.append(A[i])
    
print(A[4001])
k=''
if k=='':
    print("hello")
Sno=[]
i=1

DrugName=[]
CapSize=[]
for i in range(43):
    media = "http://www.medguideindia.com/npp_price_list.php?nav_link=&pageNum_rr={}&nav_link=&selectme={}".format(i,i)
    print(media)
    page=urllib.request.urlopen(media)
    soup = BeautifulSoup(page)
    a_tag=soup.find_all('tr',{'class':'row'})
    for a in a_tag:
        CapSize.append(a.contents[7].text)
import pandas as pd
df=pd.DataFrame(Sno,columns=['Sno'])
df['Generic/Quantity']=DrugName
df['Package Unit']=CapSize
df['Price(in Rs.)']=Price
df
from pandas import DataFrame
export_csv = df.to_csv (r'C:\Users\Lenovo\Desktop\export_dataframe.csv', index = None, header=True) 