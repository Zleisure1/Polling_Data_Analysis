

#########################################################################
import os
import csv

os.chdir(os.path.dirname(__file__)) #changed directory to source of this main.py file  
csvpath = os.path.join('..', '..', 'PyPoll', 'Resources', 'election_data.csv')

print(csvpath) #WORKS
#/Homework 3; Python/python-challenge/PyBank/pypoll.py
#/Homework 3; Python/Poll/Resources/election_data.csv
#file = '../../PyPoll/Resources/election_data.csv'

with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  next(csvreader)
  pypoll_list = list(csv.reader(csvfile)