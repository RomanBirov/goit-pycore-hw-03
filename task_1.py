from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        enter_date = datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.today().date()
        diff_between_date = today_date - enter_date
        return diff_between_date.days
    except ValueError:
        print("Incorrect date format. Please use the 'YYYY-MM-DD' format.")
        return 0
print(get_days_from_today("13.14.2020"))
