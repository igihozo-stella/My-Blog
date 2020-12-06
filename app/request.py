import requests
from config import Config
from .models import Quotes
quotes_url=Config.QUOTES_URL

def getQuotes():
    random_quote=requests.get(quotes_url)
    new_quote=random_quote.json()
    quote=new_quote.get("quote")
    author=new_quote.get("author")
    quote_object=Quotes(quote,author)
    return quote_object
