# Spam_Email_Classification_Using_NLP_And_ML

Problem Statement : Spam emails are a big problem in today’s communication. They fill up inboxes with unwanted messages and often carry security threats like phishing and fraud. Simple filters are not enough to block these advanced spam techniques. Therefore, we need a smart system to quickly and accurately detect and block spam emails.

System Design :
1. Input
•	Receive Email: The system starts by receiving an email that needs to be classified.
•	Preprocess Email: Initial preprocessing is performed, such as removing unwanted characters, converting to lowercase, and cleaning the text to prepare it for analysis.
2. NLP (Natural Language Processing)
•	Tokenize Text: The preprocessed email is split into smaller units (words or tokens) for further analysis.
•	Remove Stop Words: Commonly used words like "and," "the," and "is" are removed, as they do not contribute to the classification.
•	Stemming: Words are reduced to their root forms (e.g., "running" becomes "run"), reducing dimensionality and improving model efficiency.
3. Feature Extraction
•	Vectorize Text: The cleaned text is converted into numerical form using techniques like CountVectorizer or TF-IDF.
•	Extract Features: Important features are extracted from the numerical data for model input.
4. Machine Learning Model
•	Load Trained Model: A pre-trained machine learning model (e.g., Naive Bayes or Logistic Regression) is loaded.
•	Predict Spam or Not: Based on the extracted features, the model predicts whether the email is spam or not.
5. Output
•	Mark as Spam: If the email is classified as spam, it is marked accordingly.
•	Mark as Not Spam: If classified as genuine, it is marked as not spam.
This system ensures efficient email classification by combining natural language processing for data preparation and machine learning for prediction.

Software Requirements:
•	Programming Language: Python 3.8 or higher.
•	Libraries and Tools:
o	Pandas: For data manipulation and preprocessing.
o	scikit-learn: For machine learning algorithms (Naive Bayes, CountVectorizer).
o	Streamlit: For creating the user interface.
o	Pickle: For saving and loading the model and vectorizer.
•	Dataset: A labeled email dataset (e.g., spam.csv).
•	IDE: Jupyter Notebook or any Python-supported IDE.
•	Browser: For accessing the Streamlit interface.
