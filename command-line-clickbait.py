#!/usr/bin/env python
"""Reads in a CSV of title,link and click-bait-ify's it,
also shortens the url for CLI output"""
import os
import random
import xml.etree.ElementTree as ET


class ClickBait:
    def __init__(self):
        titles = []
        local_dir = os.path.dirname(os.path.realpath(__file__))
        tree = ET.parse(os.path.join(local_dir, 'lbgen.xml'))
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
        title = title.title()
        title = title.replace("'S", "'s")
        title = title.replace("'T", "'t")
        return title

    def un_pluralize(self, title, subject):
        """Takes out S's, is/are based on if the subject is plural or not"""
        if self.is_plural(subject):
            title = title.replace("[is|are]", "are")
            title = title.replace("[it|they]", "they")
            title = title.replace("[isn't|aren't]", "are't")
            title = title.replace("[s]", "s")
            title = title.replace("[s2]", "s")
        else:
            title = title.replace("[is|are]", "is")
            title = title.replace("[it|they]", "it")
            title = title.replace("[isn't|aren't]", "isn't")
            title = title.replace("[s]", "")
            title = title.replace("[s2]", "")
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
    local_dir = os.path.dirname(os.path.realpath(__file__))
    csv_filename = os.path.join(local_dir, 'clickbait.csv')
    with open(csv_filename) as f:
        for line in f:
            yield line.strip().replace('"', '').split(',')


def blue(text):
    return "\033[36m%s\033[0m" % text


if __name__ == '__main__':
    cb = ClickBait()
    links = list(read_csv())
    print "Users who ran that command also liked:"
    for i in xrange(3):
        title, link = random.choice(links)
        print '  %s: %s' % (cb.baitify(title), blue(link))
