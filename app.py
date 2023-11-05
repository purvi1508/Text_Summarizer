# app.py

from flask import Flask, render_template, request
from scraper import scraper
from summarizer import summarizer, estimated_reading_time
from translation import translate_to_hindi, translate_to_japanese, translate_to_korean

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# Your existing route for handling article summarization goes here...

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')

        try:
            article_title, text = scraper(url)
            summary = summarizer(text)
            reading_time = estimated_reading_time(summary.split())

            # Get the selected language from the form
            target_language = request.form.get('language')

            if target_language == "en":
                translated_summary = summary  
            elif target_language == "hi":
                translated_summary = translate_to_hindi(summary)
            elif target_language == "ja":
                translated_summary = translate_to_japanese(summary)
            elif target_language == "ko":
                translated_summary = translate_to_korean(summary)
        
            return render_template("index.html", article_title=article_title, reading_time=reading_time, summary=translated_summary)

        except TypeError:
            print('Invalid URL entered')

    else:
        return render_template("index.html")

@app.route("/translate", methods=['POST'])
def translate():
    data = request.get_json()
    summary_text = data['summary']
    target_language = data['language']
    
    print(f"Translating to language: {target_language}")
    print(f"Original text: {summary_text}")
    
    if target_language == "en":
        translated_summary = summary_text
    elif target_language == "hi":
        translated_summary = translate_to_hindi(summary_text)
    elif target_language == "ja":
        translated_summary = translate_to_japanese(summary_text)
    elif target_language == "ko":
        translated_summary = translate_to_korean(summary_text)
    
    print(f"Translated text: {translated_summary}")
    
    return translated_summary

if __name__ == "__main__":
    app.run(debug=True)
