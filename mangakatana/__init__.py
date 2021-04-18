
def search(*, title: str):
	from mangakatana.mangasearch import MangaSearch

	return MangaSearch(title).get()


def chapter_list(*, url: str):
	from mangakatana.chapterlist import ChapterList

	return ChapterList(url).get()
