import requests
from bs4 import BeautifulSoup

def scrape_school_data(page_number):
    url = f"https://skoodos.com/schools-in-odisha?page={page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if response.status_code == 200:
        print(f"Scraping data from page {page_number}")
    else:
        print(f"Failed to retrieve data from page {page_number}. Status code: {response.status_code}")
        return []
    schools = []
    
    # Find all school listings
    school_listings = soup.find_all('div', class_='col-8 col-md-10')

    for listing in school_listings:
        # Extract school name and additional details
        school_name_element = listing.find('h2', class_='maintitle').a
        school_name = school_name_element.text.strip() if school_name_element else ""
        
        # Extract location info if available
        location_info_element = listing.find('span', class_='sz-14px')
        location_info = location_info_element.text.strip() if location_info_element else ""
        address = ' '.join(location_info.split()[2:])  # Extracting address from location_info
        
        # Extract contact number, email, and website if available
        contact_number_element = listing.find('img', src='https://skoodos.com/public/assets/img/search/icons/call.png').find_next('p')
        contact_number = contact_number_element.text.strip() if contact_number_element else ""
        
        email_element = listing.find('img', src='https://skoodos.com/public/assets/img/search/icons/mail.png').find_next('p')
        email = email_element.text.strip() if email_element else ""
        
        website_element = listing.find('img', src='https://skoodos.com/public/assets/img/search/icons/web.png').find_next('p')
        website = website_element.text.strip() if website_element else ""
        
        # Append data to schools list
        schools.append({
            'name': school_name,
            'address': address,
            'contact_number': contact_number,
            'email': email,
            'website': website
        })
    for school in schools[:5]:
        print(f"Name: {school['name']}")
        print(f"Address: {school['address']}")
        print(f"Contact Number: {school['contact_number']}")
        print(f"Email: {school['email']}")
        print(f"Website: {school['website']}")
        print("=" * 30)

scrape_school_data(4)