import feedparser
    
class Reader:
  def __init__(self, feed):
    self.feed = feed
    self.feed = self.read()

  def read(self):
    feed = feedparser.parse(self.feed)
    return feed
    

