# create twitter app - https://apps.twitter.com/app/new
# get keys
# get started - https://python-twitter.readthedocs.io/en/latest/twitter.html

import twitter

api = twitter.Api(consumer_key="cD7xGCwCxiVb1fWJqja5OYGOD",
				  consumer_secret="WSjh7e6yqs2P2PUEuRegiFFMqlCSsCTCTDRiaHIBtPuv5nuThm",
				  access_token_key="788930090608590848-e1EQgJHc6u0QBimp2ycsuqxaE6FcWg2",
				  access_token_secret="MX1KRpE3MgJvwhKwqYr9kmTZv1bokFkOCqwt9ubnxzNMr")

def getFriends(api):
	users = api.GetFriends()
	for u in users:
		print(u.name)

getFriends(api)

def post(api, msg):
	status = api.PostUpdate(msg)
	print(status.text)

# post(api, "Testing Python Twitter API!")

def DM(api, user, msg):
	dm = api.PostDirectMessage(msg, user)
	print(dm)

DM(api, "1107124159", "BOO") # message Amy Shan "Boo"
