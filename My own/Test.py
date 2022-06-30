import datetime
today = datetime.date.today().day
if today == 'Saturday':
 print('Party!!')
elif today == 'Sunday':
 print('Recover.')
else:
 print('Work, work, work.')
