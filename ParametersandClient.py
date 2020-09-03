import tweepy
import DBTwitter as DBT
import json


def get_twitter_auth():
    
        consumer_key = "c3eDgJEQiLDB4OVmbYJ5fPNzh"
        consumer_secret = "6gu2KTOzyE1Z1EivkojYkuC0BW5aFNtQkKmZj4q3Hko81X4Dkl"
        access_token = "1292048921087348742-StKBKU8IsXzuGAqYroqKidnsGDW7wu"
        access_Token_Secret = "tMRJbY8qCt9zDjNv2RiQ2y9tmBEHLXmbSah9ADDVp24jA"
        auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        return auth


def get_twitter_api():
    
    auth = get_twitter_auth()
    
    api = tweepy.API(auth, 
                     wait_on_rate_limit= True,
                     wait_on_rate_limit_notify = True
                    )

    return api





#parameters scrap_usersTimelines
screen_name = "DoctorFarola"



# scraptweets(search_words, date_since, numTweets, numRuns)

   

