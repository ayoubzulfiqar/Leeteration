import collections

def count_artist_occurrences(ranking_list):
    artist_counts = collections.Counter()
    for item in ranking_list:
        if isinstance(item, dict) and 'artist' in item:
            artist_counts[item['artist']] += 1
    return artist_counts