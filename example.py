#!/usr/bin/env python3

from afeedprocessor.anitemprocessor import ItemProcessor
from afeedprocessor.afeedprocessor import FeedProcessor
from afeedprocessor.afeedparser import FeedParser


class HackerNewsItemProcessor(ItemProcessor):
    def get_title(self, title, item):
        return title.replace('Alphabet', 'Evil Corp')

    def get_description(self, description, item):
        return description  # actually fetching and modifying the description is left as an exercise for the reader.


class HackerNewsFeedProcessor(FeedProcessor):
    def get_title(self, title, feed):
        return 'Hacked News'

    def get_description(self, description, feed):
        return description.replace('readers', 'hackers')


if __name__ == '__main__':
    feed_url = 'http://news.ycombinator.com/rss'
    feed = FeedParser().parse(feed_url)

    processor = HackerNewsFeedProcessor(HackerNewsItemProcessor())
    processed_feed = processor.process(feed)

    feed_string = processed_feed.to_xml()
    print(feed_string)
