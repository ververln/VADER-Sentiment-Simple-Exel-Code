#This simple Python code takes a row from your Excel dataset and applies VADER Sentiment Analyzer to it by looping through each row and displaying the compound, positive, neutral and negative sentiment each in separate row next to the original data.
#Replace your_path\data.csv with path on your own PC.

#If you are using this code, please credit.

import vaderSentiment.vaderSentiment 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import pandas as pd

with open("your_path\data.csv", 'r', encoding="windows-1252") as infile:
    data = infile.read()
    data = data.split("\n")
    
output = []

for row in data:
    score = SentimentIntensityAnalyzer().polarity_scores(row)
    score["text"] = row
    output.append(score)
    
df = pd.DataFrame(output)
df.to_csv("texts_and_scores_add.csv")
print ()
