import pyrebase

config = {
    #Place firebase config here
}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
