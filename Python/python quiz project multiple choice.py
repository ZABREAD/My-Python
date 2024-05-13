def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 2:
        if guess.lower() == answer.lower():
            print('Your answer is correct!')
            score = score + 1
            print('Your score is: %s \n' % score)
            still_guessing = False
        else:
            if attempt < 1:
                guess = input('Sorry wrong answer. Try again: ')
            attempt = attempt + 1
    if attempt == 2:
        print('The correct answer is ' +answer)
        

score = 0

print('Welcome to my random fact quiz!')
print('Are you ready for some random information? Here we go!\n')

#from Mr. Nelson
guess1 = input('What is the name of the original Spiderman?\n \
A)Peter Parker\n B)Miles Morales\n C) Gwen Stacy\n D)Uncle Ben\n: ')
check_guess(guess1, 'A')

guess2 = input('What is the suicide and crisis lifeline number?\n \
A)988\n B)411\n C)998\n D)911\n: ')
check_guess(guess2, 'A')

#https://www.mentimeter.com/blog/audience-energizers/55-free-trivia-and-fun-quiz-question-templates
guess3 = input('How many dots appear on a pair of dice?\n \
A)42\n B)50\n C)45\n D)39\n: ')
check_guess(guess3, 'A')

#https://htschool.hindustantimes.com/editorsdesk/knowledge-vine/africa-the-only-continent-that-touches-upon-all-four-hemispheres
guess4 = input('What is the only continent with land in all four hemispheres?\n \
A)Zimbabwe\n B)united States\n C)Africa\n D)United Kingdom\n: ')
check_guess(guess4, 'C')

guess5 = input ('Which Disney movie has had the most sequels?\n \
A)Mulan\n B)The Lion King\n C)Frozen\n D)Toy Story\n: ')
check_guess(guess5, 'D')
#https://en.wikipedia.org/wiki/Mickey_Mouse?scrlybrkr=f3db633f#:~:text=Mickey%20Mouse%20is%20an%20American,yellow%20shoes%2C%20and%20white%20gloves.
guess6 = input ('What color are Mickey Mouse\'s shoes?\n \
A)red\n B)Yellow\n C)orange\n D)pink\n: ')
check_guess(guess6, 'B')

guess7 = input ('How many \'Academy Awards for Best Original Song\' has Disney won?\n \
A)20\n B)16\n C)15\n D)14\n: ')
check_guess(guess7, 'D')

#https://parade.com/944584/parade/trivia-questions-for-kids/

guess8 = input ('What is the name of the toy cowboy in Toy Story?\n \
A)Lotso\n B)Buzz Lightyear\n C)Jessie\n D)Woody\n: ')
check_guess(guess8, 'D')

guess9 = input ('What is something you hit with a hammer?\n \
A)wall\n B)finger\n C)hand\n D)nail\n: ')
check_guess(guess9, 'D')

guess10 = input ('Whose nose grew longer every time he lied?\n \
A)Geppetto\n B)Pinocchio\n C)Jiminy Cricket\n D)the Fox\n: ')
check_guess(guess10, 'B')

guess11 = input ('What is the name of the fairy in Peter Pan?\n \
A)Captain Hook\n B)Peter Pan\n C)Tinkerbell\n D)Mr. Smee\n: ')
check_guess(guess11, 'C')

#https://www.buzzfeed.com/kellyrissman/best-trivia-questions?scrlybrkr=f3db633f
guess12 = input ('If you freeze water, what do you get?\n \
A)cold water\n B)Ice\n C)white water\n D)cold\n: ')
check_guess(guess12, 'B')

#https://www.buzzfeed.com/kellyrissman/best-trivia-questions?scrlybrkr=f3db633f
guess13 = input ('What is the name of the scale used to measure spiciness of peppers?\n \
A)Scoville scale\n B)Heat Scale\n C)Spicy Scale\n D)Scale\n: ')
check_guess(guess13, 'A')

#https://www.buzzfeed.com/kellyrissman/best-trivia-questions?scrlybrkr=f3db633f
guess14 = input ('Pickles start out as which vegetable?\n \
A)Green Beans\n B)Brocoli\n C)Carrot\n D)Cucumber\n: ')
check_guess(guess14, 'D')

#https://www.buzzfeed.com/kellyrissman/best-trivia-questions?scrlybrkr=f3db633f
guess15 = input ('How many bones do sharks have?\n \
A)0\n B)100\n C)200\n D)357\n: ')
check_guess(guess15, 'A')


print('Congratulayions, you survived the quiz!')
print('Your final score is: %s ')
percent = (score / 15) * 100
percent = round(percent, 2)
percent = str(percent)
print('You get a ' + percent + '%')

percent = float(percent)

if percent >= 90 and percent <= 100:
    print ('Your grade is an A!')
elif percent >= 80 and percent <= 89:
    print ('Your grade is an B!')
elif percent >= 70 and percent <= 79:
    print('Your gradde us ab C')
elif percent >= 60 and percent <= 69:
    print('Yourgrade is an D...')
else:
    print('You failed..........')






