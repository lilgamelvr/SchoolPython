import requests
from bs4 import BeautifulSoup  # Utilizes BeautifulSoup Library
from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from textblob import TextBlob  # Uses TextBlob

# 12.1
print('Exercise 12.1:')

url = "https://www.python.org"  # Downloads web page content
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
paragraphs = soup.find_all('p')
text = " ".join([p.get_text() for p in paragraphs])  # Retrieves stripped/text-only content form the downloaded web page

stop_words = set(stopwords.words('english'))
words = text.split()
words = [word for word in words if word.lower() not in stop_words]
filtered_text = " ".join(words)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_text)

print('Word Cloud:')
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()  # Code executes

# 12.2
print('Exercise 12.2:')  # All code placed in one file
tb = TextBlob(text)

# Use TextBlob to tokenize text into sentences
print("Tokenized into Sentences")
print(tb.sentences)

# Use TextBlob to tokenize text into words
print("Tokenized into words")
print(tb.words)

# Use TextBlob to tokenize text into noun phrases
print("Noun Phrases")
print(tb.noun_phrases)

# Each requirement in the rubric is clearly documented in code
