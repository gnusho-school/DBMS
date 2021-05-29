import pymysql as pms
import pandas as pd
import csv

db=pms.connect(user='root', 
	passwd='Curry5407!', 
	host='127.0.0.1',
	db='music_db',
	charset='utf8')

cursor=db.cursor(pms.cursors.DictCursor)

sql = """insert into music(music_name, enroll_date, artist, album) values (%s,%s, %s, %s)"""

data=(
('Distorted Records','2018-05-25',	101	,'TESTING')
,('Tony Tone','	2018-05-25',	101	,'TESTING')
,('OG Beeper','	2018-05-25',	101	,'TESTING')
,('Wickr me','	2020-04-08',	102	,'DETOX')
,('Price Tag','	2020-04-08',	102	,'DETOX')
,('WASABI','	2020-04-08',	102	,'DETOX')
,('GET YOU','	2017-08-25',	103	,'Freudian')
,('Best Part','	2017-08-25',	103	,'Freudian')
,('Blessed','2017-08-25',	103	,'Freudian')
,('Jasmine','	2017-12-07',	104	,'Her')
,('Martini Blue','	2017-12-07',	104	,'Her')
,('Text Me','	2017-12-07',	104	,'Her')
,('주사위','	2015-08-27',	105	,'The Anecdote')
,('Back In Time','	2015-08-27',	105	,'The Anecdote')
,('Unknown Verse','	2015-08-27',	105	,'The Anecdote')
,('Kill You','	2000-05-23',	106	,'The Marshall Mathers LP')
,('Stan','	2000-05-23',	106	,'The Marshall Mathers LP')
,('Amityville','	2000-05-23',	106	,'The Marshall Mathers LP')
,('White Ferrari','	2016-08-20',	107	,'Blonde')
,('Self Control','	2016-08-20',	107	,'Blonde')
,('Ivy','	2016-08-20',	107	,'Blonde')
,('All Of The Lights','	2010-01-01',	108	,'My Beautiful Dark Twisted Fantasy')
,('So Appalled','	2010-01-01',	108	,'My Beautiful Dark Twisted Fantasy')
,('Blame Game','	2010-01-01',	108	,'My Beautiful Dark Twisted Fantasy')
,('u','	2015-03-18',	109	,'To Pimp A Butterfly')
,('Mortal Man','	2015-03-18',	109	,'To Pimp A Butterfly')
,('Alright','	2015-03-18',	109	,'To Pimp A Butterfly')
,('Thank You','	2018-09-28',	110	,'YSIV')
,('Everybody Dies','	2018-09-28',	110	,'YSIV')
,('The Return','	2018-09-28',	110	,'YSIV')
,('Came From The Bottom','	2011-11-29',	112	,'Stormy Friday')
,('BENTLY 2','	2020-11-11',	112	,'BENTLEY 2')
,('귀로','	2011-11-29',	112	,'Stormy Friday')
,('아부다비','	2020-11-11',	112	,'BENTLEY 2')
,('Mr.Lonely part 2','	2011-11-29',	112	,'Stormy Friday')
,('나랑 아니면','	2017-05-30',	113	,'TEAM BABY')
,('혜야','	2017-05-30',	113	,'TEAM BABY')
,('EVERYTHING','	2017-05-30',	113	,'TEAM BABY')
,('Sell The Soul','	2016-06-14',	117	,'2 MANY HOMES 4 1 KID')
,('아뜰리에','	2016-06-14',	117	,'2 MANY HOMES 4 1 KID')
,('Welcome to My HOME','	2016-06-14',	117	,'2 MANY HOMES 4 1 KID')
,('unlucky','	2019-11-18',	215	,'Love poem')
,('이 지금','	2017-04-21',	215	,'Palette')
,('Love poem','	2019-11-18',	215	,'Love poem')
,('잼잼','	2017-04-21',	215	,'Palette')
,('Bluming','	2019-11-18',	215	,'Love poem')
,('이름에게','	2017-04-21',	215	,'Palette')
,('비가 내리는 날에는','	2019-07-02',	216	,'STABLE MINDSET')
,('어려운 일','	2019-07-02',	216	,'STABLE MINDSET')
,('Lonely','	2019-07-02',	216	,'STABLE MINDSET')
,('Midnight Driver','	2018-11-06',	218	,'Midnight Candy')
,('어린밤에 우리','	2018-11-06',	218	,'Midnight Candy')
,('영원처럼 안아줘','	2018-11-06',	218	,'Midnight Candy')
,('Wonderwall','	1997-03-01',	311	,'Morning Glory')
,('Cast No Shadow','	1997-03-01',	311	,'Morning Glory')
,('Champagne Supernova','	1997-03-01',	311	,'Morning Glory')
,('어려운 달','	2016-05-19',	314	,'서울병')
,('석류의 맛','	2016-05-19',	314	,'서울병')
,('서울','	2016-05-19',	314	,'서울병')

)

cursor.executemany(sql,data)

db.commit()
db.close()