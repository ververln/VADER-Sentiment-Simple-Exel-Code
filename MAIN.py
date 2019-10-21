#This simple Python code takes a row from your Excel dataset and applies VADER Sentiment Analyzer to it by looping through each row and displaying the compound, positive, neutral and negative sentiment each in separate row next to the original data.
#Replace your_path\data.csv with path on your own PC.

#If you are using this code, please credit.

import vaderSentiment.vaderSentiment 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import pandas
     
analyser = SentimentIntensityAnalyzer()
    
def sentiment_analyzer_scores(text):
    score = analyser.polarity_scores(text)
    print("{:-<40} {}".format(text, str(score)))

with open(r'your_path\data.csv', 'r+') as data:
    for row in data:
        ap = sentiment_analyzer_scores(str(row))
        print (ap)
        writer = csv.writer(data)
        writer.writerow(ap)
