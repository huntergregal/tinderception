import requests
import uuid

def request(context, flow):
        request = flow.request
        if(request.host == "api.gotinder.com" or request.host == "images.gotinder.com" or request.host == "api.crittercism.com" and x == 1):
                url = "http://"  + request.host + request.path
                print "REQUEST TO: " + url
def response(context, flow):
        response = flow.response
        if (response.request.host == "api.gotined.com" or response.request.host == "images.gotinder.com"):
                print "RESPONSE FROM: " + response.request.scheme + "://" + response.request.host + response.request.path
                responseFILE = "./photos/response" + str(uuid.uuid4())
                foo = open(responseFILE, "w+")
                print >> foo, response.content
def start(context, argv):
        print 'Starting...'

