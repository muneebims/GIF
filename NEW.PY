import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3 :
        sys.exit("Too many command-line arguments")
    checkcsv()

def checkcsv():
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        opencsv()
    else:
        sys.exit("Not a CSV file")

def opencsv():
    try:
        with open(sys.argv[1]) as csv1:
            datacleaning(csv1)
    except FileNotFoundError:
        sys.exit("File Not Found")

def datacleaning(csv1):
    with open(sys.argv[2] ,"w", newline="") as csv2:
        reader = csv.reader(csv1)
        writer = csv.writer(csv2)

        writer.writerow(["first" , "last","house"])

        next(reader)

        for row in reader:
            last, first = row[0].split(",")
            first = first.strip()
            last = last.strip()
            writer.writerow([first,last,row[1]])

main()
