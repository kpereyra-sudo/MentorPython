import ParametersandClient as tr
import tweepy
import DBTwitter as DBT
import json
#parameters search
# search_words = "Liz Maria"
# date_since = "2020-08-21"
# numTweets = 50
# numRuns = 1

# #parameters scrap_usersTimelines
# screen_name = "DoctorFarola"


# def scrap_user_account(screen_name, date_since, numRuns):
    
#     api = tr.get_twitter_api()
    
#     timelines = tweepy.Cursor(api.user_timeline,
#                                screen_name=screen_name,
#                                since=date_since,
#                                tweet_mode='extended'
#                               ).items(1)
    
    
#     for tweet in timelines:

#         user_name = tweet.user.name
#         screen_name = tweet.user.screen_name
#         followers = tweet.user.followers_count
#         Twitter_ID = tweet.user.id
#         total_tweets = tweet.user.statuses_count
#         total_retweet = tweet.retweet_count
#         user_createdts = tweet.user.created_at
#         hashtags = json.dumps(tweet.entities['hashtags'], indent=5)

#         DBT.save_user_account(user_name,
#                            screen_name,
#                             Twitter_ID,
#                          user_createdts)


# def scrap_about_user(screen_name, date_since, numRuns):

#     api = tr.get_twitter_api()
    
#     timelines = tweepy.Cursor(api.user_timeline,
#                                screen_name=screen_name,
#                                since=date_since,
#                                tweet_mode='extended'
#                               ).items(1)
    
    
#     for tweet in timelines:

#         user_name = tweet.user.name
#         screen_name = tweet.user.screen_name
#         followers = tweet.user.followers_count
#         Twitter_ID = tweet.user.id
#         total_tweets = tweet.user.statuses_count
#         total_retweet = tweet.retweet_count
#         user_createdts = tweet.user.created_at
#         hashtags = json.dumps(tweet.entities['hashtags'], indent=5)

#         DBT.save_about_user(Twitter_ID,
#                              followers,
#                             total_tweets,
#                             total_retweet,
#                             )
                        
     
def scrap_tweets(search_words, date_since, numTweets, numRuns):
    
    api = tr.get_twitter_api()
    
    tweets = tweepy.Cursor(api.search,
                           q=search_words,
                           since=date_since,
                           tweet_mode='extended'
                          ).items(numTweets)

    for tweet in tweets:
        
        FromTwitterId = tweet.user.id
        username = tweet.user.screen_name
        location = tweet.user.location
        tweetcreatedts = tweet.created_at
        tweet_ID = tweet.id
        text = tweet.full_text
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
        Symbols = tweet.entities['symbols']
        source = tweet.source
        in_reply_to_status_id = tweet.in_reply_to_status_id
        in_reply_to_screen_name = tweet.in_reply_to_screen_name

        print(retweetcount)

       
        DBT.save_search( FromTwitterId,
                               username,
                                   text,
                               location,
                         tweetcreatedts,
                               tweet_ID,
                  in_reply_to_status_id, 
                                 source
                         )



# def scrap_usersreplys(screen_name, date_since, numTweets, numRuns):
    
#     api = tr.get_twitter_api()

#     tweets = tweepy.Cursor(api.search,
#                            q=search_words,
#                            since=date_since,
#                            tweet_mode='extended'
#                           ).items(numTweets)

#     for tweet in tweets:
#         in_reply_to_status_Id = tweet.in_reply_to_status_id
#         in_reply_to_screen_name = tweet.in_reply_to_screen_name
#         createdAt = tweet.created_at
#         twitter_ID = tweet.user.id
#         tweet_text = tweet.full_text
#         tweet_ID = tweet.id_str
#         retweeted = tweet.retweet_count
#         like_count = tweet.favorite_count
#         is_quote_status = tweet.is_quote_status
#         source = json.dumps(tweet._json['source'])
        
#         DBT.save_timeline(createdAt,
#                          twitter_ID,
#                          tweet_text,
#                            tweet_ID,
#                           retweeted,
#                          like_count,
#             in_reply_to_screen_name,
#             in_reply_to_status_Id,
#                     is_quote_status,
#                               source 
#                         )
        
        
        
#         print(in_reply_to_status_Id, in_reply_to_screen_name, tweet_text )






def scrap_usersTimelines(screen_name, date_since, numTweets, numRuns):
    
    api = tr.get_twitter_api()

    timelines = tweepy.Cursor(api.user_timeline,
                             screen_name=screen_name,
                             since_id=date_since,
                             tweet_mode='extended'
                             ).items(numTweets)

    for tweet in timelines:

        createdAt = tweet.created_at
        twitter_ID = tweet.user.id
        tweet_text = tweet.full_text
        tweet_ID = tweet.id_str
        retweeted = tweet.retweet_count
        like_count = tweet.favorite_count
        in_reply_to_status_Id = tweet.in_reply_to_status_id
        in_reply_to_screen_name = tweet.in_reply_to_screen_name
        is_quote_status = tweet.is_quote_status
        source = json.dumps(tweet._json['source'])
        
        DBT.save_tweets_timeline(createdAt,
                         twitter_ID,
                         tweet_text,
                           tweet_ID,
                              source 
                        )

# def scrap_tweets_metric(screen_name, date_since, numTweets, numRuns):
    
#     api = tr.get_twitter_api()

#     timelines = tweepy.Cursor(api.user_timeline,
#                              screen_name=screen_name,
#                              since=date_since,
#                              tweet_mode='extended'
#                              ).items(numTweets)

#     for tweet in timelines:

#         createdAt = tweet.created_at
#         twitter_ID = tweet.user.id
#         tweet_text = tweet.full_text
#         tweet_ID = tweet.id_str
#         retweeted = tweet.retweet_count
#         like_count = tweet.favorite_count
#         in_reply_to_status_Id = tweet.in_reply_to_status_id
#         in_reply_to_screen_name = tweet.in_reply_to_screen_name
#         is_quote_status = tweet.is_quote_status
#         source = json.dumps(tweet._json['source'])
        
#         DBT.save_tweets_metric(tweet_ID,
#                                 retweeted,
#                                 like_count,
#                     in_reply_to_screen_name,
#                         in_reply_to_status_Id,
#                                 is_quote_status
#                               )   

      
        
  
# scrap_usersTimelines(screen_name, date_since, numTweets, numRuns)  

if __name__ == '__main__':
    
    search_words = "@bunburyoficial"
    date_since = "2020-08-30"
    numTweets = 100
    numRuns = 1

    # scrap_tweets(search_words, date_since, numTweets, numRuns),

    #parameters scrap_usersTimelines
    screen_name = "@bunburyoficial"

    # scrap_usersTimelines(screen_name, date_since, numTweets, numRuns)
    # scrap_tweets_metric(screen_name, date_since, numTweets, numRuns)  
    # scrap_about_user(screen_name, date_since, numRuns)
    # scrap_user_account(screen_name, date_since, numRuns)
    # scrap_usersreplys(screen_name, date_since, numTweets, numRuns)
    scrap_tweets(search_words, date_since, numTweets, numRuns)