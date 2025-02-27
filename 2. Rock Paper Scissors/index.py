import random

game = True
scores = {'player':0,'computer':0}
while game:
    print('lets play the game......')
    print('$'*40)
    while max(scores.values()) != 5:
        print('1 => Rock','2 => Paper','3 => Scissors')
        try:
            p_choice = int(input("Enter your choice:-   "))
            print('%'*40)
            if p_choice == 1:
                player_c = 'Rock'
            elif p_choice == 2:
                player_c = 'Paper'
            elif p_choice == 3:
                player_c = 'Scissors'
            else:
                print('Choose only from 1 to 3')
                p_choice = int(input('Enter Your Choice:-  '))
        except Exception as e:
            print(e)
            p_choice = int(input('Enter Your Choice:-  '))

        print('Player has chosen:-   ',player_c)
        print(' ')
        print('%'*40)
        c_choice  = random.randint(1,3)

        if c_choice == 1:
            computer_c = 'Rock'

        elif c_choice == 2:
            computer_c = 'Paper'
        else:
            computer_c = 'Scissors'

        print('Computer has chosen:- ',computer_c)
        print(' ')
        print(' ')
        print(' ')
        print(player_c, 'V/s', computer_c)

        if p_choice == 1 and c_choice == 2 or p_choice == 2 and  c_choice == 1:
            result = 'Paper'
            if player_c == result:
                scores['player'] += 1
            else:
                scores['computer'] += 1

        elif p_choice == 1 and c_choice == 3 or p_choice == 3 and c_choice == 1:
            result = 'Rock'
            if player_c == result:
                scores['player'] += 1
            else:
                scores['computer'] +=1

        elif p_choice == 2 and c_choice == 3 or p_choice == 3 and c_choice == 2:
            result = 'Scissors'

            if player_c == result:
                scores['player'] += 1
            else:
                scores['computer'] += 1

        print(scores)
        for key,value in scores.items():
            if value == 5:
                print(' ')
                print(key,value) 
                print(' ')

        if max(scores.values()) == 5:
            game = False
        
        for player, score in scores.items():
            if score == 5:
                print('%H%'*10)
                print('')
                print(player,'Wins')
                print(' ')
                print('%H%'*10)

