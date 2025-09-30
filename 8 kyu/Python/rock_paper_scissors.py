# [ 8 kyu ] Rock Paper Scissors!
def rps(p1, p2):
    #your code here
    status = ''
    if p1 == 'rock':
        if p2 == 'rock':
            status = 'Draw!'
        elif p2 == 'paper':
            status = 'Player 2 won!'
        else:
            status = 'Player 1 won!'
    elif p1 == 'paper':
        if p2 == 'rock':
            status = 'Player 1 won!'
        elif p2 == 'paper':
            status = 'Draw!'
        else:
            status = 'Player 2 won!'
    elif p1 == 'scissors':
        if p2 == 'rock':
            status = 'Player 2 won!'
        elif p2 == 'paper':
            status = 'Player 1 won!'
        else:
            status = 'Draw!'
    return status
