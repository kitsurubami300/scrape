
import mangakatana as mankat

result = mankat.search(title="Naruto")

first = result[0]

print(first.title, first.url)

for chapter in first.chapter_list():
	print(chapter.chapter, chapter.title, chapter.url)
