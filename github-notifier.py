import json
from twilio.rest import Client

##Created by Keith Low 

## Script that notifies you if an item is available in newegg

threshold = 300 ## Change this to the value of the price you are looking into
text = 'The GPU is available!:' ## Text can be changed to whatever message you want to have in your sms message
item_name = 'Sapphire Radeon NITRO+ RX 580 8GB GDDR5 PCI-E Dual HDMI / DVI-D / Dual DP w/ backplate (UEFI), 100411NT+8GL' ## Name of the item you are searching for

####################### TO SEND TEXT INFO #######################

account_sid = '' # Found on Twilio Console Dashboard
auth_token = '' # Found on Twilio Console Dashboard
myPhone = '' # Phone number you used to verify your Twilio account
TwilioNumber = '' # Phone number given to you by Twilio

####################### TO SEND TEXT INFO #######################

def getData(filename):
	with open(filename) as json_data:
		new_data = json.load(json_data)
		return new_data

def checkData(data):
	links = '\n'
	found = False
	for item in data:
		if (item['title'] == item_name):
			if (int(item['price']) < threshold):
				links += (str(item['link']) + "\n\n")
				found = True
	if (found == True):
		sendText(text + '\n' + links) 
		print('SENDING SMS!')
	else:
		print("PRODUCT NOT FOUND!\n" + item_name)

def sendText(text): ## Script that sends text messages to the 'myphone' recipient on call
	client = Client(account_sid, auth_token)
	client.messages.create(to=myPhone,from_=TwilioNumber,body= text)

def main():	
	print('+++++++++++++++++++START+++++++++++++++++++')
	new_data = getData('newdata.json') ## The scraper names the file new data
	checkData(new_data) ## Checks if there is a discounted gpu
	print('+++++++++++++++++++END+++++++++++++++++++++')

if __name__ == '__main__':
	main()
