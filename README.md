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

Run ```pip install git+git://github.com/jarcoal/django-simple-cities.git#egg=django-simple-cities``` to install the package.

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
>>>c = City.objects.get(name='Portland', region='OR', country_code='US')

>>>c.nearby_cities(miles=5)
[<City: Alameda, OR, US>, <City: Albina, OR, US>, <City: Arleta, OR, US>, <City: Barnes Heights, OR, US>, <City: Bridlemile, OR, US>, <City: Brooklyn, OR, US>, <City: Burlingame, OR, US>, <City: Capitol Hill, OR, US>, <City: Carson Heights, OR, US>, <City: East Portland, OR, US>, <City: Eastmoreland, OR, US>, <City: Errol Heights, OR, US>, <City: Glencullen, OR, US>, <City: Green Hills, OR, US>, <City: Hillsdale, OR, US>, <City: Hollywood, OR, US>, <City: Irvington, OR, US>, <City: Kenton, OR, US>, <City: Kings Heights, OR, US>, <City: Laurelhurst, OR, US>, '...(remaining elements truncated)...']
```
