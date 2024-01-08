from google_play_scraper import app

result = app(
    'com.pathao.user',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

# print(result)

for i in result:
  print("-------------------------------")
  print(i)
  print("-------------------------------")
  print(result[i])


# finding all the top comments
print("These are the reviews(Top Comments) for the pathao application:")

print(result["comments"])
all_comments = result["comments"]


for i in all_comments:
  print(i)
  print("-------------------------------------------------")