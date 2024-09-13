# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 3

def summarizetext(text):
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    paragraph = ""

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        paragraph += str(sentence)

    return paragraph

if __name__ == "__main__":
    url = "https://www.fijivillage.com/news/Police-arrest-suspect-in-Raiwaqa-murder-case-after-manhunt-5r84fx/"
    
    s = summarizetext(url=url)
    print(s)