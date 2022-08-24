ball_order = 1
moves = input()

for p in range(0, len(moves)):
    if moves[p]== "A":
        if ball_order == 1:
            ball_order =2
        elif ball_order == 2:
            ball_order = 1
    if moves[p]== "B":
        if ball_order == 2:
            ball_order =3
        elif ball_order == 3:
            ball_order = 2
    if moves[p]== "C":
        if ball_order == 1:
            ball_order =3
        elif ball_order == 3:
            ball_order = 1

print(ball_order)