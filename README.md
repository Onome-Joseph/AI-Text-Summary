# Text Summarization Model  
This project implements an **AI text summary model** that simplifies lengthy articles, news, passages, or text into concise summaries based on the desired number of sentences. The model is designed to deliver summaries quickly and with good performance, making it a practical tool for various applications.  

## Key Features  
- **Customizable Summaries**: Allows users to specify the number of sentences for the summary.  
- **Fast Processing**: Generates summaries in a fraction of the time.  
- **Good Performance**: Delivers coherent and meaningful summaries.  

## Applications  
The Text Summarization Model has versatile applications:  
1. **Media and Journalism**: Quickly summarize news articles or reports.  
2. **Education**: Help students and researchers condense large volumes of text.  
3. **Business**: Summarize reports, emails, or meeting notes for efficient decision-making.  
4. **Content Curation**: Assist in generating summaries for blogs, newsletters, or social media posts.  

# Flask Text Summarization App
This repository also contains a Flask-based web application for summarizing text. Users can input an article and specify the number of sentences for the summary.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Onome-Joseph/AI-Text-Summary.git
   cd AI-Text-Summary
   ```

2. **Install Dependencies**:
   Ensure you have Flask and NLTK installed. Run the following command to install all required libraries:
   ```bash
   pip install flask nltk
   ```

3. **Download NLTK Data**:
   The application uses NLTK for text processing. Download the necessary datasets by running:
   ```python
   python
   >>> import nltk
   >>> nltk.download('punkt')
   >>> nltk.download('stopwords')
   >>> exit()
   ```

4. **Run the Flask Application**:
   Start the Flask server using the command:
   ```bash
    summary_app.py
   ```

5. **Access the Application**:
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

6. **Use the Interface**:
   - Paste the text/article you want to summarize in the input field.
   - Specify the number of sentences for the summary.
   - Click "Summarize" to view the result.

## Folder Structure
```
.
├── summary_app.py                  # Flask application
├── templates/
│   └── index.html          # Frontend HTML template

## Contributions  
Contributions are welcome! Feel free to fork the repository, propose enhancements, or report issues.
