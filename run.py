
import mangakatana as mankat

result = mankat.search(title="Naruto")

first = result[0]

print(first.title, first.url, first.status, sep=" | ")

for chapter in first.chapter_list():
	print(chapter.num, chapter.title, chapter.url, sep=" | ")
