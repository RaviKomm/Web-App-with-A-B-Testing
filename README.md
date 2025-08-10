# Web-App-with-A-B-Testing
# A/B Testing Web App

This is a simple Flask-based web application demonstrating A/B testing with two versions of a user interface. It tracks user interactions (button clicks) and logs them in a CSV file for analysis.

---

## Features

- User login via name input.
- Random assignment to **Version A** (green-themed) or **Version B** (blue-themed).
- Bootstrap-based responsive UI for both versions.
- Tracking of button clicks with user info, timestamp, and version.
- Data stored in a CSV file (`interaction_log.csv`).
- Optional results page to view aggregated click counts.
- Session management for consistent user experience.
- Logout functionality.

---

## Requirements

- Python 3.7+
- Flask

---

## Installation

1. Clone the repository or download the source code.

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Flask:
pip install flask
Running the App
Make sure you have the templates folder with the following HTML files:

intro.html

version_a.html

version_b.html


Run the Flask application:

python app.py
Open your browser and visit:

cpp

http://127.0.0.1:5000/
Usage
Enter your name on the intro page and start the experiment.

You will be randomly assigned to Version A or Version B.

Click the button on your assigned version to simulate interaction.

Your clicks and related data are logged to interaction_log.csv.

Click "Logout" to restart or switch users.

(Optional) Visit /results to see aggregated click statistics
