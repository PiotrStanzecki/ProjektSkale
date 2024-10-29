import random

notes = ["C","Db","D","Eb","E","F","Gb","G","Ab","A",
"Bb","B"]

quality = ["maj","min","sus2","sus4","majb5","dim",
    "maj7","min7","7","maj7#11","min6","7#11","maj7#5","maj69",
    "dimmaj7","min7b5"]

def randomprog(notes, quality, n):
    prog = ""
    for i in range(1, n+1):
        randnote = random.choice(notes)
        randquality = random.choice(quality)

        if(i%4 != 0):
        
            prog += randnote + randquality + " "
        else:
        
            prog += randnote + randquality + '\n'
        
    return prog

print(randomprog(notes, quality, 8))
