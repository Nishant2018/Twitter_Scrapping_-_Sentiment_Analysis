from flask import Flask, request, render_template, send_file
from apify_client import ApifyClient
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__, static_folder='static')

# Initialize the ApifyClient with your Apify API token
client = ApifyClient("apify_api_bn5pkv46MG1SfFYIBWxAbBajfWTaKK0JXz8i")

# Load the sentiment-analysis pipeline with a pre-trained BERT model
sentiment_pipeline = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['action'] == 'Analyze Tweets':
            handles = request.form.get('handles').split(',')
            tweets_desired = int(request.form.get('tweets_desired'))

            # Prepare the Actor input
            run_input = {
                "handles": handles,
                "tweetsDesired": tweets_desired,
                "proxyConfig": { "useApifyProxy": True },
            }

            # Run the Actor and wait for it to finish
            run = client.actor("quacker/twitter-scraper").call(run_input=run_input)

            # Print the dataset URL
            dataset_url = f"https://console.apify.com/storage/datasets/{run['defaultDatasetId']}"

            # Extract data and convert to DataFrame
            dataset = client.dataset(run["defaultDatasetId"])
            data = []
            for item in dataset.iterate_items():
                tweet_data = {
                    'user_id': item['user']['id_str'],
                    'user_screen_name': item['user']['screen_name'],
                    'user_name': item['user']['name'],
                    'tweet_id': item['id'],
                    'tweet_text': item['full_text'],
                    'created_at': item['created_at'],
                    'reply_count': item['reply_count'],
                    'retweet_count': item['retweet_count'],
                    'favorite_count': item['favorite_count'],
                    'hashtags': ','.join(item.get('hashtags', [])),
                    'urls': ','.join(url['expanded_url'] for url in item.get('urls', [])),
                    'media': ','.join(media['media_url'] for media in item.get('media', [])),
                    'is_retweet': item['is_retweet'],
                }
                data.append(tweet_data)

            df = pd.DataFrame(data)

            # Perform sentiment analysis
            texts = df['tweet_text'].tolist()
            results = sentiment_pipeline(texts)

            # Add sentiment analysis results to the DataFrame
            df['sentiment'] = [result['label'] for result in results]
            df['score'] = [result['score'] for result in results]

            # Save to CSV
            csv_file_path = 'tweets_data.csv'
            df.to_csv(csv_file_path, index=False)

            # Calculate positive and negative tweet counts
            positive_count = df[df['sentiment'] == 'POSITIVE'].shape[0]
            negative_count = df[df['sentiment'] == 'NEGATIVE'].shape[0]

            # Create a bar plot for sentiment counts
            fig, ax = plt.subplots()
            ax.bar(['Positive', 'Negative'], [positive_count, negative_count], color=['green', 'red'])
            ax.set_xlabel('Sentiment')
            ax.set_ylabel('Count')
            ax.set_title('Sentiment Analysis Results')

            # Save plot to a BytesIO object and encode as base64
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')
            plt.close(fig)

            return render_template('index.html', dataset_url=dataset_url, positive_count=positive_count, negative_count=negative_count, plot_url=plot_url)

        elif request.form['action'] == 'Get Sentiment':
            sentiment_label = None
            sentiment_score = None
            sentence = request.form.get('sentence')

            # Perform sentiment analysis on the sentence
            result = sentiment_pipeline(sentence)[0]

            # Extract the label and score
            sentiment_label = result['label']
            sentiment_score = result['score']

            return render_template('index.html', sentiment_label=sentiment_label, sentiment_score=sentiment_score)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
