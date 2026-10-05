import datetime

print("Day of the Week Finder (type 'q' to quit)")

while True:
    day = input("Enter day: ")
    if day.lower() == "q":
        break
    month = input("Enter month: ")
    year = input("Enter year: ")

    try:
        date = datetime.date(int(year), int(month), int(day))
    except ValueError:
        print("Invalid date! Please try again.\n")
        continue

    print(f"That day is a {date.strftime('%A')}\n")