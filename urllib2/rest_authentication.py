#! /usr/bin/python
import urllib2

theurl = 'https://localhost:8089/services'
username = 'admin'
password = 'changefd'

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, theurl, username, password)
# because we have put None at the start it will always
# use this username/password combination for  urls
# for which `theurl` is a super-url

authhandler = urllib2.HTTPBasicAuthHandler(passman)

opener = urllib2.build_opener(authhandler)
pagehandle = urllib2.install_opener(opener)

try:
    pagehandle = urllib2.urlopen(theurl)

	# All calls to urllib2.urlopen will now use our handler
	# Make sure not to include the protocol in with the URL, or
	# HTTPPasswordMgrWithDefaultRealm will be very confused.
	# You must (of course) use it when fetching the page though.
    pagehandle = urllib2.urlopen(theurl)
	# authentication is now handled automatically for us
    print pagehandle.read()

except Exception as e:
	print e


