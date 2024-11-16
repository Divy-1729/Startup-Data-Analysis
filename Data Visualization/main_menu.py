import DataFunctions
import ChartFunctions
import SearchFunctions

# Show Data Analysis Menu
def DataAnalysisMenu():
   while True:
       print()
       print('-----------------------------')
       print('DATA ANALYSIS')
       print('----------------------------')
       print('Show cities With Most No Of startups : Press 0')
       print("Show the investors who have invested in maximum number of startups : Press 1")
       print("Show years With Most Number Of startups : Press 2")
       print('To visualize startups with most valuation: Press 3')
       print('To visualize startup by country : Press 4')
       print('To visualize no of investors per startup : Press 5')
       print('To visualize no of startups per industry, Press 6')
       print('To exit : Press 7')
       print()

       ch = int(input('Enter Your Choice: '))
       if ch == 0:
           ChartFunctions.ShowCitiesWithMostStartups()
       elif ch == 1:
           ChartFunctions.ShowInvestedinMaxValStartups()
       elif ch == 2:
           ChartFunctions.ShowYearswithMaxStartups()

        elif ch == 3:
      ChartFunctions.ShowNoOfMoviesInEachBudgetRange()
    elif ch == 4:
      ChartFunctions.ShowMoviesWithMostScreens()
    elif ch == 5:
      ChartFunctions.ShowNoOfMoviesInEachGenre()
    else:
      break

# Search Menu
def SearchMenu():
   while True:
       print()
       print('-----------------------------')
       print('Search')
       print('----------------------------')
       print('1. Search by Startup Name')
       print('2. Search By Startup Country')
       print('3. Search by Industry')
       print('4. Search by Investor')
       print('5. Search by latest date')
       print('6. Search by city')
       print('10. Exit')
       print()

       ch = int(input('Enter Your Choice: '))
       if ch == 1:
           SearchFunctions.SearchByStartupName()
       elif ch == 2:
           SearchFunctions.SearchByStartupCountry()
       elif ch == 3:
           SearchFunctions.SearchByIndustry()
       elif ch==4:
           SearchFunctions.SearchByInvestor()
       elif ch==5:
           SearchFunctions.LatestStartup()
       elif ch==6:
           SearchFunctions.SearchbyCity()
       else:
           break
# Show Main Menu
while True:
   print()
   print('-----------------------------')
   print('Startups DATA ANALYSIS PROJECT')
   print('----------------------------')
   print('1. Show All Data')
   print('2. Show Data Analysis')
   print('3. Search Startup Data')
   print('4. Update Startup Data')
   print('0. Exit')
   print()

   ch = int(input('Enter Your Choice: '))
   if ch == 1:
       DataFunctions.ShowData()
   elif ch == 2:
       DataAnalysisMenu()
   elif ch == 3:
       SearchMenu()
   elif ch == 4:
       DataFunctions.UpdateCsv()
   else:
       break
