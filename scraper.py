import requests
from bs4 import BeautifulSoup

def find_h3_tags(url):
    # Set a custom User-Agent to avoid being blocked
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Make a GET request to the webpage and get its HTML content
    response = requests.get(url, headers=headers)
    html_content = response.content

    # Parse the HTML content with BeautifulSoup and find all the <h3> tags with class "_eYtD2XCVieq6emjKBH3m"
    soup = BeautifulSoup(html_content, "html.parser")
    h3_tags = soup.find_all("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})

    # Extract the text content of all the <h3> tags found
    h3_text_list = [h3.text for h3 in h3_tags]

    # Return the list containing the text content of all the <h3> tags found
    return h3_text_list

# Call the function with a URL as an argument
url = "http://reddit.com/r/news"
h3_text_list = find_h3_tags(url)

# Print the text content of all the <h3> tags found
for h3_text in h3_text_list:
    print(h3_text)
