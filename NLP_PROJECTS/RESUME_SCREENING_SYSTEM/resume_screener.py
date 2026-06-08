import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the small English model from spaCy
nlp = spacy.load("en_core_web_sm")

# 1. Sample Data
job_description = """
We are looking for a Data Scientist with 3+ years of experience. 
The ideal candidate must be proficient in Python, SQL, and Machine Learning. 
Experience with Deep Learning, NLP, and deploying models using Flask or FastAPI is highly preferred. 
Strong data visualization skills using Tableau or PowerBI are a plus.
"""

# Two sample resumes to compare
resume_candidate_A = """
John Doe - Data Scientist
Skills: Python, SQL, Machine Learning, NLP, Deep Learning, Git, Docker.
Experience: Built and deployed predictive machine learning models using Python and Flask. 
Extensive experience cleaning text data for Natural Language Processing tasks. Experienced with SQL databases.
"""

resume_candidate_B = """
Jane Smith - Creative Marketing Manager
Skills: Digital Marketing, SEO, Copywriting, Social Media Strategy, Adobe Photoshop.
Experience: Led a team of content creators. Developed high-converting email marketing campaigns. 
Proficient in Google Analytics and data visualization for marketing metrics.
"""


def preprocess_text(text):
    """
    Cleans text by lowercasing, removing punctuation, 
    removing stop words, and reducing words to their base form (lemmatization).
    """
    doc = nlp(text.lower())
    cleaned_tokens = []

    for token in doc:
        # Filter out stop words, punctuation, spaces, and numbers
        if not token.is_stop and not token.is_punct and not token.is_space and not token.like_num:
            # Append the lemma (base form) of the word
            cleaned_tokens.append(token.lemma_)

    return " ".join(cleaned_tokens)


def calculate_match(job_desc, resume):
    """
    Preprocesses both texts, converts them to TF-IDF vectors, 
    and calculates their Cosine Similarity score.
    """
    # Clean both strings
    cleaned_jd = preprocess_text(job_desc)
    cleaned_resume = preprocess_text(resume)

    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the texts into mathematical vectors
    tfidf_matrix = vectorizer.fit_transform([cleaned_jd, cleaned_resume])

    # Calculate Cosine Similarity between the first vector (JD) and second vector (Resume)
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    # FIXED: Extracted the float value from the matrix index before rounding
    match_percentage = round(float(similarity_matrix) * 100, 2)
    return match_percentage


# 3. Run the Screening Pipeline
if __name__ == "__main__":
    print("--- Initializing Resume Screening Pipeline ---\n")

    score_A = calculate_match(job_description, resume_candidate_A)
    score_B = calculate_match(job_description, resume_candidate_B)

    print(f"Candidate A (Data Scientist Resume) Match Score: {score_A}%")
    print(f"Candidate B (Marketing Resume) Match Score: {score_B}%")

    # Ranking logic
    results = [("Candidate A", score_A), ("Candidate B", score_B)]
    
    # FIXED: Sort results specifically by the score (x) instead of trying to sort the whole tuple object
    ranked_results = sorted(results, key=lambda x: x, reverse=True)

    print("\n--- Final Rankings ---")
    # FIXED: Removed the broken trailing ".i" syntax error
    for rank, (candidate, score) in enumerate(ranked_results, 1):
        print(f"Rank {rank}: {candidate} with a score of {score}%")

        