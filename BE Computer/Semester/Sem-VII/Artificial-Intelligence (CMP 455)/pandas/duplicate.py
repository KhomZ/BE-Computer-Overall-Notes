# importing pandas package
import pandas as pd
  
# making data frame from csv file
data = pd.read_csv(r"C:\Users\ACER\Desktop\myProj\what-I-learnt-as-a-Computer-Engineering-Student\BE Computer\Semester\Sem-VII\Artificial-Intelligence (CMP 455)\pandas\employees.csv")
print(data)

# storing unique value in a variable
unique_value = data["Team"].nunique()
  
# printing value
print(unique_value)