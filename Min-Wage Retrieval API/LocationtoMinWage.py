'''
Riddhi J Shah & Akash Mankar

Social Activism Intended to be Provocative
Minimum wage restriction on crowdsourcing tasks

The following code can be used by crowdsourcing requesters to obtain location based minimum wage
Source: http://en.wikipedia.org/wiki/List_of_minimum_wages_by_country

Usage:
python LocationtoMinWage.py <country_name>

If country name has a space - Eg: United States, specify it in this format - United\ States

The hourly wage (in US$) is obtained.

Please Note that this version currently does not handle wikipedia format changes.

'''

from bs4 import BeautifulSoup
import urllib2
import re
import sys

# Function to obtain hourly minimum wage by the country
def getMinimumWage(country):
  
  #wikipage =  urllib2.urlopen('http://en.wikipedia.org/wiki/List_of_minimum_wages_by_country').read()

  wikipage = open('wikilist.html').read()

  soup = BeautifulSoup(wikipage)
  min_wage = ''
  country_found = False
  for row in  soup.find('table',{'class':'sortable wikitable'}).findAll('tr'):
    rowlist = row.findAll('td')
    for i in range(len(rowlist)):
      if ((i==0) and ((rowlist[0].contents[-1].text).encode('ascii','ignore')) == country):
        country_found = True
      if (i==5):
        manip1 = (re.sub(r'<span.*span>','',str(rowlist[i])))
        manip2 = (re.sub(r'<.*?>','',manip1))
        min_wage = manip2
    if (country_found==True):      
      break
  return min_wage      

def main(argv):
  if (len(argv)!=2):
    print("Please specify the country for which you want the minimum wage")
    sys.exit(1)
  else:
    # country being the only command line argument 
    country = argv[1]
    print ("In "+country+" the hourly minimum wage(US$) is:"+getMinimumWage(country))

main(sys.argv)
