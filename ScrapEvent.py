from lxml import html
import requests

login_url = 'http://utdpmidkijakarta.or.id/publikasi#event-agenda'
session_requests = requests.session()
result = session_requests.get(login_url)
htmlpage = html.fromstring(result.text)

#values to jsonify
class Event:
    storedEventNames = []
    storedEventPlaces = []
    storedEventAddress = []
    storedEventTimes = []
    storedEventPhotos = []

#print(result.text)

def getEvent():

    rows = htmlpage.xpath('//div[@class="row"]')[0]

    event = Event()

    event.storedEventNames.clear()
    event.storedEventPhotos.clear()
    event.storedEventAddress.clear()
    event.storedEventPlaces.clear()
    event.storedEventTimes.clear()

    #get Event Names
    eventNames = rows.xpath('.//div[@class="marg-top5"]')
    for name in eventNames:
        event.storedEventNames.append(name.text_content().lstrip().rstrip())

    #get Event Place, Address, Time
    eventPlace = rows.xpath('.//div[@class="avenir14 marg-top5"]')
    for item in eventPlace:
        Tempat = item.text_content().find('Tempat : ')
        TempatEnd= Tempat + 9
        Alamat = item.text_content().find('Alamat : ')
        AlamatEnd = Alamat + 9
        Waktu = item.text_content().find('Waktu : ')
        WaktuEnd = Waktu + 8

        event.storedEventPlaces.append(item.text_content()[TempatEnd:Alamat-1].lstrip().rstrip())
        event.storedEventAddress.append(item.text_content()[AlamatEnd:Waktu-1].lstrip().rstrip())
        event.storedEventTimes.append(item.text_content()[WaktuEnd:].lstrip().rstrip())

    #get Event Photos
    eventPhotos = rows.xpath('.//div[@class="col-md-4 no-padding sm-foto-content"]/a/img')
    for item in eventPhotos:
        event.storedEventPhotos.append(item.attrib['src'])

    return event
    #print (storedEventNames)
    #print (storedEventPlaces)
    #print (storedEventAddress)
    #print (storedEventTimes)
    #print (storedEventPhotos)
