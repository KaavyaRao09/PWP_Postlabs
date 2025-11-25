# import pandas as pd
# df_csv = pd.read_csv(r"D:\SEM 3 Subjects\Python\openpyxl\sample_data.csv")
# df_json = pd.read_json(r"D:\SEM 3 Subjects\Python\openpyxl\sample_data.json")
# df_excel = pd.read_excel(r"D:\SEM 3 Subjects\Python\openpyxl\sample_data.xlsx")
# def check_data_types(df, name):
#     print(f"\nData Types for {name}:")
#     print(df.dtypes)
# check_data_types(df_csv, "CSV DataFrame")
# check_data_types(df_json, "JSON DataFrame")
# check_data_types(df_excel, "Excel DataFrame")



import pandas as pd
import numpy as np
df_csv = pd.read_csv(r"D:\SEM 3 Subjects\Python\openpyxl\sample_data.csv")
df_json = pd.read_json(r"D:\SEM 3 Subjects\Python\openpyxl\sample_data.json")
df_excel = pd.read_excel(r"D:\SEM 3 Subjects\Python\openpyxl\sample_data.xlsx")
df_csv.loc[1, 'Age'] = np.nan # CSV DataFrame
df_json.loc[1, 'Age'] = np.nan
df_excel.loc[1, 'Age'] = np.nan
def fill_missing_with_mean(df, name):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    print(f"\n{name} after filling missing 'Age' values with mean:")
    print(df)
fill_missing_with_mean(df_csv, "CSV DataFrame")
fill_missing_with_mean(df_json, "JSON DataFrame")
fill_missing_with_mean(df_excel, "Excel DataFrame")
