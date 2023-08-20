def days_in_feb(user_year):
    feb = 28
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                feb = 29
            else:
                feb = 28
        else:
            feb = 29
    else:
        feb = 28
    return feb
year = int(input("What year is it?"))
if __name__ == '__main__':
    print(f'{year} has {days_in_feb(year)} days in February')


