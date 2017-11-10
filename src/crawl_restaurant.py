from twitter_crawler.crawler_service import CrawlerService
from data_service.mongo_accessor import TweetDataMongoAccessorSingleton



def crawler_operator(restaurant_key, restaurant_query):
    print("")
    print("")
    print("Crawling "+restaurant_key + "  with key word " + restaurant_query)
    print("")
    print("")
    tweet_data = TweetDataMongoAccessorSingleton.getInstance()
    tweet_data_collection = tweet_data.coll
    crawler = CrawlerService()
    message = crawler.crawl(restaurant_query)
    for tweet in message:
        if (tweet_data_collection.find({'message':tweet.text}).count() == 0):
            print(tweet.text)
            data = {}
            data["restaurant"] = restaurant_key
            data['message'] = tweet.text
            tweet_data_collection.insert(data)

def read_query_file():
     query_file = open("resto_query.txt","r")
     for line in query_file:
         restaurant_key, restaurant_query = line.split("|")
         restaurant_query = restaurant_query.replace("\n","")
         crawler_operator(restaurant_key,restaurant_query)

read_query_file()
