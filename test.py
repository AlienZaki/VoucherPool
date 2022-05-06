from datetime import datetime

s = datetime.strptime("17 May, 2022", '%d %B, %Y').strftime('%Y-%m-%d')
print(s)