from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

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

		if expected_files['Pfizer'] is not None:
			default_storage.delete('storage/uploads/pfizer/pfizer.txt')
			path = default_storage.save('storage/uploads/pfizer/pfizer.txt', ContentFile(expected_files['Pfizer'].read()))
		
		if expected_files['Sinovac'] is not None:
			default_storage.delete('storage/uploads/sinovac/sinovac.txt')
			path = default_storage.save('storage/uploads/sinovac/sinovac.txt', ContentFile(expected_files['Sinovac'].read()))

		if expected_files['Astrazeneca'] is not None:
			default_storage.delete('storage/uploads/astrazeneca/astrazeneca.txt')
			path = default_storage.save('storage/uploads/astrazeneca/astrazeneca.txt', ContentFile(expected_files['Astrazeneca'].read()))

		if expected_files['Moderna'] is not None:
			default_storage.delete('storage/uploads/moderna/moderna.txt')
			path = default_storage.save('storage/uploads/moderna/moderna.txt', ContentFile(expected_files['Moderna'].read()))

	return Response("test")