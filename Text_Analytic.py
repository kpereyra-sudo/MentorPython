import DBTwitter as DBT
import json
import requests
from pprint import pprint
import KeyAndEndPoint as key



key_header = key.get_key_endpoint()


def call_text_analytic():

    query = DBT.read_tweetID_mssql()

    for columns in query:
        tweet_ID = columns[0]
        text = columns[1]

        documents = {"documents": [
            {"id": tweet_ID, "text": text},
            ]}

        iso_name = key.get_language_api_url(documents)

        documents = {"documents": [
            
            {"id": tweet_ID, "language": iso_name,
            "text": text},
            ]}
        

        azure_response = key.get_sentiment_url(documents)
        keyphrase = key.get_keyphrase_url(documents)
        entities = key.get_entities_url(documents)

        try:    
                
                azure_documents = azure_response['documents']
                azure_sentimental = azure_documents[0]['sentiment']
                score_positive = azure_documents[0]['confidenceScores']['positive']
                score_neutral = azure_documents[0]['confidenceScores']['neutral']
                score_negative = azure_documents[0]['confidenceScores']['negative']
                azure_key = keyphrase['documents']
                azure_id = keyphrase['documents'][0]['id']
                azure_keyphrase = keyphrase['documents'][0]['keyPhrases']
                entities_confidenceScore = entities['documents'][0]['entities'][0]['confidenceScore']
                entities_text = entities['documents'][0]['entities'][0]['text']  
                entities_category = entities['documents'][0]['entities'][0]['category']
                
               
                
        except:
            pass

        DBT.save_sentiment(
                            tweet_ID, azure_sentimental, score_positive, score_neutral, score_negative) 
        
        print('Insert Sentiment')
        
        DBT.save_entities(
                            tweet_ID, entities_text,  entities_category,  entities_confidenceScore)
        
        print('Insert Entities')

        for keywords in azure_keyphrase:
    
                
                DBT.save_keyphrase(
                                    tweet_ID, keywords)           
                
                print('Insert Keyphrase')
                

call_text_analytic()   