""" Write a Python program to get the latest number of confirmed deaths and recovered people of Novel Coronavirus (COVID-19) cases Country/Region - Province/State wise""" 
# importing Pandas and granting it an alias pd
import  pandas as pd

#hitting url for dataset
dataset_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"

#reading the dataset as a csv file format
dataset = pd.read_csv(dataset_url)

#print first 5 rows as samples of the dataset including headings
# print(dataset.head())


# Formatting the dataset as desired
formatted_dataset = dataset.groupby(['Country/Region','Province/State'])['Confirmed','Deaths','Recovered','Last Update'].max()
pd.set_option('display.max_rows',None)
print(formatted_dataset.sort_values( by='Country/Region',ascending=True,kind="mergesort"))