from datetime import datetime

today: datetime = datetime.now()
print(f"Today is {today.strftime(format='%B %d, %Y')}.")
