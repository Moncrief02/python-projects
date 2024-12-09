import random
def play():
    user=input(" please choose:'r' for rock,'p' for paper,'s' for scissors ")
    computer=random.choice(['r','p','s'])
    trial=0
    rival=0
    human=0
    while trial>=3:
        if user == computer:
            human +=1
            rival +=1
            return 'Tie' 
        if is_win(user,computer):
            human +=1
            return 'You won!'
        rival +=1
        return 'You lost'  
    trial+=1
    if (rival>human ):
        return "computer wins{rival}'-' {humans}"
    else:
        return "huamn wins {humans}'-'{rival}"
def is_win(player,opponent):
    if ((player== 'r' and opponent == 's')or (player== 's' and opponent=='p')or
    (player== 'p' and opponent=='r')):
        return True

print(play())

