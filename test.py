import pandas as pd
import cx_Oracle

conn = cx_Oracle.connect("VDMSTGTOYT/v8^P-4[Ht-T_2d@oracle-db1-pvdm.imanheim.com/PVDM_SVC1")
cur=conn.cursor()
sql = "select * from vehicle_base where vin = '2T1BU4EEXDC076474'"
cur.execute(sql)

# print("connected"+orcl.version)
print(cur.bindnames())
for i in cur:
    colnames = [row[0] for row in cur.description]
    print(cur)
    print(i)
cur.close()
conn.close()

print(colnames)
# dsn_tns = cx_Oracle.makedsn(HOST, port, 'Service name')
# connection = cx_Oracle.connect('VDMSTGTOYT', 'v8^P-4[Ht-T_2d', dsn_tns)
# query = "select abc.source_code,abc.mmyy, sum(abc.cnt) from(select source_code,model_year,ltrim(TO_CHAR(Created_timestamp,'mm-yyyy'),'0') as mmyy,count(*) as cnt from VENDOR_VEHICLE_ON_BOARD_ARCH group by source_code,model_year,Created_timestamp) abc group by abc.source_code,abc.mmyy"
# df= pd.read_sql(query,con=connection)
# print(df)