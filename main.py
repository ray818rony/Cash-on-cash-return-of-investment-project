from erealtors import CalcRoi

import time

test = CalcRoi

print("""

Hello My friend, My name is Lana, Short for Laniakea.
think of me as Clippy from MS.office, But a bit smarter ;)
""")
time.sleep(0)
# time is 4.5
while True:
    answer = input(
        "Would you like to start the 4 squared method to "
        "calculate your Cash on Cash return? yes or Learn more? "
        ">")
    if answer == "yes":
        print("perfect, I have some questions about your income.")
        test.addingIncs(answer)
        test.addingExpes(answer)
        test.cocRoi(answer)
        test.cashOnCashROI(answer)

    elif answer == "learn more":
        print("""
            In this method I would use 3 type of information to calculate 
        your cash on cash return on investments that is also know as R.O.I.
        we would start with your income.
        1- Amount of all of your property rental income.
        2- The amount of money you get from any Vending machines, that 
           are on your property. 
        3- Check if you have any other forms of Income.
        I will use those numbers for the total of all your monthly income.""")
        time.sleep(0.0)
        # Time is 10 secs
        print("""
            Then we will go through your expenses 
        1- Taxes.
        2- How much you pay for insurance.
        3- Vacancy: in-case you had a vacant property how much have you saved for it.
        4- Mortgage.
        5- Any repairs per month.
        6- Check weather you pay for Utility or not.
        After getting all your expenses I would be able to calculate your Cash Flow.
        That is very important for the next step.
        """)
        time.sleep(0.0)
        # time is 10 secs
        print("""
            In the final phase. I will collect your investment expenses:
        1- How much you paid for your down-payment.
        2- If you had any extra expenses at the time of finalizing the owner-
        ship of your property.
        3- I will check if you added any expenses to repair the property.
        4- And I will check if you had any extra Miscellaneous expenses at the time.
        That is when i will be ready to give you a Final Percentage of Your
        Cash On Cash R.O.I.
        """)

    else:
        print("sorry I don't I understand that one ")
