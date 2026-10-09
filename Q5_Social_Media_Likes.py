# Question 5: Social Media Likes

def analyze_likes(likes):
    highest_post = likes.index(max(likes)) + 1
    print("Post with highest likes:", highest_post, "-", max(likes), "likes")
    print("Total likes:", sum(likes))
    print("Posts with at least 100 likes:",
          [(i + 1, value) for i, value in enumerate(likes) if value >= 100])

analyze_likes([80, 150, 230, 95, 120])
