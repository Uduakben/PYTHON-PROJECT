
age = input('What is your current age?')
ageAsInt = int(age)

years_remaining = 90 - ageAsInt
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = (f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months remaining")
print(message)