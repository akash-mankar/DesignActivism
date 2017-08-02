# Design Activism for Minimum Wage Crowd Work
## Public Dataset Repository
This is a public dataset repository for the paper [Design activism for minimum wage crowd work](https://arxiv.org/abs/1706.10097)

---
### What is in this repository?
- README.md
- Data
- API to retrieve location based minimum wage

---
### How to access the data?
In the folder Data, you should be able to find <b>TabularData.xlsx</b>
You'll find different tabs in this spreadsheet.
-  <b>Tabular Data Tab </b><br />
This will give all the data in a tabular format. It includes individual responses, their country, city and state as well as how they feel about the policy, categoriezed in column 'answer' as bad, good or neutral. The individual IDs and IP addresses have been removed in order to maintain anonymity of responses.

-  <b>Country Distribution tab </b><br />
This tab shows the number of responses received distributed by country. More than 95% of the responses were received from the United states.

-  <b>Answer Distribution tab </b><br />
This tab shows the overall feeling about the policy, categorized as bad, good and neutral.

-  <b>Distribution by US states tab </b><br />
This tab gives color coded distrbution of overall feeling about this policy within United states but by individual states.
Look at Distribution by states US.png in the same folder to see how the color grading works. Image shows how opinions are distributed for the state of Texas.

---
### Additional files
- DistributionByStates.mp4 is a 10 second video showing color coded distrbution of sentiment across US.
- Distribution by Country.png - Already included in spreadsheet.
- Distribution by states US.png - Already included in spreadsheet.

---
### API to retrieve location based minimum wage
- The python script "<b>LocationMinWage.py</b>" located inside folder <b> Min-Wage Retrieval API</b> can be used by crowdsourcing requesters to obtain location based minimum wage
- <b>Source</b>: http://en.wikipedia.org/wiki/List_of_minimum_wages_by_country
- <b>Usage</b>: python LocationtoMinWage.py <country_name>
 - If country name has a space - Eg: United States, specify it in this format - United\ States
- The hourly wage (in US$) is obtained.
- Please Note that this version currently does not handle wikipedia format changes