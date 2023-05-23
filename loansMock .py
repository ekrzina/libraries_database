#program for mocking loans data
import random
import datetime

#function returns random isbn of text file
def give_isbn():
    isbns = content.split('\n')
    return random.choice(isbns)

#function to return random date
def give_date():
    start_date = datetime.date(2018, 1, 1)
    end_date = datetime.date(2022, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

#function to return random date between two given
def give_date_b(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

f = open('isbns.txt', 'r')
content = f.read()
latefee = 0.17

#on repeat
for i in range(2008):
    #random employee from 1 to 24
    employee = random.randint(1,24)
    #picking random number between 1 and 1000
    member = random.randint(1,1000)
    #picking isbn
    chosen_isbn = give_isbn()
    #dates
    date_of_loan = give_date()
    date_to_return = date_of_loan + datetime.timedelta(days=31)
    
    #late or not + latefee
    yesno = random.randint(0,10)
    if(yesno < 10):
        date_returned = give_date_b(date_of_loan, date_to_return)
        latefee = 0
    else:
        days_late = random.randint(1,356)
        date_returned = date_to_return + datetime.timedelta(days=days_late)
        latefee = latefee * days_late
        latefee = round(latefee, 2)

    #returned or not
    sql_statement = "INSERT INTO loans (dateOfLoan, dateToReturn, dateReturned, lateFee, membershipNumber, ISBN, employeeInCharge) VALUES('" + str(date_of_loan) + "','" + str(date_to_return) + "','" + str(date_returned) + "'," + str(latefee) + "," + str(member) + "," + str(chosen_isbn) + "," + str(employee) + ");"
    #sql_statement = "INSERT INTO loans (dateOfLoan, dateToReturn, dateReturned, lateFee, membershipNumber, ISBN, employeeInCharge) VALUES('" + str(date_of_loan) + "','" + str(date_to_return) + "',null," + str(latefee) + "," + str(member) + "," + str(chosen_isbn) + "," + str(employee) + ");"
    
    print(sql_statement);

    #ratings 1 out of 5
    rates = random.randint(1,5)
    if(rates < 2):
        #random rating from 0 to 10
        rate = random.randrange(11)
        rate_statement = "INSERT INTO ratings VALUES (" + str(member) + ", " + str(chosen_isbn) + ", " + str(rate) + ");"
        print(rate_statement)

    #set late fee back to 0.17    
    latefee=0.17
    
f.close();


