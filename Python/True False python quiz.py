def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt <= 1:
        if guess.lower() == answer.lower():
            print('Your answer is correct!')
            score = score + 1
            print('Your score is: %s \n' % score)
            still_guessing = False
        else:
            if attempt < 1:
                print('Sorry wrong answer.')
            attempt = attempt + 1
        

score = 0

print('Welcome to my true / false quiz!')
print('Are you ready for some random information? Here we go!\n')

#from Mr. Nelson
guess1 = input('What is the name of the original Spiderman is Miles Morales. Type true or false\n')
check_guess(guess1, 'False')
print('The answer is Peter Parker\n')

guess2 = input('The suicide and crisis lifeline number is 988. Type true or false\n')
check_guess(guess2, 'True')

#https://www.mentimeter.com/blog/audience-energizers/55-free-trivia-and-fun-quiz-question-templates
guess3 = input('A dice has 22 dots\n')
check_guess(guess3, 'False')
print('The answer is 21\n')

#https://www.mentimeter.com/blog/audience-energizers/55-free-trivia-and-fun-quiz-question-templates
guess4 = input('Africa is the only continent in all 4 hemisphears. Type true or false\n')
check_guess(guess4, 'True')

guess5 = input ('Toy story has the most sequels in disny. Type true or false\n')
check_guess(guess5, 'True')

guess6 = input ('Mickey Mouse\'s shoes are red. Type true or false\n')
check_guess(guess6, 'False')
print('The answer was Yellow\n')

guess7 = input ('Disney has won 14 original song trophies. Type true or false\n')
check_guess(guess7, 'True')

#https://parade.com/944584/parade/trivia-questions-for-kids/

guess8 = input ('The toy cowboy in toy story is called Jessie. Type true or false\n')
check_guess(guess8, 'False')
print('The answer is Woody\n')

guess9 = input ('you hit your hand with a hammer. Type true or false\n')
check_guess(guess9, 'False')
print('The answer was a nail\n')

guess10 = input ('Jiminy Cricket\'s nose grew everytime he lied. Type true or false\n')
check_guess(guess10, 'False')
print('The answer is Pinocchio\n')

guess11 = input ('Tinkerbell is the fairy in peter pan. Type true or false\n')
check_guess(guess11, 'True')

#https://www.buzzfeed.com/kellyrissman/best-trivia-questions?scrlybrkr=f3db633f
guess12 = input ('you get cold water if you freeze water. Type true or false\n')
check_guess(guess12, 'False')
print('The answer is Ice\n')

#https://www.buzzfeed.com/kellyrissman/best-trivia-questions?scrlybrkr=f3db633f
guess13 = input ('you use a scovile scale to measure the pungancy of something. Type true or false\n')
check_guess(guess13, 'True')

#https://www.buzzfeed.com/kellyrissman/best-trivia-questions?scrlybrkr=f3db633f
guess14 = input ('pickles start out as broccoli. Type true or false\n')
check_guess(guess14, 'false')
print('The answer is cucumber\n')

#https://www.buzzfeed.com/kellyrissman/best-trivia-questions?scrlybrkr=f3db633f
guess15 = input ('Sharks have 0 Bones. Type true or false\n')
check_guess(guess15, 'True')


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






