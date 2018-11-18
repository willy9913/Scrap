from lxml import html
import requests

login_url = 'http://utdpmidkijakarta.or.id/publikasi/berita'
session_requests = requests.session()
result = session_requests.get(login_url)
htmlpage = html.fromstring(result.text)


#values to jsonify
class News:
    storedNewsTitles = []
    storedNewsDates = []
    storedNewsPhotos = []
    storedNewsLinks = []

def getNews():

    rows = htmlpage.xpath('//div[@class="row"]')[0]

    news = News()

    news.storedNewsTitles.clear()
    news.storedNewsPhotos.clear()
    news.storedNewsDates.clear()
    news.storedNewsLinks.clear()

    #get News Title
    newsTitles = rows.xpath('.//div[@class="marg-top5"]')
    for titles in newsTitles:
        news.storedNewsTitles.append(titles.text_content().lstrip().rstrip())

    #get News Photos
    newsPhotos = rows.xpath('.//div[@class="col-md-4 no-padding sm-foto-content"]/a/img')
    for item in newsPhotos:
        news.storedNewsPhotos.append(item.attrib['src'])

    # get News Dates
    newsDates = rows.xpath('.//div[@class="date-part avenir14"]')
    for item in newsDates:
        news.storedNewsDates.append(item.text_content().lstrip().rstrip())

    # get News Link
    newsLinks = rows.xpath('.//div[@class="col-md-4 no-padding sm-foto-content"]/a')
    for item in newsLinks:
        news.storedNewsLinks.append(item.attrib['href'])


    return news

