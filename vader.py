from fastapi import FastAPI
from fastapi.params import Body
import nltk
nltk.download('punkt')
# import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

vader_api = FastAPI()

@vader_api.get("/")
async def index():
    return {"messaage": "hello world"}


@vader_api.post("/analyze")
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

        return {
                "sentiment": sentiment_dict,
                "positive-words":pos_word_list,
                "neutral-words":neu_word_list,
                "negative-words":neg_word_list      
                }
    except Exception as e:
        return { "message": str(e) }
