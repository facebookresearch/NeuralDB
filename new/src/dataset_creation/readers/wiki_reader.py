import xml.sax
import logging
logger = logging.getLogger(__name__)

class WikiReader(xml.sax.ContentHandler):
    def __init__(self,filter_namespace,article_callback,redirect_callback):
        super().__init__()
        logger.debug("Init WikiReader")

        self.stack = []
        self.text = None
        self.title = None
        self.redirTarget = None
        self.ns = 0

        self.num_articles = 0
        self.num_redirects = 0
        self.tick = 0

        self.filter_namespace = filter_namespace
        self.article_callback = article_callback
        self.redirect_callback = redirect_callback

    def startElement(self, name, attributes):
        if name == "ns":
            assert self.stack == ["page"]
            self.ns = 0
        elif name == "page":
            assert self.stack == []
            self.text = None
            self.title = None
            self.redirTarget = None
        elif name == "title":
            assert self.stack == ["page"]
            assert self.title is None
            self.title = ""
        elif name == "text":
            assert self.stack == ["page"]
            assert self.text is None

            if self.redirTarget is not None:
                return
            self.text = ""
        elif name == "redirect":
            assert self.stack == ["page"]
            assert self.redirTarget is None
            assert self.title is not None
            self.redirTarget = attributes['title']
        else:
            assert len(self.stack) == 0 or self.stack[-1] == "page"
            return

        self.stack.append(name)

    def endElement(self, name):
        if len(self.stack) > 0 and name == self.stack[-1]:
            del self.stack[-1]

        if self.filter_namespace(self.ns):
            if self.redirTarget is None and name == "text":
                self.num_articles += 1
                self.article_callback(self.title, self.text)
            elif name == "redirect":
                self.num_redirects += 1
                self.redirect_callback(self.title,self.redirTarget)

    def characters(self, content):
        assert content is not None and len(content) > 0
        if len(self.stack) == 0:
            return

        if "redirect" not in self.stack:
            if self.stack[-1] == "text":
                assert self.title is not None
                self.text += content
                logger.debug("Set text to string[{0}]".format(len(self.text)))

        if self.stack[-1] == "title":
            self.title += content
            logger.debug("Set title to {0}".format(self.title))

        if self.stack[-1] == "ns":
            self.ns += int(content)
            logger.debug("Set ns to {0}".format(self.ns))
