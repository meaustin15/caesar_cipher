import tkinter
alpha = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,
         "I":8,"J":9,"K":10,"L":11,"M":12,"O":13,"P":14,"Q":15,
         "R":16,"S":17,"T":18,"U":19,"V":20,"W":21,"X":22,"Y":23,"Z":24
         }

shift = input("Enter The Shift Amount: ")
shift = int(shift)
plaintext = input("Enter Your plaintext ").upper()
plainlist = list(plaintext)

values = list(alpha.values())
keys = list(alpha.keys())
for char in plainlist:
    if char in alpha:
        if alpha[char]+shift >= 25:
            print(keys[values.index((alpha[char]+shift)-25)], end="")
        else:
            print(keys[values.index(alpha[char]+shift)],end="")


