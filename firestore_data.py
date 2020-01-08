import firebase_admin
from firebase_admin import credentials, firestore
import RPi.GPIO as GPIO
import relay_solenoid as relay

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def add_history(unlock_method):
    data = {
        u'openedBy': unlock_method,
        u'time': firestore.SERVER_TIMESTAMP
    }
    db.collection(u'access_history').add(data)

def get_password():    
    doc_ref = db.collection('smartdoor').document('password')
    try:
        doc = doc_ref.get()
    #     print('Document data: {}'.format(doc.to_dict()))
        password = str(doc.to_dict().get("pin"))

    except Exception as e:
        print('No such document!')
    
    return password

def check_pin(pin):
    if pin == get_password():
        return True
    else:
        return False

def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(u'Received document snapshot: {}'.format(doc.id))
        lock_status = doc_ref.get().to_dict()['locked']
        print(lock_status)
        if not lock_status:
            relay.unlock(21)
            doc_ref.set({
                u'locked': True},
                merge=True)
        
         
doc_ref = db.collection(u'smartdoor').document(u'status')
lock_status = True

# Watch the document
doc_watch = doc_ref.on_snapshot(on_snapshot)