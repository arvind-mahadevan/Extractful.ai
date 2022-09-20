import sqlite3
import pandas as pd
import math
# replace StringIO(x) with open('file.csv', 'r')
# replace StringIO(x) with 'file.csv'
df = pd.read_csv('Sheet2.csv')
sh=df.shape
print(sh)
rows=sh[0]
cols=sh[1]
for i in range(rows):
  c=0
  for j in range(cols):
    if(isinstance(df.iloc[i,j],int)==True or isinstance(df.iloc[i,j],float)==True):
      if(math.isnan(df.iloc[i,j])==False):
        c+=1
      else:
        continue
    elif(isinstance(df.iloc[i,j],str)==True):
      c+=1
      continue
  if(c>2):
    print("This row is the reader:",i)
    num=i
    head=df.iloc[[i]]
    print(head)
    break
conn=sqlite3.connect('first.db')
print("Connection successful!")
conn.execute('''CREATE TABLE SALES
(SNO INT PRIMARY KEY NOT NULL,
SKU DESCRIPTION VARCHAR(20) NOT NULL,
VENDOR SKU VARCHAR(20) NOT NULL,
PRICE INT,
ORDERQTY INT,
TAX INT);''')
conn.commit()
for i in range(num+1,rows):
	ndf=df[[i]]
	ndf.to_sql('SALES',conn)
conn.commit()
c.execute("SELECT * FROM SALES;")

