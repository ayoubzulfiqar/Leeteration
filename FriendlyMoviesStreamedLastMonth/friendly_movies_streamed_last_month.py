import datetime

def get_friendly_movies_last_month(streaming_records):
    friendly_movies = set()
    
    today = datetime.date.today()
    
    if today.month == 1:
        last_month_year = today.year - 1
        last_month_month = 12
    else:
        last_month_year = today.year
        last_month_month = today.month - 1

    for record in streaming_records:
        try:
            stream_date_str = record['stream_date']
            stream_date = datetime.datetime.strptime(stream_date_str, '%Y-%m-%d').date()
            movie_rating = record['rating']
            movie_name = record['movie_name']

            is_last_month = (stream_date.year == last_month_year and
                             stream_date.month == last_month_month)

            is_friendly = (movie_rating >= 4.0)

            if is_last_month and is_friendly:
                friendly_movies.add(movie_name)
        except (ValueError, KeyError):
            continue

    return sorted(list(friendly_movies))