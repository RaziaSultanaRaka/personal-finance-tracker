from datetime import datetime

date_format = '%d-%m-%Y'
CATEGORIES = {'I': 'Income', 'E': 'Expense'}
PAYMENTS = {'M': 'Cash', 'B': 'Bkash', 'N': 'Nagad', 'C': 'Credit Card'}

#DATE
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print('Invalid date format. Please enter date in dd-mm-yyyy format')
        return get_date(prompt, allow_default)
    

#CATEGORY
def get_category():
    category =input("Enter the category('I' for Income / 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print('Invalid category. Please enter "I" for Income or "E" for Expense')
    return get_category()


#AMOUNT
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <=0:
            raise ValueError("Amount Must be a non-negative non-zero number")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
        

#PAYMENT METHOD
def get_payment_method():
    payment_method =input("Enter the payment method('M' for Cash / 'B' for Bkash / 'N' for Nagad / 'C' for Credit Card): ").capitalize()
    if payment_method in PAYMENTS:
        return PAYMENTS[payment_method]
    print('Invalid payment method. Please enter "M" for Cash, "B" for Bkash, "N" for Nagad or "C" for Credit Card')
    return get_payment_method()

#DESCRIPTION
def get_description():
    return input("Enter a description(optional): ")
