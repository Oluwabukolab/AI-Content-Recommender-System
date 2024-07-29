import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def fetch_coursera_courses(topic):
    url = f"https://www.coursera.org/search?query={topic}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch data for topic: {topic}. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Print the raw HTML to debug the structure
    # Uncomment the following line to see the HTML structure
    # print(soup.prettify())
    
    results = []
    courses = soup.find_all('li', class_='ais-InfiniteHits-item')
    if not courses:
        print(f"No courses found for topic: {topic}")
    
    for course in courses:
        title_element = course.find('h2', class_='color-primary-text card-title')
        rating_element = course.find('span', class_='ratings-text')
        
        title = title_element.text if title_element else 'No Title'
        rating = rating_element.text if rating_element else 'No Rating'
        
        results.append({'Title': title, 'Rating': rating})
    
    # Adding a random delay between requests to avoid being blocked
    time.sleep(random.uniform(5, 10))
    
    return results

# Comprehensive list of diverse topics
topics = [
    # Science and Mathematics
    "science", "mathematics", "machinelearning", "artificial", "datascience", "algebra", "geometry",
    "calculus", "biology", "genetics", "evolution", "ecology", "anatomy", 
    "microbiology", "botany", "zoology", "chemistry", "organicchemistry", "inorganicchemistry",
    "physicalchemistry", "biochemistry", "physics", "classicalmechanics", "electromagnetism",
    "thermodynamics", "quantummechanics", "relativity", "optics", "statistics", "probability",

    # Computer Science and Technology
    "computerscience", "technology", "programming", "learnpython", "java", "cpp", "javascript",
    "html", "css", "sql", "softwaredevelopment", "webdev", "mobileappdevelopment",
    "networking", "cybersecurity", "cloudcomputing", "databasemanagement", "itsupport",

    # Humanities and Social Sciences
    "humanities", "socialscience", "history", "ancienthistory", "modernhistory", "culturalhistory", 
    "geography", "physicalgeography", "humangeography", "environmentalgeography",
    "geopolitics", "literature", "englishliterature", "poetry", "drama", 
    "literarytheory", "ethics", "logic", "metaphysics", "epistemology", "politicalphilosophy",
    "developmentalpsychology", "clinicalpsychology", "cognitivepsychology", "socialpsychology",
    "neuropsychology", "socialtheory", "socialstratification", "genderstudies", 
    "urbansociology", "ruralsociology",

    # Arts and Music
    "art", "music", "drawing", "painting", "sculpture", "photography", "arthistory", "musictheory", 
    "composition", "instrumentalperformance", "vocalperformance", "musichistory",
    "theater", "dance", "filmstudies", "acting",

    # Business and Economics
    "business", "economics", "microeconomics", "macroeconomics", "internationaleconomics", "developmentaleconomics", 
    "behavioraleconomics", "management", "marketing", "finance", "accounting", 
    "entrepreneurship", "businessethics", "constitutionallaw", "criminallaw", 
    "internationallaw", "corporatelaw", "intellectualpropertylaw",

    # Health and Medicine
    "health", "medicine", "surgery", "pediatrics", "psychiatry", "radiology", "patientcare",
    "nursingethics", "pharmacology", "nursing", "epidemiology", 
    "biostatistics", "healthpolicy", "environmentalhealth",

    # Engineering and Applied Sciences
    "engineering", "appliedsciences", "civilengineering", "structuralengineering", "geotechnicalengineering", 
    "transportationengineering", "electricalengineering", "circuitanalysis", 
    "signalprocessing", "telecommunications", "mechanicalengineering", 
    "thermodynamics", "fluidmechanics", "robotics", "chemicalengineering", 
    "processengineering", "materialsscience", "biochemicalengineering",

    # Miscellaneous
    "spanish", "french", "german", "chinese", 
    "arabic", "conservationbiology", "climatechange", "sustainabledevelopment",
    "internationalrelations", "comparativepolitics", "politicaltheory", 
    "teaching", "curriculumdevelopment", "educationalpsychology"
]

all_courses = []

for topic in topics:
    all_courses.extend(fetch_coursera_courses(topic))

df = pd.DataFrame(all_courses)
df.to_csv('/mnt/data/coursera_courses.csv', index=False)
print("Data saved to coursera_courses.csv")
