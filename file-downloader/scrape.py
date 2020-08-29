#! python3

import requests
from html.parser import HTMLParser

def get_page_download_links(url):
    html = requests.get(url).text
    downloads = {}

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            d = dict(attrs)
            if tag == 'a' and 'href' in d:
                self.tag = tag
                self.link = d['href']

        def handle_data(self, data):
            if ('Python Cheat Sheet' in data):
                self.name = data

        def handle_endtag(self, tag):
            if hasattr(self, 'name') and hasattr(self, 'link') and not self.name in downloads:
                downloads[self.name] = getattr(self, 'link')


    parser = MyHTMLParser()
    parser.feed(html)

    return downloads


# address = 'https://ehmatthes.github.io/pcc_2e/cheat_sheets/cheat_sheets/'
# html = requests.get(address).text

# downloads = {}


# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         d = dict(attrs)
#         if tag == 'a' and 'href' in d:
#             self.tag = tag
#             self.link = d['href']

#     def handle_data(self, data):
#         if ('Cheat Sheet' in data):
#             self.name = data

#     def handle_endtag(self, tag):
#         if hasattr(self, 'name') and hasattr(self, 'link') and not self.name in downloads:
#             downloads[self.name] = getattr(self, 'link')



# parser = MyHTMLParser()
# parser.feed(html)