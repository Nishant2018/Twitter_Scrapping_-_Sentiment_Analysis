
# Twitter Sentiment Analysis Web Application

![Alt text](https://github.com/Nishant2018/Twitter_Scrapping_-_Sentiment_Analysis/blob/main/1.jpg)


![Alt text](https://github.com/Nishant2018/Twitter_Scrapping_-_Sentiment_Analysis/blob/main/Screenshot%20(188).png)
## Overview
   
This web application performs sentiment analysis on tweets using Twitter's API. The application provides two primary functionalities:
1. **Sentiment Count**: Analyzes a specified number of tweets from given Twitter handles and provides a sentiment breakdown (positive or negative).
2. **Get Sentiment Only**: Analyzes the sentiment of a single user-provided sentence.
   
The application features an interactive interface with options to view live Twitter feeds and visualize sentiment analysis results.

## Features
   
- **Twitter Sentiment Count**: Fetches and analyzes tweets from specified Twitter handles.
- **Single Sentence Sentiment Analysis**: Analyzes the sentiment of a user-provided sentence.   
- **Live Twitter Feed**: Displays a live feed of tweets from selected handles.
- **Visualizations**: Provides a visual representation of positive and negative sentiment counts.
- **Responsive Design**: Mobile-friendly and interactive UI with Bootstrap.   

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **APIs**: Twitter API
- **Data Analysis**: Python, Sentiment Analysis Libraries
- **Deployment**: Local environment or web server

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Bootstrap
- Twitter API credentials

### Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set Up the Environment**

   Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Twitter API Credentials**

   Update your credentials in the Flask application configuration:

   ```python
   consumer_key = 'your-consumer-key'
   consumer_secret = 'your-consumer-secret'
   access_token = 'your-access-token'
   access_token_secret = 'your-access-token-secret'
   ```

5. **Run the Application**

   ```bash
   python app.py
   ```

   Access the application in your web browser at `http://127.0.0.1:5000`.

### Usage

1. **Sentiment Count**: Enter Twitter handles and the number of tweets to analyze. Click "🔍 Analyze Tweets 🔍" to fetch and analyze tweets.

2. **Get Sentiment Only**: Enter a sentence for sentiment analysis and click "🔍 Get Sentiment 🔍".

3. **View Live Feed**: Check the live Twitter feed card for real-time updates from selected handles.

### Project Structure

- **`app.py`**: The main Flask application file that handles routes and API interactions.
- **`static/css/styles.css`**: Custom styles for the web application.
- **`templates/`**: HTML templates for rendering pages.
- **`requirements.txt`**: List of Python dependencies.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any questions or feedback, please contact [nishantraghuwanshi2018@gmail.com](nishantraghuwanshi2018@gmail.com).


Feel free to adjust the sections and details according to your project's specific requirements.
