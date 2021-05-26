# Python Based Webscraper

### Project Description 
This code is a group project by Johannes Küchenhoff (johanneskuechenhoff), Carolin Schmitt (CaroSchmitt), and Manuel Zwerger (not.available) for the class "Programming with Advanced Computer Languages" by Dr Mario Silic. 
The project comprises a Python-based web scraper that extracts all articles and their respective metadata from the website `TheConversation` that fit a specific keyword and were published in a given timeframe. For example, as a keyword for this project, we chose `vaccination`, and our timeframe ranges from 1.01.2020 to 01.05.2021. However, the user can easily modify the keyword and timeframe according to his/her preferences. 
### Objective
The purpose of this web scraper is to extract data from a website. All data and information collected are then exported into the "storage_file.csv". This file provides an overview for the user of all articles that were published on "TheConversation" within the defined timeframe. After having consolidated all articles, the data can be used for further analysis, such as contextual topic identification models.
### Relevance
"TheConversation" is one of the world's largest networks for non-profit media that offers articles, commentaries, and debates on topics of politics, science, health, the environment and culture. Those articles are written by academics and researchers that are active within the specific research field and are therefore of high content quality. 
"TheConversation" has a monthly online audience of approximately 11 million users and a reach of 40 million people, including republication. This demonstrates the vast breadth and actuality that it provides compared to traditional scientific papers. For the latter, up to two years pass until a submission is eventually published, given the extensive review processes. Deductively, researchers typically prefer to use more up-to-date websites like "TheConversation" to gain a deeper understanding of current topics. Vaccination strategies, e.g. regarding COVID-19, are clearly topics in which actuality is crucial. Thus, "TheConversation" is a predestined database to get a comprehensive overview of the current state of the vaccination process.
However, due to its enormous number of articles published, it is nearly impossible for users to read all articles for a given keyword in a given timeframe. Hence, to get a good overview and thorough understanding of a particular research stream, researchers often filter for specific keywords. Our web scraper simplifies this search process for users of "TheConversation" as it automatically downloads all articles and their respective metadata related to a particular keyword. Such an algorithm eliminates the effort of downloading all papers of interest manually. The web scraper aggregates all articles and metadata which are published on "TheConversation" for a given keyword (in our case "Vaccination") in a given timeframe (in our case 01.01.2020 to 01.05.2021) into one file (in our case called "storage_file.csv"). This file will provide an overview of all relevant articles and can be utilized for further analysis, as mentioned above.
### Pre-installations required:
*``pip install os``
*``pip install python-dateutil``
*``pip install beautifulsoup4``
*``pip install langdetect``
*``pip install datetime``
*``pip install requests``
*``pip install pandas``

### Files needed:
This repository consists of two files:
+ "main.py": file imports the medium scraper and executes the web scraper
+ "conversation_scraper.py": file defines the medium scraper class

Attention: Both files must be stored in the same directory!
### How to run the code:
Open the directory where "main.py" and "conversation_scraper.py" is stored 
```
Run "main.py" in order to execute the scraper
``
Before the code can be executed, **four parameters** must be defined in advance:
+ `codeword`: keyword to search on theconversation.com (here: vaccination)
+ `storage_file`: name of the csv file the data will be stored in (here: storage_file.csv)
+ `start`: starting point from which articles are scraped and saved (here: 01-01-2020)
+ `end`: latest point from which articles are scraped and saved (here: 01-05-2021)

As a result, the csv file `storage_file.csv`, which contains all relevant articles for our keyword vaccination in our given timeframe (01.01.2020 till 01.05.2021) is saved in the same directory.

