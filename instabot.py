import random
from instapy import InstaPy
from instapy import smart_run
try:
    import config
except ImportError as e:
    raise e

# login credentials
for key, value in config.config.items():
    insta_username = value["user"]
    insta_password = value["pass"]

    tags_to_like = value["tags"]
    tags_to_not_like =  ['dick', 'elections','fakenews','crypto','trade','trading','fake','news', 'squirt', 'gay', 'homo', '#fit', '#fitfam', '#fittips',
         '#abs', '#kids', '#children', '#child',
         '[nazi','bot',
         'jew', 'judaism', '[muslim', '[islam', 'bangladesh', '[hijab',
         '[niqab', '[farright', '[rightwing',
         '#conservative', 'death', 'racist']

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

    session = InstaPy(username=insta_username, password=insta_password,bypass_security_challenge_using='sms',
                      headless_browser=True,
                      disable_image_load=True,
                      multi_logs=True)

    

    with smart_run(session):
        """ Activity flow """

        session.set_mandatory_language(enabled=True, character_set=['LATIN', 'GREEK'])

        session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-1.21,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    max_following=5555,
                                    min_followers=45,
                                    min_following=77)

        session.set_dont_like(tags_to_not_like)
    

        session.set_user_interact(amount=5, randomize=True, percentage=80)
        session.set_do_follow(enabled=True, percentage=70)
        session.set_do_like(enabled=True, percentage=100)

    # activity
        session.like_by_tags(tags_to_like,
                         amount=random.randint(50, 100), interact=True)

        session.unfollow_users(amount=random.randint(75, 150),
                           instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO",
                           unfollow_after=90 * 60 * 60, sleep_delay=501)

        session.set_do_comment(enabled = True, percentage = 95)
        session.set_comments(photo_comments, media = 'Photo')
