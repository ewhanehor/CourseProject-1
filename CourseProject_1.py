#
def Get_Emp_Name():
    emp_name = input('Enter employee name: ')
    return emp_name
#write the GetHoursWorked function
def Get_Hours_Worked():
    hours_worked = float(input('Enter hours worked:  '))
    return hours_worked

#write the GetHourlyRate function
def Get_Hourly_Rate():
    hourly_rate = float(input('Enter hourly rate:  '))
    return hourly_rate


# write the GetTaxRate function
def Get_Tax_Rate():
    tax_rate = float(input('Enter the tax rate:  '))
    return tax_rate


def Calc_Tax_And_Net_Pay(hours_worked, hourly_rate, tax_rate):
    gross_pay = Get_Hours_Worked() * Get_Hourly_Rate()
    income_tax = gross_pay * Get_Tax_Rate()
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def print_info(emp_name, hours_worked, hourly_rate, gross_pay, tax_rate, income_tax, net_pay):
    print(emp_name, f"{hours_worked:,.2f}", f"{hourly_rate:,.2f}", f"{gross_pay:,.2f}", f"{tax_rate:,.1%}", f"{income_tax:,.2}", f"{net_pay:,.2f}")

def Print_Totals(Tot_Employees, Tot_Hours, Tot_Gross_Pay, Tot_Tax, Tot_Net_Pay):    
    print()
    print(f"Total Number Of Employees: {Tot_Employees}")
    # write the code to print TotHours, TotGrossPay, TotTax, and TotNetpay with 2 decimal place
    print(f"Total hours worked: {Tot_Hours:,.2f}")
    print(f"Total Gross Pay: {Tot_Gross_Pay:,.2f}") 
    print(f"Total Tax Paid: {Tot_Tax:,.2f}") 
    print(f"Total Net Pay: {Tot_Net_Pay:,.2f}")


if __name__ == "__main__":
    Tot_Employees = 0
    Tot_Hours = 0.00
    Tot_Gross_Pay = 0.00
    Tot_Tax = 0.00
    Tot_Net_Pay = 0.00
    while True:
        emp_name = Get_Emp_Name()
        if (emp_name.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
        hours_worked = Get_Hours_Worked()
        if (hours_worked == "END"):
            break
        # write the code to assign to hourlyrate the return value from GetHourlyRate
        hourly_rate = Get_Hourly_Rate
        if (hourly_rate == "END"):
            break

        # write the code to assign to taxrate the return value from GetTaxRate
        tax_rate = Get_Tax_Rate
        if (tax_rate == "END"):
            break
        
        gross_pay, income_tax, net_pay = Calc_Tax_And_Net_Pay(hours_worked, hourly_rate, tax_rate)
        print_info(emp_name, hours_worked, hourly_rate, gross_pay, tax_rate, income_tax, net_pay)
        Tot_Employees += 1
        # write the code to increment the other total variables with the appropriate values
        Tot_Hours += 1
        Tot_Gross_Pay += 1
        Tot_Tax += 1
        Tot_Net_Pay += 1



    Print_Totals (Tot_Employees, Tot_Hours, Tot_Gross_Pay, Tot_Tax, Tot_Net_Pay)



