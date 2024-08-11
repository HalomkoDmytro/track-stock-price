import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "" # TODO: add api key


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": NEWS_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(diff_percent) < 5:
    news_param = {"apiKey": NEWS_API_KEY, "qInTitle": COMPANY_NAME}
    news_response = requests.get(NEWS_ENDPOINT, news_param)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    formated_articles = [f"{STOCK_NAME} {up_down} {diff_percent}% \n Headline: {article['title']}. \nBrief: {article['description']}\n" for article in three_articles]




