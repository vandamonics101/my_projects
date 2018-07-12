import tweepy

auth = tweepy.OAuthHandler('KpusMO0j0UbUbVhl6TJqCNG6C','OuM7N5EwfylGtKJGrkN0eIxe71nrj46z4Lrvt2b4B10n4SZuDY')
auth.set_access_token('1014873974793220101-WlFj6VfmgmwrYX6n4iEfU0GqOZJSTj','8YAlVBWihJJyG8VzaPdKFhAQGy3mwTmb4efaiMZ3P4qUO')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)

