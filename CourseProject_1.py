#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#write the GetHoursWorked function
def GetHoursWorked():
    hoursworked = float(input("Enter hoursworked: "))
    return hoursworked

#write the GetHourlyRate function
def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate


# write the GetTaxRate function
def GetTaxRate():
    taxrate = float(input("Enter the tax rate: "))
    return taxrate


def CalcTaxAndNetPay(hoursworked, hourlyrate, taxrate):
    grosspay = GetHoursWorked() * GetHourlyRate()
    incometax = grosspay * GetTaxRate()
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print(empname, f'{hours:,.2f}', f'{hourlyrate:,.2f}', f'{grosspay:,.2f}', f'{taxrate:,.1%}', f'{incometax:,.2f}', f'{netpay:,.2f}')

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    # write the code to print TotHours, TotGrossPay, TotTax, and TotNetpay with 2 decimal places
    print(f"{TotHours:.2f}", f"{TotGrossPay:.2f}", f"{TotTax:.2f}", f"{TotNetPay:.2f}")


if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        # write the code to assign to hours the return value from GetHoursWorked
        hoursworked = GetHoursWorked()
        if (hoursworked == "END"):
            break
        # write the code to assign to hourlyrate the return value from GetHourlyRate
        hourlyrate = GetHourlyRate
        if (hourlyrate == "END"):
            break

        # write the code to assign to taxrate the return value from GetTaxRate
        taxrate = GetTaxRate
        if (taxrate == "END"):
            break
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hoursworked, hourlyrate, taxrate)
        printinfo(empname, hoursworked, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        # write the code to increment the other total variables with the appropriate values
        TotHours += 1
        TotGrossPay += 1
        TotTax += 1
        TotNetPay += 1



    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)



