from twitter_crawler.crawler_service import CrawlerService
from data_service.mongo_accessor import TweetDataMongoAccessorSingleton



def crawler_operator(restaurant):
    print("")
    print("")
    print("Crawling "+restaurant)
    print("")
    print("")
    tweet_data = TweetDataMongoAccessorSingleton.getInstance()
    tweet_data_collection = tweet_data.coll
    restaurant_key = restaurant
    crawler = CrawlerService()
    message = crawler.crawl(restaurant_key)
    for tweet in message:
        if (tweet_data_collection.find({'message':tweet.text}).count() == 0):
            print(tweet.text)
            data = {}
            data["restaurant"] = restaurant_key
            data['message'] = tweet.text
            tweet_data_collection.insert(data)


crawler_operator("KFC");
crawler_operator("McDonalds")
