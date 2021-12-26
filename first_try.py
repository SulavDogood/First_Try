import pandas as pd
import numpy as np
import csv
pd.set_option('display.max_colwidth',-1)
jp = pd.read_csv(r"C:\Users\Sulav\Downloads\jeopardy_starting2\jeopardy_starting\jeopardy.csv")



jp.columns=["Show Number","Air Date","Round","Category","Value","Question","Answer"]

#jp=jp.Value[1:]

jp.Value=jp.Value.str.replace("$","")
jp.Value=jp.Value.str.replace("None","0")
jp.Value=jp.Value.str.replace(",","")
jp.Value= jp.Value.astype(float)

King_Names= jp[jp.Question.str.contains("King|king") & jp.Question.str.contains("England|england") ]

King = jp[jp.Question.str.contains("King|king")]

King_Difficulty= King.Value.mean()

#print(King[King.Answer==""].count())

#Unique_Answers= King.groupby("Answer").nunique().sort_values("Answer", ascending=False).reset_index()

print(King_Difficulty)

def Unique_Answers(columnn):
    for i in columnn:
        return columnn.unique().groupby("columnn").sort_by(i.nunique(), ascending=False)

Unique_Answers_Group = (King.Answer.value_counts(normalize=False, sort=True, ascending=False).reset_index())

print(Unique_Answers(King.Answer))

