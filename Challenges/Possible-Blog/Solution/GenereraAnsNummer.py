# Generera ett tal som är kompatibelt med registreringsfunktionen

# MUST BE 6 Characters
# Must be divisable by 2
# When squared, must be at least 12 numbers long
# When rooted, must be perfect square
# Must have the number 5 in it

import math

startnumber = 100000
NUMBERSDESIRED = 10
i = 0
currentnumber = startnumber

while True:
#    print(f"\nCurrent Number is: || {currentnumber} ||")
    if ("5" not in str(currentnumber)):
        currentnumber += 1
        continue

    if (currentnumber % 2 != 0):
        currentnumber += 1
        continue
    
    if (currentnumber ** 2 <= 99999999999):
        currentnumber += 1
        continue
    
    if (math.sqrt(currentnumber) != math.floor(math.sqrt(currentnumber))):
        currentnumber += 1
        continue
    print(f"We have a winner! -- {currentnumber} --")
    print()
    i += 1
    if i == NUMBERSDESIRED:
        break
    currentnumber += 1

