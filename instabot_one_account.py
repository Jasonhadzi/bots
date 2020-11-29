import random
from instapy import InstaPy
from instapy import smart_run
try:
    import config
except ImportError as e:
    raise e



# get a session!
session = InstaPy(username=config.insta_account['user'],
password=config.insta_account['pass'],bypass_security_challenge_using='sms',headless_browser=False,disable_image_load=True, multi_logs=True)


tags_to_not_like =  ['dick', 'elections','fakenews','crypto','trade','trading','fake','news', 'squirt', 'gay', 'homo', '#fit', '#fitfam', '#fittips',
         '#abs', '#kids', '#children', '#child',
         '[nazi','bot',
         'jew', 'judaism', '[muslim', '[islam', 'bangladesh', '[hijab',
         '[niqab', '[farright', '[rightwing',
         '#conservative', 'death', 'racist']

tags_to_like = config.insta_account['tags']

photo_comments = ['Nice shot! @{}',
    'Awesome! @{}',
    'Cool :thumbsup:',
    'Just incredible :open_mouth:',
    'Love your posts @{}',
    'Looks awesome @{}',
    'Nice @{}',
    'Wow',
    'Amazing',
    ':raised_hands: Yes!',
    'I can feel your passion @{} :muscle:']

# let's go! :>
with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-1.21,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    max_following=5555,
                                    min_followers=45,
                                    min_following=77)

    session.set_mandatory_language(enabled=True, character_set=['LATIN', 'GREEK'])
    session.set_dont_like(tags_to_not_like)


    session.set_user_interact(amount=5, randomize=True, percentage=80)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=100)

    session.set_do_comment(enabled = True, percentage = 95)
    session.set_comments(photo_comments, media = 'Photo')

    # activity
    session.like_by_tags(tags_to_like,
                         amount=random.randint(50, 100), interact=True)

    session.unfollow_users(amount=random.randint(75, 150),
                           instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO",
                           unfollow_after=90 * 60 * 60, sleep_delay=501)
