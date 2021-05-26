#----------------------------------------------------------------------------------------------------------
# Task:     The following searches through all articles on the website The Conversation for the codeword 
#           "vaccination" and loads these into a file, allowing the user to get an easy and quick 
#           overview of the current situation of vaccination. 
#  
# Date:     1 May 2021
# Author:   Carolin Schmitt, Johannes Küchenhoff, Manuel Zwerger 
#----------------------------------------------------------------------------------------------------------
# 0. Setup - Importing libraries 
#----------------------------------------------------------------------------------------------------------
import csv
import time
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from _datetime import datetime as dt

#----------------------------------------------------------------------------------------------------------
# 1. Main Code - Consisting of separate functions  
#----------------------------------------------------------------------------------------------------------
class conversationScraper:

    # Assign input data to instance of function
    def __init__(self,codeword,storage_file,start,end):
        self.codeword = codeword
        self.start = dt.strptime(start, '%d-%m-%Y').date()
        self.end = dt.strptime(end, '%d-%m-%Y').date()
        self.storage_file = storage_file

    # Take a DataFrame with the article information and append it to csv file
    def save_article(self, article):
        csv_columns = ['date', 'title', 'text']
        print('............................')
        with open(self.storage_file, 'a', encoding='UTF-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter='|')
            writer.writerow(article)
            csvfile.close()

    # Open file if existent, otherwise creates new file
    def create_file(self):
        try:
            f = open(self.storage_file)
            f.close()
        except IOError:
            csv_columns = ['date', 'title', 'text']
            with open(self.storage_file, 'a', encoding='UTF-8', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter='|')
                writer.writeheader()
                csvfile.close()

    # Iterate through urls and extract article metadata and full text 
    def get_articles(self, init_soup):
        results = init_soup.findAll('div', {'id': 'content-results'})
        for i in range(1, len(results[0].contents)-3, 2):
            try:
                date = parse(results[0].contents[i].contents[1].contents[1].contents[1].attrs['datetime']).date()
            except AttributeError:
                date = 'No date available'
            try:
                title = results[0].contents[i].contents[1].contents[1].contents[3].contents[1].attrs['title']
                print(str(date) + ' ' + title)
            except AttributeError:
                title = 'No title'
            try:
                href = results[0].contents[i].contents[1].contents[1].contents[3].contents[1].attrs['data-original-href']
                link = 'https://theconversation.com' + href
                data = requests.get(link)
                soup = BeautifulSoup(data.content, 'html.parser')
                tags = soup.findAll('div', {'itemprop': 'articleBody'})
                try:
                    text = ''
                    for k in range(1, len(tags[0].contents), 2):
                        text += tags[0].contents[k].text + ' '
                    text = text.replace('\n', '')
                except AttributeError:
                    text = 'No text available'
            except AttributeError:
                link = 'No link'
                text = 'No text available'
            article = {'date': date,
                       'title': title,
                       'text': text,}
            self.save_article(article)
            time.sleep(1)

    # Scrape all relevenant articles
    def scrape(self):
        # Create url for respective archive page on The Conversation website
        url = 'https://theconversation.com/global/search?q=' + self.codeword + \
              '&sort=recency&language=en&' + \
              'date=custom&date_from=%s' % self.start + \
              '&date_to=%s' % self.end
        print(url)
        # Get HTML data 
        data = requests.get(url)
        # Identify content and scrape information from webpage
        soup = BeautifulSoup(data.content, 'html.parser')
        check = soup.findAll(soup.findAll('div', {'class': 'error'}))
        try:
            if len(check.source.name[0].contents) > 0:
                print(check.source.name[0].text.strip())
        except IndexError:
            self.get_articles(soup)
            # Search through archive
            more_results = True
            page = 2
            while more_results is True:
                url = 'https://theconversation.com/global/search?q=%s' % self.codeword + \
                      '&sort=recency&language=en&' + \
                      'date=custom&date_from=%s' % self.start + \
                      '&date_to=%s' % self.end + \
                      '&page=%s' % page
                data = requests.get(url)
                soup = BeautifulSoup(data.content, 'html.parser')
                check = soup.findAll(soup.findAll('div', {'class': 'error'}))
                try:
                    if len(check.source.name[0].contents) > 0:
                        more_results = False
                        print(check.source.name[0].text.strip() + 'on page %s' % str(page))
                except IndexError:
                    self.get_articles(soup)
                page += 1
        return print('Scraping done')


#----------------------------------------------------------------------------------------------------------
# 2. Execution - Executes the main functions 
#----------------------------------------------------------------------------------------------------------
    def run(self):
        
        # Check file name includes extention .csv, if not, add it. 
        if len(self.storage_file.split('.')) == 1:
            self.storage_file += '.csv'

        # Create file and start scraping
        self.create_file()
        self.scrape()

        # Remove all duplicates
        print('Removing duplicates')
        df = pd.read_csv(self.storage_file, self.storage_file, delimiter='|')
        len1 = len(df)
        df = df.drop_duplicates(subset=['text'])
        len2 = len1 - len(df)
        df.to_csv(self.storage_file, sep='|', index=False)
        print('Dropped %s duplicates' % str(len2))