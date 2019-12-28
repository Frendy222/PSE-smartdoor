import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import RPi.GPIO as GPIO
import time

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

doc_ref = firestore_client.collection('smartdoor').document('status')
doc = doc_ref.get()
