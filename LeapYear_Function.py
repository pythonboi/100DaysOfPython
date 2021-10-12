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

    # print(is_leap(year))
    if not is_leap(year):
        for count in range(len(month_days)):
            if count == month:
                return month_days[0]
            elif count == month:
                return month_days[1]
            elif count == month:
                return month_days[2]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
