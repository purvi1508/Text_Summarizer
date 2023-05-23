from flask import Flask, render_template, request, flash
import nltk
from nltk.corpus import stopwords
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

nltk.download('stopwords')
nltk.download('punkt')

app = Flask(__name__)
app.secret_key = '8f42a73054b1749f8f58848be5e6502c'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        # Retrieve form data
        input_text = request.form.get('text-input')
        selected_option = request.form.get('summary-length')

        # Validate the form data
        if not input_text:
            error_message = "Input text is required."
            flash(error_message, 'error')
            return render_template('index.html')

        if not selected_option:
            error_message = "Summary length option is required."
            flash(error_message, 'error')
            return render_template('index.html')

        # Additional validation and handling code...
        # Perform any other required checks or validations on the form data

        # Clean the text by removing stop words and punctuation marks
        stop_words = set(stopwords.words("english"))
        cleaned_text = " ".join([word for word in input_text.split() if word.lower() not in stop_words])
        print("Cleaned Text:", cleaned_text)

        # Tokenize the text into sentences
        sentences = nltk.sent_tokenize(cleaned_text)
        print("Sentences:", sentences)

        # Get the total number of sentences
        total_sentences = len(sentences)
        print("Total Sentences:", total_sentences)

        # Initialize the tokenizer
        tokenizer = Tokenizer("english")

        # Initialize the summarizer
        parser = PlaintextParser.from_string(cleaned_text, tokenizer)
        summarizer = LexRankSummarizer()

        # Determine the target word count or sentence count based on user selection
        if selected_option == 'custom-word':
            target_word_count = int(request.form.get('custom-word'))
            target_sentence_count = None
            print("Target Word Count:", target_word_count)
        elif selected_option == 'custom-sentence':
            target_sentence_count = int(request.form.get('custom-sentence'))
            target_word_count = None
            print("Target Sentence Count:", target_sentence_count)

        # Perform summarization based on the selected target count
        current_word_count = 0
        summary_sentences = []
        for sentence in summarizer(parser.document, sentences_count=total_sentences):
            sentence_word_count = len(sentence.words)
            if target_word_count is not None and current_word_count + sentence_word_count <= target_word_count:
                summary_sentences.append(sentence)
                current_word_count += sentence_word_count
            elif target_sentence_count is not None and len(summary_sentences) < target_sentence_count:
                summary_sentences.append(sentence)
            else:
                break

        # Join the summary sentences and print the result
        summary = " ".join(str(sentence) for sentence in summary_sentences)
        print("Summary:", summary)
        flash("Summary generated successfully.", 'success')

        return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
