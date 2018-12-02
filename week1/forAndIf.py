blood = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

ablood = 0
bblood = 0
oblood = 0
abblood = 0

for ads in blood:
    if ads == 'A':
        ablood += 1
    elif ads == 'B':
        bblood += 1
    elif ads == 'O':
        oblood += 1
    elif ads == 'AB':
        abblood +=1
print(ablood)