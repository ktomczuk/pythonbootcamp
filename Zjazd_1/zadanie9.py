import datetime

a = int(input(' Poadaj rok narodzin'))
b = datetime.datetime.today().year
if 2018 - a <= 18:
	print('Gówaniarz jestes')
else:
	print('mozesz chlac')
	