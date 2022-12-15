import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd

st.title('Heading Scraper by Arpad')

# Define a function to scrape the page
def scrape_page(url):
  # Check if the URL is empty
  if not url:
    st.error('Please enter a valid URL')
  else:
    # Send a GET request to the URL of the page you want to scrape
    data = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(data.text, 'html.parser')

    # Find all the heading tags on the page
    headings = soup.find_all(['h1', 'h2', 'h3'])

    # Create a pandas DataFrame to hold the scraped data
    df = pd.DataFrame(columns=['Heading Type', 'Heading Text'])

    # Only print the headings that the user selected
    if h1:
      st.header('H1 Headings')
      for heading in headings:
        if heading.name == 'h1':
          st.write(heading.get_text())
          df = df.append({'Heading Type': 'H1', 'Heading Text': heading.get_text()}, ignore_index=True)

    if h2:
      st.header('H2 Headings')
      for heading in headings:
        if heading.name == 'h2':
          st.write(heading.get_text())
          df = df.append({'Heading Type': 'H2', 'Heading Text': heading.get_text()}, ignore_index=True)

    if h3:
      st.header('H3 Headings')
      for heading in headings:
        if heading.name == 'h3':
          st.write(heading.get_text())
          df = df.append({'Heading Type': 'H3', 'Heading Text': heading.get_text()}, ignore_index=True)

    # Return the pandas DataFrame
    return df

# Get the URL from the user, with a default value of "http://"
url = st.text_input('Enter the URL of the page you want to scrape:', 'http://')

# Check if the URL starts with "http://" or "https://"
if not url.startswith('http://') and not url.startswith('https://'):
  # If it doesn't, add "https://" to the beginning of the URL
  url = 'https://' + url

# Create checkboxes for the different heading types
left, right = st.columns(2)
with left: 
   st.markdown('Select Which Headings You Want to Scrape')
with right:
    h1 = st.checkbox('H1')
    h2 = st.checkbox('H2')
    h3 = st.checkbox('H3')

# Add a "Scrape" button
if st.button('Scrape'):
  # Call the scrape_page function when the "Scrape" button is clicked
  scrape_page(url)