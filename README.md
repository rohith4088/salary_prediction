## Salary Prediction Project

## Overview

This project aims to predict salaries based on years of experience using a machine learning model. The project includes a Flask web application that allows users to input the years of experience and receive a salary prediction.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project structure is as follows:

- `app.py`: Flask web application for the salary prediction.
- `reg_model.pkl`: Pickle file containing the trained machine learning model.
- `scaling.pkl`: Pickle file containing the scaler used for feature scaling.
- `templates/`: HTML templates for the web application.
- `static/`: Static files (e.g., CSS, images).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/rohith4088/salary_prediction.git
Navigate to the project directory:
bash
Copy code
cd salary-prediction
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage

Run the Flask application:
bash
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000/ to access the salary prediction web application.
Enter the years of experience, and the application will provide a salary prediction.
Dependencies

Flask
NumPy
Pandas
Scikit-learn
Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.

License

This project is licensed under the MIT License.
