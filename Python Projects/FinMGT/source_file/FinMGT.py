#!/usr/bin/env python
# coding: utf-8

# In[1]:


def allsheet_info():
    # Make all updates monthlylog sheet for now
    import xlsxwriter
    workbook = xlsxwriter.Workbook(r'C:\Users\sun\OneDrive\Documents\Main_Work\Programming\Python Projects\FinMGT\source_file\FinMgt21.xlsx')
    worksheet = workbook.add_worksheet('Monthly Log')
    underline_format = workbook.add_format({'underline': True})
    
    # Monthly Log sheet Portion
    # write month numbers 1-12
    for n in range(1,13):
        worksheet.write(0,n,n)

    worksheet.write(0,0,'Month')
    worksheet.write(2,0,'Incomes',underline_format)
    worksheet.write(3,0,'Salary')
    worksheet.write(4,0,'Other')
    worksheet.write(5,0,'Total Inc.')
    worksheet.write(7,0,'Expenses',underline_format)
    worksheet.write(8,0,'Basic Exp.')
    worksheet.write(9,0,'Extra Exp.')
    worksheet.write(10,0,'Total Exp.')
    worksheet.write(12,0,'Balance',underline_format)
    worksheet.write(13,0,'Total Bal.')

    # Assign values from monthlylog_input
    current_month,monthly_salary,other_income,basic_exp,extra_exp = monthlylog_userinput()
    for i in range(1,13):
        if int(current_month) == i:
            worksheet.write(3,i,int(monthly_salary))
            worksheet.write(4,i,int(other_income))
            worksheet.write(5,i,int(monthly_salary)+int(other_income))
            worksheet.write(8,i,int(basic_exp))
            worksheet.write(9,i,int(extra_exp))
            worksheet.write(10,i,int(basic_exp)+int(extra_exp))
            worksheet.write(13,i,int(monthly_salary)+int(other_income)-int(basic_exp)-int(extra_exp))
            
    # Investment Debt sheet Portion
    worksheet = workbook.add_worksheet('InvestmentDebt')    
    current_year = input('Enter current year: ')
    pv = input("Enter pv: ")
    r = input("Enter interest rate (%): ")
    t = input("Enter number of years: ")
    c = float(pv) / ((1 - (1 / (1+float(r)/100)**float(t))) / (float(r)/100))
    
    worksheet.write(0,0,'Year')
    worksheet.write(0,2,int(current_year)) # needs to change
    worksheet.write(2,0,'Debt',underline_format)
    worksheet.write(3,0,'PV (Present Value)')
    worksheet.write(4,0,'I (Interest Rate)')
    worksheet.write(5,0,'T (No. of Years)')
    worksheet.write(6,0,'C (Monthly Payment)')
    worksheet.write(3,2,int(pv))
    worksheet.write(4,2,float(r))
    worksheet.write(5,2,float(t))
    worksheet.write(6,2,float(c))
    
    workbook.close()


# In[2]:


def monthlylog_userinput():
    
    current_month = input("Enter current month: ") 
    monthly_salary = input("Salary: ")
    other_income = input("Other income: ")
    basic_exp = input("Basic exp: ")
    extra_exp = input("Extra exp: ")
    
    return current_month,monthly_salary,other_income,basic_exp,extra_exp
    
    #Print user the balance and ask how much investment they would like to make?


# In[3]:


def main():
    allsheet_info()


# In[4]:


main()


# 

# In[ ]:




