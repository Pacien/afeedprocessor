import PyRSS2Gen

from afeedprocessor.adescription import Description


class ItemProcessor:
    def get_title(self, title, item):
        return title

    def get_link(self, link, item):
        return link

    def get_description(self, description, item):
        return description

    def get_author(self, author, item):
        return author

    def get_categories(self, categories, item):
        return categories

    def get_comments(self, comments, item):
        return comments

    def get_enclosure(self, enclosure, item):
        return enclosure

    def get_guid(self, guid, item):
        return guid

    def get_pub_date(self, pub_date, item):
        return pub_date

    def get_source(self, source, item):
        return source

    def process(self, item: PyRSS2Gen.RSSItem):
        return PyRSS2Gen.RSSItem(
            title=self.get_title(item.title, item),
            link=self.get_link(item.link, item),
            description=Description(self.get_description(item.description, item)),
            author=self.get_author(item.author, item),
            categories=self.get_categories(item.categories, item),
            comments=self.get_comments(item.comments, item),
            enclosure=self.get_enclosure(item.enclosure, item),
            guid=self.get_guid(item.guid, item),
            pubDate=self.get_pub_date(item.pubDate, item),
            source=self.get_source(item.source, item)
        )
