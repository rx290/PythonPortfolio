"""Write a Python program to get the latest number of confirmed, deaths, recovered and active cases of Novel Coronavirus (COVID-19) Country wise. """ 

# importing Pandas and granting it an alias pd
import  pandas as pd

#hitting url for dataset
dataset_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv"

#reading the dataset as a csv file format
dataset = pd.read_csv(dataset_url)

#print first 5 rows as samples of the dataset including headings
# print(dataset.head())


# Formatting the dataset as desired
formatted_dataset = dataset[['Country/Region','Province/State','Confirmed','Deaths','Recovered','Last Update']]
formatted_dataset['Active'] = formatted_dataset['Confirmed'] - formatted_dataset['Deaths'] - formatted_dataset['Recovered']

print(formatted_dataset.sort_values( by='Country/Region',ascending=True,kind="mergesort"))