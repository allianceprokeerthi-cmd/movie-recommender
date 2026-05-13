# 🎬 Movie Recommendation System Using NLP

## 📌 Project Overview
This project is a Content-Based Movie Recommendation System developed using Python and Machine Learning techniques. The system recommends movies similar to a selected movie based on genres, keywords, and movie overviews using Natural Language Processing (NLP).

---

## 🎯 Problem Statement
With thousands of movies available across platforms, users often struggle to find movies matching their interests.  
The objective of this project is to build a recommendation engine that suggests similar movies based on movie content and metadata.

---

## 📂 Dataset Description
Dataset Used:

Source: [TMDB](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

The dataset contains movie-related information such as:
- Movie Title
- Overview
- Genres
- Keywords
- Cast & Crew Details

### 🔑 Key Features
- `title` → Movie name  
- `overview` → Short movie description  
- `genres` → Movie categories  
- `keywords` → Important movie tags  

---

## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-learn
- NumPy
- NLP (TF-IDF Vectorization)

---

## 🔍 Methodology

### 1️⃣ Data Preprocessing
- Loaded dataset using Pandas
- Selected relevant columns:
  - title
  - overview
  - genres
  - keywords
- Handled missing values
- Converted JSON-like text data into readable format using `ast.literal_eval()`

### 2️⃣ Exploratory Data Analysis (EDA)
- Checked missing values and data structure
- Analyzed movie metadata columns
- Combined textual features into a single `tags` column

### 3️⃣ Model Development
- Applied **TF-IDF Vectorization** to convert text into numerical vectors
- Used **Cosine Similarity** to calculate similarity scores between movies
- Built a recommendation function to fetch top similar movies

### 4️⃣ Model Evaluation
- Tested recommendations using different movie titles
- Verified similarity relevance manually
- Evaluated recommendation quality based on movie genres and themes

---

## 📊 Model Performance
- Successfully generated Top 10 similar movie recommendations
- Fast similarity computation using cosine similarity matrix
- Recommendations were contextually relevant for most popular movies

---

## ⚖️ Model Behavior Insight
The recommendation system works based on movie content rather than user ratings.  
Movies sharing similar genres, themes, or keywords are recommended together.

Example:
- Sci-fi movies recommend other sci-fi/adventure films
- Action movies recommend similar action/thriller movies

---

## 📈 Key Insights
- Combining overview, genres, and keywords improves recommendation quality
- TF-IDF effectively captures important textual information
- Cosine similarity works well for content-based filtering problems
- NLP techniques can build powerful recommendation systems with simple approaches

---

## ⚠️ Challenges Faced
- Handling JSON-like nested data columns
- Cleaning and preprocessing textual data
- Managing sparse matrices generated from TF-IDF
- Improving recommendation relevance for less popular movies

---

## 💡 Conclusion
This project demonstrates how NLP and Machine Learning techniques can be used to build a movie recommendation engine.  
The system provides personalized movie suggestions based on content similarity and serves as a strong beginner-level recommendation system project.

Future improvements can include:
- Adding movie posters using TMDB API
- Building a Streamlit web application
- Hybrid recommendation system using collaborative filtering

---

## 👤 Author

**Keerthi**

🔗 GitHub: [allianceprokeerthi-cmd](https://github.com/allianceprokeerthi-cmd)
