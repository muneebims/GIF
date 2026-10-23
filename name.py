import csv

name = input("whats your name? ")
home = input("where are you from? ")

with open("names.csv","a", newline="") as file:
    writer=csv.DictWriter(file, fieldnames=["names","home"])
    writer.writerow({"names":name,"home":home})
