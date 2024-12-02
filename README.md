
# Survey Management System

## Overview
This is a Django-based web application for creating, managing, and taking surveys. 
It supports two user roles:
- **Creators**: Can create, publish, and manage surveys.
- **Takers**: Can take available surveys and view survey completion details.

## Features
- **Survey Creation**: Add questions with multiple-choice options.
- **Survey Management**: Publish, close, or edit surveys.
- **Dashboard**: Separate dashboards for creators and takers.
- **Survey Responses**: View aggregated results for closed surveys.
- **User Authentication**: Registration, login, and role-based access control.

## Project Structure
- `db.sqlite3`: Database file for storing application data.
- `manage.py`: Django's command-line utility for administrative tasks.
- `survey_app/`: Contains the core functionality of the application.
    - `models.py`: Database models for surveys, questions, options, and responses.
    - `views.py`: Handles the application logic for different pages.
    - `templates/survey_app/`: HTML templates for user interfaces.
    - `static/survey_app/`: Static files (CSS, JS, images).
- `survey_project/`: Project configuration directory.
    - `settings.py`: Configuration settings for the Django project.
    - `urls.py`: URL routing for the application.

## Setup Instructions

### Prerequisites
- Python 3.12 or higher
- Django 4.2 or higher
- Virtual environment (recommended)

### Installation
1. Clone or unzip the project into your desired directory.
2. Navigate to the project directory:
   ```bash
   cd survey_project
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Usage
1. Access the application in your browser at `http://127.0.0.1:8000/`.
2. Register as a user and log in.
3. Depending on your role:
   - **Creators** can create and manage surveys from their dashboard.
   - **Takers** can participate in available surveys.

## Folder Structure
```
survey_project/
│
├── db.sqlite3               # SQLite database
├── manage.py                # Django's management script
├── survey_app/              # Main application directory
│   ├── migrations/          # Database migrations
│   ├── static/              # Static assets (CSS/JS)
│   ├── templates/           # HTML templates
│   ├── views.py             # Application logic
│   └── models.py            # Database models
└── survey_project/          # Django project configuration
    ├── settings.py          # Project settings
    └── urls.py              # URL routing
```

## License
This project is for educational purposes and can be used as a starting point for similar survey-based applications.

# Survey Management System

## Overview
This is a Django-based web application for creating, managing, and taking surveys. 
It supports two user roles:
- **Creators**: Can create, publish, and manage surveys.
- **Takers**: Can take available surveys and view survey completion details.

## Features
- **Survey Creation**: Add questions with multiple-choice options.
- **Survey Management**: Publish, close, or edit surveys.
- **Dashboard**: Separate dashboards for creators and takers.
- **Survey Responses**: View aggregated results for closed surveys.
- **User Authentication**: Registration, login, and role-based access control.

## Project Structure
- `db.sqlite3`: Database file for storing application data.
- `manage.py`: Django's command-line utility for administrative tasks.
- `survey_app/`: Contains the core functionality of the application.
    - `models.py`: Database models for surveys, questions, options, and responses.
    - `views.py`: Handles the application logic for different pages.
    - `templates/survey_app/`: HTML templates for user interfaces.
    - `static/survey_app/`: Static files (CSS, JS, images).
- `survey_project/`: Project configuration directory.
    - `settings.py`: Configuration settings for the Django project.
    - `urls.py`: URL routing for the application.

## Setup Instructions

### Prerequisites
- Python 3.12 or higher
- Django 4.2 or higher
- Virtual environment (recommended)

### Installation
1. Clone or unzip the project into your desired directory.
2. Navigate to the project directory:
   ```bash
   cd survey_project
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Usage
1. Access the application in your browser at `http://127.0.0.1:8000/`.
2. Register as a user and log in.
3. Depending on your role:
   - **Creators** can create and manage surveys from their dashboard.
   - **Takers** can participate in available surveys.

## Folder Structure
```
survey_project/
│
├── db.sqlite3               # SQLite database
├── manage.py                # Django's management script
├── survey_app/              # Main application directory
│   ├── migrations/          # Database migrations
│   ├── static/              # Static assets (CSS/JS)
│   ├── templates/           # HTML templates
│   ├── views.py             # Application logic
│   └── models.py            # Database models
└── survey_project/          # Django project configuration
    ├── settings.py          # Project settings
    └── urls.py              # URL routing
```

## License
This project is for educational purposes and can be used as a starting point for similar survey-based applications.


# Survey Management System

## Overview
This is a Django-based web application for creating, managing, and taking surveys. 
It supports two user roles:
- **Creators**: Can create, publish, and manage surveys.
- **Takers**: Can take available surveys and view survey completion details.

## Features
- **Survey Creation**: Add questions with multiple-choice options.
- **Survey Management**: Publish, close, or edit surveys.
- **Dashboard**: Separate dashboards for creators and takers.
- **Survey Responses**: View aggregated results for closed surveys.
- **User Authentication**: Registration, login, and role-based access control.

## Project Structure
- `db.sqlite3`: Database file for storing application data.
- `manage.py`: Django's command-line utility for administrative tasks.
- `survey_app/`: Contains the core functionality of the application.
    - `models.py`: Database models for surveys, questions, options, and responses.
    - `views.py`: Handles the application logic for different pages.
    - `templates/survey_app/`: HTML templates for user interfaces.
    - `static/survey_app/`: Static files (CSS, JS, images).
- `survey_project/`: Project configuration directory.
    - `settings.py`: Configuration settings for the Django project.
    - `urls.py`: URL routing for the application.

## Setup Instructions

### Prerequisites
- Python 3.12 or higher
- Django 4.2 or higher
- Virtual environment (recommended)

### Installation
1. Clone or unzip the project into your desired directory.
2. Navigate to the project directory:
   ```bash
   cd survey_project
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Usage
1. Access the application in your browser at `http://127.0.0.1:8000/`.
2. Register as a user and log in.
3. Depending on your role:
   - **Creators** can create and manage surveys from their dashboard.
   - **Takers** can participate in available surveys.

## Folder Structure
```
survey_project/
│
├── db.sqlite3               # SQLite database
├── manage.py                # Django's management script
├── survey_app/              # Main application directory
│   ├── migrations/          # Database migrations
│   ├── static/              # Static assets (CSS/JS)
│   ├── templates/           # HTML templates
│   ├── views.py             # Application logic
│   └── models.py            # Database models
└── survey_project/          # Django project configuration
    ├── settings.py          # Project settings
    └── urls.py              # URL routing
```

## License
This project is for educational purposes and can be used as a starting point for similar survey-based applications.


