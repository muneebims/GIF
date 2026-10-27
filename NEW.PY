import sys
import csv

dic={}

def main():
    if len(sys.argv) == 3:
        checkcsv()
    elif len(sys.argv) <  3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3 :
        sys.exit("Too many command-line arguments")
    



def checkcsv():
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        opencsv()
    else:
        sys.exit("Not a csv file")

def opencsv():
    try:
        with open(sys.argv[1]) as csv1:
            handle(csv1)
    except FileNotFoundError:
        sys.exit("File not Found")

def handle(csv1):
    try:
        with open(sys.argv[2],"w", newline="") as csv2:
            reader = csv.reader(csv1)
            writer = csv.writer(csv2)
            #header
            writer.writerow(["first", "last" , "house"])
            next(reader)
            for row in reader:
                last, first = row[0].split(",")
                last=last.rstrip()
                first=first.rstrip()
                writer.writerow([first, last, row[1]])

        
    except:
        return
main()