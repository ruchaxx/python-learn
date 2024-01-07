from random import shuffle

l1 = [1,2,3,4,5]
def shuffle_list(l1):
    shuffle(l1)
    return l1
result = shuffle_list(l1)
print(result)

#game - find hidden 'o'
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick a num : 0 ,1 or 2 ")

    return int(guess)

def check_guess(l2,guess):
    if l2[guess] == 'o':
        print("Correct")
    else:
        print("wrong guess")
        print(l2)

l2 = ['','o',''] # initial list
mixedup_list = shuffle_list(l2) #shuffled list
guess = player_guess() #user guess
check_guess(mixedup_list,guess) #check guess
