# Bigger Pockets ROI Calculator

import os
import time

class ROIcalc():
    """
    This class will function as a return on investment calculator.
    It does not require any initial attributes.
    All inputs are expected to be integers.
    """

    # Input and calculate total income from property.
    def totalIncome(self):
        print("First, let's calculate your total income. ")
        self.rental_income = int(input('How much do you expect in rental income? '))
        self.misc_income = int(input('Please enter any other amount of misc income you expect from your rental property. '))
        self.total_monthly_income = (self.rental_income + self.misc_income)
        os.system("clear")
        print(f"Great, looks like you'll have about: ${self.total_monthly_income} in monthly income.")
        time.sleep(3)
        os.system("clear")

    # Input and calculate total expenses for property.
    def totalExp(self):
        print("Next, let's calculate your total monthly expenses. ")
        time.sleep(2.5)
        os.system("clear")
        self.tax = int(input('Enter amount for monthly property taxes: '))
        os.system("clear")
        self.insurance = int(input('Enter amount for monthly property insurance: '))
        os.system("clear")
        self.utilities = int(input('Enter amount for monthly utilities: '))
        os.system("clear")
        self.hoa = int(input('Enter amount for monthly HOA (if applicable): '))
        os.system("clear")
        self.lawn_care = int(input('Enter amount for monthly lawn care: '))
        os.system("clear")
        self.vacancy = int(input('Enter amount for monthly vacancy savings: '))
        os.system("clear")
        self.repairs = int(input('Enter amount for monthly repair savings: '))
        os.system("clear")
        self.capex = int(input('Enter amount for monthly CapEx savings: '))
        os.system("clear")
        self.management = int(input('Enter amount for property manager payment: '))
        os.system("clear")
        self.mortgage = int(input('Enter amount for monthly property mortgage: '))
        os.system("clear")
        self.total_monthly_exp = (self.tax + self.insurance + self.utilities + self.hoa + self.lawn_care + self.vacancy + self.repairs +
                             self.capex + self.management + self.mortgage)
        print(f"Okay, so your estimated total monthly expenses are: ${self.total_monthly_exp}")
        time.sleep(3)
        os.system("clear")
        
    # Auto calculates cash flow from previous two functions.    
    def cashFlow(self):
        self.total_cash_flow = (self.total_monthly_income - self.total_monthly_exp)
        print(f"Which means your estimated total monthly Cash Flow is: ${self.total_cash_flow}")
        time.sleep(3)
        os.system("clear")

    # Input and calculate total investment for property.
    def totalInvestment(self):
        print("Lastly, let's estimate your total investment. ")
        time.sleep(2.5)
        os.system("clear")
        self.down_payment = int(input('How much was your down payment? '))
        os.system("clear")
        self.closing_costs = int(input('How much were your closing costs? '))
        os.system("clear")
        self.rehab_budget = int(input('How much did you spend on initial rehab for the home? '))
        os.system("clear")
        self.misc = int(input('How much did you spend on any other miscellaneous expenses? '))
        os.system("clear")
        self.total_investment = (self.down_payment + self.closing_costs + self.rehab_budget + self.misc)
        print(f"Great, so your total investment was about: ${self.total_investment}")
        time.sleep(3)
        os.system("clear")

    # Calculates ROI by using totals above and some basic math conversions.
    def cashOnCashROI(self):
        print("Calculating your cash on cash ROI now...")
        time.sleep(2.5)
        self.annual_cashflow = (self.total_cash_flow * 12)
        self.cashROI = (self.annual_cashflow/self.total_investment)
        self.ROIconversion = round(self.cashROI * 100, 2)
        print(f"From the information provided, your total Cash on Cash ROI would be an estimated: {self.ROIconversion}%")


investor = ROIcalc()

def activateROIcalc():
    """
    This function is to activate the ROI calculator.
    Uses a while loop until the user no longer wants to calculate potential cash ROI.
    """

    while True:
        response = input("Hello, would you like to calculate your estimated ROI on a property? Yes/No ")
        if response.lower() == 'no':
            print('Thank you. ')
            break
        elif response.lower() == 'yes':
            investor.totalIncome()
            investor.totalExp()
            investor.cashFlow()
            investor.totalInvestment()
            investor.cashOnCashROI()
        else:
            print('I am sorry, that is an invalid response. Please try again.')

activateROIcalc()