#Importing resquest module for requesting web server
import requests
#Importing beautiful soup for scraping
from bs4 import BeautifulSoup

#Initializing the url
url='http://howstat.com/cricket/Statistics/WorldCup/PointsTable.asp?SeriesCode=1009'

#Get the html
data = requests.get(url)
html_code = data.content
# print(html_code)

#Parser
soup = BeautifulSoup(html_code, 'html.parser')

#Get the title of html page
title=soup.find(class_="TableLined")
# print(type(title))


# Initializing a list for storing only the strings from all scraped data into a list in stripped form
table_elements=[]

# Iterating from the striped strings and appending the each string into the above initialized list
for i in title.stripped_strings:
    table_elements.append(i)

# You can Un-comment the following print statement to watch the list
# print(table_elements)

# The data in table_elements list -
#  0-9    = 'Team', 'Matches', 'Won', 'Lost', 'Tied', 'N/R', 'Points', 'Net R/R', 'For', 'Against'
# 10-19   = 'India', '9', '7', '1', '0', '1', '15', '+0.657', '2260/391.0', '1998/390.0'
# 20-29   = 'Australia', '9', '7', '2', '0', '0', '14', '+0.868', '2678/434.5', '2381/450.0'
# 30-39   = 'England', '9', '6', '3', '0', '0', '12', '+1.152', '2716/433.1', '2303/450.0'
# 40-49   = 'New Zealand', '9', '5', '3', '0', '1', '11', '+0.175', '1674/344.0', '1868/398.1'
# 50-59   = 'Pakistan', '9', '5', '3', '0', '1', '11', '-0.430', '2025/388.5', '1994/353.4'
# 60-69   = 'Sri Lanka', '9', '3', '4', '0', '2', '8', '-1.087', '1606/341.0', '1621/279.4'
# 70-79   = 'South Africa', '9', '3', '5', '0', '1', '7', '-0.030', '1905/365.0', '2068/394.0'
# 80-89   = 'Bangladesh', '9', '3', '5', '0', '1', '7', '-0.410', '2278/391.3', '2474/397.1'
# 90-99   = 'West Indies', '9', '2', '6', '0', '1', '5', '-0.225', '1969/363.4', '2113/374.4'
# 100-109 = 'Afghanistan', '9', '0', '9', '0', '0', '0', '-1.382', '1832/439.0', '2123/382.1'

# Initializing the dictionary for each country for storing data,
# like Ind_dict={'Team':'India', 'Matches':9, 'Won':7, ...}
Ind_dict={}
Aus_dict={}
Eng_dict={}
NZ_dict={}
Pak_dict={}
SL_dict={}
SA_dict={}
Ban_dict={}
WI_dict={}
Afg_dict={}

# Making a dictionary of above dictionaries,
# with the key= Country shortname and value= above dictionary for specific country
Data_dict={
'Ind':Ind_dict,
'Aus':Aus_dict,
'Eng':Eng_dict,
'NZ':NZ_dict,
'Pak':Pak_dict,
'SL':SL_dict,
'SA':SA_dict,
'Ban':Ban_dict,
'WI':WI_dict,
'Afg':Afg_dict,}

# Initializing count=0 for further use
count=0

# Inserting data into all dictionaries Ind_dict, Aus_dict, ...
# Iterating through Data_dict and then inserting values
for country,country_dict in Data_dict.items():
    for i in range(10):
        Data_dict[country].update({table_elements[i]:table_elements[(count*10)+10+i]})
    count+=1

print('\n')

# Now all is set, every information of every team has inserted in its specific dictionary
# Just access the information as follow

# India's won matches
print(f'''India has won {Data_dict['Ind']['Won']} matches in Worldcup19''')

print('\n')

# Accessing the 'Eng' key in Data_dict dictionary means accessing Eng_dict dictionary
print(Data_dict['Eng'])