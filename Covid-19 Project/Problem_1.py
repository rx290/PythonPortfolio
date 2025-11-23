"""Write a Python program to display first 5 rows from COVID-19 dataset. Also print the dataset information and check the missing values. """ 
# importing Pandas and granting it an alias pd
import  pandas as pd

#hitting url for dataset
dataset_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"

#reading the dataset as a csv file format
dataset = pd.read_csv(dataset_url)

#print first 5 rows as samples of the dataset including headings
print(dataset.head())
