import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Read the CSV file
file_path = "C:\\Users\\Sam\\OneDrive\\Desktop\\Fashion\\Myntra-Kurtis\\Myntra Kurtis\\Myntra kurtis.csv"
data = pd.read_csv(file_path)

# Data Preprocessing
data = data.drop("Image", axis=1)
data = data.dropna()

# Define virtual assistant functions
def display_brand_wordcloud(data):
    text = " ".join(brand for brand in data["Brand Name"])
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    plt.figure(figsize=(15,10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def recommend_outfits(data):
    # Example: Recommend outfits based on the highest rated products
    highest_rated_outfits = data.sort_values(by=["Product Ratings"], ascending=False).head(3)
    for index, outfit in highest_rated_outfits.iterrows():
        print(f"Outfit {index + 1}:")
        print("Brand:", outfit["Brand Name"])
        print("Product Info:", outfit["Product Info"])
        print("Product Ratings:", outfit["Product Ratings"])
        print("Selling Price:", outfit["Selling Price"])
        print("Discount:", outfit["Discount"])
        print()

def display_highest_rated_products(data):
    highest_rated = data.sort_values(by=["Product Ratings"], ascending=False).head(10)
    print(highest_rated[['Product Info', "Product Ratings", "Brand Name"]])

# Define scoring function for recommendations
def calculate_score(data):
    mr = data['Product Ratings'].mean()
    m = data['Number of ratings'].quantile(0.9)
    n = data['Number of ratings']
    a = data['Product Ratings']
    data["Score"]  = (n/(n+m) * a) + (m/(m+n) * mr)

def display_recommendations(data):
    calculate_score(data)
    recommendations = data.sort_values('Score', ascending=False).head(10)
    print(recommendations[['Brand Name', 'Product Info', 'Product Ratings', 'Score', 'Selling Price', 'Discount']])

# Main function to handle user interaction
def virtual_assistant():
    print("Welcome to the Fashion Virtual Assistant!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Display Brands collabing with us")
        print("2. Recommend Outfits")
        print("3. Display Highest Rated Products")
        print("4. Display Recommendations")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            display_brand_wordcloud(data)
        elif choice == '2':
            recommend_outfits(data)
        elif choice == '3':
            display_highest_rated_products(data)
        elif choice == '4':
            display_recommendations(data)
        elif choice == '5':
            print("Thank you for using the Fashion Virtual Assistant. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")

# Call the virtual assistant function
virtual_assistant()
