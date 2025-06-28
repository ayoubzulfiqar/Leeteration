def find_invalid_tweets(tweets: list[dict]) -> list[dict]:
    invalid_tweet_ids = []
    for tweet in tweets:
        tweet_id = tweet['tweet_id']
        content = tweet['content']
        
        # A tweet is considered invalid if its content length is less than 1
        # (i.e., empty) or strictly greater than 15 characters.
        if len(content) < 1 or len(content) > 15:
            invalid_tweet_ids.append({'tweet_id': tweet_id})
            
    return invalid_tweet_ids