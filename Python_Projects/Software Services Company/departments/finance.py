class finance():
    current_revenue = 1000000000

    def income(income_source):
        finance.current_revenue += income_source
        print("$" + str(income_source) + " added to revenue")
        print("Current renewed revenue: " + str(finance.current_revenue))

    def expense(expense_source):
        finance.current_revenue -= expense_source
        print("$" + str(expense_source) + " deducted from revenue due to expense")
        print("Current renewed revenue: " + str(finance.current_revenue))

    def revenue_report():
        print("Current Revenue: " + str(finance.current_revenue))