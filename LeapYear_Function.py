def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
                # print("Leap year.")
            else:
                return False
                # print("Not leap year.")
        else:
            return True
            # print("Leap year.")
    else:
        return False
        # print("Not leap year.")


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not is_leap(year):
        for months in range(1, len(month_days)):

            if months == 1:
                return month_days[0]
            elif month == 2:
                return month_days[1]
            elif month == 3:
                return month_days[2]
            elif month == 4:
                return month_days[3]
            elif month == 5:
                return month_days[6]
            elif month == 6:
                return month_days[7]
            elif month == 7:
                return month_days[8]
            elif month == 8:
                return month_days[9]
            elif month == 9:
                return month_days[10]
            elif month == 10:
                return month_days[11]
            elif month == 11:
                return month_days[12]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
