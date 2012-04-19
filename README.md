#django-simple-cities
###City models and distance querying without GeoDjango

----

###Requirements

Download MaxMind cities of the world dataset (free):

http://www.maxmind.com/app/worldcities

http://www.maxmind.com/download/worldcities/worldcitiespop.txt.gz (direct DL)

Please note that if you are using sqlite3, you will need to install the extension-functions.c package, found at the bottom of this page:

http://www.sqlite.org/contrib

----

###Installation

Run ```pip install -e git+git://github.com/jarcoal/django-simple-cities.git#egg=django-simple-cities``` to install the package.

Add ```cities``` to ```INSTALLED_APPS``` in your settings file:

```python
INSTALLED_APPS = (
	...
	'cities',
)
```

Now run ```./manage.py syncdb``` to setup the City table.

----

###Populating Your Database with Cities

I have included a management command to help with the city importing.  Here's how to use it:

```./manage.py import_cities /path/to/worldcitiespop.txt [COUNTRY_CODES...]```

The country codes are a space-separated list of two-letter country codes that you want imported.  If you provide none, all countries will be included.  Here is an example for United States and Canada:

```./manage.py import_cities /path/to/worldcitiespop.txt US CA```

This might take a while.  If you database is not local or on a LAN, it will take VERY long.

----

###"I need to find all cities within X miles of a city"

```python
>>>from cities.models import City
>>>pdx = City.objects.get(name='Portland', region='OR', country_code='US')
>>>pdx.nearby_cities(miles=5)
[<City: Alameda, OR, US>, <City: Albina, OR, US>, <City: Arleta, OR, US>, ...]
```

----

###"I need to find my related models near a city"

```python
#Example Related Model
from django.db import models
from cities.models import City

class Store(models.Model):
	city = models.ForeignKey(City)
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name


#Some dummy data
>>>Store.objects.create(city=City.objects.get(name='Eugene', region='OR', country_code='US'), name='Eugene Store')
>>>Store.objects.create(city=City.objects.get(name='Portland', region='OR', country_code='US'), name='Portland Store')

#The Query
>>>eugene = City.objects.get(name='Eugene', region='OR', country_code='US')
>>>eugene.nearby_related(Store, miles=25)
[<Store: Eugene Store>]
>>>eugene.nearby_related(Store, miles=150)
[<Store: Eugene Store>, <Store: Portland Store>]
```