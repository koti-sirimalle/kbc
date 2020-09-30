
from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if(question["answer"]==answer):
        return True
    else:
        return False#remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    print(f'\t\t\tOption 2: {ques["option2"]}')
    print(f'\t\t\tOption 3: {ques["option3"]}')
    ans1=input('Your choice (2-3) : ')
    return ans1
def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print("welcome to the game")
    count=0
    total=0
    life=0
    for i in range(0,15):
        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations
        
        if(ans.lower()=="lifeline"):
            if(life==1):
                print("LIFELINE is available only once.Please select from options mentioned above.")
                ans1=input('Your choice ( 1-4 ) : ')
            else:
                if(i==14):
                    print("LiFELINE is not available for last question.Please select from options mentioned above")
                    ans1=input('Your choice ( 1-4 ) : ')
                else:
                    ans1=lifeLine(QUESTIONS[i])
                    life=1
                    
            ans=ans1
        if(ans.lower()=="quit"):
            print(total)
            exit(0)
        else:
            if isAnswerCorrect(QUESTIONS[i], int(ans ) ):
                # print the total money won.
                # See if the user has crossed a level, print that if yes
                print('\nCorrect !')
                count+=1
                total+=QUESTIONS[i]["money"]
                print(total)

            else:
                # end the game now.
                # also print the correct answer
                print('\nIncorrect !')
                print("Answer is {}".format(QUESTIONS[i]["option2"]))
                if(count<=4):
                    print(total)
                elif(count>=5 and count<10):
                    print(total+10000)
                else:
                    print(total+320000)
                exit(0)
        

    print("You won :",total)


kbc()
