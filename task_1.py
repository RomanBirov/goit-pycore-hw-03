from datetime import datetime

def get_days_from_today(date: str) -> int:
    enter_date = datetime.strptime(date, "%Y-%m-%d").date()
    today_date = datetime.today().date()
    diff_between_date = today_date - enter_date
    return diff_between_date.days