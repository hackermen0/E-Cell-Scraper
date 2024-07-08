# LinkedIn Profile Scraper

This script is designed to extract LinkedIn profiles for specific roles within companies listed in an input CSV file. It performs a Google search to find LinkedIn profiles and saves the results, including emails found using the Hunter API, to a CSV file.

## Prerequisites

- Python 3.x
- `googlesearch-python` package
- `pyhunter` package
- A Hunter API Key

## Setup

1. Ensure Python 3.x is installed on your system.
2. Install the required packages using pip:

```sh
pip install googlesearch-python pyhunter
```

3. Obtain a Hunter API Key:
   - Sign up or log in at [Hunter](https://hunter.io/).
   - Navigate to the API section and copy your API

## Key

- Replace `'INSERT_YOUR_HUNTER_API_KEY_HERE'` in the [`scraper.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FKIIT0001%2FDesktop%2FAcademics%2FECEll%2FESummit%2FHackathon%2Fscraper-for-cell%2Fweb-scraper2%2Fscraper.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\\Users\KIIT0001\Desktop\Academics\ECEll\ESummit\Hackathon\scraper-for-cell\web-scraper2\scraper.py") script with your actual Hunter API Key.

## Usage

1. Populate the `input_companies.csv` file in the [`web-scraper2`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FKIIT0001%2FDesktop%2FAcademics%2FECEll%2FESummit%2FHackathon%2Fscraper-for-cell%2Fweb-scraper2%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\\Users\KIIT0001\Desktop\Academics\ECEll\ESummit\Hackathon\scraper-for-cell\web-scraper2") directory with the names of the companies you're interested in. The file should contain one company name per line.
2. Run the [`scraper.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2FKIIT0001%2FDesktop%2FAcademics%2FECEll%2FESummit%2FHackathon%2Fscraper-for-cell%2Fweb-scraper2%2Fscraper.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\\Users\KIIT0001\Desktop\Academics\ECEll\ESummit\Hackathon\scraper-for-cell\web-scraper2\scraper.py") script:

```sh
python web-scraper2/scraper.py
```

3. The script will create a `linkedin_profiles.csv` file in the `web-scraper2` directory, containing columns for the company name, profile name, LinkedIn URL, role, and email (if found).

## Output

The output CSV file (`linkedin_profiles.csv`) will contain the following columns:

- `Company Name`: The name of the company.
- `Profile Name`: The name of the individual extracted from the LinkedIn profile.
- `LinkedIn URL`: The URL of the LinkedIn profile.
- `Role`: The role for which the profile was found.
- `Email`: The email address found using Hunter (if any).

For detailed information on the implementation, refer to the [`scraper.py`](web-scraper2/scraper.py) script.
