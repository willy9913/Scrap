from flask import Flask, jsonify, abort, make_response, request, render_template

#for Event
import ScrapEvent

#for News
import ScrapNews

app = Flask(__name__)

@app.route('/event', methods=['GET'])
def get_profile():
    Event = ScrapEvent.getEvent()

    itemSize = len(Event.storedEventNames)

    jsonEvent={}
    jsonEvent.clear()

    EventBucket=[]

    for i in range(1, itemSize + 1):
        jsonEvent['name'] = Event.storedEventNames[i - 1];
        jsonEvent['place'] = Event.storedEventPlaces[i - 1];
        jsonEvent['time'] = Event.storedEventTimes[i - 1];
        jsonEvent['address'] = Event.storedEventAddress[i - 1];
        jsonEvent['photo'] = Event.storedEventPhotos[i - 1];

        EventBucket.append(jsonEvent.copy())
        jsonEvent.clear()

    #a
    lastOut={}
    lastOut.clear()

    lastOut['obj']=EventBucket

    return jsonify(EventBucket)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)