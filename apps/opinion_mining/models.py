from django.db import models
from djongo.models import fields

#Holds Opinion Mining Results
class OpinionMiningResult(models.Model):
    _id = fields.ObjectIdField()
    aspectStats = models.TextField()                #Holds opinion mining results according to device aspects (in JSON form)
    deviceName = models.TextField(default="noName") #Holds the device brand and model
    reportDate = models.TextField(default="noDate") #Holds date report was generated
    textCount = models.IntegerField()               #Holds the total number of comments included in the analysis
    companyName = models.TextField()


#Holds tester comments on devices
class Comment(models.Model):
    _id = fields.ObjectIdField()
    testerId = models.TextField()                   #Holds the id of the tester
    deviceName = models.TextField()                 #Holds brand and model of the device
    testDate = models.TextField()                   #Holds the date test occured
    content = models.TextField()                    #The comment text itself
    sentenceCount = models.IntegerField()           #Total number of sentences in the test text
    wordCount = models.IntegerField()               #Total number of words in the test text
    positiveWordCount = models.IntegerField()       #Total number positive of words in the test text
    negativeWordCount = models.IntegerField()       #Total number of negative words in the test text
    companyName = models.TextField()


#Responsible for tracking the device model related information
class Product(models.Model):
    _id = fields.ObjectIdField()
    deviceName = models.TextField(default="noName")                         #Holds the device brand and model
    checkpoint = models.TextField()                                         #Holds the id of the checkpoint comment
    prevCount = models.IntegerField()                                       #Holds the number of comments previously in MongoDB with deviceName
    companyName = models.TextField()
