import tweepy

auth = tweepy.OAuthHandler('BRRzUTfkkfap5FvDSah1JhRQ6', 'XDyuHzXOwYD1ZssSvuNo3AWkK7oTHwjyDnhJauaVHuRUB2NFN0')
auth.set_access_token('1299813553881395200-wVcfbhEDVKVgTb436u4Igijjw36ySH', '5B0r4wx2NZSske3cW20gXFZiGOK5E3rgnIrJem9VKIqCA')

api = tweepy.API(auth,  wait_on_rate_limit=True)

