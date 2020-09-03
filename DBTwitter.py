import pyodbc
import json


with open('config.json', 'r') as file:
    config = json.load(file)


database_name = config['ConnectionStrings']['DB_NAME']
database_user = config['ConnectionStrings']['DB_USER']
database_password = config['ConnectionStrings']['DB_PASSWORD']
database_server = config['ConnectionStrings']['SERVER']
dbms_driver = config['ConnectionStrings']['driver']

ConnectionString = "DRIVER={0};SERVER={1};DATABASE={2};UID={3};PWD={4}".format(dbms_driver
                                                                                ,database_server
                                                                                ,database_name
                                                                                ,database_user
                                                                                ,database_password
                                                                               )

def get_db_connection():
    connection = pyodbc.connect(ConnectionString)
    return connection

def read_tweetID_mssql():

    sqlStatement = "SELECT TweetID, TweetText FROM [Twitter].[SearchedTweetsReplies]"
    
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    var = insert.fetchall()
    return var

def save_search(FromTwitterId, username, text, location, tweetcreatedts, tweet_ID, in_reply_to_status_id, source ):
    
    sqlStatement = """INSERT INTO [Twitter].[SearchedTweets]([FromTwitterID]
                                                            , [UserName]
                                                            , [TweetText]
                                                            , [Location]
                                                            , [CreatedAt]
                                                            , [TweetID]
                                                            , [InReplyToTweetID]
                                                            , [Source]) 
                                                            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')""".format(
                                                                                                                                str(FromTwitterId),username, text, location, 
                                                                                                                                tweetcreatedts, tweet_ID,str(in_reply_to_status_id),
                                                                                                                                str(source)
                                                                                                                              )
    
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    Context.commit()


def save_tweets_timeline(createdAt, twitter_ID, tweet_text, tweet_ID, source ):
    
    sqlStatement = """INSERT INTO [Twitter].[AccountTweetsTimeline]([CreatedAt]
                                                                    ,[TwitterID]
                                                                    ,[TweetText]
                                                                    ,[TweetID]
                                                                    ,[Source]) 
                                                                    VALUES ('{0}',{1},'{2}','{3}','{4}')""".format(createdAt, twitter_ID,
                                                                                                                    str(tweet_text),tweet_ID, str(source) 
                                                                                                                  )
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    Context.commit()

def save_tweets_metric(tweet_ID, retweeted, like_count, in_reply_to_screen_name, in_reply_to_status_Id, is_quote_status):
    
    sqlStatement = """INSERT INTO [Twitter].[TweetsMetricsReplysQuotes]([TweetID]
                                                                    , [Retweeted]
                                                                    , [LikeCount]
                                                                    , [InReplyToStatusName]
                                                                    , [InReplyToStatusID]
                                                                    , [IsQuoteStatus]) 
                                                                    VALUES ('{0}',{1},{2},'{3}','{4}','{5}')""".format(tweet_ID, retweeted, like_count, in_reply_to_screen_name, in_reply_to_status_Id, is_quote_status
                                                                                                                  )
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    Context.commit()

def save_user_account(user_name, screen_name, Twitter_ID, user_createdts):
    
    sqlStatement = """ INSERT INTO [Twitter].[UserAccount]([UserName]
                                                        ,[ScreenName]
                                                        ,[TwitterID]
                                                        ,[Usercreatedts])
                                                        VALUES ('{0}','{1}',{2},'{3}')""".format(
                                                                                                    user_name, screen_name, Twitter_ID, str(user_createdts)
                                                                                                 )
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    Context.commit()



def save_about_user(Twitter_ID, followers, total_tweets, total_retweet):
    
    sqlStatement = """ INSERT INTO [Twitter].[AboutUserAccount]([TwitterID]
                                                                ,[Followers]
                                                                ,[TotalTweets]
                                                                ,[TotalRetweet])
                                                                VALUES ({0},{1},{2},{3})""".format(
                                                                                                    Twitter_ID, followers, total_tweets, total_retweet
                                                                                                    )
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    Context.commit()

# def metodo():
#     sqlStatement = """select * from [Twitter].[SentimentScore]"""
#     Context = get_db_connection()
#     insert = Context.cursor()
#     insert.execute(sqlStatement) 
#     var = insert.fetchone()
#     return var
    
    

def save_search_replys(FromTwitterId, username, text, location, tweetcreatedts, tweet_ID, in_reply_to_user_id , in_reply_to_status_id, source ):
    
    sqlStatement = """INSERT INTO [Twitter].[SearchedTweetsReplies]([FromTwitterID]
                                                            , [UserName]
                                                            , [TweetText]
                                                            , [Location]
                                                            , [CreatedAt]
                                                            , [TweetID]
                                                            , [AboutTwitterID]
                                                            , [InReplyToTweetID]
                                                            , [Source]) 
                                                            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')""".format(
                                                                                                                                str(FromTwitterId),username, text, location, 
                                                                                                                                tweetcreatedts, str(tweet_ID), in_reply_to_user_id, str(in_reply_to_status_id),
                                                                                                                                str(source)
                                                                                                                              )
    
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    Context.commit()

def save_sentiment(tweet_ID, azure_sentimental, score_positive, score_neutral, score_negative):
    
    sqlStatement = """INSERT INTO [Twitter].[SentimentScore]([TweetID]
                                                            , [Sentiment]
                                                            , [PositiveScore]
                                                            , [NeutralScore]
                                                            , [NegativeScore]) 
                                                            VALUES ('{0}','{1}','{2}','{3}',{4})""".format( tweet_ID
                                                                                                     ,azure_sentimental
                                                                                                    , score_positive
                                                                                                    , score_neutral
                                                                                                    , score_negative
                                                                                                        )
    
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    Context.commit()


def save_keyphrase(tweet_ID, keywords):
    # values = ",".join(azure_keyphrase) 

    sqlStatement = """INSERT INTO [Twitter].[TweetsKeyWords]([TweetID]
                                                            , [Phrase]) 
                                                            VALUES ({0},'{1}')""".format(tweet_ID, keywords)
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    Context.commit()



    


def save_entities(tweet_ID, entities_text,  entities_category, entities_confidenceScore):
    
    sqlStatement = """INSERT INTO [Twitter].[TweetsEntities]([TweetID]
                                                            , [Text]
                                                            , [Category]
                                                            , [ConfidenceScore]) 
                                                            VALUES ('{0}','{1}','{2}',{3})""".format(
                                                                                         tweet_ID, entities_text,  entities_category, entities_confidenceScore)
    
    Context = get_db_connection()
    insert = Context.cursor()
    insert.execute(sqlStatement) 
    Context.commit()

