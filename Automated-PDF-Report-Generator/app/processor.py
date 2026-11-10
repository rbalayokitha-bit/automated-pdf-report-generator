def process_posts(posts):

    total_posts = len(posts)

    total_title_length = 0

    user_ids = set()

    for post in posts:

        total_title_length += len(post["title"])

        user_ids.add(post["userId"])

    if total_posts > 0:
        average_title_length = total_title_length / total_posts
    else:
        average_title_length = 0

    result = {
        "total_posts": total_posts,
        "total_users": len(user_ids),
        "average_title_length": round(average_title_length, 2)
    }

    return result


if __name__ == "__main__":

    from api import fetch_posts

    posts = fetch_posts(10)

    result = process_posts(posts)

    print("DATA ANALYSIS REPORT")
    print("----------------------")

    print("Total Posts:", result["total_posts"])

    print("Total Users:", result["total_users"])

    print("Average Title Length:", result["average_title_length"])