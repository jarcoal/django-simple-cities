from django.db import models

# SQL for filtering cities given the lat/lng of another city
geo_filter = 'pow(%s, 2) > (69.1 * (`geo_city`.`latitude` - %s)) * (69.1 * (`geo_city`.`latitude` - %s)) + (69.1 * (`geo_city`.`longitude` - %s) * COS(%s / 57.3)) * (69.1 * (`geo_city`.`longitude` - %s) * COS(%s / 57.3))'


class City(models.Model):
	"""
	Represents a City
	"""
	
	name = models.CharField(max_length=255, db_index=True)
	country_code = models.CharField(max_length=2, db_index=True)
	
	region = models.CharField(max_length=2, db_index=True)
	
	latitude = models.FloatField(db_index=True)
	longitude = models.FloatField(db_index=True)
	
	population = models.IntegerField(db_index=True, default=0)
	
	
	def nearby_cities(self, miles=25):
		"""
		Returns a list of cities within `miles` of this city
		"""
		return City.objects.extra(where=[geo_filter], params=[miles, self.latitude, self.latitude, self.longitude, self.latitude, self.longitude, self.latitude])
	
	
	def nearby_related(self, related_model, related_name='city', miles=25):
		"""
		Returns a queryset for a related model
		"""
		return related_model.objects.extra(where=[geo_filter], params=[miles, self.latitude, self.latitude, self.longitude, self.latitude, self.longitude, self.latitude]).select_related(related_name)
	
	
	def __unicode__(self):
		return ', '.join([self.name, self.region, self.country_code])