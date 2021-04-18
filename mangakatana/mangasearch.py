import string

import functools as ft

from bs4 import BeautifulSoup

from mangakatana import siterequests
from mangakatana.chapterlist import ChapterList


class SearchResult:
	def __init__(self, soup):
		self._soup = soup

	@ft.cached_property
	def title(self) -> str: return self._soup.find("h3", class_="title").find("a").text

	@ft.cached_property
	def status(self) -> str: return self._soup.find("div", class_="status completed uk-hidden-small").text.strip()

	@ft.cached_property
	def url(self) -> str: return self._soup.find("h3", class_="title").find("a").get("href")

	@ft.lru_cache()
	def chapter_list(self): return ChapterList(self.url).get()


class MangaSearch:
	def __init__(self, title: str):
		self._raw_title = title

	def get(self):
		r = self._send_request()

		return self._extract_response(r)

	def _send_request(self):
		return siterequests.search(self._validate_title(self._raw_title))

	def _extract_response(self, resp) -> list:
		soup = BeautifulSoup(resp.content, "html.parser")

		return [SearchResult(ele) for ele in soup.find_all("div", class_="item")]

	@staticmethod
	def _validate_title(title: str) -> str:
		allowed_characters: str = string.ascii_letters + string.digits + "_"

		return "".join([char.lower() for char in title.replace(" ", "_") if char in allowed_characters])
