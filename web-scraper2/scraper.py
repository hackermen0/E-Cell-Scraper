import csv
from googlesearch import search

# Function to perform Google search and extract LinkedIn profile info
def get_linkedin_profiles(company_name):
    query = f"{company_name} linkedin india marketing head"
    search_results = list(search(query, num_results=3))  # Convert generator to list

    profiles = []
    for result in search_results[:3]:  # Limit to top 3 results
        if "linkedin.com" in result:
            # Extract the profile name from the URL
            profile_name = result.split('/in/')[-1].replace('-', ' ').split('/')[0].title()
            profiles.append((profile_name, result))
    
    return profiles

# Read the company names from input CSV
input_file = 'input_companies.csv'
output_file = 'linkedin_profiles.csv'

with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    companies = [row[0] for row in reader]

# Write the LinkedIn profile info to output CSV
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Company Name', 'Profile Name', 'LinkedIn URL'])

    for company in companies:
        profiles = get_linkedin_profiles(company)
        for profile in profiles:
            writer.writerow([company, profile[0], profile[1]])

print(f"LinkedIn profiles saved to {output_file}")
