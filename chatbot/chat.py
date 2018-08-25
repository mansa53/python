from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from six.moves import urllib

bot=ChatBot('Bot')
bot.set_trainer(ListTrainer)
path='shakespeare_input.txt'


for files in os.listdir('/home/manasa/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
	data=open('/home/manasa/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
	bot.train(data)

	
	#data=urllib.request.urlretrieve("https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/			    shakespeare_input.txt", path)
	#bot.train(data)
while True:
	message=raw_input('You:')
	if message.strip()!="Bye":
		reply=bot.get_response(message)
		print 'ChatBot:',reply
	if message.strip()=="Bye":
			print('Chackogirl:Bye')
			break
