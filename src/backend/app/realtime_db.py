import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase App
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://<your-database-name>.firebaseio.com"
})

# Example function to set data
def set_data(path, data):
    ref = db.reference(path)
    ref.set(data)

# Example function to get data
def get_data(path):
    ref = db.reference(path)
    return ref.get()
