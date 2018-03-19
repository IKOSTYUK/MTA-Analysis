# MTA-Project
MTA Turnstile Data Analysis

Included are the three scripts used to download, read, and analyze the MTA turnstile data:

http://web.mta.info/developers/turnstile.html

The download.py file downloads all .csv files between a specified date range and saves them as individual csv files locally. The read.py file reads in all of the .csv files in the folder to create one datafram from which any station can be filtered.
the analyze.py file is then used to clean up the data and calculate actual entries from the cummulative entries provided. 

Inspiration for this project came from Metis: Project Benson and other github users who have tackled this analysis! 

https://github.com/jkeung/MTA_Analysis/tree/master/clean_data
http://piratefsh.github.io/projects/2015/10/03/mta-subway-turnstile-data.html
https://github.com/floofydugong/Metis-Projects/blob/master/Project_Benson/Benson_Team5_Analysis.ipynb

special mention:
https://arettines.com/tag/mta/

