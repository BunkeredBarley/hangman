import random
words = ['cat', 'car', 'penis', 'deer', 'ass', 'moran', 'jelly']
rndm = random.choice(words)
def hangman (word):
    wrong = 0
    stages = ['',
              '______________          ',
              '|            |          ',
              '|            O          ',
              '|           /|\         ',
              '|           / \         ',
              '|                       ',]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Добро пожаловать на казнь!')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Введите букву: '
        guess = input(msg)
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong += 1
        print(''.join(board))
        e = wrong + 1
        print('\n'.join(stages[0: e]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: ')
            print(''.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('Вы проиграли! Было загадано слово: {}'.format(word))

hangman(rndm)