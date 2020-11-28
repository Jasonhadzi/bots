from instapy import InstaPy
from instapy import smart_run
try:
    import config
except ImportError as e:
    raise e

# login credentials
insta_username = config.config["user"]
insta_password = config.config["pass"]

#path to your workspace
#set_workspace(path="/Users/jasonhadzikostas")

tags_to_like =["startup","socialmedia"]
tags_to_not_like = ["naked", "nsfw","bot","scam","fake"]


session = InstaPy(username=insta_username, password=insta_password,bypass_security_challenge_using='sms',
                  headless_browser=True,
                  disable_image_load=True,
                  multi_logs=True)



with smart_run(session):
        """ Activity flow """
        # general settings
    
        #Skip private account
        #Skip users that don't have profile picture
        session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=100)
        #This is used to check the number of existing likes a post has 
        #and if it either exceed the maximum value set OR does not pass the minimum value set 
        #then it will not like that post
        session.set_delimit_liking(enabled=True, max_likes=2005, min_likes=5)
    
        #Your bot won’t interact with posts by users who have more than 8,500 followers.
        session.set_relationship_bounds(enabled=True,min_posts=10,
                                 max_posts=500, max_followers=8500)
        session.set_dont_like(tags_to_not_like)
    
        # activity
        # Like posts based on hashtags and like 5 posts of its poster
        session.set_user_interact(amount=5, randomize=True, percentage=100, media='Photo')
        #By default, InstaPy will like the first nine top posts in addition to your amount value. In this case, 
        #that brings the total number of likes per tag to ten (nine top posts plus the one you specified in amount).
        session.like_by_tags(tags_to_like, amount=6, interact=True)
    

        #You can tell the bot to not only like the posts but also 
        #to follow some of the authors of those posts. You can do that with set_do_follow():
        #percentage 50% means follow half the users whose posts it liked
        session.set_do_follow(True, percentage=50)
    
    
        """ Joining Engagement Pods...
        """
        photo_comments = ['Nice shot! @{}',
        'Awesome! @{}',
        'Cool :thumbsup:',
        'Just incredible :open_mouth:',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Nice @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']
    
    
        session.set_do_comment(enabled = True, percentage = 95)
        session.set_comments(photo_comments, media = 'Photo')
        session.join_pods(topic='entertainment', engagement_mode='no_comments')
