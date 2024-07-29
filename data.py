import requests
import pandas as pd

def fetch_data_from_source(source_url, topic):
    try:
        response = requests.get(f"{source_url}?q={topic}")
        if response.status_code == 200:
            data = response.json()
            return data['results']  # Adjust based on the actual response structure
        else:
            print(f"Failed to fetch data for topic: {topic}. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching data for topic: {topic}. Error: {e}")
        return []

def collect_data(topics, sources):
    all_data = []
    for topic in topics:
        for source in sources:
            print(f"Fetching data from {source['name']} for topic: {topic}")
            data = fetch_data_from_source(source['url'], topic)
            for item in data:
                all_data.append({'Source': source['name'], 'Topic': topic, 'Data': item})
    return all_data

topics = [
    "science", "mathematics", "machine learning", "artificial intelligence", "data science", "algebra", "geometry",
    "calculus", "biology", "genetics", "evolution", "ecology", "anatomy",
    "microbiology", "botany", "zoology", "chemistry", "organic chemistry", "inorganic chemistry",
    "physical chemistry", "biochemistry", "physics", "classical mechanics", "electromagnetism",
    "thermodynamics", "quantum mechanics", "relativity", "optics", "statistics", "probability",
    "computer science", "technology", "programming", "learn python", "java", "c++", "javascript",
    "html", "css", "sql", "software development", "web development", "mobile app development",
    "networking", "cybersecurity", "cloud computing", "database management", "it support",
    "humanities", "social science", "history", "ancient history", "modern history", "cultural history",
    "geography", "physical geography", "human geography", "environmental geography",
    "geopolitics", "literature", "english literature", "poetry", "drama",
    "literary theory", "ethics", "logic", "metaphysics", "epistemology", "political philosophy",
    "developmental psychology", "clinical psychology", "cognitive psychology", "social psychology",
    "neuropsychology", "social theory", "social stratification", "gender studies",
    "urban sociology", "rural sociology",
    "art", "music", "drawing", "painting", "sculpture", "photography", "art history", "music theory",
    "composition", "instrumental performance", "vocal performance", "music history",
    "theater", "dance", "film studies", "acting",
    "business", "economics", "microeconomics", "macroeconomics", "international economics", "developmental economics",
    "behavioral economics", "management", "marketing", "finance", "accounting",
    "entrepreneurship", "business ethics", "constitutional law", "criminal law",
    "international law", "corporate law", "intellectual property law",
    "health", "medicine", "surgery", "pediatrics", "psychiatry", "radiology", "patient care",
    "nursing ethics", "pharmacology", "nursing", "epidemiology",
    "biostatistics", "health policy", "environmental health",
    "engineering", "applied sciences", "civil engineering", "structural engineering", "geotechnical engineering",
    "transportation engineering", "electrical engineering", "circuit analysis",
    "signal processing", "telecommunications", "mechanical engineering",
    "thermodynamics", "fluid mechanics", "robotics", "chemical engineering",
    "process engineering", "materials science", "biochemical engineering",
    "spanish", "french", "german", "chinese",
    "arabic", "conservation biology", "climate change", "sustainable development",
    "international relations", "comparative politics", "political theory",
    "teaching", "curriculum development", "educational psychology"
]

sources = [
    {"name": "OpenLibrary", "url": "https://openlibrary.org/search.json"},
    {"name": "AnotherSource", "url": "https://api.anothersource.com/search"}  # Example, replace with actual sources
]

data = collect_data(topics, sources)

df = pd.DataFrame(data)
df.to_csv('combined_data.csv', index=False)
print("Data saved to combined_data.csv")
