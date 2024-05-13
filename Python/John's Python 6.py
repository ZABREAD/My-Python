#1
#I think it will say hello 0

for x in range(0, 20):

             print('hello %s' % x)

             if x < 9:

                 break

#2

for x in range(2, 18, 2):
 print(x)

#3

ingredients = ['snails', 'leeches', 'gorilla belly-button lint',
 'caterpillar eyebrows', 'centipede toes']
x = 1
for i in ingredients:
    print('%s %s' % (x, i))
    x = x + 1

#4

weight = 120
for year in range(1, 16):
 weight = weight + 1
 moon_weight = weight * 0.165
 print('Year %s is %s' % (year, moon_weight))





