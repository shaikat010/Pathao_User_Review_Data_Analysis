# Filtering the review by the stars received
# Finding out the 2 star reviews
from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'com.pathao.user',
    lang='en',  # defaults to 'en'
    country='us',  # defaults to 'us'
    sort=Sort.NEWEST,  # defaults to Sort.NEWEST
    count=100,  # defaults to 100
    filter_score_with=2  # defaults to None(means all score)
)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

result, _ = reviews(
    'com.pathao.user',
    continuation_token=continuation_token  # defaults to None(load from the beginning)
)

print(result)

print(type(result))

print("-----------------------------Single Reviews -----------------------------------------")
for i in result:
    i = dict(i)
    print(i['content'])
    with open('2_Star.txt', 'a', encoding='utf-8') as file:
        data = i['content']
        file.write(data)
        file.write("\n")
    print("--------------------------------------------")
