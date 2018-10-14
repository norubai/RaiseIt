import urllib
import os
MONGO = {
    'USERNAME': os.environ['MONGO_USERNAME'],
    'PASSWORD': urllib.parse.quote(os.environ['MONGO_PASSWORD']),
    'HOSTPORT': os.environ['MONGO_HOSTPORT'],
    'DATABASE': os.environ['MONGO_DATABASE']
}
MONGO_URI = "mongodb://%s:%s@%s/%s" % (MONGO['USERNAME'], MONGO['PASSWORD'], MONGO['HOSTPORT'], MONGO['DATABASE'])

TWILIO = {
    'ACCOUNT_SID': os.environ['TWILIO_ACCOUNT_SID'],
    'AUTH_TOKEN': os.environ['TWILIO_AUTH_TOKEN'],
    'PHONE_NUMBER': os.environ['TWILIO_PHONE_NUMBER']
}
