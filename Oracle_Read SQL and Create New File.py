import pandas as pd
import cx_Oracle

conn = cx_Oracle.connect("VDMSTGTOYT/v8^P-4[Ht-T_2d@oracle-db1-pvdm.imanheim.com/PVDM_SVC1")
cur = conn.cursor()
cur.("""Select SOURCE_CODE,extract(month from CREATED_TIMESTAMP),
             extract(year from CREATED_TIMESTAMP),count(*) from vehicle_base 
             group by SOURCE_CODE,CREATED_TIMESTAMP""")
data = cur.fetchall()
data.to_excel("c:\datafile.xlsx")

# head = [i[0] for i in cur.description]
cur.close()
conn.close()

