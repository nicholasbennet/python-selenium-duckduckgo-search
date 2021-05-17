from bs4 import BeautifulSoup
from selenium import webdriver
import csv

base_url = "https://duckduckgo.com/?q="
search_queries = ["EV charging","EV charging map","EV charging app","Electric vehicle charging","Electric vehicle charging map","Electric vehicle charging app"]
link_a_list = []
for query in search_queries:
   query = query.lower()
   query = query.replace(" ","+")
   query_url = base_url+query
   print(query_url)
   driver = webdriver.Edge()
   driver.get(query_url)
   for index in range(5):
      more_btn = driver.find_element_by_class_name('result--more__btn')
      more_btn.click()
   page_source = driver.page_source
   driver.quit()
   soup = BeautifulSoup(page_source, 'html.parser')
   link_a = soup.find_all('a', class_="result__url")
   link_a_list = link_a_list + link_a
link_a_uniq = []
for link in link_a_list:
   if (link not in link_a_uniq) and (link.span != None):
      link_a_uniq.append(link)
with open('link.csv', 'w', newline='') as csvfile:
   linkwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
   for link in link_a_uniq:
      link_doamin = link.find('span', class_="result__url__domain").text
      link_link = link.get('href')
      linkwriter.writerow([link_doamin, link_link])