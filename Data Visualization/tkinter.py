import pandas
def ShowData():
   df = pandas.read_csv("Unicorn_Clean.csv")
   print(df)

import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg

def UpdateCsv():
   # Read the CSV file
   df = pd.read_csv('Unicorn_Clean.csv')

   def showitem(event):
       # Use 'record' variable to retrieve selected row values
       record = itemsTable.item(itemsTable.focus())

       # Update Entry widgets with the selected row values

       txtCompany.delete(0, tk.END)
       txtCompany.insert(0, record['values'][0])

       txtValuation.delete(0, tk.END)
       txtValuation.insert(0, record['values'][1])

       txtDateJoined.delete(0, tk.END)
       txtDateJoined.insert(0, record['values'][2])

       txtCountry.delete(0, tk.END)
       txtCountry.insert(0, record['values'][3])

  txtCity.delete(0, tk.END)
 txtCity.insert(0, record['values'][4])

 txtIndustry.delete(0, tk.END)
 txtIndustry.insert(0, record['values'][5])

 txtInvestor.delete(0, tk.END)
 txtInvestor.insert(0, record['values'][6])

 def UpdateCSV():
 # Get the current index from the selected row
 confirm = msg.askyesno('Confirm', 'Are you sure?')
 if confirm == True:
 currInd = itemsTable.index(itemsTable.focus())

 # Get values from Entry widgets
 company = txtCompany.get()
 valuation = txtValuation.get()
 date_joined = txtDateJoined.get()
 country = txtCountry.get()
 city = txtCity.get()
 industry = txtIndustry.get()
 investor = txtInvestor.get()

 selectedrow = itemsTable.focus() # Get selected row
 itemsTable.delete(selectedrow)
 itemsTable.insert('', currInd, values=[company, valuation, date_joined, country, city, industry, investor])
 # Update the DataFrame with the new values
 df.at[currInd, 'Company'] = company
 df.at[currInd, 'Valuation'] = valuation
 df.at[currInd, 'Date Joined'] = date_joined

df.at[currInd, 'Country'] = country
 df.at[currInd, 'City'] = city
 df.at[currInd, 'Industry'] = industry
 df.at[currInd, 'Investor'] = investor

 # Save the updated DataFrame to CSV
 df.to_csv('Unicorn_Clean.csv', index=False)

 msg.showinfo('Message', 'CSV File Updated !')

 # Create the main window
 df = pandas.read_csv('Unicorn_Clean.csv')
 win = tk.Tk()
 win.title('Unicorn Data')
 width = 1500 # Width
 height = 668 # Height

 screen_width = win.winfo_screenwidth() # Width of the screen
 screen_height = win.winfo_screenheight() # Height of the screen

 x = (screen_width // 2) - (width // 2)
 y = (screen_height // 2) - (height // 2)
   win.geometry('1500x668+%d+%d' % (x, y - 50))
   win.resizable(False, False)

   # Configure Treeview style
   style = ttk.Style(win)
   style.theme_use("clam")
   style.configure('Treeview', background='silver', foreground='black', rowheight=40, fieldbackground='silver', font=('Arial', 11))
   style.configure('Treeview.Heading', font=('Arial', 11))
   style.map('Treeview', background=[('selected', 'green')])

   
itemsTable = ttk.Treeview(win, style='Treeview', height=8) itemsTable.bind('<ButtonRelease-1>', showitem)

   treeScrollvert = ttk.Scrollbar(win)
   treeScrollvert.configure(command=itemsTable.yview)
   itemsTable.configure(yscrollcommand=treeScrollvert.set)
   treeScrollvert.pack(side='right', fill='both')

   # Create vertical scrollbar
   treeScrollvert = ttk.Scrollbar(win, command=itemsTable.yview)
   itemsTable.configure(yscrollcommand=treeScrollvert.set)
   treeScrollvert.pack(side='right', fill='y')

   for item in itemsTable.get_children():
       itemsTable.delete(item)

   for ri, rd in df.iterrows():
       itemsTable.insert('', 'end', values=list(rd))

   itemsTable["columns"] = ("0", "1", "2", "3", "4", "5", "6")
   itemsTable['show'] = 'headings'

   # Add columns to the Treeview
   itemsTable.heading("0", text="Company")
   itemsTable.heading("1", text="Valuation")
   itemsTable.heading("2", text="Date Joined")
   itemsTable.heading("3", text="Country")
   itemsTable.heading("4", text="City")
   itemsTable.heading("5", text="Industry")
   itemsTable.heading("6", text="Investor")

   # Set column widths
 itemsTable.column("0", width=200)
 itemsTable.column("1", width=100)
 itemsTable.column("2", width=100)
 itemsTable.column("3", width=100)
 itemsTable.column("4", width=100)
 itemsTable.column("5", width=200)
 itemsTable.column("6", width=200)

 itemsTable.place(x=20, y=20)
 # Create labels and Entry widgets for data entry

   lblCompany = tk.Label(win, text='Company', font='Arial 11')
   txtCompany = tk.Entry(win, font='Arial 11')
   lblCompany.place(x=20, y=400)
   txtCompany.place(x=130, y=400)

   lblValuation = tk.Label(win, text='Valuation', font='Arial 11')
   txtValuation = tk.Entry(win, font='Arial 11')
   lblValuation.place(x=20, y=430)
   txtValuation.place(x=130, y=430)
  lblDateJoined = tk.Label(win, text='Date Joined', font='Arial 11')
   txtDateJoined = tk.Entry(win, font='Arial 11')
   lblDateJoined.place(x=20, y=460)
   txtDateJoined.place(x=130, y=460)

   lblCountry = tk.Label(win, text='Country', font='Arial 11')
   txtCountry = tk.Entry(win, font='Arial 11')
   lblCountry.place(x=20, y=490)
   txtCountry.place(x=130, y=490)


   lblCity = tk.Label(win, text='City', font='Arial 11')
   txtCity = tk.Entry(win, font='Arial 11')
   lblCity.place(x=20, y=520)
   txtCity.place(x=130, y=520)

   lblIndustry = tk.Label(win, text='Industry', font='Arial 11')
   txtIndustry = tk.Entry(win, font='Arial 11')
   lblIndustry.place(x=20, y=550)
   txtIndustry.place(x=130, y=550)

   lblInvestor = tk.Label(win, text='Investor', font='Arial 11')
   txtInvestor = tk.Entry(win, font='Arial 11')
   lblInvestor.place(x=600, y=400)
   txtInvestor.place(x=710, y=400)

   btnSave = tk.Button(win, text='Update CSV', width=25,
                       background='RED', foreground='WHITE', font='Arial 12 bold',
                       command=UpdateCSV)
   btnSave.place(x=20, y=600)
   win.mainloop()

