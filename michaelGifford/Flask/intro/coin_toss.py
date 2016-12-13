import random

def coinToss():
    random_num = random.random()
    if round(random_num) == 0:
        face = 'heads'
    else:
        face = 'tails'
    return face

def coinGame(throws):
    arrHeads = []
    arrTails = []
    turn = 0
    while (turn < throws):
        turn += 1
        flip = coinToss()
        if flip == 'heads':
            arrHeads.append(True)
        elif flip == 'tails':
            arrTails.append(True)

        total = len(arrHeads)+len(arrTails)
        headPer = len(arrHeads)/total
        tailPer = len(arrTails)/total

        print ('#{}: {} | {} H {}% | {} T {}%'.format(
            turn,
            flip,
            len(arrHeads),
            round(headPer*100),
            len(arrTails),
            round(tailPer*100)
            ))

coinGame(5000)
