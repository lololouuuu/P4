import sys

if len(sys.argv) != 2:
    print("\n\tUSAGE: python class_score.py [results_file.txt]\n")
else:
    filename = sys.argv[1]
    file = open(filename)
    lines = file.readlines()

    ok = err = 0
    for line in lines:
        postr = line.find('SES')
        pospr = line.rfind("SES")
        truth = line[(postr+3):(postr+6)]
        predicted = line[(pospr+3):(pospr+6)]
        if truth == predicted:
            ok=ok+1
        else:
            err=err+1
            print("Impostor identificado como: " + predicted + "\nVerdadero locutor: " + truth + "\n")

    score = (ok/(ok+err))*100
    print('Score de acierto = %.3f' %score)