import string
import dataclasses

from bs4 import BeautifulSoup

from mangakatana import siterequests
from mangakatana.chapterlist import ChapterList


@dataclasses.dataclass(frozen=True)
class SearchResult:
	title: str
	url: str

	def chapter_list(self):
		return ChapterList(self.url).get()

	@classmethod
	def create_from_soup(cls, soup):
		return cls(
			title=soup.find("h3", class_="title").find("a").text,
			url=soup.find("h3", class_="title").find("a").get("href")
		)


def perform_search(title):
	allowed_characters: str = string.ascii_letters + string.digits + "_+"

	title = "".join([char for char in title.replace(" ", "+") if char in allowed_characters]).lower()

	r = siterequests.search(title)

	soup = BeautifulSoup(r.content, "html.parser")

	return [SearchResult.create_from_soup(ele) for ele in soup.find_all("div", class_="item")]
