class Description:
    def __init__(self, description):
        self.tag = 'description'
        self.description = description

    def is_cdata(self):
        if self.description is None:
            return False

        return self.description.startswith('<![CDATA[') and self.description.endswith(']]>')

    def publish(self, handler):
        handler.startElement(self.tag, {})

        if self.description is not None:
            if self.is_cdata():
                handler._write(self.description)
            else:
                handler.characters(self.description)

        handler.endElement(self.tag)
