from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from collections import Counter

from .utils import preprocess_text, remove_stopwords

import sklearn
import pickle

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

		default_storage.delete('storage/uploads/pfizer/pfizer.txt')
		default_storage.delete('storage/uploads/sinovac/sinovac.txt')
		default_storage.delete('storage/uploads/astrazeneca/astrazeneca.txt')
		default_storage.delete('storage/uploads/moderna/moderna.txt')

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
			df = pd.read_csv('storage/uploads/' + key + '/' + key + '.csv', encoding='cp1252', sep=';')
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
			df = pd.read_csv('storage/uploads/' + item['name'] + '/' + item['name'] + '.csv', encoding='cp1252', sep=';')
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