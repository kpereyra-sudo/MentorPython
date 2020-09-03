import requests
# import TextAnalyticsClient
# import AzureKeyCredential
import json
from pprint import pprint
import DBTwitter  as DBT



def get_key_endpoint():

    subscription_key = "2b366bf7bfe34b2691251f909bf63cb6"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    return headers 

key_header = get_key_endpoint()

def get_language_api_url(documents):
    
    language_api_url =  "https://textanalyticssti.cognitiveservices.azure.com/text/analytics/v3.0/languages"
    response = requests.post(language_api_url, headers=key_header, json=documents)
    languages = response.json()
    iso639name = languages['documents'][0]['detectedLanguage']['iso6391Name']
    return iso639name


def get_sentiment_url(documents):

    sentiment_url =  "https://textanalyticssti.cognitiveservices.azure.com/text/analytics/v3.0/sentiment"
    response  = requests.post(sentiment_url, headers=key_header, json=documents)
    azure_response = response.json()
    return azure_response


def get_keyphrase_url(documents):

    keyphrase_url =  "https://textanalyticssti.cognitiveservices.azure.com/text/analytics/v3.0/keyphrases"
    response  = requests.post(keyphrase_url, headers=key_header, json=documents)
    keyphrase = response.json()
    return keyphrase


def get_entities_url(documents):

    entities_url =  "https://textanalyticssti.cognitiveservices.azure.com/text/analytics/v3.0/entities/recognition/general"
    response  = requests.post(entities_url, headers=key_header, json=documents)
    entities = response.json()
    return entities

