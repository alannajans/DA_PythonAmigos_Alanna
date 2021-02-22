#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse the total number of visitors to Singapore from the top 3 countries in the South East Asia region
#Name:< Alanna Janssens >
#Group Name: < pythonamigos >
#Class: < PN2004L >
#Date: < 9 feb 2021 >
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#importing pandas into dataframe / df
import pandas as pd
import matplotlib.pyplot as pit

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):
    #show specific country dataframe
    sortCountry()

#########################################################################
#CLASS Branch: End of Code
#########################################################################
#PART 1
def sortCountry():

  #load excel data (CSV format) to dataframe - 'df'
  df = pd.read_csv('MonthlyVisitors.csv')

  #creating list of countries for the chart
  country = ['Brunei Darussalam', 'Indonesia', 'Malaysia', 'Philippines', 'Thailand', 'Viet Nam', 'Myanmar']

  #displaying countries in SEA region and the given year for the region (1998 - 2008)
  print("\n\n" + "The countries in the region are shown below. With the given year range: 1998 - 2008" + "\n")

  #assigning specific columns to region 
  #print region to display countries , year and month
  #using iloc to select specific columns for the year 1998 - 2008 as well as the rows for the year, month and countries
  region = df.iloc[240:372, 0:9]
  print(region)
  
  #selecting only the countries for calculation purposes in the next step
  countries = df[[' Brunei Darussalam ', ' Indonesia ', ' Malaysia ', ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ']][240:372]
  
  #creating a total to calculate the number of visitors from each country in the region
  #using axis=0 to calculate the years as axis=0 is used to calculate the rows 
  totalVisitors = countries.sum(axis=0)
  print("\n" + "The total number of visitors from each country in SEA region are as shown:" + "\n") 
  #display the countries as well as the total visitors to show
  print(totalVisitors)

  #sorting the top 3 countries in descending order
  #to ensure that it is descending, ascending has to equal to False
  top7countries = totalVisitors.sort_values(ascending=False)

  #display the top 3 countries that visited Singapore over the span of 10 years
  #using .head() to display top 3 countries this function returns the first number of rows 
  print("\n" + "The Top 3 countries of visitors to Singapore from the selected region over the span of 10 years is:" + "\n")
  print(top7countries.head(3))

  #########################################################################
  #Pie-chart to display the top 3 countries
  #########################################################################

 #importing matplotlib so that the pie chart can be seen in console 
  activities = country
  slices = top7countries
  colours = ['r', 'g', 'm', 'b', 'o', 'p', 'y']

  pit.pie(slices,
         labels=activities,
         startangle=90,
         shadow=True,
         explode=(0.2, 0, 0, 0, 0, 0 ,0),
         autopct='%1.2f%%')

  pit.legend()

  pit.show()

  #########################################################################
  #Pie-chart to display the top 3 countries: End of code
  #########################################################################


 
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')
  

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################

