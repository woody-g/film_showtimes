#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:38:39 2024

@author: george.wood
"""

from pathlib import Path

import scrapy

class BfiSpider(scrapy.Spider):
    name = "bfi"
    allowed_domains = ['whatson.bfi.org.uk/Online']
    start_urls = [
        'https://whatson.bfi.org.uk/Online/article/filmsindex',
    ]

            
    def parse(self, response):
        
        movie_names = response.css('.article-body-container li a::text').extract()
        for movie_name in movie_names:
            yield {
                'name': movie_name
                }