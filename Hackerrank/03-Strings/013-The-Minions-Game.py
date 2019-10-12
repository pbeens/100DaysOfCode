# 013-The-Minions-Game.py
# https://www.hackerrank.com/challenges/the-minion-game/problem

debug = False

vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'


def minion_game(S):
    num_cons = 0
    num_vow = 0
    for i in range(len(S)):
        if S[i] in vowels:
            num_vow += len(S) - i
        else:
            num_cons += len(S) - i

    if num_cons > num_vow:
        print('Stuart {}'.format(num_cons))
    elif num_vow > num_cons:
        print('Kevin {}'.format(num_vow))
    else:
        print('Draw')


if debug:
    s = 'BANANA'
else:
    s = input()
minion_game(s)
