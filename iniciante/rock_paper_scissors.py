"""
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return
"""
def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 == 'rock':
        if p2 == 'scissors':
            return 'Player 1 won!'
        else:
            return 'Player 2 won!'
    elif p1 == 'paper':
        if p2 == 'scissors':
            return 'Player 2 won!'
        else:
            return 'Player 1 won!'
    elif p1 == 'scissors':
        if p2 == 'paper':
            return 'Player 1 won!'
        else:
            return 'Player 2 won!'
    return None