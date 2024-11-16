import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime as dt
import pandas

def ShowCountryWiseStartup():
   df = pandas.read_csv('Unicorn_Clean.csv')
   g = df.groupby('Country')
   s = g['Company'].count()
   x = list(s.index)
   y = list(s.values)
   plt.figure(figsize=(12, 6))
   plt.bar(x, y, width=.4)
   plt.xticks(rotation=90)
   plt.title('Number Of Startups In Each Country')
   plt.xlabel('Country---------------------------------------->')
   plt.ylabel('No Of Startups--------------------------------->')
   plt.yticks(range(0, 651, 50))
   for i in range(len(y)):
      plt.text(i, y[i] + 1, y[i], ha='center', bbox=dict(facecolor='gray'))
   plt.tight_layout()
   plt.show()

def ShowInvestPerStartup():
   df = pandas.read_csv('Unicorn_Clean.csv')
   s = df["Investor"].value_counts()
   a = np.array([1,2,3,4,5])
   plt.figure(figsize=(12, 6))
   plt.hist(s,bins=a, color='olive', edgecolor='k')
   plt.xticks(a)


 plt.title('No of startups in range of investors')
 plt.xlabel('No of investors------------------------>')
 plt.ylabel('No Of Startups----------------------------------->')
 plt.show()
def ShowYearswithMaxStartups():
 df = pandas.read_csv('Unicorn_Clean.csv')
 df['year'] = df['Date Joined'].str[-4:]
 g = df.groupby('year')
 s = g['Company'].count()
 s = s.sort_values(ascending=False)
 s = s.head(10)
 plt.figure(figsize=(12, 6))
 plt.bar(s.index, s, width=.4)
 plt.xticks(rotation=90)
 plt.title('Startups By Year')
 plt.xlabel('Years')
   plt.ylabel('Number of Startups')
   plt.tight_layout()
   y = list(s)
   for i in range(len(y)):
      plt.text(i, y[i] + 1, y[i], ha='center', bbox=dict(facecolor='gray'))
   plt.show()

def ShowMostVal():
   df = pandas.read_csv('Unicorn_Clean.csv')
   s = df.sort_values(by = 'Valuation',ascending=False)
   s = s.head(20)
   plt.figure(figsize=(12, 6))
   plt.bar(s.Company, s.Valuation, width=.4)
   plt.xticks(rotation = 90)
 
 plt.title('Top 10 Startups with most Valuation')
 plt.xlabel('Valuation($B)')
 plt.ylabel('Name of Startups')
 plt.tight_layout()
 y = list(s)
 plt.show()

def ShowCitiesWithMostStartups():
   df = pandas.read_csv('Unicorn_Clean.csv')
   g = df.groupby('City')
   s = g['Company'].count()
   s = s.sort_values(ascending=False)
   s = s.head(10)
   plt.figure(figsize=(12, 6))
   plt.bar(s.index, s, width=.4)
   plt.xticks(rotation=90)
   plt.title('Top 10 Cities with Most Startups')
   plt.xlabel('Cities')
   plt.ylabel('Number of Startups')
   plt.tight_layout()
   y = list(s)
   for i in range(len(y)):
      plt.text(i, y[i] + 1, y[i], ha='center', bbox=dict(facecolor='gray'))
   plt.show()

def ShowInvestedinMaxValStartups():
   df = pandas.read_csv('Unicorn_Clean.csv')
   g = df.groupby('Investor')
   s = g['Company'].count()

s = s.sort_values(ascending=False)
   s = s.head(10)
   plt.figure(figsize=(12, 6))
   plt.bar(s.index, s, width=.4)
   plt.xticks(rotation=90)
   plt.title('Top 10 Investors')
   plt.xlabel('Investor Name')
   plt.ylabel('Total Number of Companies Invested')
   plt.tight_layout()
   y = list(s)
   for i in range(len(y)):
      plt.text(i, y[i] + 1, y[i], ha='center', bbox=dict(facecolor='gray'))
   plt.show()
def ShowIndustryWise():
   df = pandas.read_csv('Unicorn_Clean.csv')
   g = df.groupby('Industry')
   s = g['Company'].count()
   s = s.sort_values(ascending=False)
   plt.figure(figsize=(12, 6))
   plt.bar(s.index, s, width=.4)
   plt.xticks(rotation=90)
   plt.title('No of Startups per industry')
   plt.xlabel('Industry Name')
   plt.ylabel('Total Number of Companies')
   plt.tight_layout()
   y = list(s)
   for i in range(len(y)):
       plt.text(i, y[i] + 1, y[i], ha='center', bbox=dict(facecolor='gray'))
   plt.show()


s = s.sort_values(ascending=False)
   s = s.head(10)
   plt.figure(figsize=(12, 6))
   plt.bar(s.index, s, width=.4)
   plt.xticks(rotation=90)
   plt.title('Top 10 Investors')
   plt.xlabel('Investor Name')
   plt.ylabel('Total Number of Companies Invested')
   plt.tight_layout()
   y = list(s)
   for i in range(len(y)):
      plt.text(i, y[i] + 1, y[i], ha='center', bbox=dict(facecolor='gray'))
   plt.show()

def ShowIndustryWise():
   df = pandas.read_csv('Unicorn_Clean.csv')
   g = df.groupby('Industry')
   s = g['Company'].count()
   s = s.sort_values(ascending=False)
   plt.figure(figsize=(12, 6))
   plt.bar(s.index, s, width=.4)
   plt.xticks(rotation=90)
   plt.title('No of Startups per industry')
   plt.xlabel('Industry Name')
   plt.ylabel('Total Number of Companies')
   plt.tight_layout()
   y = list(s)
   for i in range(len(y)):
       plt.text(i, y[i] + 1, y[i], ha='center', bbox=dict(facecolor='gray'))
   plt.show()



