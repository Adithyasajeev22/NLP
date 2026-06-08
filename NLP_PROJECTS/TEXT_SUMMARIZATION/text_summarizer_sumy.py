from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Input paragraph
text = input("Enter a paragraph:\n")

# Create parser
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Summarizer
summarizer = LsaSummarizer()

print("\nSummary:\n")

# Generate 2-sentence summary
for sentence in summarizer(parser.document, 2):
    print(sentence)