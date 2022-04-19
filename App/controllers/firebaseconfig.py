import pyrebase

config = {
    "apiKey": "AIzaSyDLQdpdODUrVMdsb9K32TnhkHK3oVAABQs",
    "authDomain": "info2602try2.firebaseapp.com",
    "databaseURL": "https://info2602try2-default-rtdb.firebaseio.com",
    "storageBucket": "info2602try2.appspot.com"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
