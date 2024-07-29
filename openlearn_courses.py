import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# List of topics to scrape
topics = [
    "science", "mathematics", "machine learning", "artificial intelligence", "data science", "algebra", "geometry",
    "calculus", "biology", "genetics", "evolution", "ecology", "anatomy", 
    "microbiology", "botany", "zoology", "chemistry", "organic chemistry", "inorganic chemistry",
    "physical chemistry", "biochemistry", "physics", "classical mechanics", "electromagnetism",
    "thermodynamics", "quantum mechanics", "relativity", "optics", "statistics", "probability",

    # Computer Science and Technology
    "computer science", "technology", "programming", "learn python", "java", "c++", "javascript",
    "html", "css", "sql", "software development", "web development", "mobile app development",
    "networking", "cybersecurity", "cloud computing", "database management", "it support",

    # Humanities and Social Sciences
    "humanities", "social science", "history", "ancient history", "modern history", "cultural history", 
    "geography", "physical geography", "human geography", "environmental geography",
    "geopolitics", "literature", "english literature", "poetry", "drama", 
    "literary theory", "ethics", "logic", "metaphysics", "epistemology", "political philosophy",
    "developmental psychology", "clinical psychology", "cognitive psychology", "social psychology",
    "neuropsychology", "social theory", "social stratification", "gender studies", 
    "urban sociology", "rural sociology",

    # Arts and Music
    "art", "music", "drawing", "painting", "sculpture", "photography", "art history", "music theory", 
    "composition", "instrumental performance", "vocal performance", "music history",
    "theater", "dance", "film studies", "acting",

    # Business and Economics
    "business", "economics", "microeconomics", "macroeconomics", "international economics", "developmental economics", 
    "behavioral economics", "management", "marketing", "finance", "accounting", 
    "entrepreneurship", "business ethics", "constitutional law", "criminal law", 
    "international law", "corporate law", "intellectual property law",

    # Health and Medicine
    "health", "medicine", "surgery", "pediatrics", "psychiatry", "radiology", "patient care",
    "nursing ethics", "pharmacology", "nursing", "epidemiology", 
    "biostatistics", "health policy", "environmental health",

    # Engineering and Applied Sciences
    "engineering", "applied sciences", "civil engineering", "structural engineering", "geotechnical engineering", 
    "transportation engineering", "electrical engineering", "circuit analysis", 
    "signal processing", "telecommunications", "mechanical engineering", 
    "thermodynamics", "fluid mechanics", "robotics", "chemical engineering", 
    "process engineering", "materials science", "biochemical engineering",

    # Miscellaneous
    "spanish", "french", "german", "chinese", 
    "arabic", "conservation biology", "climate change", "sustainable development",
    "international relations", "comparative politics", "political theory", 
    "teaching", "curriculum development", "educational psychology"
]

def fetch_openlearn_courses(topic):
    base_url = 'https://www.open.edu/openlearn/search-results'
    params = {'q': topic}
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    results = []
    
    response = requests.get(base_url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"Failed to fetch data for topic: {topic}. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    courses = soup.find_all('li', class_='ou-search__result')
    
    for course in courses:
        title_element = course.find('h3', class_='ou-search__result-title')
        title = title_element.text.strip() if title_element else 'No Title'
        
        description_element = course.find('p', class_='ou-search__result-description')
        description = description_element.text.strip() if description_element else 'No Description'
        
        link_element = course.find('a', class_='ou-search__result-title-link')
        link = link_element['href'] if link_element else 'No URL'
        
        results.append({'Title': title, 'Description': description, 'URL': link})
    
    return results

all_courses = []

for topic in topics:
    print(f"Fetching courses for topic: {topic}")
    all_courses.extend(fetch_openlearn_courses(topic))

df = pd.DataFrame(all_courses)
df.to_csv('openlearn_courses.csv', index=False)
print("Data saved to openlearn_courses.csv")
