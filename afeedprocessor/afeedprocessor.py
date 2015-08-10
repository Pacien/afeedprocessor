import PyRSS2Gen

from afeedprocessor.anitemprocessor import ItemProcessor


class FeedProcessor:
    def __init__(self, item_processor: ItemProcessor=None):
        if item_processor is None:
            self.item_processor = ItemProcessor()
        else:
            self.item_processor = item_processor

    def get_title(self, title, feed):
        return title

    def get_link(self, link, feed):
        return link

    def get_description(self, description, feed):
        return description

    def get_language(self, language, feed):
        return language

    def get_copyright(self, copyright, feed):
        return copyright

    def get_managing_editor(self, managing_editor, feed):
        return managing_editor

    def get_web_master(self, web_master, feed):
        return web_master

    def get_pub_date(self, pub_date, feed):
        return pub_date

    def get_last_build_date(self, last_build_date, feed):
        return last_build_date

    def get_categories(self, categories, feed):
        return categories

    def get_generator(self, generator, feed):
        return generator

    def get_docs(self, docs, feed):
        return docs

    def get_cloud(self, cloud, feed):
        return cloud

    def get_ttl(self, ttl, feed):
        return ttl

    def get_image(self, image, feed):
        return image

    def get_rating(self, rating, feed):
        return rating

    def get_text_input(self, text_input, feed):
        return text_input

    def get_skip_hours(self, skip_hours, feed):
        return skip_hours

    def get_skip_days(self, skip_days, feed):
        return skip_days

    def get_items(self, items, feed):
        return [self.item_processor.process(item) for item in items]

    def process(self, feed: PyRSS2Gen.RSS2):
        return PyRSS2Gen.RSS2(
            title=self.get_title(feed.title, feed),
            link=self.get_link(feed.link, feed),
            description=self.get_description(feed.description, feed),
            language=self.get_language(feed.language, feed),
            copyright=self.get_copyright(feed.copyright, feed),
            managingEditor=self.get_managing_editor(feed.managingEditor, feed),
            webMaster=self.get_web_master(feed.webMaster, feed),
            pubDate=self.get_pub_date(feed.pubDate, feed),
            lastBuildDate=self.get_last_build_date(feed.lastBuildDate, feed),
            categories=self.get_categories(feed.categories, feed),
            generator=self.get_generator(feed.generator, feed),
            docs=self.get_docs(feed.docs, feed),
            cloud=self.get_cloud(feed.cloud, feed),
            ttl=self.get_ttl(feed.ttl, feed),
            image=self.get_image(feed.image, feed),
            rating=self.get_rating(feed.rating, feed),
            textInput=self.get_text_input(feed.textInput, feed),
            skipHours=self.get_skip_hours(feed.skipHours, feed),
            skipDays=self.get_skip_days(feed.skipDays, feed),
            items=self.get_items(feed.items, feed)
            # Hurray for code generation!
        )
