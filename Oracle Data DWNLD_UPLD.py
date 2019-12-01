import cx_Oracle
import pandas as pd

conn = cx_Oracle.connect("VDMSTGTOYT/v8^P-4[Ht-T_2d@oracle-db1-pvdm.imanheim.com/PVDM_SVC1")
cur = conn.cursor()
result = cur.execute("""Select SOURCE_CODE,extract(month from CREATED_TIMESTAMP) as Month,
             extract(year from CREATED_TIMESTAMP) as Year,count(*) as Count from vehicle_base 
             group by SOURCE_CODE,CREATED_TIMESTAMP""")

header = [i[0] for i in cur.description]
f = open("C:\Data Files\Datafile11.csv","w")
f.write(str(header))

df = pd.DataFrame(result.fetchall())
for j in df:
    f.write(str(df)+'\n')

f.close()
cur.close()
conn.close()
