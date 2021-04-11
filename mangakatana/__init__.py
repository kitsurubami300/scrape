
def search(*, title: str):
	from bs4 import BeautifulSoup

	from mangakatana import siterequests
	from mangakatana.searchresult import SearchResult

	r = siterequests.search(title=title)

	soup = BeautifulSoup(r.content, "html.parser")

	entries = soup.find_all("div", class_="item")

	return [SearchResult(e) for e in entries]


def chapter_list(*, url: str):
	from mangakatana import utils

	return utils.chapters_from_url(url)


__ALL__ = (
	"search",
	"chapteR_list"
)
