user_year = int (input())
def days_in_feb (user_year):
    
    if user_year % 4 == 0 and not user_year % 100 == 0 :
        days = print(user_year, "has 29 days in February.")
    elif user_year % 100 == 0 and user_year % 400 == 0:
        days = print (user_year," has 29 days in February.")
    else:
        days = print(user_year, " has 28 days in February.")
    return days


days_in_feb (user_year)


