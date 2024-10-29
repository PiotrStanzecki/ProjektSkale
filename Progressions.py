import random
from fpdf import FPDF

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


def printProgToPdf(outputName, amount):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 10)
    for i in range(amount):
        pdf.cell(200, 10, txt = randomprog(notes, quality, 10) +
        "Pozycja: " + str(random.randint(1,4)), 
        ln = 1, align = 'L')
    pdf.output(outputName)






    

#1 poz. od 1 progu
#2 poz. od 5 progu
#3 poz. od 10 progu
#4 poz. od 15 progu

def main() :
    print(randomprog(notes, quality, 8))
    print("Pozycja: " + str(random.randint(1,4)))
    printProgToPdf("Chord_Progression.pdf", 25)


if __name__ == '__main__':
    main()
    

