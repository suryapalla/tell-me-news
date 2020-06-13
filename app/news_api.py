import os
from newsapi import NewsApiClient
from datetime import date, timedelta


newsapi = NewsApiClient(api_key=os.environ.get('API_KEY'))
today_date = date.today().strftime("%Y-%m-%d")
yesterday_date = (date.today() - timedelta(1)).strftime("%Y-%m-%d")

class NewsApi(object):
	def __init__(self, parameter):
		self.parameter = parameter
		self.top_headlines = newsapi.get_top_headlines(q=self.parameter)
		self.description = []
		self.url = []
		self.image_link = []
		self.title = []
		self.sources = []
		for article in self.top_headlines['articles']:
			self.description.append(article['description'])
			self.url.append(article['url'])
			self.image_link.append(article['urlToImage'])
			self.title.append(article['title'])
			self.sources.append(article['source']['name'])

	def get_description(self):
		return self.description

	def get_url(self):
		return self.url

	def get_images(self):
		return self.image_link

	def get_title(self):
		return self.title

	def get_sources(self):
		return self.sources

class NewsApiEverything(NewsApi):
	def __init__(self, parameter,sources):
		self.parameter = parameter
		self.sources = sources
		self.allnews = newsapi.get_everything(q=self.parameter,
										sources=self.sources,
										language='en',
										sort_by='relevancy',
										page=1)
		self.description = []
		self.url = []
		self.image_link = []
		self.title = []
		self.sources = []
		for article in self.allnews['articles']:
			self.description.append(article['description'])
			self.url.append(article['url'])
			self.image_link.append(article['urlToImage'])
			self.title.append(article['title'])
			self.sources.append(article['source']['name'])
