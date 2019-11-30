import tweepy
import time
import haiku
import sentences
import random
import ml_poetry


consumer_key = 'YOUR TWITTER API PUBLIC CONSUMER KEY'
consumer_secret = 'YOUR TWITTER API PRIVATE CONSUMER KEY'
access_token = 'YOUR TWITTER API PUBLIC ACCESS TOKEN'
access_token_secret = 'YOUR TWITTER API PRIVATE ACCESS TOKEN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Generate n haikus
def haiku_main(n):
    bank = haiku.init_bank()
    count = 0

    while count != n:
        api.update_status(haiku.make_haiku(bank))
        time.sleep(60)
        count += 1

# Generates n questions and replies to each with an answer
def sentence_main(n):

    count = 0
    sets = sentences.init_sets()

    while count != n:
        verb = random.choice(list(sets[0]))
        noun = random.choice(list(sets[1]))

        api.update_status(sentences.create_question(verb, noun))

        for tweet in api.user_timeline():
            if len(tweet.entities.get("hashtags")) != 0:
                if tweet.entities.get("hashtags")[0].get('text') == "question" and not tweet.favorited:
                    api.update_status(sentences.create_reply(verb,noun), in_reply_to_status_id = tweet.id)
                    api.create_favorite(tweet.id)
        time.sleep(60)
        count += 1

# Generates n Li Bai-like sentences
def li_bai_main(n):
    count = 0
    ml_poetry.clean_main()
    while count != n:
        api.update_status(ml_poetry.generate_main())
        time.sleep(20)
        count += 1

def main():
    n = 5
    # haiku_main(n)
    # sentence_main(n)
    li_bai_main(n)

main()