# Car Price Prediction

## Overview
This project focuses on predicting car prices based on data extracted from over 7,000 webpages of car listings on [Shobiddak](https://www.shobiddak.com/ar). The project includes web scraping, data cleaning, feature extraction, and machine learning modeling to determine the most accurate price prediction. The final model is deployed using Flask, allowing users to input car features and get price predictions through a web interface.

## Features
- Web scraping of car listings.
- Data cleaning and preprocessing.
- Feature extraction and analysis.
- Model training and evaluation to predict car prices.
- Flask-based web app for user interaction.

## Project Structure
- **Data Extraction**: Python scripts using BeautifulSoup to scrape data from thousands of webpages.
- **Data Cleaning and Analysis**: Jupyter Notebook used for preprocessing and exploring the data, finding correlations, and selecting relevant features.
- **Machine Learning Models**: The notebook contains model training and evaluation to select the best performing model.
- **Flask Web App**: A simple Flask app that serves the model to users, allowing them to input car details and receive a price prediction.



## Usage
After running the Flask app, you can access the web interface at `http://localhost:5000/` . Input the car features like brand, model, year, and mileage, and the app will return an estimated price based on the trained model.

## Technologies Used
- Python
- BeautifulSoup (for web scraping)
- Pandas and NumPy (for data processing)
- Scikit-learn (for model training)
- Flask (for web deployment)
- Jupyter Notebook (for data analysis)

## Model Details
The project uses a variety of models, including Linear Regression , Decision Tree and K Neighbors , and evaluates their performance. The best model is selected based on metrics like accuracy, R-squared, and mean squared error. This model is deployed using Flask for real-time predictions.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork this repository, create a branch, and submit a pull request.



## Contact
For any questions or suggestions, feel free to reach out via [Linked in](https://www.linkedin.com/in/tareq-saymeh-721635311/) or open an issue in this repository.
