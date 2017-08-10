"""
Script to obtain location based minimum wage
Source: https://en.wikipedia.org/wiki/List_of_minimum_wages_by_country

Note: 

1. Wikipedia source changes not supported. The currently supported
version's source file can be found in `wikilist.html` under the current folder.

2. If country name has a space - Eg: United States, surround the argument with quotes: 'United States'
"""

#!/usr/bin/env python
import argparse
import re
import sys

from bs4 import BeautifulSoup


# Function to obtain hourly minimum wage by the country
def get_minimumwage(country_name, source='wikilist.html'):
    min_wage = None
    country_found = False

    wikipage = open(source).read()
    soup = BeautifulSoup(wikipage, "html.parser")

    for row in soup.find(
        'table', {'class': 'sortable wikitable'}
    ).findAll('tr'):
        columns = row.findAll('td')
        for col_num in range(len(columns)):
            if col_num == 0:
                cname = columns[col_num].contents[-1].text
                if cname.lower() == country_name.lower():
                    country_found = True
            elif col_num == 5 and country_found:
                manip1 = (re.sub(r'<span.*span>', '', str(columns[col_num])))
                manip2 = (re.sub(r'<.*?>', '', manip1))
                min_wage = manip2
            elif country_found and min_wage:
                break
            else:
                continue

    if min_wage is None:
        print("Could not determine the hourly minimum wage for {}".format(
            country_name)
        )
        sys.exit(0)
    else:
        return min_wage


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve hourly minimum wage(in US$) for "
                    "specified country"
    )
    parser.add_argument("--country", required=True, type=str)
    args = parser.parse_args()

    min_wage = get_minimumwage(args.country)

    print("The hourly minimum wage in {} is ${}".format(
        args.country, min_wage)
    )


if __name__ == '__main__':
    main()
