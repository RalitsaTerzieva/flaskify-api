# Flaskify-App Application


FlaskifyAPI is a streamlined web application designed to help developers practice building and testing RESTful APIs using Flask, Postman, and related technologies.

---

## Installation

### Prerequisites
Ensure you have Python (3.7 or higher) and `pip` installed on your machine.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/RalitsaTerzieva/flaskify-api/tree/main
   cd flaskifyapi

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   
6. Initialize the database:
   ```bash
   export FLASK_APP=app.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   
8. Run the application:
   ```bash
   flask run
