import sqlite3
import csv

f = "discobandit.db"

db = sqlite3.connect(f)
c = db.cursor()

names = []
ids = []
averages = []


def showGrades(id):
    command = "SELECT name, mark, code from peeps, courses WHERE peeps.id = courses.id AND peeps.id = %s;" %(str(id))
    data = c.execute(command)
    for x in data:
        print x
#showGrades(1)

def fillNames():
    command = "SELECT name from peeps"
    data = c.execute(command)
    for x in data:
        names.append(str(x[0]))
fillNames()
#print names

def fillIDs():
    command = "SELECT id from peeps"
    data = c.execute(command)
    for x in data:
        ids.append(x[0])
fillIDs()
#print ids

def fillAverages():
    for num in ids:
        command = "SELECT mark from courses WHERE courses.id = %d" %(num)
        data = c.execute(command)
        total = 0
        courses = 0 
        for x in data:
            total += x[0]
            courses += 1
        averages.append((total * 1.0)/courses)
fillAverages()
#print averages

def display():
    for i in range(0,len(names)):
        print "name: " + names[i] + " id: " + str(ids[i]) + " average: " + str(averages[i])
display()

def createTable():
    command = "CREATE TABLE peeps_avg (id INTEGER, avg REAL);"
    c.execute(command)
    for i in range(0,len(names)):
        command = "INSERT INTO peeps_avg VALUES (%d, %f)" %(ids[i], averages[i])
        c.execute(command)
createTable()

    
