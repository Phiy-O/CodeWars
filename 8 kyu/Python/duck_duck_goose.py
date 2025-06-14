def duck_duck_goose(players, goose):
    
    res = ''
    x = 0
    while x < goose:
        res = players[x]
        x += 1
        if x >= len(players):
            players += players
            if x == goose:
                break
    
    return res.name
