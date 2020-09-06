#Use this to configure functions to make calls to Google Firebase

from Student import Student
import firebase_admin
import json
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("howdy-hack-firebase-adminsdk-yeun6-f6e2df0815.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://howdy-hack.firebaseio.com"
})

#Returns a list of Student
def getStudents(checkpoint):#objects at the specified checkpoint
    ref = db.reference(checkpoint)
    result = ref.get()
    if result:
        students = []
        for key, value in result.items():
            students.append(Student(key, value))
        return students
    else:
        return []

def pushStudent(checkpoint, name, email):
#Adds a student to the checkpoint
    ref = db.reference(checkpoint)
    ref.update({
        name: email
    })

def removeStudent(checkpoint, name):
#Removes student from checkpoint
    ref = db.reference(checkpoint)
    result = ref.get()
    if result:
        newDict = {}
        for key, value in result.items():
            if not key == name:
                newDict.update({key: value})
        ref.set(newDict)

def AddChat(number, checkpoint, name, message):
    # Adds a student to the checkpoint
    if message:
        chatboxdbname = checkpoint + "_chat"
        entry = name + ": " + message
        ref = db.reference(chatboxdbname)
        numbe = str(number)
        ref.push(entry)

def getChats(checkpoint):#objects at the specified checkpoint
    chatdb = checkpoint + "_chat"
    ref = db.reference(chatdb)
    result = ref.get()
    if result:
        chats = []
        for key, value in result.items():
            chats.append(value)
        return chats
    else:
        return []



