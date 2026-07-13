import pandas as pd

# 绝对路径读取
df = pd.read_csv("D:/telecom_flow_analysis/data/raw/train.csv")

# 1. 缺失值填充
num_cols = df.select_dtypes(include=['int64','float64']).columns
text_cols = df.select_dtypes(include=['object']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
df[text_cols] = df[text_cols].fillna("未知")

# 2. 修正字段名，使用完整列名
df = df[(df["过去三个月的平均每月使用分钟数"] <= 1000) & (df["平均月费用"] <= 500)]

# 3. 消费分层
def fee_level(fee):
    if fee < 30:
        return "低消费用户"
    elif fee < 80:
        return "中等消费用户"
    else:
        return "高消费用户"
df["消费分层"] = df["平均月费用"].apply(fee_level)

# 4. 保存清洗后数据
df.to_csv("D:/telecom_flow_analysis/data/processed/clean_telecom.csv", index=False, encoding="utf-8")
print("清洗完成，已保存到processed文件夹")
print("清洗后数据量：", df.shape)