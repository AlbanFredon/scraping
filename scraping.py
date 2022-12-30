import csv
import requests
from bs4 import BeautifulSoup

# Ask the user to input the data points to organize the data around
data_1 = input("Enter the first data point: ")
data_2 = input("Enter the second data point: ")

# Initialize variables to store the scraped data
data = []

# Set the URL to scrape
url = "https://www.example.com"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html = response.content

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Use BeautifulSoup to extract the desired data
titles = soup.find_all("h1")
subheadings = soup.find_all("h2")
paragraphs = soup.find_all("p")

# Organize the data around the two data points
for title in titles:
    data.append([url, data_1, title.get_text(), data_2])

for subheading in subheadings:
    data.append([url, data_1, subheading.get_text(), data_2])

for paragraph in paragraphs:
    data.append([url, data_1, paragraph.get_text(), data_2])

# Print the scraped data as a numbered list
for i, item in enumerate(data):
    print(f"{i+1}. {item[0]}, {item[1]}, {item[2]}, {item[3]}")

# Write the scraped data to a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Print a message to confirm that the data has been written to the CSV file
print("Data written to scraped_data.csv")
