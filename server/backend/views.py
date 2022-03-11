from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from collections import Counter, OrderedDict

from .utils import preprocess_text, remove_stopwords

import sklearn
import pickle
import re

import pandas as pd


# Create your views here.
@api_view(['POST'])
def upload(request):

	if request.method == 'POST':
		files = request.FILES

		expected_files = {
			'Pfizer': None,
			'Sinovac': None,
			'Astrazeneca': None,
			'Moderna': None
		}

		for file in files:
			expected_files[file]  = files[file]

		default_storage.delete('storage/uploads/pfizer/pfizer.csv')
		default_storage.delete('storage/uploads/sinovac/sinovac.csv')
		default_storage.delete('storage/uploads/astrazeneca/astrazeneca.csv')
		default_storage.delete('storage/uploads/moderna/moderna.csv')

		if expected_files['Pfizer'] is not None:
			path = default_storage.save('storage/uploads/pfizer/pfizer.csv', ContentFile(expected_files['Pfizer'].read()))
		
		if expected_files['Sinovac'] is not None:
			path = default_storage.save('storage/uploads/sinovac/sinovac.csv', ContentFile(expected_files['Sinovac'].read()))

		if expected_files['Astrazeneca'] is not None:
			path = default_storage.save('storage/uploads/astrazeneca/astrazeneca.csv', ContentFile(expected_files['Astrazeneca'].read()))

		if expected_files['Moderna'] is not None:
			path = default_storage.save('storage/uploads/moderna/moderna.csv', ContentFile(expected_files['Moderna'].read()))

	return Response("test")

@api_view(['GET'])
def data_overview(request):

	data = {
		'pfizer':  None,
		'sinovac':  None,
		'astrazeneca':  None,
		'moderna':  None,
	}

	for key in data:
		try:
			df = pd.read_csv('storage/uploads/' + key + '/' + key + '.csv')
			num_tweets = df.shape[0]
			data[key] = num_tweets
		except:
			data[key] = None

	return Response(data)

@api_view(['GET'])
def sentiment_overview(request):

	model = pickle.load(open('storage/models/model.pkl', 'rb'))
	vectorizer = pickle.load(open('storage/models/vectorizer.pkl', 'rb'))

	data = [
		{
			'name': 'pfizer',
			'sentiments': [
				{
					'positive': 0,
					'negative': 0
				}
			]
		},
		{
			'name': 'sinovac',
			'sentiments': [
				{
					'positive': 0,
					'negative': 0
				}
			]
		},
		{
			'name': 'astrazeneca',
			'sentiments': [
				{
					'positive': 0,
					'negative': 0
				}
			]
		},
		{
			'name': 'moderna',
			'sentiments': [
				{
					'positive': 0,
					'negative': 0
				}
			]
		},
	]

	for item in data:
		try:
			df = pd.read_csv('storage/uploads/' + item['name'] + '/' + item['name'] + '.csv')
			df = preprocess_text(df)
			df = remove_stopwords(df)
			
			corpus = vectorizer.transform(df['Text'])
			predictions = model.predict(corpus)
			
			count_dict = dict(Counter(predictions))
			item['sentiments'] = [
				{
					'positive': count_dict[1],
					'negative': count_dict[0]
				}
			]

		except:
			item['sentiments'] = None




	return Response(data)

@api_view(['GET'])
def sentiment_overtime(request):

	model = pickle.load(open('storage/models/model.pkl', 'rb'))
	vectorizer = pickle.load(open('storage/models/vectorizer.pkl', 'rb'))

	data = [
		{
			'name': 'pfizer',
			'sentiments': []
		},
		{
			'name': 'sinovac',
			'sentiments': []
		},
		{
			'name': 'astrazeneca',
			'sentiments': []
		},
		{
			'name': 'moderna',
			'sentiments': []
		},
	]

	for item in data:
		try:
			df = pd.read_csv('storage/uploads/' + item['name'] + '/' + item['name'] + '.csv')

			df_shape = df.shape
			for i in range(df_shape[0]):
				s = re.sub(r' (\d{2}):(\d{2}):(\d{2})', '', df.at[i, 'Created-At']).split('-')
				s = s[0] + '/' + s[1]
				df.at[i, 'Created-At'] = s
			
			df = preprocess_text(df)
			df = remove_stopwords(df)

			corpus = vectorizer.transform(df['Text'])
			predictions = model.predict(corpus)

			predictions = pd.Series(predictions)
			df['Sentiments'] = predictions.values

			labels = df['Created-At'].value_counts()
			labels = labels.keys()

			positive_sentiments = {}
			negative_sentiments = {}

			for label in labels:
				df_shape = df.shape
				pos_sentiments = 0
				neg_sentiments = 0
				for i in range(0, df_shape[0]):
					if(df.at[i, 'Created-At'] == label and df.at[i, 'Sentiments'] == 1):
					 	pos_sentiments += 1
					elif(df.at[i, 'Created-At'] == label and df.at[i, 'Sentiments'] == 0):
					  	neg_sentiments += 1

				positive_sentiments[label] = pos_sentiments
				negative_sentiments[label] = neg_sentiments

			item['sentiments'].append(OrderedDict(sorted(positive_sentiments.items())))
			item['sentiments'].append(OrderedDict(sorted(negative_sentiments.items())))

		except FileNotFoundError:
			item['sentiments'] = None

	return Response(data)