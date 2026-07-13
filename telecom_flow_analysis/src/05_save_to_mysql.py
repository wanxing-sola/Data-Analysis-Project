import pandas as pd
import pymysql
from sqlalchemy import create_engine

# 格式 mysql://用户名:密码@localhost:3306/数据库名
engine = create_engine("mysql://root:428428@localhost:3306/telecom_db")

# 读取清洗后完整数据
df = pd.read_csv("D:/telecom_flow_analysis/data/processed/clean_telecom.csv")

# 2. 将数据写入mysql表 telecom_user
df.to_sql(
    name="telecom_user",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000
)
print("15万条电信用户数据入库完成")

# 3. 测试SQL分组查询（运营商常用统计语句）
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="428428",
    database="telecom_db"
)
test_sql = """
SELECT 消费分层, AVG(`过去三个月的平均每月使用分钟数`) AS 平均使用时长, COUNT(客户ID) AS 用户总数
FROM telecom_user
GROUP BY 消费分层
ORDER BY 平均使用时长 DESC;
"""
sql_result = pd.read_sql(test_sql, conn)
print("SQL分组统计结果：")
print(sql_result)
conn.close()