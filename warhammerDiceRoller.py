import random

def rollxdxCheckx(num, dice, check):
    successes = 0
    crit_successes = 0
    total = 0
    for k in range(int(num)):
        roll = random.randint(1, int(dice))
        total += roll
        print("Roll " + str(k + 1) +  ": " + str(roll))
        if roll >= int(check):
            if roll == int(dice):
                crit_successes += 1
            else:
                successes += 1
    return [successes, crit_successes, total]

while True:
    p = input(">>")
    if p.count("c") > 0:
        p = p.split("d")
        p[1] = p[1].split("c")
        rollTime = rollxdxCheckx(p[0],p[1][0],p[1][1])
        print(str(rollTime[0]) + " successes and " + str(rollTime[1]) + " critical successes") if rollTime[1] > 0 else print(str(rollTime[0]) + " successes")
    else:
        p = p.split("d")
        rollTime = rollxdxCheckx(p[0],p[1],-1)
        print("Total:", rollTime[2])
        
    
