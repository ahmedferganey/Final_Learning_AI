# NLP for SMS Spam Classification (with English/Arabic Text Processing)

## Overview

This project walks through a full **Natural Language Processing (NLP) pipeline** to classify SMS messages as **spam** or **ham** (not spam). It follows a CRISP-DM style structure — from business understanding through data preparation, feature engineering, model building, and evaluation — and includes side-by-side demonstrations of core NLP preprocessing techniques in **both English and Arabic**.

The notebook is written in a tutorial style, with explanatory markdown alongside runnable code, making each NLP concept easy to follow before it's applied to the full dataset.

## Dataset

- **Source:** [SMS Spam Collection](./Dataset/sms+spam+collection/SMSSpamCollection)
- **Format:** Tab-separated file with no header, containing two columns:
  - `label` — `spam` or `ham`
  - `body_text` — the raw SMS message content

## Project Workflow

### 1. Business & Data Understanding
- Introduction to core NLP concepts (NLU, NLG, human–machine interaction)
- Exploratory Data Analysis (EDA): dataset shape, summary statistics, class balance (ham vs. spam), missing values, and visualizations (pie charts)

### 2. Text Preprocessing
Custom functions are built and applied step by step:
- **Punctuation removal**
- **Lowercasing**
- **Tokenization** (via NLTK's `word_tokenize`, plus a regex-based alternative)
- **Stopword removal** — demonstrated for **both English and Arabic**, including a worked Arabic sentence example and a discussion of how naive stopword removal can distort meaning (e.g. dropping negation words like "not")
- **Stemming** — using the Porter Stemmer, with examples illustrating *over-stemming* (`universal`/`university`/`universe`) and *under-stemming* (`alumnus`/`alumni`/`alumnae`)
- **Lemmatization** — using the WordNet Lemmatizer, compared directly against stemming results
- All steps are combined into a single `clean_text()` pipeline function applied to the entire dataset

### 3. Vectorization
Demonstrated first on toy example sentences, then applied to the cleaned SMS corpus:
- **Count Vectorization** (bag-of-words)
- **N-Grams** (1–3 grams)
- **TF-IDF** (Term Frequency–Inverse Document Frequency)

### 4. Feature Engineering
Additional handcrafted features derived from the raw message text:
- Message length (excluding whitespace)
- Percentage of punctuation characters
- Percentage of capital letters
- **Min-Max scaling** applied to normalize these numeric features

### 5. Model Building
- TF-IDF features combined with the engineered numeric features into a final feature matrix
- **Train/test split** (80/20)
- **Random Forest Classifier** trained and evaluated, then re-tuned with `n_estimators=200`
- Feature importance analysis to identify the most predictive features

### 6. Model Evaluation
- Alternate **holdout split** (70/30) for comparison
- **K-Fold Cross-Validation** (5 folds) to assess model stability and generalization

## Key Techniques Covered
- Text cleaning & normalization
- Tokenization
- Stopword removal (English + Arabic)
- Stemming vs. Lemmatization
- Bag-of-Words, N-Grams, and TF-IDF vectorization
- Feature engineering from raw text
- Random Forest classification
- Model validation (holdout & cross-validation)

## Requirements
- Python 3.12
- `nltk`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

NLTK resources used (downloaded within the notebook):
```
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
```

## Notes
- This is a learning/teaching-oriented notebook: each concept (stemming, lemmatization, vectorization, etc.) is first demonstrated on small toy examples before being applied to the full SMS dataset.
- The Arabic NLP components (stopword removal, tokenization) are shown for comparison purposes and are not carried through into the final spam classification model, which is trained on the English SMS dataset.