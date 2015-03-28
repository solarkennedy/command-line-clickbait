#!/usr/bin/env python
"""Reads in a CSV of title,link and click-bait-ify's it,
also shortens the url for CLI output"""
import random
import xml.etree.ElementTree as ET


class ClickBait:
    def __init__(self):
        titles = []
        tree = ET.parse('lbgen.xml')
        root = tree.getroot()
        for child in root:
            bait_array = [x.text for x in child.getchildren()[0:4]]
            titles.append(" ".join(bait_array))
        self.titles = titles

    def baitify(self, subject):
        """Takes a subject (title) and returns a click-baity version of it"""
        title = random.choice(self.titles)
        title = title.replace("BLANK", subject)
        title = title.replace('[#]', str(random.randint(3, 10)))
        title = self.un_pluralize(title, subject)
        return title.title().replace("'S", "'s")

    def un_pluralize(self, title, subject):
        """Takes out S's, is/are based on if the subject is plural or not"""
        if self.is_plural(subject):
            title = title.replace("[is|are]", "are")
            title = title.replace("[s]", "s")
        else:
            title = title.replace("[is|are]", "is")
            title = title.replace("[s]", "")
        return title

    def is_plural(self, subject):
        """Detects if the subject is plural in a very naive way"""
        last_word = subject.split(" ")[-1]
        if last_word.endswith("s"):
            return True
        else:
            return False


def read_csv():
    """Genrator that returns tupels of title, link"""
    with open('devops.csv') as f:
        for line in f:
            yield line.strip().replace('"', '').split(',')


def shorten(url):
    """Retruns a shortened version of the url"""
    return "(%s)" % url


if __name__ == '__main__':
    cb = ClickBait()
    for title, link in read_csv():
        print cb.baitify(title), shorten(link)
