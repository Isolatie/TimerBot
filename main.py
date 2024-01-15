#Bot	tools
import	discord
import	os
from dotenv import find_dotenv, load_dotenv
from	discord.ext	import	commands
import	asyncio
import	time
import	threading
import	multiprocessing
from	discordwebhook	import	Discord
from ratelimit import limits
import requests

#store your API key in an other file

FIFTEEN_MINUTES = 900

@limits(calls=15, period=FIFTEEN_MINUTES)
def call_api(url):
		response = requests.get(url)

		if response.status_code != 200:
				raise Exception('API response: {}'.format(response.status_code))
		return response


client	=	commands.Bot(command_prefix=',',	intents=discord.Intents.all(),	prefix="+")


global	bosses

bosses	=	multiprocessing.Manager().dict()


@client.event
async	def	on_ready():
				#	await	timer()
				print('We	have	logged	in	as	{0.user}'.format(client))


@client.event
async	def	on_message(message):
		if	(message.channel.id	==	#################CENSORED##################):
				if	message.author	==	client.user:
								return

				msg	=	message.content

#legendary	bosses
				if	msg.startswith('mord'):
								boss	=	'mord'
								await	timer(message,	boss)
				if	msg.startswith('necro'):
								boss	=	'necro'
								await	timer(message,	boss)
				if	msg.startswith('hrung'):
								boss	=	'hrung'
								await	timer(message,	boss)
				if	msg.startswith('aggy'):
								boss	=	'aggy'
								await	timer(message,	boss)
				if	msg.startswith('prot'):
								boss	=	'prot'
								await	timer(message,	boss)
				if	msg.startswith('gele'):
								boss	=	'gele'
								await	timer(message,	boss)
				if	msg.startswith('bt'):
								boss	=	'bt'
								await	timer(message,	boss)
				if	msg.startswith('dhio'):
								boss	=	'dhio'
								await	timer(message,	boss)

#EDL
				if	msg.startswith('185'):
								boss	=	'185'
								await	timer(message,	boss)
				if	msg.startswith('190'):
								boss	=	'190'
								await	timer(message,	boss)
				if	msg.startswith('195'):
								boss	=	'195'
								await	timer(message,	boss)
				if	msg.startswith('200'):
								boss	=	'200'
								await	timer(message,	boss)
				if	msg.startswith('205'):
								boss	=	'205'
								await	timer(message,	boss)
				if	msg.startswith('210'):
								boss	=	'210'
								await	timer(message,	boss)
				if	msg.startswith('215'):
								boss	=	'215'
								await	timer(message,	boss)

#DL
				if	msg.startswith('150'):
								boss	=	'150'
								await	timer(message,	boss)
				if	msg.startswith('155'):
								boss	=	'155'
								await	timer(message,	boss)
				if	msg.startswith('160'):
								boss	=	'160'
								await	timer(message,	boss)
				if	msg.startswith('165'):
								boss	=	'165'
								await	timer(message,	boss)
				if	msg.startswith('170'):
								boss	=	'170'
								await	timer(message,	boss)
				if	msg.startswith('180'):
								boss	=	'180'
								await	timer(message,	boss)

#Rings
				if	msg.startswith('north'):
								boss	=	'north'
								await	timer(message,	boss)

				if	msg.startswith('south'):
								boss	=	'south'
								await	timer(message,	boss)

				if	msg.startswith('center'):
								boss	=	'center'
								await	timer(message,	boss)

				if	msg.startswith('east'):
								boss	=	'east'
								await	timer(message,	boss)
#frozen
				#	if	msg.startswith('eye'):
				#					boss	=	'eye'
				#					await	timer(message,	boss)
				#	if	msg.startswith('swampy'):
				#					boss	=	'swampy'
				#					await	timer(message,	boss)
				#	if	msg.startswith('woody'):
				#					boss	=	'woody'
				#					await	timer(message,	boss)
				#	if	msg.startswith('chained'):
				#					boss	=	'chained'
				#					await	timer(message,	boss)
				#	if	msg.startswith('stone'):
				#					boss	=	'stone'
				#					await	timer(message,	boss)
				#	if	msg.startswith('lava'):
				#					boss	=	'lava'
				#					await	timer(message,	boss)

#soon	command
				if	msg.startswith('dl'):
								dl	=	'dl'
								await	timer(message,	dl)
				if	msg.startswith('edl'):
								edl	=	'edl'
								await	timer(message,	edl)
				if	msg.startswith('legend'):
								legend	=	'legend'
								await	timer(message,	legend)
				if msg.startswith('set'):
								await	timer(message,msg)


	
#Part of new timer

	
		if	(message.channel.id	==	#################CENSORED##################):
			if	message.author	==	client.user:
							return
		
			msg	=	message.content
		
		#legendary	bosses
			if	msg.startswith('mord'):
							boss	=	'mord'
							await	new_timer(message,	boss)
			if	msg.startswith('necro'):
							boss	=	'necro'
							await	new_timer(message,	boss)
			if	msg.startswith('hrung'):
							boss	=	'hrung'
							await	new_timer(message,	boss)
			if	msg.startswith('aggy'):
							boss	=	'aggy'
							await	new_timer(message,	boss)
			if	msg.startswith('prot'):
							boss	=	'prot'
							await	new_timer(message,	boss)
			if	msg.startswith('gele'):
							boss	=	'gele'
							await	new_timer(message,	boss)
			if	msg.startswith('bt'):
							boss	=	'bt'
							await	new_timer(message,	boss)
			if	msg.startswith('dhio'):
							boss	=	'dhio'
							await	new_timer(message,	boss)
		
		#EDL
			if	msg.startswith('185'):
							boss	=	'185'
							await	new_timer(message,	boss)
			if	msg.startswith('190'):
							boss	=	'190'
							await	new_timer(message,	boss)
			if	msg.startswith('195'):
							boss	=	'195'
							await	new_timer(message,	boss)
			if	msg.startswith('200'):
							boss	=	'200'
							await	new_timer(message,	boss)
			if	msg.startswith('205'):
							boss	=	'205'
							await	new_timer(message,	boss)
			if	msg.startswith('210'):
							boss	=	'210'
							await	new_timer(message,	boss)
			if	msg.startswith('215'):
							boss	=	'215'
							await	new_timer(message,	boss)
		
		#DL
			if	msg.startswith('150'):
							boss	=	'150'
							await	new_timer(message,	boss)
			if	msg.startswith('155'):
							boss	=	'155'
							await	new_timer(message,	boss)
			if	msg.startswith('160'):
							boss	=	'160'
							await	new_timer(message,	boss)
			if	msg.startswith('165'):
							boss	=	'165'
							await	new_timer(message,	boss)
			if	msg.startswith('170'):
							boss	=	'170'
							await	new_timer(message,	boss)
			if	msg.startswith('180'):
							boss	=	'180'
							await	new_timer(message,	boss)
		
		#Rings
			if	msg.startswith('north'):
							boss	=	'north'
							await	new_timer(message,	boss)
		
			if	msg.startswith('south'):
							boss	=	'south'
							await	new_timer(message,	boss)
		
			if	msg.startswith('center'):
							boss	=	'center'
							await	new_timer(message,	boss)
		
			if	msg.startswith('east'):
							boss	=	'east'
							await	new_timer(message,	boss)
		#frozen
			#	if	msg.startswith('eye'):
			#					boss	=	'eye'
			#					await	new_timer(message,	boss)
			#	if	msg.startswith('swampy'):
			#					boss	=	'swampy'
			#					await	new_timer(message,	boss)
			#	if	msg.startswith('woody'):
			#					boss	=	'woody'
			#					await	new_timer(message,	boss)
			#	if	msg.startswith('chained'):
			#					boss	=	'chained'
			#					await	new_timer(message,	boss)
			#	if	msg.startswith('stone'):
			#					boss	=	'stone'
			#					await	new_timer(message,	boss)
			#	if	msg.startswith('lava'):
			#					boss	=	'lava'
			#					await	new_timer(message,	boss)
		
		#soon	command
			if	msg.startswith('dl'):
							dl	=	'dl'
							await	new_timer(message,	dl)
			if	msg.startswith('edl'):
							edl	=	'edl'
							await	new_timer(message,	edl)
			if	msg.startswith('legend'):
							legend	=	'legend'
							await	new_timer(message,	legend)
			if msg.startswith('set'):
							await	new_timer(message,msg)
		
					
@client.command()
async	def	timer(message,	boss):
				start	=	time.perf_counter()							
				exitFlag	=	0

				class	myThread	(multiprocessing.Process):
								def	__init__(self,	threadID,	name,	counter,	due,	type):
												multiprocessing.Process.__init__(self)
												self.threadID	=	threadID
												self.name	=	name
												self.counter	=	counter
												self.due	=	due
												self.type	=	type
												self.value	=	None
												self._stop	=	threading.Event()

								def	run(self):
												print	("Starting	"	+	self.name)
												self.value	=	print_time(self.threadID,	self.name,	self.counter,	self.due,	self.type)
												print	("Exiting	"	+	self.name)





				def	print_time(threadID,	threadName,	counter,	due,	type):
								prio	=	Discord(url="https://discord.com/api/webhooks/#################CENSORED##################")
								noti	=	Discord(url="https://discord.com/api/webhooks/#################CENSORED##################")
								while	counter:
																mins,	secs	=	divmod(counter,	60)
																hours,	mins	=	divmod(mins,	60)
																time.sleep(1)
																timer	=	'{:02d}:{:02d}:{:02d}'.format(hours,	mins,	secs)
																if hours == 0 and mins == 6 and secs == 59:
																	if threadID == 6 or threadID == 9 or threadID == 10 or threadID == 11 or threadID == 12 or threadID == 13 or threadID == 14 or threadID == 15 or threadID == 16 or threadID == 17 or threadID == 18 or threadID == 19 or threadID == 20 or threadID == 21 or threadID == 22 or threadID == 23 or threadID == 24 or threadID == 25:
																		prio.post(content='@everyone	In	7	minutes	%s 	will	be	due!'%(threadName))
																	else:
																		noti.post(content='In	7	minutes	%s		will	be	due!'%(threadName))

																if	threadID	in	bosses:
																	del	bosses[threadID]

																bosses[threadID]	=	["%s:	%s"%(threadName,	timer)]

																counter	-=	1

								if	counter	==	0:
												while	due:
																if	exitFlag:
																				threadID.exit()
																Dmins,	Dsecs	=	divmod(due,	60)
																Dhours,	Dmins	=	divmod(Dmins,	60)
																time.sleep(1)
																Dtimer	=	'{:02d}:{:02d}:{:02d}'.format(Dhours,	Dmins,	Dsecs)

																if	threadID	in	bosses:
																	del	bosses[threadID]

																bosses[threadID]	=	["DUE	%s:	%s"%(threadName,	Dtimer)]

																due	-=	1
								del	bosses[threadID]

				async	def	call(col):
							t	=	multiprocessing.Process(target=await	boss_call(col))
							t.start()


				async	def	boss_call(col):
							embed	=	discord.Embed(title=f"Timers	of	bosses",	color=discord.Color.teal(),	timestamp=message.created_at)

							if	col	==	'dl':
												for	key	in	bosses.items():

													if	key[0]	==	1	or	key[0]	==	2	or	key[0]	==	3	or	key[0]	==	4	or	key[0]	==	5	or	key[0]	==	6:
														embed.add_field(name	='-----------------------------',	value	=	f"**{key[1][0]}**",	inline	=	False)

												embed.set_footer(text=f"Requested	by	{message.author.name}")		
												await	message.channel.send(embed=embed)

							if	col	==	'edl':
												for	key	in	bosses.items():

													if	key[0]	==	7	or	key[0]	==	8	or	key[0]	==	9	or	key[0]	==	10	or	key[0]	==	11	or	key[0]	==	12	or	key[0]	==	13:
														embed.add_field(name	='-----------------------------',	value	=	f"**{key[1][0]}**",	inline	=	False)

												embed.set_footer(text=f"Requested	by	{message.author.name}")		
												await	message.channel.send(embed=embed)

							if	col	==	'legend':
												for	key	in	bosses.items():

													if key[0] == 14 or key[0] == 15 or key[0] == 16 or key[0] == 17 or key[0] == 18 or key[0] == 19 or key[0] == 20 or key[0] == 21 or key[0] == 22 or key[0] == 23 or key[0] == 24 or key[0] == 25:
														embed.add_field(name	='-----------------------------',	value	=	f"**{key[1][0]}**",	inline	=	False)

												embed.set_footer(text=f"Requested	by	{message.author.name}")		
												await	message.channel.send(embed=embed)


				async	def	reset_timer():
							global	processes
							global	wyrmlist	
							global	spiderlist	
							global	hplist	
							global	kinglist
							global	srenglist	
							global	snorlist	
							global	doglist	
							global	skathlist	
							global	gronlist	
							global	implist	
							global	craglist	
							global	revenantlist	
							global	unoxlist	
							global	aggylist
							global	mordlist	
							global	necrolist	
							global	hrunglist
							global	protlist	
							global	gelelist	
							global	btlist	
							global	dhiolist
							global	northlist
							global	southlist
							global	centerlist
							global	eastlist

							raw_boss = None
							raw_time = 0

							if	boss.startswith('set'):
												raw_boss = boss.split(" ")[1]
												raw_time = int(boss.split(" ")[2])


							if	boss	==	'150' or raw_boss	==	'150':
												type	=	'dl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												wyrm	= myThread(1,"150", (55+raw_time)*60,	10*6,type)
												wyrm.start()
												wyrmlist.append(wyrm)
												await	message.channel.send('150	has	been	resetted')

							if	boss	==	'155' or raw_boss	==	'155':
												type	=	'dl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												spider	=	myThread(2,	"155",	(60+raw_time)*60,	10*6,type)
												spider.start()
												spiderlist.append(spider)
												await	message.channel.send('155	has	been	resetted')

							if	boss	==	'160' or raw_boss	==	'160':
												type	=	'dl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												hp	=	myThread(3,"160",	(65+raw_time)*60,	10*6,type)
												hp.start()
												hplist.append(hp)
												await	message.channel.send('160	has	been	resetted')

							if	boss	==	'165' or raw_boss	==	'165':
												type	=	'dl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												king	=	myThread(4,"165",	(70+raw_time)*60,	10*6,type)
												king.start()
												kinglist.append(king)
												await	message.channel.send('165	has	been	resetted')

							if	boss	==	'170' or raw_boss	==	'170':
												type	=	'dl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												sreng	=	myThread(5,"170",	(80+raw_time)*60,	10*6,type)
												sreng.start()
												srenglist.append(sreng)
												await	message.channel.send('170	has	been	resetted')

							if	boss	==	'180' or raw_boss	==	'180':
												type	=	'dl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												snor	=	myThread(6,"180",	(90+raw_time)*60,	10*6,type)
												snor.start()
												snorlist.append(snor)
												await	message.channel.send('180	has	been	resetted')

							if	boss	==	'185' or raw_boss	==	'185':
												type	=	'edl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												dog	=	myThread(7,"185",	(75+raw_time)*60,	10*6,type)
												dog.start()
												doglist.append(dog)
												await	message.channel.send('185	has	been	resetted')

							if	boss	==	'190' or raw_boss	==	'190':
												type	=	'edl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												skath	=	myThread(8,"190",	(85+raw_time)*60,	10*6,type)
												skath.start()
												skathlist.append(skath)
												await	message.channel.send('190	has	been	resetted')

							if	boss	==	'195' or raw_boss	==	'195':
												type	=	'edl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												gron	=	myThread(9,"195",	(95+raw_time)*60,	10*6,type)
												gron.start()
												gronlist.append(gron)
												await	message.channel.send('195	has	been	resetted')

							if	boss	==	'200' or raw_boss	==	'200':
												type	=	'edl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												imp	=	myThread(10,"200",	(105+raw_time)*60,	10*6,type)
												imp.start()
												implist.append(imp)
												await	message.channel.send('200	has	been	resetted')

							if	boss	==	'205' or raw_boss	==	'205':
												type	=	'edl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												crag	=	myThread(11,	"205",	(115+raw_time)*60,	10*6,type)
												crag.start()
												craglist.append(crag)
												await	message.channel.send('205	has	been	resetted')

							if	boss	==	'210' or raw_boss	==	'210':
												type	=	'edl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												revenant	=	myThread(12,"210",	(125+raw_time)*60,	10*6,type)
												revenant.start()
												revenantlist.append(revenant)
												await	message.channel.send('210	has	been	resetted')

							if	boss	==	'215' or raw_boss	==	'215':
												type	=	'edl'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												unox	=	myThread(13,"215",	(135+raw_time)*60,	10*6,type)
												unox.start()
												unoxlist.append(unox)
												await	message.channel.send('215	has	been	resetted')

							if	boss	==	'aggy' or raw_boss	==	'aggy':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												aggy	=	myThread(14,"Aggy",	(1440+raw_time)*60,	1440*60,type)
												aggy.start()
												aggylist.append(aggy)
												await	message.channel.send('Aggy	has	been	resetted')

							if	boss	==	'mord' or raw_boss	==	'mord':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												mord	=	myThread(15,"Mord",	(1440+raw_time)*60,	1440*60,type)
												mord.start()
												mordlist.append(mord)
												await	message.channel.send('Mord	has	been	resetted')

							if	boss	==	'necro' or raw_boss	==	'necro':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												necro	=	myThread(16,"Necro",	(1440+raw_time)*60,	1440*60,type)
												necro.start()
												necrolist.append(necro)
												await	message.channel.send('Necro	has	been	resetted')

							if	boss	==	'hrung' or raw_boss	==	'hrung':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												hrung	=	myThread(17,"Hrung",	(1440+raw_time)*60,	1440*60,type)
												hrung.start()
												hrunglist.append(hrung)
												await	message.channel.send('Hrung	has	been	resetted')

							if	boss	==	'prot' or raw_boss	==	'prot':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												prot	=	myThread(18,"Prot",	(1080+raw_time)*60,	45*60,type)
												prot.start()
												protlist.append(prot)
												await	message.channel.send('Prot	has	been	resetted')

							if	boss	==	'gele' or raw_boss	==	'gele':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												gele	=	myThread(19,"Gele",	(2160+raw_time)*60,	2160*60,type)
												gele.start()
												gelelist.append(gele)
												await	message.channel.send('Gele	has	been	resetted')

							if	boss	==	'bt' or raw_boss	==	'bt':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												bt	=	myThread(20,"BT",	(2160+raw_time)*60,	2160*60,type)
												bt.start()
												btlist.append(bt)
												await	message.channel.send('BT	has	been	resetted')

							if	boss	==	'dhio' or raw_boss	==	'dhio':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												dhio	=	myThread(21,"Dhio",	(2160+raw_time)*60,	2160*60,type)
												dhio.start()
												dhiolist.append(dhio)
												await	message.channel.send('Dhio	has	been	resetted')

							if	boss	==	'north' or raw_boss	==	'north':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												north	=	myThread(22,"North",(225+raw_time)*60,	20*60,type)
												north.start()
												northlist.append(north)
												await	message.channel.send('North	has	been	resetted')

							if	boss	==	'south' or raw_boss	==	'south':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												south	=	myThread(23,"South",(225+raw_time)*60,	20*60,type)
												south.start()
												southlist.append(south)
												await	message.channel.send('South	has	been	resetted')

							if	boss	==	'center' or raw_boss	==	'center':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												center	=	myThread(24,"Center",(225+raw_time)*60,	20*60,type)
												center.start()
												centerlist.append(center)
												await	message.channel.send('Center	has	been	resetted')

							if	boss	==	'east' or raw_boss	==	'east':
												type	=	'legendary'
												ClearTimer(boss)
												ClearTimer(raw_boss)
												east	=	myThread(25,"East",(225+raw_time)*60,	20*60,type)
												east.start()
												eastlist.append(east)
												await	message.channel.send('East	has	been	resetted')

				def	ClearTimer(boss):
							if	boss	==	'150':
									for	pop	in	wyrmlist:
												pop.kill()
												wyrmlist.remove(pop)

							if	boss	==	'155':
									for	pop	in	spiderlist:
												pop.kill()
												spiderlist.remove(pop)

							if	boss	==	'160':
									for	pop	in	hplist:
												pop.kill()
												hplist.remove(pop)

							if	boss	==	'165':
									for	pop	in	kinglist:
												pop.kill()
												kinglist.remove(pop)

							if	boss	==	'170':
									for	pop	in	srenglist:
												pop.kill()
												srenglist.remove(pop)

							if	boss	==	'180':
									for	pop	in	snorlist:
												pop.kill()
												snorlist.remove(pop)

							if	boss	==	'185':
									for	pop	in	doglist:
												pop.kill()
												doglist.remove(pop)

							if	boss	==	'190':
									for	pop	in	skathlist:
												pop.kill()
												skathlist.remove(pop)

							if	boss	==	'195':
									for	pop	in	gronlist:
												pop.kill()
												gronlist.remove(pop)

							if	boss	==	'200':
									for	pop	in	implist:
												pop.kill()
												implist.remove(pop)

							if	boss	==	'205':
									for	pop	in	craglist:
												pop.kill()
												craglist.remove(pop)

							if	boss	==	'210':
									for	pop	in	revenantlist:
												pop.kill()
												revenantlist.remove(pop)

							if	boss	==	'215':
									for	pop	in	unoxlist:
												pop.kill()
												unoxlist.remove(pop)

							if	boss	==	'aggy':
									for	pop	in	aggylist:
										pop.kill()
										aggylist.remove(pop)

							if	boss	==	'mord':
									for	pop	in	mordlist:
												pop.kill()
												mordlist.remove(pop)

							if	boss	==	'necro':
									for	pop	in	necrolist:
											pop.kill()
											necrolist.remove(pop)

							if	boss	==	'hrung':
									for	pop	in	hrunglist:
												pop.kill()
												hrunglist.remove(pop)

							if	boss	==	'prot':
									for	pop	in	protlist:
												pop.kill()
												protlist.remove(pop)

							if	boss	==	'gele':
									for	pop	in	gelelist:
												pop.kill()
												gelelist.remove(pop)

							if	boss	==	'bt':
									for	pop	in	btlist:
												pop.kill()
												btlist.remove(pop)

							if	boss	==	'dhio':
									for	pop	in	dhiolist:
												pop.kill()
												dhiolist.remove(pop)

							if	boss	==	'north':
									for	pop	in	northlist:
												pop.kill()
												northlist.remove(pop)

							if	boss	==	'south':
									for	pop	in	southlist:
												pop.kill()
												southlist.remove(pop)

							if	boss	==	'center':
									for	pop	in	centerlist:
												pop.kill()
												centerlist.remove(pop)

							if	boss	==	'east':
									for	pop	in	eastlist:
												pop.kill()
												eastlist.remove(pop)

				await	reset_timer()
				await	call(boss)
				finish	=	time.perf_counter()
				print(f'Finished	in	{round(finish-start,2)}	seconds(s)')




wyrmlist	=	[]
spiderlist	=	[]
hplist	=	[]
kinglist	=	[]
srenglist	=[]
snorlist	=	[]
doglist	=	[]
skathlist	=	[]
gronlist	=	[]
implist	=	[]
craglist	=	[]
revenantlist	=	[]
unoxlist	=	[]
aggylist	=	[]
mordlist	=	[]
necrolist	=	[]
hrunglist	=	[]
protlist	=	[]
gelelist	=	[]
btlist	=	[]
dhiolist	=	[]
northlist = []
southlist = []
centerlist = []
eastlist = []


api_key = os.getenv('api_key')
client.run(api_key)
