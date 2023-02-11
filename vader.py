from fastapi import FastAPI, HTTPException
from fastapi.params import Body
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import numpy as np
import urllib
import nltk
nltk.download('punkt')
# import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()

@app.get("/")
async def index():
    return {"messaage": "hello world"}


@app.post("/analyze")
async def analyze(payload: dict = Body(...)):
    try:
        # data = pd.read_csv("senti.csv")
        sid_obj = SentimentIntensityAnalyzer() 

        data = payload["scraped"]

        sentiment_dict = sid_obj.polarity_scores(data) 
        tokenized_sentence = nltk.word_tokenize(data)
        pos_word_list=[]
        neu_word_list=[]
        neg_word_list=[]

        for word in tokenized_sentence:
            if (sid_obj.polarity_scores(word)['compound']) >= 0.1:
                pos_word_list.append(word)
            elif (sid_obj.polarity_scores(word)['compound']) <= -0.1:
                neg_word_list.append(word)
            else:
                neu_word_list.append(word)

                
        wordcloud = WordCloud().generate(" ".join(pos_word_list))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        
        # Save the image to a buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        pos_image = urllib.parse.quote(buffer.getvalue().hex())
        
        wordcloud = WordCloud().generate(" ".join(neg_word_list))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        
        # Save the image to a buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        neg_image = urllib.parse.quote(buffer.getvalue().hex())

        return {
                "sentiment": sentiment_dict,
                "positive-words":pos_word_list,
                "negative-words":neg_word_list,
                "neutral-words":neu_word_list,
                "pos-image" : pos_image,
                "neg-image" : neg_image
                }
    except Exception as e:
        return { "message": str(e) }