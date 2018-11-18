import Scrap
from flask import jsonify

Event = Scrap.getEvent()

jsonEvent={}

EventBucket = {}

itemSize = len(Event.storedEventNames)
Output = '[ '

for i in range(1, itemSize + 1):
    jsonEvent['name'] = Event.storedEventNames[i - 1];
    jsonEvent['place'] = Event.storedEventPlaces[i - 1];
    jsonEvent['time'] = Event.storedEventTimes[i - 1];
    jsonEvent['address'] = Event.storedEventAddress[i - 1];
    jsonEvent['photo'] = Event.storedEventPhotos[i - 1];

    EventBucket['A'+str(i)] = jsonEvent
    #EventBucket[i-1]=jsonify(jsonEvent)

#print(EventBucket)


#this is how to add dictionary
#jsonEvent['asd']='asd'

jsonEvent.clear()

print(jsonEvent.items())

#print(jsonEvent)
