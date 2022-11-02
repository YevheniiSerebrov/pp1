import pandas as pd 
# import pip
# pip.main(["install", "openpyxl"])
import numpy as np 
import statistics as ss 

# a=pd.read_excel("pyt-ecos.xlsx")
# print("Sum: ", a["x1"].sum())
# print("max: ", a["x2"].max())
# _________________
# df = {
#     "y" : [1,3,5,7,5,4,3,1],
#     "x1": [3,4,7,6,7,9,8,11],
#     "x2": [34,34,56,67,78,56,45,34]
# }
# data = pd.DataFrame(df)
# print(data.corr(method="pearson"))
#_______________________
# x=(1,2,3,4,5,6,7,8)
# y=(123,234,239,344,543,565,455,765)

# print(ss.correlation(x, y))
# print(ss.linear_regression(x, y))
# y1=ss.linear_regression(x, y).slope*10+ss.linear_regression(x, y).intercept
# print(pd.merge(x, y))
# ______________
df = pd.DataFrame({
    "Name":["Hayovska","Todoshchuk","Dugaev","Sobil","Serebrov","Gordey"],
    "Grade": [95,82,60,93,94,55],
    "City":["Chortkiv","Chernivtsi","Chernivtsi","Ternopil","Chernivtsi","Kiseliv"],
    "Height": [155,162,185,175,181,163],
    "Even grade": [5,4,3,5,5,3]
})
print(df.sort_values(by=["Height","Grade"],ascending=[False,False]))
# print(df)