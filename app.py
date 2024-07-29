import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load your data
df = pd.read_csv('content_data.csv')

# Combine text columns to create a single feature for text-based analysis
text_columns = ['Course Name', 'University', 'Difficulty Level', 'Course Rating', 'Course Description', 'Skills']
df['Content'] = df[text_columns].apply(lambda x: ' '.join(x.astype(str)), axis=1)

# Create a TF-IDF Vectorizer and fit the data
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Content'])

# Compute the cosine similarity matrix
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, cosine_similarities=cosine_similarities):
    idx = df[df['Course Name'].str.contains(title, case=False)].index[0]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Get top 5 recommendations
    book_indices = [i[0] for i in sim_scores]
    return df.iloc[book_indices]

# Streamlit app
st.title('Content Recommender System')
st.markdown("<h6 style='text-align: center; color: white;'> AI Recommender System created by Oluwabukola Bamigbade</h6>", unsafe_allow_html=True)

course_name = st.text_input('Enter a course name or a key phrase:')

if course_name:
    try:
        recommendations = get_recommendations(course_name)
        st.write('Recommendations:')
        for idx, row in recommendations.iterrows():
            st.write(f"**Course Name:** {row['Course Name']}")
            st.write(f"**University:** {row['University']}")
            st.write(f"**Difficulty Level:** {row['Difficulty Level']}")
            st.write(f"**Course Rating:** {row['Course Rating']}")
            st.write(f"**Course URL:** {row['Course URL']}")
            st.write(f"**Course Description:** {row['Course Description']}")
            st.write(f"**Skills:** {row['Skills']}")
            st.write('---')
    except IndexError:
        st.write("Content name not found.")


    st.markdown("<h6 style='text-align: center; color: red;'>Copyright reserved by Respective Course Owners</h6>", unsafe_allow_html=True)
