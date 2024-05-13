#1
#SyntaxError: indent

#2
twinkies = 600
if twinkies < 100 or twinkies > 500:
    print('Too few or too many')

#3
amount = 800
if (amount >= 100 and amount <= 500) or (amount >= 1000 \
        and amount <= 5000):
    print('amount is between 100 & 500 or between 1000 & 5000')
amount = 400
if (amount >= 100 and amount <= 500) or (amount >= 1000 \
        and amount <= 5000):
    print('amount is between 100 & 500 or between 1000 & 5000')
amount = 3000
if (amount >= 100 and amount <= 500) or (amount >= 1000 \
        and amount <= 5000):
    print('amount is between 100 & 500 or between 1000 & 5000')

#4
ninjas = 5
if ninjas < 10:
    print('I can fight those ninjas!')
elif ninjas < 30:
    print("It'll be a struggle, but I can take 'em")

elif ninjas < 50:
    print('That/'s too many')
    
