# Timer-Bot
Timer Bot for CH,

In this game, monsters appear that you must defeat to acquire stronger equipment. Once a monster is defeated, it disappears for a certain period. Now, there are quite a few of these monsters, and each one has its own timer until it reappears. Not only that, but the timers for these monsters keep increasing. The harder the monster, the longer the time. It can go up to 2 days.

In theory, you could time all these intervals on your mobile device. However, the problem is that you can't defeat these monsters alone; you need a lot of people to come online at the same time to defeat the monster.
This bot does not only serve as timer, but also as notifier.

## Important Note

For 'message.channel.id', copy your channel id where you want to start and check timers.

For variable 'prio', copy your bot's webhook url for the important monsters that you want to receive notifications from.

For variable 'noti', copy your bot's webhook url for the _less_ important monsters that you want to receive notifications from.

Last line of code in **main.py**, you will need to insert the API key from your discord bot, make sure to hide the key well.

## Commands

**CALLING COMMAND**:

 'dl'     Will show you all current bosses of the type Dragonlord Bosses
 
 'edl'   Will show you all current bosses of the type Exalted Dragonlord Bosses
 
 'legend'  Will show you all current bosses of the type Legendary Bosses 

**RESET TIMERS COMMAND**:

Dragonlord Bosses

'150'  Will reset timer for wyrm

'155'  Will reset timer for spider

'160'  Will reset timer for high priest

'165'  Will reset timer for king

'170'  Will reset timer for sreng

'180'  Will reset timer for snor

Exalted Dragonlord Bosses

'185'  Will reset timer for dog

'190'  Will reset timer for skath

'195'  Will reset timer for gron

'200' Will reset timer for  imp

'205' Will reset timer for crag

'210'  Will reset timer for reve

'215'  Will reset timer for unox

Legendary Bosses

'aggy'  Will reset timer for Aggy

'hrung'  Will reset timer for Hrung

'mord'  Will reset timer for Mord

'necro'  Will reset timer for Necro

'prot'  Will reset timer for Prot

'gele'  Will reset timer for Gele

'bt'  Will reset timer for BT

'dhio'  Will reset timer for Dhio

'north' will reset timer for North ring

'center' will reset timer for Center ring

'south' will reset timer for South ring

'east' will reset timer for East ring

**NEW COMMAND**

'set (bossname) (-amount of time too late)'
