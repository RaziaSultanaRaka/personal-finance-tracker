import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from data_entry import get_date, get_category, get_amount, get_payment_method, get_description


class CSV:
    CSV_FILE = 'personal_finance_tracker.csv'
    COLOUMNS = ['Date', 'Category', 'Amount','Payment Method','Description']  
    FORMAT =  '%d-%m-%Y'
    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLOUMNS)
            df.to_csv(cls.CSV_FILE,index=False)    
                   
    @classmethod
    def add_entry(cls,date,category,amount,payment_method,description):
        new_entry = {
            'Date': date,
            'Category': category,
            'Amount': amount,
            'Payment Method': payment_method,
            'Description': description
        }
        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLOUMNS)
            writer.writerow(new_entry)
            print('Entry added successfully')
            
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"]= pd.to_datetime(df["Date"], format=CSV.FORMAT)
        
        start_date= datetime.strptime(start_date,CSV.FORMAT)
        end_date= datetime.strptime(end_date,CSV.FORMAT)
        
        #apply to the rows inside of a dataframe & filter diffrent element
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df =df.loc[mask]
        
        if filtered_df.empty:
            print("No transactions found in the given data range.")
        else:
            print(f'Transactions {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}')
            print(filtered_df.to_string(
                index= False, formatters={"date": lambda x:x.strftime(CSV.FORMAT)}
            ))
            
            total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
            total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
            saved_amount = total_income - total_expense
            
            print("\nOverview:")
            print(f'Total Income: ${total_income:.2f}')
            print(f'Total Expense: ${total_expense:.2f}')
            print(f'SAVED: ${(saved_amount):.2f}')
            
        return filtered_df
                    
#CALL A FUNCTION FROM data_entry.py
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date(dd-mm-yyyy) or enter today's date: ", allow_default=True) 
    category= get_category()  
    amount=  get_amount()
    payment_method= get_payment_method() 
    desription= get_description() 
    CSV.add_entry(date,category,amount,payment_method,desription)   

#graph >>>>>
def plot_transactions(df):
    df.set_index('date', inplace=True)
    
    income_df = (
        df[df['Category'] == 'Income']
        .resample("D")
        .sum()
        .reindex(df.index, fill_value =0)
    )
    expense_df = (
        df[df['Category'] == 'Expense']
        .resample("D")
        .sum()
        .reindex(df.index, fill_value =0)
    )
   
    plt.figure(figsize=(10, 5))
    width =0.5  # Bar width
    plt.bar(income_df.index, income_df['Amount'], width=width, label='Income', color='green')
    plt.bar(expense_df.index, expense_df['Amount'], width=width, bottom=income_df['Amount'], label='Expense', color='red')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Income and Expense Breakdown')
    plt.legend()
    plt.grid(True)  
    plt.show()

#.................... MAIN..................... 

def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and overview for a certain time period.")
        print("3. Exit.")
        
        option = input("Pick an option (1-3): ")
        if option == '1':
            add()
            
        elif option == '2':
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date,end_date)
            
            if input("Do you want to see a plot? (y/n)").lower()=='y':
                plot_transactions(df)
                
        elif option == '3':
            print("Exiting....")
            break
        else:
            print("Invalid option.\nEnter 1/2 or 3.")
            

if __name__ == '__main__':
    main()

#meow_