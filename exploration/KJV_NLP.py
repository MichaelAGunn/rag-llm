import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#from langchain import SentimentAnalyzer
from textblob import TextBlob

cwd = os.getcwd()
print("CWD:", cwd)
p2cwd = os.path.dirname(cwd)
#kjv_df = pd.read_csv(os.path.join(p2cwd, 'data','en_kjv.csv'))
kjv_df = pd.read_csv(os.path.join(cwd, 'data','en_kjv.csv'))

sentiments = []
for index, row in kjv_df.iterrows():
	book = row['book']
	chapter = int(row['chapter'])
	verse = int(row['verse'])
	text = row['text']
	blob = TextBlob(text)
	sentiment_result = blob.sentiment
	# print("Book:", book, "| Chapter:", chapter, "| Verse:", verse)
	# if sentiment_result.polarity > 0:
	# 	print("Sentiment: Positive")
	# elif sentiment_result.polarity < 0:
	# 	print("Sentiment: Negative")
	# else:
	# 	print("Sentiment: Neutral")
	sentiments.append(sentiment_result.polarity)

kjv_df.insert(0, 'sentiment', sentiments)
print(kjv_df.head(50))
print(kjv_df.tail(50))

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
kjv_df.to_csv('bible_sentiment.csv', index=False)

'''
NLP Ideas:
- sentiment analysis of psalms by author (including anonymous group)
- sentiment analysis of section's 1 & 2 of Isaiah
- sentiment analysis of each NT author
- sentiment analysis of 2nd Kings with reference to who was king at any given time, and whether the king was good or evil
Visualization Ideas:
- seaborn's heatmap to visualize relationship between sentiments and authors
- latplotlib's lineplot to look at sentiment changes over time (best for 2nd Kings or 1st & 2nd Chronicles)
- 
'''
if __name__ == '__main__':
    book_sentiment_df = kjv_df.groupby('book')['sentiment'].mean().reset_index()
    melted_df = pd.melt(book_sentiment_df, id_vars='book', var_name='Sentiment')
    print(melted_df.head())
    plt.figure(figsize=(8, 6))
    sns.heatmap(melted_df.pivot_table(index='book', columns='Sentiment', values='value'), cmap='coolwarm', center=0, annot=True, fmt=".2f")
    plt.title('Sentiment by Book')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Books')
    plt.show()
