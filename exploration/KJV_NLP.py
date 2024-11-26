import os
import pandas as pd
#from langchain import SentimentAnalyzer
from textblob import TextBlob

cwd = os.getcwd()
print("CWD:", cwd)
p2cwd = os.path.dirname(cwd)
#kjv_df = pd.read_csv(os.path.join(p2cwd, 'data','en_kjv.csv'))
kjv_df = pd.read_csv(os.path.join(cwd, 'data','en_kjv.csv'))

# sentiment_analyzer = SentimentAnalyzer()

for index, row in kjv_df.iterrows():
	book = row['book']
	chapter = int(row['chapter'])
	verse = int(row['verse'])
	text = row['text']
	blob = TextBlob(text)
	sentiment_result = blob.sentiment
	print("Book:", book, "| Chapter:", chapter, "| Verse:", verse)
	if sentiment_result.polarity > 0:
		print("Sentiment: Positive")
	elif sentiment_result.polarity < 0:
		print("Sentiment: Negative")
	else:
		print("Sentiment: Neutral")
	break

# bible_sentiment_data = pd.DataFrame(
# 	{
# 		'book': kjv_df['book'],
# 		'chapter': kjv_df['chapter'],
# 		'verse': kjv_df['verse'],
# 		# 'sentiment': [result.sentiment for result in pipeline.run(kjv_df['text'])]
# 		'sentiment': [result.sentiment for result in [sentiment_analyzer.analyze(text) for text in kjv_df['text']]]
# 	}
# )
# bible_sentiment_data.to_csv('bible_sentiment.csv', index=False)