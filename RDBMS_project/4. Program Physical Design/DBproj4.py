# -*- Encoding:UTF-8 -*- 
import numpy as np
import pymysql
import pandas as pd
from datetime import datetime
import random
import time
import threading

db=pymysql.connect(user='root', 
	passwd='Curry5407!', 
	host='127.0.0.1',
	db='db',
	charset='utf8')

cursor=db.cursor(pymysql.cursors.DictCursor)

#프로그램 실시할 때 마다 날짜가 지나있으면 자동으로 date 생성하는 코드
today_date=None
if datetime.today().day<10:today_date=str(datetime.today().year)+'-'+str(datetime.today().month)+'-0'+str(datetime.today().day)

else: today_date=str(datetime.today().year)+'-'+str(datetime.today().month)+'-'+str(datetime.today().day)
sql_date=("SELECT* FROM date_stream WHERE str_date LIKE '%s';"%today_date)
cursor.execute(sql_date)
result_date=cursor.fetchall()
result_date=pd.DataFrame(result_date)
if result_date.empty:
	sql_music="SELECT* FROM music;"
	cursor.execute(sql_music)
	result_music=cursor.fetchall()
	sql_str_insert="""insert into date_stream(str_cnt,music,artist,album,str_date)
	values (%s, %s, %s, %s, %s)"""
	for row in result_music:
		cnt=random.randrange(10,100)
		a=(cnt, row['music_name'], row['artist'], row['album'], today_date)
		cursor.execute(sql_str_insert,a)
	db.commit()

login=False
manager=0 #0:user 1:manager

while login==False:
	print("You have to log in first")
	print("0: for login as user")
	print("1: for login as manager")

	input_a=input("숫자를 입력하세요: ")
	manager=int(input_a)#향후 에러처리 해주기

	input_name=input("Name: ")
	input_passwd=input("Passwd: ")

	if manager==1:
		sql_login=("SELECT* FROM manager WHERE name='%s' AND passwd='%s'"%(input_name,input_passwd))
		cursor.execute(sql_login)
		result_login=cursor.fetchall()
		if result_login!=(): login=True

	if manager==0:
		sql_login=("SELECT* FROM user WHERE name='%s' AND password='%s'"%(input_name,input_passwd))
		cursor.execute(sql_login)
		result_login=cursor.fetchall()
		if result_login!=(): login=True
	print()		

if manager==1: print("You log in as manager!")
else: print("You log in as user!")

def str_update(music, artist, album, str_date):
	inputt=(music,artist,album,str_date)
	sql=("UPDATE date_stream SET str_cnt=str_cnt+1 WHERE music='%s' AND artist='%s' AND album='%s' AND str_date='%s'"%inputt)
	cursor.execute(sql)
	db.commit()
timer=0
def streaming(): 
	global timer
	print("play!")
	timer+=1
	if timer==5: timer=0
	else: threading.Timer(1,streaming).start()

def search_music():
	global today_date
	init=True
	while init==True:
		tmp=input("Search Music: ")
		#string 일부만으로도 검색가능!
		tmp='%'+tmp+'%'
		sql_tmp=("SELECT a.name as artist, m.music_name as music, m.album FROM music AS m, artist AS a WHERE a.a_index=m.artist AND music_name LIKE '%s'"%(tmp))
		cursor.execute(sql_tmp)
		result_=cursor.fetchall()
		if result_==():
			print("There is no result")
			continue
		another=False
		while another==False:
			result_tmp=pd.DataFrame(result_)
			print(result_tmp)
			print()

			print("0: Finish Search")
			print("1: Select One")
			print("2: Search Another")
			select=int(input("Enter: "))
			print()
			if select==0: 
				init=False
				another=True
			elif select==2: another=True
			elif select==1:
				music_num=int(input("Enter Music Num: "))
				select_music=result_tmp.loc[[music_num],:]
				print(select_music)
				print("\nSelect Your Service")
				print("1: Play")
				print("2: Back")

				service_num=int(input("Enter Service Num: "))

				if service_num==1:
					cntt=0
					for row in result_:
						if cntt==music_num: break
						else: cntt+=1
					sql_tmptmp=("SELECT a_index From artist WHERE name='%s'" %(row['artist']))
					cursor.execute(sql_tmptmp)
					artist_tmp=cursor.fetchall()
					artist_num=artist_tmp[0]['a_index']
					#print(artist_num)
					str_update(row['music'],artist_num,row['album'],today_date)
					streaming()
					#print(select_music['name'])
					time.sleep(5)
					print("Finish Music!\n")

def search_artist():
	global today_date
	init=True
	while init==True:
		tmp=input("Search Music by Artist: ")
		#string 일부만으로도 검색가능!
		tmp='%'+tmp+'%'
		sql_tmp=("SELECT a.name as artist, m.music_name as music, m.album FROM music AS m, artist AS a WHERE a.a_index=m.artist AND a.name LIKE '%s'"%(tmp))
		cursor.execute(sql_tmp)
		result_=cursor.fetchall()
		if result_==():
			print("There is no result")
			continue
		another=False
		while another==False:
			result_tmp=pd.DataFrame(result_)
			print(result_tmp)
			print()

			print("0: Finish Search")
			print("1: Select One")
			print("2: Search Another")
			select=int(input("Enter: "))
			print()
			if select==0: 
				init=False
				another=True
			elif select==2: another=True
			elif select==1:
				music_num=int(input("Enter Music Num: "))
				select_music=result_tmp.loc[[music_num],:]
				print(select_music)
				print("\nSelect Your Service")
				print("1: Play")
				print("2: Back")

				service_num=int(input("Enter Service Num: "))

				if service_num==1:
					cntt=0
					for row in result_:
						if cntt==music_num: break
						else: cntt+=1
					sql_tmptmp=("SELECT a_index From artist WHERE name='%s'" %(row['artist']))
					cursor.execute(sql_tmptmp)
					artist_tmp=cursor.fetchall()
					artist_num=artist_tmp[0]['a_index']
					#print(artist_num)
					str_update(row['music'],artist_num,row['album'],today_date)
					streaming()
					#print(select_music['name'])
					time.sleep(5)
					print("Finish Music!\n")

def search_album():
	global today_date
	init=True
	while init==True:
		tmp=input("Search Music by Album: ")
		#string 일부만으로도 검색가능!
		tmp='%'+tmp+'%'
		sql_tmp=("SELECT a.name as artist, m.music_name as music, m.album FROM music AS m, artist AS a WHERE a.a_index=m.artist AND m.album LIKE '%s'"%(tmp))
		cursor.execute(sql_tmp)
		result_=cursor.fetchall()
		if result_==():
			print("There is no result")
			continue
		another=False
		while another==False:
			result_tmp=pd.DataFrame(result_)
			print(result_tmp)
			print()

			print("0: Finish Search")
			print("1: Select One")
			print("2: Search Another")
			select=int(input("Enter: "))
			print()
			if select==0: 
				init=False
				another=True
			elif select==2: another=True
			elif select==1:
				music_num=int(input("Enter Music Num: "))
				select_music=result_tmp.loc[[music_num],:]
				print(select_music)
				print("\nSelect Your Service")
				print("1: Play")
				print("2: Back")

				service_num=int(input("Enter Service Num: "))

				if service_num==1:
					cntt=0
					for row in result_:
						if cntt==music_num: break
						else: cntt+=1
					sql_tmptmp=("SELECT a_index From artist WHERE name='%s'" %(row['artist']))
					cursor.execute(sql_tmptmp)
					artist_tmp=cursor.fetchall()
					artist_num=artist_tmp[0]['a_index']
					#print(artist_num)
					str_update(row['music'],artist_num,row['album'],today_date)
					streaming()
					#print(select_music['name'])
					time.sleep(5)
					print("Finish Music!\n")

def search_all():
	global today_date, result_login
	init=True
	while init==True:
		tmp=input("Search Music by All Method: ")
		#string 일부만으로도 검색가능!
		tmp='%'+tmp+'%'
		sql_tmp=("SELECT a.name as artist, m.music_name as music, m.album FROM music AS m, artist AS a WHERE a.a_index=m.artist AND (music_name LIKE '%s' OR a.name LIKE '%s' OR m.album LIKE '%s')"%(tmp,tmp,tmp))
		cursor.execute(sql_tmp)
		result_=cursor.fetchall()
		if result_==():
			print("There is no result")
			continue
		another=False
		while another==False:
			result_tmp=pd.DataFrame(result_)
			print(result_tmp)
			print()

			print("0: Finish Search")
			print("1: Select One")
			print("2: Search Another")
			select=int(input("Enter: "))
			print()
			if select==0: 
				init=False
				another=True
			elif select==2: another=True
			elif select==1:
				music_num=int(input("Enter Music Num: "))
				select_music=result_tmp.loc[[music_num],:]
				print(select_music)
				print("\nSelect Your Service")
				print("1: Play")
				print("2: Put into your playlist")
				print("0: Back")

				service_num=int(input("Enter Service Num: "))

				if service_num==1:
					cntt=0
					for row in result_:
						if cntt==music_num: break
						else: cntt+=1
					sql_tmptmp=("SELECT a_index From artist WHERE name='%s'" %(row['artist']))
					cursor.execute(sql_tmptmp)
					artist_tmp=cursor.fetchall()
					artist_num=artist_tmp[0]['a_index']
					#print(artist_num)
					str_update(row['music'],artist_num,row['album'],today_date)
					streaming()
					#print(select_music['name'])
					time.sleep(5)
					print("Finish Music!\n")

				if service_num==2:
					row=result_[music_num]
					sql_tmptmp=("SELECT a_index From artist WHERE name='%s'" %(row['artist']))
					cursor.execute(sql_tmptmp)
					artist_tmp=cursor.fetchall()
					artist_num=artist_tmp[0]['a_index']

					sql=("SELECT* FROM playlist WHERE producer=%s"%result_login[0]['u_index'])
					cursor.execute(sql)
					result_plpl=cursor.fetchall()

					if result_plpl==():
						print("There is no your playlist")
						continue

					frame=pd.DataFrame(result_plpl)
					print(frame)
					back=input("Keep going? yes or no: ")
					if back=="no": continue

					pl_n=int(input("Enter the number playlist: "))
					pl=result_plpl[pl_n]
					tmp=(pl['pl_index'], pl['producer'], row['music'],row['album'],artist_num)
					sql=("SELECT* FROM in_playlist WHERE playlist=%s AND producer=%s AND music='%s' AND album='%s' AND artist=%s"%tmp)
					cursor.execute(sql)
					ch=cursor.fetchall()

					if ch!=():
						print("Already IN!")
						continue

					else:
						sql=("insert into in_playlist(playlist,producer,music,album,artist) values (%s,%s,'%s','%s',%s)"%tmp)
						cursor.execute(sql)

						db.commit()

						print("Finish!!!")
#여기서는 각곡을 플레이리스트에 넣는 것도 가능

def create_playlist():
	global result_login
	check=input("If You really want make new Playlist, enter YES or No\n")
	if check=='No': return

	pl_name=input("Input Playlist Name: ")
	producer=result_login[0]['u_index']
	sql_pl=("SELECT MAX(pl_index) as max FROM playlist WHERE producer=%s"%producer)
	cursor.execute(sql_pl)	
	result_pl=cursor.fetchall()
	pl_index=0
	if result_pl[0]['max']!=None: pl_index=result_pl[0]['max']+1
	tmp=(pl_name,pl_index,producer)
	sql_pl_insert=("""insert into playlist(pl_name, pl_index, producer) values ('%s',%s, %s)"""%tmp)
	cursor.execute(sql_pl_insert)
	db.commit()
	#pl_name,pl_index,producer 까지 완료 이제 들어갈 노래 생성

	global today_date
	init=True
	while init==True:
		tmp=input("Looking for music for new Playlist: ")
		#string 일부만으로도 검색가능!
		tmp='%'+tmp+'%'
		sql_tmp=("SELECT a.name as artist, m.music_name as music, m.album FROM music AS m, artist AS a WHERE a.a_index=m.artist AND (music_name LIKE '%s' OR a.name LIKE '%s' OR m.album LIKE '%s')"%(tmp,tmp,tmp))
		cursor.execute(sql_tmp)
		result_=cursor.fetchall()
		if result_==():
			print("There is no result")
			nono=input("Done? Yes or No\n")
			if nono==Yes: init=False
			continue

		another=False
		while another==False:
			result_tmp=pd.DataFrame(result_)
			print(result_tmp)
			print()

			print("0: Finish Search")
			print("1: Select Musics")
			print("2: Search Another")
			select=int(input("Enter: "))
			print()
			if select==0: 
				init=False
				another=True
				print("Finish Creating!")
			elif select==2: another=True
			elif select==1: 
				songs=input("Enter the number you want\nYou have to use comma to write\n=>")
				songs=songs.split(',')
				songs=[int(i) for i in songs]
				n=len(songs)

				for i in songs:
					sql_artist=("SELECT a_index FROM artist WHERE name='%s'"%result_[i]['artist'])
					cursor.execute(sql_artist)
					result_tmp=cursor.fetchall()
					artist_n=result_tmp[0]['a_index']
					tmp=(pl_index,producer,result_[i]['music'],result_[i]['album'],artist_n)
					sql_inpl=("""insert into in_playlist(playlist, producer, music, album, artist) values (%s,%s,'%s','%s',%s)"""%tmp)
					cursor.execute(sql_inpl)
					db.commit()	

def search_playlist(): #여기서는 playlist 재생 구현
	global result_login
	global today_date
	init=True
	while init==True:
		key=input("Enter Keyword: ")
		key='%'+key+'%'
		sql_sp=("SELECT pl_name, u.name as creator, pl_index, producer FROM playlist as pl,user as u WHERE u.u_index=pl.producer AND pl_name LIKE '%s'"%key)
		cursor.execute(sql_sp)
		result_=cursor.fetchall()
		result=pd.DataFrame(result_)
		if result_==():
			print("There is no result")
			continue
		print(result)
		print()
		print("1. Choose a Playlist")
		print("0. Back")
		cmd=int(input("Enter Number: "))

		if cmd==0: 
			init=False
			continue
		elif cmd==1:
			pln=int(input("Enter the number playlist you want: "))
			select_pl=result.loc[[pln],:]
			print(select_pl)
			ttmp=(result_[pln]['pl_index'],result_[pln]['producer'])
			sql=("SELECT* FROM in_playlist WHERE playlist=%s AND producer=%s"%ttmp)
			cursor.execute(sql)
			rr_=cursor.fetchall()
			rr=pd.DataFrame(rr_)
			print(rr)
			print("1. Play this Playlist")
			print("0. Back")
			play=int(input("Enter the Number: "))

			if play==1:
				for row in rr_:
					print("play",row['music'])
					str_update(row['music'],row['artist'],row['album'],today_date)
					streaming()
					time.sleep(5)

def show_my_playlist(): #여기서 playlist재생과 내 playlist삭제 구현
	global result_login
	global today_date
	init=True
	while init==True:
		sql_sp=("SELECT pl_name, u.name as creator, pl_index, producer FROM playlist as pl,user as u WHERE u.u_index=pl.producer AND u.u_index=%s"%result_login[0]['u_index'])
		cursor.execute(sql_sp)
		result_=cursor.fetchall()
		result=pd.DataFrame(result_)
		if result_==():
			print("\nThere is no result")
			init=False
			continue
		print(result)
		print()
		print("1. Choose a Playlist")
		print("0. Back")
		cmd=int(input("Enter Number: "))

		if cmd==0: 
			init=False
			continue
		elif cmd==1:
			pln=int(input("Enter the number playlist you want: "))
			select_pl=result.loc[[pln],:]
			print(select_pl)
			print()
			ttmp=(result_[pln]['pl_index'],result_[pln]['producer'])
			sql=("SELECT* FROM in_playlist WHERE playlist=%s AND producer=%s"%ttmp)
			cursor.execute(sql)
			rr_=cursor.fetchall()
			if rr_==():
				print("There is no result")
				continue
			rr=pd.DataFrame(rr_)
			print(rr)
			print("1. Play this Playlist")
			print("2. Delete this Playlist")
			print("0. Back")
			play=int(input("Enter the Number: "))

			if play==1:
				for row in rr_:
					print("play",row['music'])
					str_update(row['music'],row['artist'],row['album'],today_date)
					streaming()
					time.sleep(5)

			elif play==2:
				ch=input("Are you really going to delete this playlist? Yes or No\n")
				if ch=='yes':
					sql_del=("DELETE FROM in_playlist WHERE playlist=%s AND producer=%s"%ttmp)
					cursor.execute(sql_del)
					db.commit()
					sql_del=("DELETE FROM playlist WHERE pl_index=%s AND producer=%s"%ttmp)
					cursor.execute(sql_del)
					db.commit()
					print("Delete done!")

#def edit_my_playlist(): #playlist선택후 노래를 추가하거나 삭제하는 함수 구현
def show_chart():
	global today_date

	servant=True
	while servant==True:
		print("1. Today's Chart")
		print("2. Monthly Chart")
		print("3. You wish to Pick speicfic day or month")
		print("0. Back")
		service=int(input("Enter the num: "))

		if service==1: #today
			keep=True
			while keep==True:
				top=int(input("Data Entry: "))
				tmp=(today_date,top)
				sql=("SELECT a.name, str.music, str.album FROM date_stream AS str, artist AS a WHERE a.a_index=str.artist AND str_date LIKE '%s' ORDER BY str.str_cnt DESC LIMIT %s"%tmp)
				cursor.execute(sql)
				result=cursor.fetchall()
				result=pd.DataFrame(result)
				print(result)
				print()
				nnn=int(input("Enter 0 for Back: "))
				if nnn==0: keep=False

		if service==2: #this month
			keep=True
			while keep==True:
				year=str(datetime.today().year)
				month=str(datetime.today().month)
				mo=year+'-'+month+'-'+'__'
				top=int(input("Data Entry: "))
				tmp=(mo,top)
				sql=("SELECT a.name as artist,str.music, str.album FROM date_stream AS str, artist AS a WHERE a.a_index=str.artist AND str.str_date LIKE '%s' GROUP BY str.music,str.artist,str.album ORDER BY SUM(str.str_cnt) DESC LIMIT %s"%tmp)
				cursor.execute(sql)
				result=cursor.fetchall()
				if result==():
					print("There is no result")
					continue
				result=pd.DataFrame(result)
				print(mo, ' Chart')
				print(result)
				print()
				nnn=int(input("Enter 0 for Back: "))
				if nnn==0: keep=False

		if service==3: #wish day
			keep=True
			while keep==True:
				year=input("input year ex)2020,2019\n")
				month=input("input month ex)01,02,04,12\n")
				date=input("input date ex)15,06\n if you dont wanna input data enter '__'\n")
				mo=year+'-'+month+'-'+date
				top=int(input("Data Entry: "))
				tmp=(mo,top)
				sql=("SELECT a.name as artist,str.music, str.album FROM date_stream AS str, artist AS a WHERE a.a_index=str.artist AND str.str_date LIKE '%s' GROUP BY str.music,str.artist,str.album ORDER BY SUM(str.str_cnt) DESC LIMIT %s"%tmp)
				
				cursor.execute(sql)
				result=cursor.fetchall()
				if result==():
					print("There is no result")
					continue
				result=pd.DataFrame(result)
				print(mo, ' Chart')
				print(result)
				print()
				nnn=int(input("Enter 0 for Back: "))
				if nnn==0: keep=False

		if service==0: servant=False
			
def manipulate_music(): #music add, delete (앨범과 아티스트가 있다고 가정)
	global today_date
	mani=True
	while mani==True:
		print("1. Add new Music")
		print("2. Delete Music")
		print("0. Back")
		man=int(input("Enter the Num: "))

		if man==0: mani=False

		elif man==1: #Add music!
			artist=input("Artist: ")
			album=input("Album: ")
			music_name=input("Music: ")

			sql=("SELECT* FROM artist WHERE NAME='%s'"%artist)
			cursor.execute(sql)
			tuple_artist=cursor.fetchall()
			if tuple_artist==(): 
				print("There is NO artist")
			else:
				sql=("SELECT* FROM album WHERE album_name='%s' AND artist=%s"%(album,tuple_artist[0]['a_index']))
				cursor.execute(sql)
				tuple_album=cursor.fetchall()

				if tuple_album==(): print("There is NO album")
				else:
					artist=tuple_artist[0]['a_index']
					tmp=(music_name,artist,tuple_album[0]['album_name'])
					sql=("SELECT* FROM music WHERE music_name='%s' AND artist=%s AND album='%s'"%tmp)
					cursor.execute(sql)
					tuple_music=cursor.fetchall()

					if tuple_music!=(): print("There is music already")
					else:
						tmp=(music_name,today_date,artist,tuple_album[0]['album_name'])
						sql=("insert into music(music_name,enroll_date,artist,album) values ('%s','%s',%s,'%s')"%tmp)
						cursor.execute(sql)
						tmp=(0,music_name,artist,tuple_album[0]['album_name'],today_date)
						sql=("insert into date_stream(str_cnt,music,artist,album,str_date) values (%s,'%s',%s,'%s','%s')"%tmp)
						cursor.execute(sql)
						db.commit()
						print("Add Finish!")

		elif man==2: #Delete music!
			artist=input("Artist: ")
			album=input("Album: ")
			music_name=input("Music: ")

			sql=("SELECT* FROM artist WHERE NAME='%s'"%artist)
			cursor.execute(sql)
			tuple_artist=cursor.fetchall()

			if tuple_artist==(): 
				print("There is NO artist")
			else:
				sql=("SELECT* FROM album WHERE album_name='%s'"%album)
				cursor.execute(sql)
				tuple_album=cursor.fetchall()

				if tuple_album==(): print("There is NO album")
				else:
					artist=tuple_artist[0]['a_index']
					tmp=(music_name,artist,album)
					sql=("SELECT* FROM music WHERE music_name='%s' AND artist=%s AND album='%s'"%tmp)
					cursor.execute(sql)
					tuple_music=cursor.fetchall()

					if tuple_music==(): print("There is no music already")

					else:
						tmp=(music_name,artist,album)
						sql0=("DELETE FROM date_stream WHERE music='%s' AND artist=%s AND album='%s'"%tmp)
						sql1=("DELETE FROM in_playlist WHERE music='%s' AND artist=%s AND album='%s'"%tmp)
						sql2=("DELETE FROM music WHERE music_name='%s' AND artist=%s AND album='%s'"%tmp)
						cursor.execute(sql0)
						cursor.execute(sql1)
						cursor.execute(sql2)
						db.commit()
						print("Delete Finish!")

def manipulate_artist(): #artist add만 
	man=True
	while man==True:
		print("You can just add new artist")
		print("1. Keep going")
		print("0. Back")

		keep=int(input("Enter the Num: "))

		if keep==1:
			artist=input("Input the new artist name: ")
			sql=("SELECT* FROM artist WHERE name='%s'"%artist)
			cursor.execute(sql)
			result_a=cursor.fetchall()

			if result_a!=(): print("There is artist already")
			else:
				sql=("SELECT MAX(a_index) as max FROM artist")
				cursor.execute(sql)
				max_index=cursor.fetchall()
				a_index=max_index[0]['max']+1
				b_date=input("Input birth form (____-__-__) or None: ")

				if b_date.lower()=='none': b_date='NULL'
				else: b_date="'"+b_date+"'"
				tmp=(a_index,artist,b_date)

				sql=("insert into artist(a_index,name,b_date) values (%s,'%s',%s)"%tmp)
				cursor.execute(sql)
				db.commit()

				print("Add artist Finish!")
		else: man=False

def manipulate_album(): #album add,delete (아티스트가 있다고 가정) #album을 지우니까 album속 수록곡들도 모두 지워버릴 예정 
	global today_date
	mani=True
	while mani==True:
		print("1. Add new Album")
		print("2. Delete Album")
		print("0. Back")
		man=int(input("Enter the Num: "))

		if man==0: mani=False

		elif man==1: #Add Album!
			artist=input("Artist: ")
			album=input("Album: ")

			sql=("SELECT* FROM artist WHERE NAME='%s'"%artist)
			cursor.execute(sql)
			tuple_artist=cursor.fetchall()
			if tuple_artist==(): 
				print("There is NO artist")
			else:
				sql=("SELECT* FROM album WHERE album_name='%s' AND artist=%s"%(album,tuple_artist[0]['a_index']))
				cursor.execute(sql)
				tuple_album=cursor.fetchall()

				if tuple_album!=(): print("There is an Album already")
				else:
					artist=tuple_artist[0]['a_index']
					tmp=(album,today_date,artist)
					sql=("insert into album(album_name,enroll_date,artist) values ('%s','%s',%s)"%tmp)
					cursor.execute(sql)
					db.commit()
					print("Add Finish!")

		elif man==2: #Delete music!
			artist=input("Artist: ")
			album=input("Album: ")

			sql=("SELECT* FROM artist WHERE NAME='%s'"%artist)
			cursor.execute(sql)
			tuple_artist=cursor.fetchall()
			if tuple_artist==(): 
				print("There is NO artist")
			else:
				sql=("SELECT* FROM album WHERE album_name='%s' AND artist=%s"%(album,tuple_artist[0]['a_index']))
				cursor.execute(sql)
				tuple_album=cursor.fetchall()

				if tuple_album==(): print("There is no Album already")
				else:
					artist=tuple_artist[0]['a_index']
					tmp=(artist,album)
					sql_music=("SELECT* FROM music WHERE artist=%s AND album='%s'"%tmp)
					cursor.execute(sql_music)
					result_music=cursor.fetchall()

					for row in result_music:
						tmptmp=(row['music_name'],album,artist)
						sql_str_=("DELETE FROM date_stream WHERE music='%s' AND album='%s' AND artist=%s"%tmptmp)
						sql_pl_del=("DELETE FROM in_playlist WHERE music='%s' AND album='%s' AND artist=%s"%tmptmp)
						cursor.execute(sql_str_)
						cursor.execute(sql_pl_del)

					db.commit()
					sql_music_del=("DELETE FROM music WHERE artist=%s AND album='%s'"%tmp)
					cursor.execute(sql_music_del)
					db.commit()
					sql_album_del=("DELETE FROM album WHERE artist=%s AND album_name='%s'"%tmp)
					cursor.execute(sql_album_del)
					db.commit()

					print("Finish Delete Album")

def manipulate_user(): #user add, delete, update
	mani=True
	while mani==True:
		sql=("SELECT * FROM user")
		cursor.execute(sql)
		show=cursor.fetchall()
		show_=pd.DataFrame(show)
		print(show_)
		print("\n1. User add")
		print("2. User delete")
		print("3. User info Update")
		print("0. Back")
		serr=int(input("Enter the Num: "))

		if serr==0: mani=False
		elif serr==1:
			sql=("SELECT MAX(u_index) AS max FROM user")
			cursor.execute(sql)
			user_num=cursor.fetchall()
			user_num=user_num[0]['max']
			u_index=user_num+1
			name=input("name (necessary): ")
			email=input("email: ")
			phone_num=input("phone num (necessary): ")
			bdate=input("birth date ('____-__-__'form) (necessary): ")
			sex=input("sex (necessary): ")
			password=input("password (necessary): ")
			tmp=(u_index,email,phone_num,name,bdate,sex,password)
			sql=("insert into user(u_index,email,phone_num,name,bdate,sex,password) values (%s, '%s', '%s', '%s', '%s', '%s', '%s')"%tmp)
			cursor.execute(sql)
			db.commit()
			print("Finish!\n")
		elif serr==2:
			del_u=int(input("Enter the index: "))
			sql1=("DELETE FROM in_playlist WHERE producer=%s"%del_u)
			sql2=("DELETE FROM playlist WHERE producer=%s"%del_u)
			sql3=("DELETE FROM user WHERE u_index=%s"%del_u)
			cursor.execute(sql1)
			cursor.execute(sql2)
			cursor.execute(sql3)
			db.commit()
			print("Finish!\n")
		elif serr==3:
			up_u=int(input("Enter the index: "))
			area=input("Update Area: ")
			new=input("Update Contents: ")
			tmp=(area,new,up_u)
			sql=("UPDATE user SET %s='%s' WHERE u_index=%s"%tmp)
			cursor.execute(sql)
			db.commit()
			print("Finish Update!")

exe=True
#User Main
while exe==True and manager==0:
	print("What Kind of Service do you want?")
	print("1. Search All")
	print("2. Search by Music")
	print("3. Search by Artist")
	print("4. Search by Album") 
	print("5. Playlist")
	print("6. Show Chart")
	print("0. Finish Program")
	input_exe=input("Enter Number: ")
	ser=int(input_exe)

	if ser==0: exe=False
	elif ser==1: search_all()	
	elif ser==2: search_music()
	elif ser==3: search_artist()
	elif ser==4: search_album()
	elif ser==5:
		exe_play=True
		while exe_play==True:
			print("1. Create New Playlist")
			print("2. Show Your Playlist")
			print("3. Search Playlist")
			#print("4. Edit Your Playlist")
			print("0. Back")
			input_play=int(input("Enter Number: "))
			if input_play==0: exe_play=False
			elif input_play==1: create_playlist()
			elif input_play==2: show_my_playlist()
			elif input_play==3: search_playlist()
			#elif input_play==4: edit_my_playlist()
	elif ser==6: show_chart() 

#Manager Main
while exe==True and manager==1:
	print("What Kind of Service do you want?")
	print("1. Manipulate Music")
	print("2. Manipulate Artist")
	print("3. Manipulate Album")
	print("4. Manipulate User")
	print("0. Finish Program")
	input_exe=input("Enter Number: ")
	ser=int(input_exe)

	if ser==0: exe=False
	elif ser==1: manipulate_music()	
	elif ser==2: manipulate_artist()
	elif ser==3: manipulate_album()
	elif ser==4: manipulate_user()

print("\nProgram Finish!\n")