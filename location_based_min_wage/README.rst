API for Location based minimum wage
====================================
The purpose of this API is to retrieve the hourly minimum wage (in US$) for a given country. Source for country names/hourly minimum wage rates (US$): https://en.wikipedia.org/wiki/List_of_minimum_wages_by_country

Pre-requisites
--------------
Make sure to have the following installed on your machine.

* Python 2.7
* Python packages: `bs4 <https://pypi.python.org/pypi/bs4>`_

Usage guidelines
----------------
* Run the script **minwage.py** under directory **location_based_min_wage**::

       python minwage.py --country 'India'

* The country name can be in uppercase or lowercase, but spelt as specified in the `source <https://en.wikipedia.org/wiki/List_of_minimum_wages_by_country>`_. **Example**: 'United States' and NOT 'UnitedStates' (without space).

* For tests, from the current folder, run::

   python -m unittest discover -b -v

NOTE
----
   The wikipedia source format changes are not supported. The currently supported format - **wikilist.html** is included under the *location_based_min_wage* directory.
 

