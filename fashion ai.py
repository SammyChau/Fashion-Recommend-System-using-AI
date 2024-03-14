import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.corpus import stopwords
import string
# Specify the file path
file_path = "C:\\Users\\Sam\\OneDrive\\Desktop\\Fashion\\Myntra-Kurtis\\Myntra Kurtis\\Myntra kurtis.csv"
print("File path:", file_path)

# Read the CSV file
data = pd.read_csv(file_path)
print(data.head())
print("Type of data:", type(data))

# Print the count of missing values in each column
print(data.isnull().sum())
data = data.drop("Image",axis=1)
data = data.dropna()
print(data.shape)
text = " ".join(i for i in data["Brand Name"])
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, 
                      background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
highest_rated = data.sort_values(by=["Product Ratings"], 
                                 ascending=False)
highest_rated = highest_rated.head(10)
print(highest_rated[['Product Info', "Product Ratings", "Brand Name"]])
mr = data['Product Ratings'].mean()
m = data['Number of ratings'].quantile(0.9)
n = data['Number of ratings']
a = data['Product Ratings']
data["Score"]  = (n/(n+m) * a) + (m/(m+n) * mr)

recommendations = data.sort_values('Score', ascending=False)
print(recommendations[['Brand Name', 'Product Info',
                       'Product Ratings', 'Score', 
                       'Selling Price', 'Discount']].head(10))
