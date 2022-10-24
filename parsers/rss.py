import feedparser as fp
from bs4 import BeautifulSoup


def parse_electrek():
    url = 'https://electrek.co/feed/'
    electrek = fp.parse(url)
    electrek_titles = [x['title'] for x in electrek['entries']]
    electrek_stories = [BeautifulSoup(x['summary'], features='html.parser').text for x in electrek['entries']]

    print(electrek_stories[1])


