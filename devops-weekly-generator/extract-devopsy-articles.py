#!/usr/bin/env python
import feedparser
from bs4 import BeautifulSoup


def extract_links(p_list):
    """Takes in a list of paragraphs and returns a list of all the links """
    links = []
    for p in p_list:
        links.extend(p.find_all('a'))
    return links


def extract_news_links(html):
    """ Takes in devops weekly html and gets news links out """
    soup = BeautifulSoup(content)
    links = []
    h1s = soup.find_all('h1')
    for h1 in h1s:
        if h1.text == 'News':
            links.extend(extract_links(h1.findNextSiblings('p')))
    return links


def extract_human_words(link):
    url = link.text.split('?')[0]
    url = url.split('.html')[0]
    url = url.split('.php')[0]
    if url.endswith('/'):
        last_part = url.split('/')[-2]
    else:
        last_part = url.split('/')[-1]
    return last_part.replace('-', ' ')


def link_is_baity(link):
    """ Tries to guess if a link is baity. Baity links are those links
    that have multi part words, like
    http://www.syslog.cl.cam.ac.uk/2014/11/25/new-directions-in-operating-systems/
    """
    url = link.text.split('?')[0]
    url = url.split('.html')[0]
    if url.endswith('/'):
        last_part = url.split('/')[-2]
    else:
        last_part = url.split('/')[-1]
    return last_part.count('-') > 3


if __name__ == '__main__':
    feed = feedparser.parse('devops.xml')
    for entry in feed['entries']:
        content = entry['content'][0]['value']
        for link in extract_news_links(content):
            if link_is_baity(link):
                print '"%s","%s"' % (extract_human_words(link), link.text)
