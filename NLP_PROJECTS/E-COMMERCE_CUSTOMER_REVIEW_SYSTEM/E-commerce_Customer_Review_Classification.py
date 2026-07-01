import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="E-Commerce Customer Review Classification",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 E-Commerce Customer Review Classification")
st.write("Enter a customer review below to classify the issue.")

# ============================================================
# DATASET
# ============================================================

data = {
    "Review": [
        "My order arrived two days late",
        "The delivery was delayed",
        "Package delivered to the wrong address",
        "Delivery boy never arrived",
        "The package is still not delivered",
        "Received the product very late",

        "Payment failed but money was deducted",
        "Payment deducted twice",
        "Unable to complete payment",
        "Transaction failed",
        "Card payment not working",
        "Online payment issue",

        "The product is damaged",
        "Received a defective item",
        "Poor product quality",
        "The item is broken",
        "The product stopped working after one day",
        "Packaging was damaged",

        "I want to return this item",
        "Refund has not been received",
        "Replacement request is pending",
        "Return request is rejected",
        "Refund is taking too long",
        "Need refund for my order",

        "Customer support is not responding",
        "Support executive was rude",
        "Need help from customer service",
        "Customer care solved my issue",
        "Support team is very helpful",
        "Unable to contact customer service"
    ],

    "Category": [
        "Delivery Issue",
        "Delivery Issue",
        "Delivery Issue",
        "Delivery Issue",
        "Delivery Issue",
        "Delivery Issue",

        "Payment Issue",
        "Payment Issue",
        "Payment Issue",
        "Payment Issue",
        "Payment Issue",
        "Payment Issue",

        "Product Quality",
        "Product Quality",
        "Product Quality",
        "Product Quality",
        "Product Quality",
        "Product Quality",

        "Return & Refund",
        "Return & Refund",
        "Return & Refund",
        "Return & Refund",
        "Return & Refund",
        "Return & Refund",

        "Customer Service",
        "Customer Service",
        "Customer Service",
        "Customer Service",
        "Customer Service",
        "Customer Service"
    ]
}

df = pd.DataFrame(data)

X = df["Review"]
y = df["Category"]

# ============================================================
# MODEL
# ============================================================

model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("classifier", MultinomialNB())
])

model.fit(X, y)

# ============================================================
# USER INPUT
# ============================================================

review = st.text_area(
    "Enter Customer Review",
    placeholder="Example: My package was damaged and I need a refund."
)

# ============================================================
# BUTTON
# ============================================================

if st.button("Classify Review"):

    if review.strip() == "":
        st.warning("Please enter a customer review.")
    else:

        prediction = model.predict([review])[0]

        priority_keywords = {
            "High": [
                "damaged", "broken", "defective",
                "failed", "deducted", "refund",
                "wrong", "missing", "cancelled",
                "fraud", "not delivered"
            ],

            "Medium": [
                "late", "delay", "quality",
                "replacement", "return",
                "issue", "problem", "slow"
            ],

            "Low": [
                "help", "information",
                "details", "query",
                "support", "thanks"
            ]
        }

        review_lower = review.lower()

        priority = "Medium"

        for level in ["High", "Medium", "Low"]:
            if any(word in review_lower for word in priority_keywords[level]):
                priority = level
                break

        solutions = {
            "Delivery Issue":
                "Forward the complaint to the Logistics Team.",

            "Payment Issue":
                "Forward the complaint to the Billing & Payment Team.",

            "Product Quality":
                "Initiate product replacement or quality inspection.",

            "Return & Refund":
                "Forward the request to the Returns & Refund Department.",

            "Customer Service":
                "Assign the issue to the Customer Support Team."
        }

        st.success("Prediction Completed!")

        st.subheader("Results")

        st.write("**Predicted Category:**", prediction)
        st.write("**Priority Level:**", priority)
        st.write("**Suggested Action:**", solutions[prediction])