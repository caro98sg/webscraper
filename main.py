# 1.1 Importing libraries
from conversation_scraper import conversationScraper
import os

# 1.2 Set working directory
#os.chdir('./Desktop/')

# 1.3 Set codeword and time period for search and define in which file to store the data (storage_file)
codeword = 'vaccination'
storage_file = 'storage_file'
start = '01-01-2020'
end = '01-05-2021'

# 1.4 Start scraping by running the function "run" of the class "ConversationScraper"
cs = conversationScraper(codeword, storage_file, start, end)
cs.run()


# 1.5 Individualisation Option: If you would like to set the codeword, storage file, start or end yourself,
# de-comment this part of the code, and put into comments the four lines under  1.3
#----------------------------------------------------------------------------------------------------------
# codeword = (input('Tag:\n')).replace(' ', '+').lower()
# storage_file = input('File name:\n')
# start = dt.strptime(input('Start date (YYYY-MM-DD):'), '%Y-%m-%d').date()
# end = dt.strptime(input('End date (YYYY-MM-DD):'), '%Y-%m-%d').date()
#----------------------------------------------------------------------------------------------------------
