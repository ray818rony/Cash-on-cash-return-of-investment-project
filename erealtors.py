
#
class CalcRoi:
    def __init__(self, income_tote, expense_tote, cashflow_tote, Roi):
        self.income_tote = income_tote
        self.expense_tote = expense_tote
        self.cashflow_tote = cashflow_tote
        self.Roi = Roi

    def addingIncs(self):
        rent = int(input("How much you get for all your rents? "
                         "> "))
        vending = int(
            input("If you have any vending machines; How much you make a month? "
                  "> "))

        other = int(
            input("if you have any other sorts of income please enter it here. "
                  "> "))

        income_tote = int(rent + vending + other)
        print(f"for your income you have a $ {income_tote} in total. ")

    def addingExpes(self):
        taxes = int(input("please enter the total of your property taxes "
                          "> $ "))

        insurance = int(
            input("If you have insurance, please enter the total here "
                  "> $ "))

        vacancy = int(input(
            "In case you dont have a tenant how much do you have for that situation? "
            "> $ "))

        mortgage = int(input("How much do you pay for Mortgage? "
                             "> $ "))

        repairs = int(input('How much do you pay for monthly repairs? '
                            '> $ '))

        Utilities = int(input('How much do you pay for your utilities? '
                              '> $ '))

        expense_tote = int(taxes + insurance + vacancy +
                           mortgage + repairs + Utilities)

        print(f"for your expenses you have a $ {expense_tote} total. ")

    def cashflow(self):
        cf_tote = self.income_tote - self.expense_tote
        cashflow_tote = int(cf_tote) * 12
        print(f"your Cash Flow is {cashflow_tote}")

    def cocRoi(self):
        down = int(input("How much money you had as a Down payment? "
                         "> $ "))
        closing = int(input("Any other payments as a closing coast? "
                            "> $ "))
        rehab = int(
            input("did you pay anything to fix the property when you first had it?"
                  "> $ "))
        misc = int(input("Any other payments you payed around that time? "
                         "> $ "))

        Roi = down + closing + rehab + misc
        print(f"Your total investments are ${Roi} in dollars")

    def cashOnCashROI(self):
        Roi_tote = self.cashflow_tote / self.Roi
        return_invest = Roi_tote * 100
        return_invest = int(return_invest)
        print(f"Your Cash on Cash return on Investment is %{return_invest}")
