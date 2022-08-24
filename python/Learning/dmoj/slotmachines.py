quarters = int(input())
m1last = int(input())
m2last = int(input())
m3last = int(input())

played = 0

while quarters > 0:
    quarters -= 1
    played += 1

    if played % 3 == 0:
        m3last += 1
        if (m3last % 10 == 0):
            quarters += 9

    elif played % 2 == 0:
        m2last += 1
        if (m2last % 100 == 0):
            quarters += 60

    else:
        m1last += 1
        if (m1last % 35 == 0):
            quarters += 30

print("Martha plays " + str(played) + " times before going broke.")