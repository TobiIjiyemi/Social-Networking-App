from django.shortcuts import render

# Create your views here.
import pyrebase
 
config={
  "apiKey": "AIzaSyD28otVLAP-g3GL_Avt4uS8TyhWqoiU8bY",
  "authDomain": "socialapp-34c1e.firebaseapp.com",
  "databaseURL": "https://socialapp-34c1e-default-rtdb.firebaseio.com",
  "projectId": "socialapp-34c1e",
  "storageBucket": "socialapp-34c1e.appspot.com",
  "messagingSenderId": "48387053736",
  "appId": "1:48387053736:web:27ca5f78b748529ddcca9d",
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()


def home(request):
    userNum = (database.child('User').get().val())
    return render(request,"home.html",{"userNum":userNum})