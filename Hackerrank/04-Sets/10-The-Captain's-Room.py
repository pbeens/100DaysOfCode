# 10-The-Captain's-Room.py
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

'''
sample input:
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
'''

# input
size = int(input())
room_number_list = input().split()

# count each time a room number occurs
room_count = {}
for room in room_number_list:
    if room not in room_count:
        room_count[room] = 1
    else:
        room_count[room] += 1

# find the one that does not equal the size
for room in room_count:
    if room_count[room] != size:
        print(room)
