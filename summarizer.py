import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

def estimated_reading_time(text):
    mins = int(len(text) / 200)
    seconds = int((float(len(text) / 200) - mins) * 60)
    return "( Estimated reading time: {} mins, {} seconds )".format(str(mins), str(seconds))

def summarizer(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Create a frequency distribution of words
    fdist = FreqDist(words)
    
    # Get a list of stopwords
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords and punctuation
    filtered_words = [word for word in words if word.lower() not in stop_words and word.isalnum()]
    
    # Calculate word frequencies
    word_frequencies = {}
    for word in filtered_words:
        if word not in word_frequencies:
            word_frequencies[word] = fdist[word]
    
    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    sentences = sent_tokenize(text)
    for sentence in sentences:
        for word in word_tokenize(sentence):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    
    # Select sentences with the highest scores
    num_sentences = int(len(sentences) * 0.2)  # You can adjust the percentage as needed
    summary_sentences = [sentence for sentence, _ in sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]]
    
    # Generate the summary
    summary = " ".join(summary_sentences)
    return summary
