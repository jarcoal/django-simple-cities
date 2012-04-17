from django.core.management.base import BaseCommand, CommandError
from cities.models import City
import csv, string

class Command(BaseCommand):
	help = 'Imports cities from MaxMind Cities of the World dataset (or equivalent formatted).  Can be downloaded here: http://www.maxmind.com/app/worldcities'
	
	def handle(self, *a, **k):
		#check for the location of the maxmind set.
		try:
			file_name = a[0]
		except:
			print 'Missing argument: Location of the cities CSV dataset.'
			return
	
		#the rest of the parameters are countries
		countries = a[1:]
		
		#no countries found
		if not len(countries):
			countries = None
	
		#open up the CSV
		csv_contents = csv.reader(open(file_name), delimiter=',')
		
		#loop through and save the data
		for country_code, ascii_name, name, region, population, latitude, longitude in csv_contents:
			#cleanup
			ascii_name = string.capwords(ascii_name)
			country_code = country_code.upper()
			
			#check pop
			try:
				population = int(population)
			except:
				population = 0
		
			#we're not supposed to record this entry, skip.
			if countries and country_code not in countries:
				continue
		
			#start loading the data
			try:
				c = City.objects.create(name=ascii_name, country_code=country_code, region=region, latitude=latitude, longitude=longitude, population=population)
				
				print 'Created City: %s (%i)' % (c.name, c.id)
				
			#something went wrong...
			except Exception, e:
				print '***Failed to import city: %s, because: %s' % (ascii_name, e.message)
		