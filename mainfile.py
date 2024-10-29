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

    

#1 poz. od 1 progu
#2 poz. od 5 progu
#3 poz. od 10 progu
#4 poz. od 15 progu

def main() :
    print(randomprog(notes, quality, 8))
    print("Pozycja: " + str(random.randint(1,4)))


if __name__ == '__main__':
    main()
    

