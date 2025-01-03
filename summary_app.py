from flask import Flask, request, render_template
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import heapq

app = Flask(__name__)

def summarize_article(article, summary_length=7):
    """
    Summarizes the input article by calculating sentence scores based on word frequencies
    and selecting the top sentences.

    Parameters:
        article (str): The input article text to summarize.
        summary_length (int): Number of sentences to include in the summary.

    Returns:
        str: A summary of the article.
    """
    # Replace non-ASCII dashes with standard hyphens
    article = article.replace('–', '-')

    # Remove URLs and links with underscores
    article = re.sub(r'https?://\S+|www\.\S+|__\S+__', '', article)

    # Tokenize the article into sentences
    sentences = sent_tokenize(article)

    # Tokenize words and calculate word frequencies
    words = word_tokenize(article)
    stop_words = set(stopwords.words('english'))
    frequency = {}

    for word in words:
        word = word.lower()
        if word.isalpha() and word not in stop_words:  # Only consider alphabetic words not in stopwords
            frequency[word] = frequency.get(word, 0) + 1

    # Normalize word frequencies
    if frequency:
        max_frequency = max(frequency.values())
        for word in frequency:
            frequency[word] /= max_frequency

    # Calculate sentence scores
    sentence_scores = {}
    for sent in sentences:
        for word in set(word_tokenize(sent)):  # Use set to avoid double-counting
            if word.lower() in frequency:
                if len(sent.split()) < 30:  # Ignore overly long sentences
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + frequency[word.lower()]

    # Select the top sentences for the summary
    summary_sentences = heapq.nlargest(summary_length, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)

    return summary

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        article = request.form.get('article')
        summary_length = int(request.form.get('summary_length', 7))

        if article:
            summary = summarize_article(article, summary_length)
            return render_template('index.html', summary=summary, article=article, summary_length=summary_length)

    return render_template('index.html', summary=None, article=None, summary_length=7)

if __name__ == '__main__':
    app.run(debug=True)