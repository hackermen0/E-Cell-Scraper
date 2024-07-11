import csv
from googlesearch import search
import time
from pyhunter import PyHunter  # Import PyHunter library

# Initialize PyHunter with your API key
hunter = PyHunter('INSERT_YOUR_HUNTER_API_KEY_HERE')

search_terms = [
    'marketing head', 'public relations head',
]

# Function to perform Google search and extract LinkedIn profile info
def get_linkedin_profiles(company_name):
    profiles = []
    for term in search_terms:
        query = f"{company_name} linkedin india {term}"
        search_results = list(search(query, num_results=3))  # Convert generator to list

        for result in search_results[:3]:  # Limit to top 3 results
            if "linkedin.com" in result:
                # Extract the profile name from the URL
                profile_name = result.split('/in/')[-1].replace('-', ' ').split('/')[0].title()
                profiles.append((profile_name, result, term))
                print(profile_name, result, term)

                # Try to find email address using PyHunter
                name_parts = profile_name.split()
                first_name = name_parts[0]
                last_name = ' '.join(name_parts[1:2])
                
                # Only try to find email if both last name and full name exist
                if last_name and profile_name:
                    try:
                        email = hunter.email_finder(company=company_name, first_name=first_name, last_name=last_name)
                        if email:
                            profiles[-1] = profiles[-1] + (email,)  # Append email to the tuple
                        else:
                            profiles[-1] = profiles[-1] + ("not found",)  # Mark email as not found
                    except Exception as e:
                        print(f"Error while fetching email for {profile_name}: {str(e)}")
                        profiles[-1] = profiles[-1] + ("not found",)  # Mark email as not found on error

    return profiles


# Read the company names from input CSV
input_file = 'input_companies.csv'
output_file = 'linkedin_profiles.csv'

with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    companies = [row[0] for row in reader]
    # Calculate the total number of companies
    total_companies = len(companies)

    # Initialize the progress bar
    progress_bar_width = 40
    progress_bar = '[' + ' ' * progress_bar_width + ']'
    print(progress_bar, end='\r')

    # Write the LinkedIn profile info to output CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Company Name', 'Profile Name', 'LinkedIn URL', 'Role', 'Email'])

        for i, company in enumerate(companies):
            profiles = get_linkedin_profiles(company)
            for profile in profiles:
                writer.writerow([company, profile[0], profile[1], profile[2], profile[3] if len(profile) > 3 else ''])

            # Update the progress bar
            progress = int((i + 1) / total_companies * progress_bar_width)
            progress_bar = '[' + '#' * progress + ' ' * (progress_bar_width - progress) + ']'
            print(progress_bar, end='\r')
            time.sleep(0.1)  # Add a small delay for visualization

    print(f"\nLinkedIn profiles (with emails if found) saved to {output_file}")
