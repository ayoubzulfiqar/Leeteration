import collections

def count_comments_per_post(comments_data):
    comment_counts = collections.defaultdict(int)
    for comment in comments_data:
        post_id = comment.get('post_id')
        if post_id is not None:
            comment_counts[post_id] += 1
    return dict(comment_counts)

if __name__ == "__main__":
    sample_comments = [
        {"comment_id": 1, "post_id": 101, "text": "Great post!"},
        {"comment_id": 2, "post_id": 102, "text": "Interesting perspective."},
        {"comment_id": 3, "post_id": 101, "text": "I agree completely."},
        {"comment_id": 4, "post_id": 103, "text": "Thanks for sharing."},
        {"comment_id": 5, "post_id": 102, "text": "Could you elaborate?"},
        {"comment_id": 6, "post_id": 101, "text": "Very insightful."},
        {"comment_id": 7, "post_id": 104, "text": "First comment!"},
        {"comment_id": 8, "post_id": 101, "text": "Another one."},
        {"comment_id": 9, "text": "Comment without post_id"},
    ]

    result = count_comments_per_post(sample_comments)
    print(result)

    empty_comments = []
    result_empty = count_comments_per_post(empty_comments)
    print(result_empty)

    no_post_id_comments = [
        {"comment_id": 10, "text": "No post id here"},
        {"comment_id": 11, "text": "Nor here"},
    ]
    result_no_id = count_comments_per_post(no_post_id_comments)
    print(result_no_id)