from googlesearch import search
import pandas as pd
from urllib import parse
import re
import time
import csv

# from pyhunter import PyHunter

# Initialize PyHunter with your API key
# hunter = PyHunter("INSERT_YOUR_HUNTER_API_KEY_HERE")

search_terms = [
    "marketing head",
    "public relations head",
]


# Function to perform Google search and extract LinkedIn profile info
def get_linkedin_profiles(company_name):
    print(f"-------------------------{company_name}-------------------------------")
    profiles = []
    for term in search_terms:
        query = f"{company_name} linkedin india {term}"
        search_results = list(search(query, num_results=3))  # Convert generator to list

        for result in search_results[:3]:  # Limit to top 3 results
            if "linkedin.com" in result:
                # Extract the profile name from the URL
                path = parse.urlparse(result).path
                if (
                    path.split("/")[1] == "in"
                ):  # Checks if the result searched is a user profile

                    profile_name = result.split("/in/")[-1].split("-")

                    # Checks whether if all the elements of the name contains only alphabets if not remove them from the list
                    pattern = re.compile(r"^[A-Za-z]+$")
                    filtered_profile_name = (
                        [item for item in profile_name if pattern.match(item)]
                        if len(profile_name) > 1
                        else profile_name
                    )
                    profile_name = " ".join(filtered_profile_name).title()
                    print(profile_name)
                    profiles.append((profile_name, term, result))
                    print(profile_name, result, term)
                    print("\n\n")

                # # Try to find email address using PyHunter
                # name_parts = profile_name.split()
                # first_name = name_parts[0]
                # last_name = " ".join(name_parts[1:2])

                # # Only try to find email if both last name and full name exist
                # if last_name and profile_name:
                #     try:
                #         email = hunter.email_finder(
                #             company=company_name,
                #             first_name=first_name,
                #             last_name=last_name,
                #         )
                #         if email:
                #             profiles[-1] = profiles[-1] + (
                #                 email,
                #             )  # Append email to the tuple
                #         else:
                #             profiles[-1] = profiles[-1] + (
                #                 "not found",
                #             )  # Mark email as not found
                #     except Exception as e:
                #         print(
                #             f"Error while fetching email for {profile_name}: {str(e)}"
                #         )
                #         profiles[-1] = profiles[-1] + (
                #             "not found",
                #         )  # Mark email as not found on error

    return profiles


# Read the company names from input CSV
input_file = "input_companies.csv"
output_file = "linkedin_profiles_test4.csv"

with open(input_file, "r") as csvfile:
    reader = csv.reader(csvfile)
    companies = [row[0] for row in reader]
    # Calculate the total number of companies
    total_companies = len(companies)

    # Initialize the progress bar
    progress_bar_width = 40
    progress_bar = "[" + " " * progress_bar_width + "]"
    print(progress_bar, end="\r")

    # Write the LinkedIn profile info to output CSV
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["Profile Name", "Company Name", "Role", "Email", "LinkedIn URL"]
        )

        for i, company in enumerate(companies):
            profiles = get_linkedin_profiles(company)
            for profile in profiles:
                writer.writerow(
                    [
                        profile[0],
                        company,
                        profile[1],
                        "",
                        (
                            f'=HYPERLINK("{profile[2]}", "Link")'
                            if len(profile) > 2
                            else ""
                        ),
                    ]
                )

            # Update the progress bar
            progress = int((i + 1) / total_companies * progress_bar_width)
            progress_bar = (
                "[" + "#" * progress + " " * (progress_bar_width - progress) + "]"
            )
            print(progress_bar, end="\r")
            time.sleep(0.1)  # Add a small delay for visualization

    print(f"\nLinkedIn profiles (with emails if found) saved to {output_file}")

# Removing Duplicates

print("Removing Duplicates")

df = pd.read_csv(output_file)
df.drop_duplicates(subset=["Profile Name"], keep="first", inplace=True)
df.to_csv(output_file, index=False)

print("Duplicates have been removed")
