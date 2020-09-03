import ParametersandClient as tr
import tweepy
import DBTwitter as DBT
import json
import requests
from pprint import pprint
import KeyAndEndPoint as key


key_header = key.get_key_endpoint()

endpoint = "https://textanalyticssti.cognitiveservices.azure.com"


language_api_url = endpoint + "/text/analytics/v3.0/languages"
sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"




# def call_text_analityc():
   




def scrap_tweets_replys(
                       search_words, date_since):
    
    query = DBT.read_tweetID_mssql()
    api = tr.get_twitter_api()
 
    # tweets = tweepy.Cursor(api.search,
    #                        q=search_words,
    #                        since=date_since,
    #                        tweet_mode='extended'
    #                     ).items()

    # for tweet in tweets:
        
    #     FromTwitterId = tweet.user.id
    #     username = tweet.user.screen_name
    #     location = tweet.user.location
    #     tweetcreatedts = tweet.created_at
    #     tweet_ID = tweet.id
    #     text = tweet.full_text
    #     retweetcount = tweet.retweet_count
    #     source = tweet.source
    #     in_reply_to_user_id = tweet.in_reply_to_user_id
    #     in_reply_to_status_id = tweet.in_reply_to_status_id
       

       
        # DBT.save_search_replys (FromTwitterId,
        #                        username,
        #                            text,
        #                        location,
        #                  tweetcreatedts,
        #                        tweet_ID,
        #             in_reply_to_user_id,
        #           in_reply_to_status_id, 
        #                          source)
         
    # query = DBT.read_tweetID_mssql()
    for columns in query:
        tweet_ID = columns[0]
        text = columns[1]


        documents = {"documents": [
            {"id": tweet_ID, "text": text},
            ]}

        iso_name = get_language_api_url( documents)
        
        
        
        documents = {"documents": [
            
            {"id": tweet_ID, "language": iso_name,
            "text": text},
            ]}
        
       
        azure_response = get_sentiment_url(documents)

        keyphrase = get_keyphrase_url(documents)
        entities = get_entities_url(documents)
        
       

#         

       
# # [0]['entities']
        
        
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
                
                # entities_subcategory = entities['documents'][0]['entities'][0]['subcategory']
                
        except:
            pass

        DBT.save_sentiment(tweet_ID, azure_sentimental, score_positive, score_neutral, score_negative) 
        DBT.save_entities(tweet_ID, entities_text,  entities_category,  entities_confidenceScore)   
             
      

        for keywords in azure_keyphrase:

                
                DBT.save_keyphrase(tweet_ID, keywords)           
                
                print('Insert Complete')
                print(json.dumps( tweet_ID, indent=5))
            
        
# #             
        # key.get_prueba(tweet_ID, text, key_header)

        

if __name__ == '__main__':
    
    search_words = "@bunburyoficial"
    date_since = "2020-08-29"
    # numTweets = 100
    # numRuns = 1

    # scrap_tweets(search_words, date_since, numTweets, numRuns),

    #parameters scrap_usersTimelines
    screen_name = "@bunburyoficial"

scrap_tweets_replys(search_words, date_since)
        