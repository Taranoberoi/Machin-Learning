import pandas as pd
import cx_Oracle
conn = cx_Oracle.connect("VDMSTGTOYT/v8^P-4[Ht-T_2d@oracle-db1-pvdm.imanheim.com/PVDM_SVC1")
cur = conn.cursor()
sql = """Select SOURCE_CODE,extract(month from CREATED_TIMESTAMP),
            extract(year from CREATED_TIMESTAMP),count(*) 
            from vehicle_base 
            group by SOURCE_CODE,CREATED_TIMESTAMP"""
cur.execute(sql)

for i in cur:
    print(cur)
    print(i)
cur.close()
conn.close()