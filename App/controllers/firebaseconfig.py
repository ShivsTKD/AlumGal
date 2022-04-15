import pyrebase

config = {
    "apiKey": "AIzaSyC3sPkuDMYh-RYI49P8jwg01YxgXE8jK_E",
    "authDomain": "info-2602-group-project-16232.firebaseapp.com",
    "databaseURL": "https://info-2602-group-project-16232-default-rtdb.firebaseio.com",
    "storageBucket": "info-2602-group-project-16232.appspot.com",
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
