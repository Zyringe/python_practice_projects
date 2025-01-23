import pandas as pd
import random

df_hsr = pd.read_csv("hsr_character-data.csv")
character_list = df_hsr['character'].tolist()
character_list.extend(['stelle', 'caelus', 'imbitator_lunae'])
character_list = [char for char in character_list if char not in ['trailblazer_0', 'trailblazer_1', 'dan_heng_IL']]

answer = random.choice(character_list)
answer.replace('_', ' ')

# For debug
print(f'Hint: {answer}')

if __name__ == '__main__':
    max_wrong_guess = 5
    wrong_guess = []
    right_guess = [' ']
    guess = ''
    answer_set = set(answer)
    print('HSR Hangman Question:', end = ' ')
    
    
    while len(wrong_guess) < max_wrong_guess:
        for char in answer:
            if char == ' ':
                print('  ', end = '')
            elif char in right_guess:
                print(char, end = ' ')
            else:
                print('_', end = ' ')
        print('')
    
        while guess in (right_guess + wrong_guess):
            guess = input('Please enter the letter/number: ')
            if guess in right_guess:
                print('You have already guessed this letter right')
            elif guess in wrong_guess:
                print('You have already guessed this wrong')
            
        if guess == '':
            guess = input('Please enter the letter/number: ')
        elif guess in answer:
            right_guess.append(guess)
            print('You got it right!')
        else:
            wrong_guess.append(guess)
            if len(wrong_guess) >= max_wrong_guess:
                print(f'You Lose. The answer is {answer}')
            else:
                print(f'You got it wrong ({max_wrong_guess - len(wrong_guess)} attempt left)')
        if answer_set.issubset(right_guess):
            print('Congratualtions!')
            break

