import pandas as pd

df=pd.read_csv("/mnt/c/Users/krcbu/Downloads/Exam_Table.csv")

filtered_df=df[df['Interval'] == '30-0']

filtered_df.to_csv("/mnt/c/Users/krcbu/Desktop/bio 191/Bulatao_B1_answer/b1_output1.csv", index=False)