from lxml import html
import requests

filename = 'C:\\Users\\a88719\\Documents\\Estudo\\Python\\learn-python\\NotTutorialRelated\\TBATE-Chap1.txt'

file = open(filename, 'a')

page = requests.get('http://gravitytales.com/novel/the-beginning-after-the-end/tbate-chapter-1')
tree = html.fromstring(page.content)

#This get the text of the page
text = tree.xpath('//div[@class="innerContent fr-view"]/p/text()')

file.truncate()

for i in range(0,len(text)):
    file.write(text[i].encode("utf-8") + "\n")

file.close()

# for i in text:
#     print i.encode("utf-8")

