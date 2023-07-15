import random
#KBC
# create two list one for questions and other for answers
# use random method to randomly select the question
# total 10 questions with 10 answers
# each questions has 5000 rupees award money

questions = ['What country has the highest life expectancy? ',
             'Where would you be if you were standing on the Spanish Steps?',
             'Which language has the more native speakers: English or Spanish?',
             'What is the most common surname in the United States?',
             'What disease commonly spread on pirate ships?',
             'Who was the Ancient Greek God of the Sun?',
             'What was the name of the crime boss who was head of the feared Chicago Outfit?',
             'What year was the United Nations established?','Who has won the most total Academy Awards?',
             'What artist has the most streams on Spotify?']

answers = ['Hong Kong','Rome','Spanish','Smith','Scurvy','Apollo','Al Capone','1945','Walt Disney','Drake']

reward = 0
print("Let the game of answers the question and won money begin!!!!!!!!!!!!!!")
for i in range(0,10):
    print(questions[i])
    print("Enter your ans: ")
    a = input()
    if a == answers[i]:
        print("Congratulations, Right answerrrrr (*_*)")
        reward = reward + 5000
        print(" Your current price money is : ", reward)
        print(("\n~~~~~~~~Way to your next question~~~~~~~~\n"))
    else:
        print("Oh no!! Wrong answer, you lose ")
        print("Your final price money is : ", reward)
        break
print("Thank you for playing this game, you win a total amount of rupees : ", reward)





