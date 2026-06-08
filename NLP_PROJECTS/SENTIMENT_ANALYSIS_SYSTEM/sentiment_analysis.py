from textblob import TextBlob
from collections import Counter
import pandas as pd

results = []

while True:
    review = input("\nEnter Review (type 'exit' to quit): ")

    if review.lower() == "exit":
        break

    # TextBlob Analysis
    analysis = TextBlob(review)

    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    # Sentiment Classification
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Basic Statistics
    words = review.split()
    word_count = len(words)
    char_count = len(review)

    # Most Frequent Word
    word_freq = Counter(words)

    if len(word_freq) > 0:
        most_common_word = word_freq.most_common(1)[0][0]
    else:
        most_common_word = "None"

    # Display Results
    print("\n----- Analysis Result -----")
    print("Review:", review)
    print("Sentiment:", sentiment)
    print("Polarity Score:", round(polarity, 2))
    print("Subjectivity Score:", round(subjectivity, 2))
    print("Word Count:", word_count)
    print("Character Count:", char_count)
    print("Most Frequent Word:", most_common_word)

    # Store Results
    results.append([
        review,
        sentiment,
        polarity,
        subjectivity,
        word_count,
        char_count,
        most_common_word
    ])

# Save Results
if results:
    df = pd.DataFrame(
        results,
        columns=[
            "Review",
            "Sentiment",
            "Polarity",
            "Subjectivity",
            "Word_Count",
            "Character_Count",
            "Most_Frequent_Word"
        ]
    )

    df.to_csv("sentiment_analysis_results.csv", index=False)

    print("\nResults saved to sentiment_analysis_results.csv")