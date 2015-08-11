import feedparser
import PyRSS2Gen
import datetime


class FeedParser:
    @staticmethod
    def date_tuple_to_datetime(date_tuple):
        return datetime.datetime(*(date_tuple[:5])) if date_tuple else None

    @staticmethod
    def get_first(lst):
        return lst[0] if lst and len(lst) > 0 else None

    @staticmethod
    def get_terms(lst):
        if lst is None:
            return None
        return [e['term'] for e in lst]

    def get_rss_item_for_entry(self, entry):
        return PyRSS2Gen.RSSItem(
            title=entry.get('title'),
            link=entry.get('link'),
            description=entry.get('description'),
            author=entry.get('author'),
            categories=self.get_terms(entry.get('tags')),
            comments=entry.get('comments'),
            enclosure=self.get_first(entry.get('enclosures')),
            guid=entry.get('id'),
            pubDate=self.date_tuple_to_datetime(entry.get('published_parsed')),
            source=entry.get('source'),
        )

    def get_rss2_from_feed(self, feed, entries):
        return PyRSS2Gen.RSS2(
            title=feed.get('title'),
            link=feed.get('link'),
            description=feed.get('subtitle'),

            language=feed.get('language'),
            copyright=feed.get('rights'),
            managingEditor=feed.get('contributors'),
            webMaster=feed.get('publisher'),
            pubDate=self.date_tuple_to_datetime(feed.get('published_parsed')),
            lastBuildDate=self.date_tuple_to_datetime(feed.get('updated_parsed')),

            categories=self.get_terms(feed.get('tags')),
            generator=feed.get('generator'),
            docs=feed.get('docs'),
            cloud=feed.get('cloud'),
            ttl=feed.get('ttl'),

            image=feed.get('image'),
            rating=None,
            textInput=feed.get('textinput'),
            skipHours=None,
            skipDays=None,

            items=[self.get_rss_item_for_entry(entry) for entry in entries],
        )

    def parse(self, feed):
        parsed_feed = feedparser.parse(feed)
        return self.get_rss2_from_feed(parsed_feed.feed, parsed_feed.entries)
