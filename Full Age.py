from datetime import datetime

year = int(input("Ano de nascimento? "))  # prompt for birth year
month = int(input("Mês de nascimento? "))  # prompt for birth month
day = int(input("Dia de nascimento? "))  # prompt for birth day

birth_date = datetime(year, month, day)  # create birth date
current_date = datetime.now()  # get current date

difference = current_date - birth_date  # calculate the difference

days = difference.days
years, days = days // 365, days % 365  # calculate years and remaining days
months, days = days // 30, days % 30  # calculate months and remaining days

print(f'Você tem {years} anos, {months} meses e {days} dias')  # display age
