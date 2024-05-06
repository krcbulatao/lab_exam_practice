import pandas as pd

df=pd.read_csv("/mnt/c/Users/krcbu/Downloads/Exam_Table.csv")

filtered_df=df[df['Genus'].str.casefold().str.startswith('st', na=False)]

filtered_df.to_csv("/mnt/c/Users/krcbu/Desktop/bio 191/Bulatao_B2_answer/b2_output2.csv", index=False)