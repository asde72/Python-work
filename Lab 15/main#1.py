import csv
import os.path
with open('C:\\Users\\ninja\\Documents\\Python\\hello\\Lab 15\\input1.csv') as input1:
    objector = csv.reader(input1, delimiter=",")
    row_num = 1
    for row in objector:
        row_num += 1
    word_count_dictionary = {i: row.count(i) for i in row}
    for key,value in word_count_dictionary.items():
        print (key,value)