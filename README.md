# Personal Finance Tracker

## Project Overview
This Personal Finance Tracker is a Python-based application designed to help users manage and track their personal finances. It allows users to input financial data, categorize transactions by payment methods (cash, bKash, Nagad, credit card), and export reports for further analysis.

## Features
- **Data Entry**: Record and categorize transactions with details like payment method.
- **Payment Methods Supported**:
  - **Cash**
  - **bKash**
  - **Nagad**
  - **Credit Card**
- **Main Application**: Processes and analyzes the entered data.
- **CSV Storage**: Transactions are stored in a CSV file for easy access and manipulation.

## Files in the Repository
- **`main.py`**: The main script that processes and analyzes the data.
- **`data_entry.py`**: A script used for entering and categorizing transactions by payment method.
- **`personal_finance_tracker.csv`**: A CSV file where all the financial transactions, along with their payment methods, are recorded.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/personal-finance-tracker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd personal-finance-tracker
    ```
3. Ensure you have Python installed. 
## Usage
1. Use `data_entry.py` to input your transactions into the CSV file, specifying the payment method (cash, bKash, Nagad, or credit card).
    ```bash
    python data_entry.py
    ```
    Example of entering a transaction:
    ```bash
    python data_entry.py --amount 500 --category "Groceries" --method "bKash"
    ```
2. Run `main.py` to analyze and process the data from the CSV, generating reports based on payment methods and categories.
    ```bash
    python main.py
    ```


##  Example Output:

### Transactions Overview
Below is a summary of the transactions recorded in the `personal_finance_tracker.csv` file.

### Sample Transactions:
| Date       | Category | Amount | Payment Method | Description         |
|------------|----------|--------|----------------|---------------------|
| 2024-09-01 | Income   | 2000   | bKash          | Salary              |
| 2024-09-02 | Expense  | 1200   | Credit Card    | Electricity bill    |
| 2024-09-03 | Expense  | 800    | Cash           | Dinner at a restaurant |
| 2024-09-04 | Expense  | 200    | Nagad          | Taxi fare           |
| 2024-09-05 | Income   | 500    | Cash           | Freelance payment   |
## Example Workflow
1. Input your daily transactions using `data_entry.py`, specifying the payment method.
2. Analyze your spending habits by running `main.py`, which reads from `personal_finance_tracker.csv`.
## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




