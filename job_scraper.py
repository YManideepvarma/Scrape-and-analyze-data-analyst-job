import requests
from bs4 import BeautifulSoup
import csv

# Target URL
url = "https://realpython.github.io/fake-jobs/"

# Fetch page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find job cards
job_cards = soup.find_all("div", class_="card-content")

# Extract data
jobs_data = []
for job in job_cards:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    date = job.find("time")["datetime"]
    link = job.find("a", string="Apply")["href"]

    jobs_data.append([title, company, location, date, link])

# Save to CSV
filename = "job_postings.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Company", "Location", "Date Posted", "Apply Link"])
    writer.writerows(jobs_data)

print(f"Scraped {len(jobs_data)} job postings and saved to {filename}")
