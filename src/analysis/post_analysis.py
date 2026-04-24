from collections import Counter

def first_digit(n):
    return int(str(n)[0]) if n > 0 else 0

def benford(nums):
    digits = [first_digit(n) for n in nums if n > 0]
    total = len(digits)
    count = Counter(digits)
    return {d: count[d] / total for d in count}

def analyze(posts, followers):
    likes = [p["likes"] for p in posts]
    comments = [p["comments"] for p in posts]

    avg_likes = sum(likes)/len(likes) if likes else 0
    avg_comments = sum(comments)/len(comments) if comments else 0
    engagement = (avg_likes + avg_comments) / followers if followers else 0

    return {
        "avg_likes": avg_likes,
        "avg_comments": avg_comments,
        "engagement": engagement,
        "benford": benford(likes)
    }