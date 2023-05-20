#!pip install pdfplumber
#!pip install nltk
#!pip install sumy
import pdfplumber
import nltk
from nltk.corpus import stopwords
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

nltk.download('stopwords')
nltk.download('punkt')

# Open the PDF file
with pdfplumber.open('/content/Operations Management.pdf') as pdf:
    # Extract the text from the PDF
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

# Clean the text by removing stop words and punctuation marks
stop_words = set(stopwords.words("english"))
text = " ".join([word for word in text.split() if word.lower() not in stop_words])

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(text)

# Get the total number of sentences
total_sentences = len(sentences)

# Initialize the tokenizer
tokenizer = Tokenizer("english")

# Initialize the summarizer
parser = PlaintextParser.from_string(text, tokenizer)
summarizer = LexRankSummarizer()

# Summarize the text with a target word count
target_word_count = 500
current_word_count = 0
summary_sentences = []
for sentence in summarizer(parser.document, sentences_count=total_sentences):
    sentence_word_count = len(sentence.words)
    if current_word_count + sentence_word_count <= target_word_count:
        summary_sentences.append(sentence)
        current_word_count += sentence_word_count
    else:
        break

# Join the summary sentences and print the result
summary = " ".join(str(sentence) for sentence in summary_sentences)

# Output the summary
print(summary)

