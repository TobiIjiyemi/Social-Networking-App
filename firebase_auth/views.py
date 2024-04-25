from django.shortcuts import render
#test account pass: helloworld

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

#How to make database
#data = {"Name": "Rachel Li", "Age": 17}
#database.child("Users").child("user" + str(1)).set(data)
userNum = 1

def updateAge(user, age):
     database.child("Users").child(user).update({"Age":age})

def createUser():
     database.child("Users").child()

def signIn(request):
    return render(request,"Login.html")
def home(request):
    return render(request,"Home.html")

def postsignInGoogle(request):
  print("Ran")
 
def postsignInEmail(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please Check your Data"
        return render(request,"Login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"Home.html",{"email":email})
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")
 
def signUp(request):
    return render(request,"Registration.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)

        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)

        # add email to database
        userNum += 1
        data = {"email": email}
        database.child("Users").child("user" + str(userNum)).set(data)
     except:
        return render(request, "Registration.html")
     return render(request,"Login.html")

def reset(request):
	return render(request, "Reset.html")

def postReset(request):
	email = request.POST.get('email')
	try:
		authe.send_password_reset_email(email)
		message = "A email to reset password is successfully sent"
		return render(request, "Reset.html", {"msg":message})
	except:
		message = "Something went wrong, Please check the email you provided is registered or not"
		return render(request, "Reset.html", {"msg":message})