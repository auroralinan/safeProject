__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import web
import json
import random


# import pwd.train_pwd as trp
import signature.train_signature as trs



bankdb = web.database(dbn='mysql', host='192.168.81.15', port=3306, db='bankassistant', user='root', pw='root')

urls = (
	"/test", "test",
	"/signature", "signature",
	"/login", "login",
	"/password", "password",
	"/upload", "Upload",
	"/getcardid", "getCardid",
	"/getrest", "getRest",
	"/newuser", "newUser",
	"/newcard", "newCard",
	"/isexistun", "isExistUN",
	"/identifycode", "identifyCode",
	"/transfer", 'transfer',
	"/receivedata", 'receiveData',
	"/confirmpaied", 'confirmPaied',
	"/changepassword", "changePassword",
	"/deletesign", "deleteSign",
	"/deletephoto", "deletePhoto",
)

# class ClassName:
# 	def GET(self):
# 		pass
#
# 	def POST(self):
# 		pass

def findinfowithid(cardid):
	str = cardid[:6]
	global bankdb
	res = bankdb.select('card_bank', what='bank, type', where="num='{}'".format(str))
	try:
		return dict(res[0])
	except:
		return {'bank': 'unknown', 'type': 'unknown'}

def jsondump(data):
	return json.dumps(data)

def transferPaied(transid):
	global bankdb
	rest = 'rest'
	try:
		res = bankdb.select('trans_log', what='transcardid, amount, fee', where="transid={}".format(transid))
		temp = res[0]
		cardid = temp.transcardid
		amount = temp.amount
		fee = temp.fee
		bankdb.select('card', what='rest', where="cardid='{}'".format(cardid), _test=True)
		res = bankdb.select('card', what='rest', where="cardid='{}'".format(cardid))
		temp = res[0]
		rest = temp.rest
		print rest
	except:
		return 'read card info wrong!'
	amount = float(amount)
	rest = float(rest)
	fee = float(fee)
	rest = rest - amount - fee
	if rest > 0:
		try:
			bankdb.update('card', where="cardid='{}'".format(cardid), rest='{}'.format(rest), _test=True)
			res = bankdb.update('card', where="cardid='{}'".format(cardid), rest='{}'.format(rest))
			bankdb.update('trans_log', where="transid={}".format(transid), payinfo='1', _test=True)
			res = bankdb.update('trans_log', where="transid={}".format(transid), payinfo='1')
			print 'change rest done!'
			return 'ok'
		except:
			return 'change rest wrong!'

def transferReceived(transid):
	global bankdb
	return bankdb.update('trans_log', where="transid={}".format(transid), receivedinfo='1')

def verify(username, tag):
	if tag == 'signature':
		return 1
	elif tag == 'password':
		return 1
	elif tag == 'identity':
		return 1
	else:
		return 1

def train(username, tag):
	if tag == 'signature':
		# return trs.train(username, bankdb)
		return 1
	elif tag == 'password':
		# return trp.train(username, bankdb)
		return 1
	elif tag == 'identity':
		return 1

def getTestTimes(username, type_):
	colname = type_ + 'Times'
	print 'get test times for {} in {}'.format(username, colname)
	global bankdb
	res = bankdb.select('user_verify', where="username='{}'".format(username), what=colname)
	try:
		num = res[0][colname]
		num = int(num) +1
		bankdb.query("UPDATE user_verify SET {}={} WHERE username='{}'".format(colname, num, username), _test=True)
		bankdb.query("UPDATE user_verify SET {}={} WHERE username='{}'".format(colname, num, username))
		return num
	except:
		return 99
# def dbconn():
# 	# myvar = dict(name="Bob")
# 	# results = db.select('mytable', myvar, where="name = $name")
# 	# where_dict = {'col1': 1, col2: 'sometext'}
# 	# db.delete('mytable', where=web.db.sqlwhere(where_dict, grouping=' OR '), _test=True)
# 	global bankdb
# 	bankdb.select('user_info', what='password', where="username='linan'", _test=True)
# 	results = bankdb.select('user_info', what='password', where="username='linan'")
# 	return results


class test:
	def GET(self):
		return self.POST()

	def POST(self):
		return transferPaied(1)

class signature:
	def GET(self):
		return "signature"

	def POST(self):
		data = web.input()
		return random.choice((True, False))

class identifyCode:
	def GET(self):
		return self.POST()

	def POST(self):
		data = web.input()
		return random.choice((True, False))

class login:
	def GET(self):
		return self.POST()

	def POST(self):
		data = web.input()
		print data
		if 'username' in data.keys():
			username = data.username
			password = data.password
			global bankdb
			res = bankdb.select('user_info', what='password', where="username='{}'".format(username))
			try:
				pwd = res[0].password
				if password == pwd:
					return 1
				else:
					return 'password wrong!'
			except:
				return 'username is not exist!'
		else:
			return 'input data wrong!'

class password:
	def GET(self):
		return "password!"

	def POST(self):
		data = web.input()
		return random.choice((True, False))

class Upload:
    def GET(self):
        return "upload!"

    def POST(self):
        x = web.input()
        print x.keys()
        filename = x.filename
        filedir = 'photo/user'
        fout = open(filedir + '/' + filename, 'wb')
        fout.write(x.file)
        fout.close()

class getCardid:
    def GET(self):
        return self.POST()

    def POST(self):
		data = web.input()
		print(data)
		if 'username' in data.keys():
			username = data.username
			global bankdb
			bankdb.select('user_info', what='uid', where="username='{}'".format(username), _test=True)
			resUid = bankdb.select('user_info', what='uid', where="username='{}'".format(username))
			try:
				lengthUid = len(resUid)
				if lengthUid != 1:
					return 'detected multi usernames exist!'
			except:
				return 'did not find this user information!'
			uid = resUid[0].uid
			bankdb.select('card', what='cardid', where="uid={}".format(uid), _test=True)
			resCard = bankdb.select('card', what='cardid', where="uid={}".format(uid))
			try:
				carddict = {'cardid':[]}
				for i in resCard:
					temp = dict(i)
					carddict['cardid'].append(temp['cardid'])
					print carddict
					string = string = '[' +', '.join('"' + str(i) + '"' for i in carddict['cardid']) + ']'
				return string
			except:
				return 'no cards of this username!'
		else:
			return 'could not find username!'


class getRest:
	def GET(self):
		return self.POST()

	def POST(self):
		data = web.input()
		if 'cardid' in data.keys():
			card = data.cardid
			global bankdb
			bankdb.select('card', what='rest, name', where="cardid='{}'".format(card), _test=True)
			resRest = bankdb.select('card', what='rest, name', where="cardid='{}'".format(card))
			try:
				lengthRest = len(resRest)
				if lengthRest != 1:
					return 'detected multi cards exist!'
			except:
				return 'did not find card information!'
			temp = dict(resRest[0])
			return jsondump(temp)
		else:
			return 'could not find cardid!'

class newUser:
	def GET(self):
		return self.POST()

	def POST(self):
		data = web.input()
		username = data.username
		password = data.password
		global bankdb
		try:
			bankdb.insert('user_verify', username=username, passwordTimes=0, signatureTimes=0, identityTimes=0)
			return bankdb.insert('user_info', username=username, password=password, pwdstatus=0, signstatus=0, photostatus=0, identitystatus=0)
		except:
			return 'something wrong!'



class newCard:
	def GET(self):
		return self.POST()

	def POST(self):
		data = web.input()
		if 'cardid' in data.keys():
			cardid = data.cardid
			global bankdb
			bankdb.select('card', where="cardid='{}'".format(cardid), _test=True)
			resUser = bankdb.select('card', where="cardid='{}'".format(cardid))
			try:
				lengthCard = len(resUser)
				if lengthCard > 0:
					return 'sorry, this card is already be logged.'
				else:
					bankdb.select('user_info', what='uid', where="username='{}'".format(data.username), _test=True)
					resUid = bankdb.select('user_info', what='uid', where="username='{}'".format(data.username))
					uid = resUid[0].uid
					randnum = random.uniform(1, 10000)
					temp = findinfowithid(cardid)
					bank = temp['bank']
					type_ = temp['type']
					name = data.name
					bankdb.insert('card', cardid=cardid, name=name, phone=data.phone, uid=uid, rest=randnum, bank=bank, type=type_)
					return 'ok'
			except:
				return 'new card wrong'
		else:
			return 'could not find cardid!'

class isExistUN:
	def GET(self):
		return self.POST()

	def POST(self):
		data = web.input()
		if 'username' in data.keys():
			username = data.username
			global bankdb
			bankdb.select('user_info',  where="username='{}'".format(username), _test=True)
			resUser = bankdb.select('user_info', where="username='{}'".format(username))
			try:
				lengthUser = len(resUser)
				print lengthUser
				if lengthUser > 0:
					return 0
				else:
					return 1
			except:
				return 1
		else:
			return 'could not find username!'

class transfer:
	def GET(self):
		return self.POST()

	def POST(self):
		data = web.input()
		if 'transcardid' in data.keys():
			try:
				global bankdb
				recardid = data.receivedcardid
				temp = findinfowithid(recardid)
				print temp
				bank = temp['bank']
				print bank
				bankdb.insert('trans_log', transcardid=data.transcardid, receivedcardid=recardid,
					receivedname=data.receivedname, receivedbank=bank, amount=data.amount, fee=data.fee, payinfo=0, receivedinfo=0, _test=True)
				return bankdb.insert('trans_log', transcardid=data.transcardid, receivedcardid=recardid,
					receivedname=data.receivedname, receivedbank=bank, amount=float(data.amount), fee=float(data.fee), payinfo=0, receivedinfo=0)
			except:
				return 'create transfer wrong!'
		else:
			return 'wrong input data!'

class receiveData:
	def GET(self):
		return self.POST

	def POST(self):
		data = web.input()
		global bankdb
		if "databody" in data.keys():
			username = data.username
			tag = data.tag
			type_ = data.ty
			databody = data.databody
			datadict = json.loads(databody)
			print username, tag, type_, type(datadict), type(databody)
			if tag == 'train':
				num = 1
			else:
				num = getTestTimes(username, type_)
			if type_ == 'signature':
				ty = 'data_' + type_
				for i in range(len(datadict)):
					temp = [int(datadict[i][u'numOfSign']), int(datadict[i][u'time']), float(datadict[i][u'x']), float(datadict[i][u'y']),
					        float(datadict[i][u'p']), float(datadict[i][u's']), datadict[i][u'status']]
					res = bankdb.insert(ty, username=username, tag=tag, num=temp[0], X=temp[2], Y=temp[3], S=temp[5],
					                    Time=temp[1], Pressure=temp[4], move=temp[6])
					if res is not None:
						print 'insert {} {}s as {} data!'.format(temp[0], type_, tag)

			elif type_ == 'identity' or type_ == 'password':
				ty = 'data_' + type_
				for i in range(len(datadict)):
					if datadict[i][u'startX'] == 0 and datadict[i][u'startY'] == 0:
						num += 1
					else:
						temp = [float(datadict[i][u'startX']), float(datadict[i][u'startY']), datadict[i][u'startSize'], int(datadict[i][u'startTime']),
						        float(datadict[i][u'endX']), float(datadict[i][u'endY']), datadict[i][u'endSize'], int(datadict[i][u'endTime']),
						        datadict[i][u'character'], float(datadict[i][u'pressure'])]
						res = bankdb.insert(ty, username=username, tag=tag, num=num, startX=temp[0], startY=temp[1], startS=temp[2],
						              startTime=temp[3], endX=temp[4], endY=temp[5], endS=temp[6], endTime=temp[7],
						              Pressure=temp[9], charKey=temp[8])
						if res is not None:
							print 'insert {} {}s as {} data!'.format(num, type_, tag)
			if tag == 'test':
				#verify and return
				if verify(username, tag) == 1:
					return 1
				else:
					return 0
			else:
				#update status
				d = {}
				d['signature'] = 'signstatus'
				d['password'] = 'pwdstatus'
				d['identity'] = 'identitystatus'
				bankdb.update('user_info', where="username='{}'".format(username), what="{}=1".format(d[tag]), _test=True)
				bankdb.update('user_info', where="username='{}'".format(username), what="{}=1".format(d[tag]))
				return train(username, tag)
		else:
			return 0

class confirmPaied:
	def GET(self):
		pass

	def POST(self):
		data = web.input()
		if 'transid' in data.keys():
			return transferPaied(data.transid)



if __name__ == "__main__":
	# print train('linan', 'signature')
	c
	app = web.application(urls, globals())
	app.run()

