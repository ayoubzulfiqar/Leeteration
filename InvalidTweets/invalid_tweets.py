import pandas as pd

def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['content_length'] = tweets['content'].apply(len)
    invalid_tweets = tweets[tweets['content_length'] > 15]
    result = invalid_tweets[['tweet_id']]
    return result