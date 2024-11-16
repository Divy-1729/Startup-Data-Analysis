import pandas
pandas.set_option('display.width', 400)
pandas.set_option("display.max_columns", 11)
pandas.set_option('display.max_rows', 2500)

# Search By Startup Name
def SearchByStartupName():
   df = pandas.read_csv('Unicorn_Clean.csv')
   tempdf = pandas.DataFrame(columns=df.columns)
   mname = input('Please Enter Startup Name Or Some Part Of It: ')
   for i in df.index:
       if mname.lower() in df.at[i, 'Company'].lower():
           tempdf.loc[i] = df.loc[i]
   print()
   print(tempdf)
   print()
   input('Press Enter To Continue.......')

# Search By Industry
def SearchByIndustry():
   df = pandas.read_csv('Unicorn_Clean.csv')
   tempdf = pandas.DataFrame(columns=df.columns)
   industry = input('Enter Name Of Industry Or Some Part Of It: ')
   for i in df.index:
       if industry.lower() in df.at[i, 'Industry'].lower():
           tempdf.loc[i] = df.loc[i]
            print()
   print(tempdf)
   print()
   input('Press Enter To Continue.......')


# Search By Startup Country
def SearchByStartupCountry():
   df = pandas.read_csv('Unicorn_Clean.csv')
   tempdf = pandas.DataFrame(columns=df.columns)
   mdirector = input('Enter Name Of Country Or Some Part Of It:')
   for i in df.index:
       if mdirector.lower() in df.at[i, 'Country'].lower():
           tempdf.loc[i] = df.loc[i]
   print()
   print(tempdf)
   print()
   input('Press Enter To Continue.......')

#Search StartUp by Investor
def SearchByInvestor():
   df = pandas.read_csv('Unicorn_Clean.csv')
   tempdf = pandas.DataFrame(columns=df.columns)
   mdirector = input('Enter Name Of Investor or Some Part of it: ')
   for i in df.index:
       if mdirector.lower() in df.at[i, 'Investor'].lower():
           tempdf.loc[i] = df.loc[i]
   print()
   print(tempdf)
   print()
   input('Press Enter To Continue.......')

def LatestStartup():
   df = pandas.read_csv('Unicorn_Clean.csv')
   tempdf = pandas.DataFrame(columns=df.columns)
   mdirector = input('Enter Year of Startup you want to see: ')
   df['year'] = df['Date Joined'].str[-4:]
   for i in df.index:
       if mdirector.lower() in df.at[i, 'year']:
           tempdf.loc[i] = df.loc[i]
   print()
   print(tempdf)
   print()
   input('Press Enter To Continue.......')

def SearchbyCity():
   df = pandas.read_csv('Unicorn_Clean.csv')
   tempdf = pandas.DataFrame(columns=df.columns)
   mdirector = input('Enter Name Of City or Some Part of it: ')
   for i in df.index:
       if mdirector.lower() in df.at[i, 'City'].lower():
           tempdf.loc[i] = df.loc[i]
   print()
   print(tempdf)
   print()
   input('Press Enter To Continue.......')
