import firebase_admin
from firebase_admin import credentials, firestore

# Replace 'path/to/your/serviceAccountKey.json' with the path to your Firebase service account key file
cred = credentials.Certificate('crash-project-cp-firebase-adminsdk-o09cn-621bb0a2f5.json')
firebase_admin.initialize_app(cred)

# Create a Firestore client
db = firestore.client()

# Function to load documents from Firestore and store them in a list
class fire():
    predict_doc = None

    def set_user(self, index,name):
        collection_ref = db.collection(name)
        docs = collection_ref.stream()
        documents = [doc for doc in docs]
        self.predict_doc = documents[index]

    def load_documents(self):
        document_list = []
        try:
            # Get a reference to the collection
            document_list.append(self.predict_doc.to_dict())
            return document_list

        except Exception as e:
            print(f"Error loading documents: {e}")
            raise e
    def write(self,field,predicted_value):
        collection = db.collection("Predictions").document("Fr1xkFiUHtewDI3844N0P6gTcar2")
        collection.update({field:predicted_value})

