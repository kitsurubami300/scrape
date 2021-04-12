import re
import functools as ft

import requests

from bs4 import BeautifulSoup


class Chapter:
	def __init__(self, soup):
		self._soup = soup

	@ft.cached_property
	def title(self): return self._soup.find("a").text

	@ft.cached_property
	def url(self): return self._soup.find("a")["href"]

	@ft.cached_property
	def num(self):
		return float(re.search("[\d\.\d]+", self.title).group())


class ChapterList:
	def __init__(self, url):
		self.url = url

	@ft.lru_cache()
	def get(self):
		page_soup = BeautifulSoup(requests.get(url=self.url).content, "html.parser")

		return [Chapter(tr) for tr in page_soup.find_all("tr")][::-1]
