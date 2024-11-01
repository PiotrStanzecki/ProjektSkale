import random
from fpdf import FPDF

notes = ["C","Db","D","Eb","E","F","Gb","G","Ab","A",
"Bb","B"]

quality = ["maj","min","sus2","sus4","majb5","dim",
"maj7","min7","7","maj7#11","min6","7#11","maj7#5","maj69",
"dimmaj7","min7b5", "7b13", "7#9", "7b9", "7b5", "susb9", "maj7add6",
"min7add4", "majaddb2", "majadd2", "majadd#2","majadd#4","majadd#5", "maj6",
"minaddb2", "minadd2", "minadd4", "minaddb6", "minmaj7", "aug"]

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
    pdf.cell(200, 10, txt = "1 Pozycja od 1 progu, 2 Pozycja od 5 progu, 3 Pozycja od 10 progu, 4 Pozycja od 15 progu",
             ln = 1, align = 'C')
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
    printProgToPdf("Chord_Progression1.pdf", 300)
    printProgToPdf("Chord_Progression2.pdf", 300)


if __name__ == '__main__':
    main()
    

