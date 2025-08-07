Web Scraping Falcon 9 & Falcon Heavy Launch Records
This repository contains a Python project that scrapes historical launch data for SpaceX’s Falcon 9 and Falcon Heavy rockets from the Wikipedia page List of Falcon 9 and Falcon Heavy launches. The script extracts each launch’s date, booster version, payload mass, orbit, launch outcome, and more, then saves the cleaned dataset as a CSV for analysis.

Table of Contents

* Project Overview
* Data Source
* Features Extracted
* Getting Started
    Prerequisites
    Installation
* Usage
* Output
* Folder Structure
* Future Work
* License
* Author

Project Overview
SpaceX’s Falcon 9 and Falcon Heavy launch vehicles have reshaped modern rocketry. This project automates the collection of their historical launch records from Wikipedia and transforms them into a tidy CSV file. You can then plug this data into analytics dashboards, machine-learning models, or reporting tools.

Data Source
Wikipedia page: List of Falcon 9 and Falcon Heavy launches <https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches>

Features Extracted
Each launch record includes:

 * Launch date
 * Rocket version (e.g. v1.0, v1.1, FT, B4, B5)
 * Launch site
 * Payload mass (kg)
 * Orbit
 * Customer
 * Launch outcome (Success/Failure)

Getting Started
Prerequisites
 * Python 3.7+
 * pip package manager

Installation
Clone this repository:

bash
git clone https://github.com/57KayBel0/falcon-launch-scraper.git
cd falcon-launch-scraper
(Optional) Create and activate a virtual environment:



Saved the consolidated dataset to falcon_launches.csv.

Output
falcon_launches.csv A CSV file containing all historical Falcon 9 and Falcon Heavy launch records with the extracted features listed above.

Folder Structure
.
├── scrape_falcon_launches.py   # Main scraping script
├── falcon_launches.csv         # Output dataset (generated)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
Future Work
Extend scraping to include booster landing outcomes and recovery details.

Automate weekly updates to keep the dataset current.

Build an interactive dashboard (e.g., Plotly Dash) to visualize success rates by booster version, orbit, and payload.

License
This project is licensed under the MIT License.

Author
Kabelo Motshabi Makgae

GitHub: @57KayBel0

Email: makgaekabelomotshabikabelo.kb@gmail.com

Feel free to raise issues or contribute enhancements via pull requests!
