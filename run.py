
import mangakatana as mankat

result = mankat.search(title="Naruto")

second = result[1]

print(second.title, second.url, second.status, sep=" | ")

for chapter in second.chapter_list():
	print(chapter.title, chapter.url, sep=" | ")
