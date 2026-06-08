from textblob import TextBlob
import pandas as pd
from datetime import datetime
import os

print("=" * 50)
print("MENTAL HEALTH SENTIMENT ANALYZER")
print("=" * 50)

text = input("\nHow are you feeling today?\n\n")

# Sentiment Analysis
analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

if polarity > 0.1:
    mood = "Positive"
elif polarity < -0.1:
    mood = "Negative"
else:
    mood = "Neutral"

# Stress / Anxiety Indicators
stress_words = [
    "stress", "stressed",
    "anxiety", "anxious",
    "panic", "worried",
    "overwhelmed", "depressed",
    "sad", "lonely",
    "tired", "fear",
    "hopeless", "pressure"
]

text_lower = text.lower()

detected_words = []

for word in stress_words:
    if word in text_lower:
        detected_words.append(word)

# Mood Score
score = round((polarity + 1) * 50, 2)

print("\n" + "=" * 50)
print("ANALYSIS RESULT")
print("=" * 50)

print("Mood:", mood)
print("Polarity Score:", round(polarity, 2))
print("Mood Score:", score, "/100")

if detected_words:
    print("\nDetected Emotional Indicators:")
    print(", ".join(detected_words))
else:
    print("\nNo stress-related indicators detected.")

# Save Results
file_name = "mood_history.csv"

data = pd.DataFrame({
    "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Text": [text],
    "Mood": [mood],
    "Polarity": [polarity],
    "MoodScore": [score]
})

if os.path.exists(file_name):
    data.to_csv(file_name, mode="a", header=False, index=False)
else:
    data.to_csv(file_name, index=False)

print("\nMood saved to mood_history.csv")

# Mood Advice
print("\n" + "=" * 50)
print("WELL-BEING MESSAGE")
print("=" * 50)

if mood == "Positive":
    print("You seem to be feeling positive today. Keep up the good energy!")
elif mood == "Neutral":
    print("Your mood appears balanced. Consider taking breaks and staying active.")
else:
    print("Your text contains negative emotions or stress indicators.")
    print("Consider talking with trusted people, practicing self-care, or seeking professional support if needed.")

print("\nThank you for using the analyzer.")

print("\nDISCLAIMER:")
print("This tool is for educational and mood-tracking purposes only.")
print("It is NOT a medical or psychological diagnostic tool.")