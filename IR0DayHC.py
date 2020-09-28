# Hash Cracker !
import hashlib
import click
import os
os.system("cls")
os.system("clear")
click.secho("""
		─────█─▄▀█──█▀▄─█─────
		────▐▌──────────▐▌────
		────█▌▀▄──▄▄──▄▀▐█────
		───▐██──▀▀──▀▀──██▌───
		──▄████▄──▐▌──▄████▄──
		     I̷R̷0̷D̷a̷y̷.̷T̷o̷d̷a̷y̷       
""", fg = "black" ,bg = "red" ,blink=True)
click.secho("""
		IR0Day.Today Hash Craker
		  Write By : X0P4SH4
		  Tnx To : Armya_Evil
		  Tele : LearnExploit
		       V 1.0
""", fg = "white" ,bg = "blue")
print (''' 

        ''')
click.secho("Use help | more information", bg="white", fg="red")
clcik_1 = click.command()
class Help:
	def Info(self):
			print ('''
		[1]-ɪɴғᴏ
		[2]-ʜᴀsʜ
		[3]-ᴇxɪᴛ
				''')
	def Exit(self):
			print(" bY !@")
	def hashcrack(self):
			print('''
		[1]-ᴍᴅ5
		[2]-sʜᴀ1
		[3]-sʜᴀ224
		[4]-sʜᴀ256
		[5]-sʜᴀ384
		[6]-sʜᴀ512
				''')
get_calss = Help()

class allhash():
	def MD5(self,hashmd5):
		return hashlib.md5(hashmd5.encode()).hexdigest().lower()
	def SHA1(self, s1):
		return hashlib.sha1(s1.encode()).hexdigest().lower()
	def SHA224(self, s224):
		return hashlib.sha224(s224.encode()).hexdigest().lower()
	def SHA256(self, s256):
		return hashlib.sha256(s256.encode()).hexdigest().lower()
	def SHA384(self, s384):
		return hashlib.sha384(s384.encode()).hexdigest().lower()
	def SHA512(self, s512):
		return hashlib.sha512(s512.encode()).hexdigest().lower()



# =============  user inputs  : =====================
class get_user():
	def getuserhash(self):
		get_userhash = str(input("Input Your Hash : ").lower())
		return get_userhash
	def passlist(self):
		pass_list = input("Input Your PassList : ")
		file = open(pass_list, "r").readlines()
		return file
# ====================== end ========================


def user_hash():
	hash1 = str(input("XOP4SH4 ~ Hash#: "))
	if hash1 == "help" or hash1 == "Help":
		get_calss.hashcrack()
		return user_hash()
		# *****************  MD5 Started Here : 
	elif hash1 == "md5" or hash1 == "Md5" or hash1 == "1":
		hash_ = get_user.getuserhash(self='')
		file = get_user.passlist(self='')
		allHash = allhash()
		for i in file:
			md5 = allHash.MD5(i)
			if hash_ == md5:
				print("Your Md5 hash is:",i)
				return user_hash()
			else:
				print("not found",hash_)
		return user_hash()
		# ***************** SHA1 Started Here : 
	elif hash1 == "Sha1" or hash1 == "sha1" or hash1 == "2":
		hash_ = get_user.getuserhash(self='')
		file = get_user.passlist(self='')
		allHash = allhash()
		for i in file:
			sha1 = allHash.SHA1(i)
			if hash_ == sha1:
				print("Your Sha1 hash is:",i)
				return user_hash()
			else:
				print("not found",hash_)
		return user_hash()
		# SHA224 started Here : 
	elif hash1 == "Sha224" or hash1 == "sha224" or hash1 == "3":
		hash_ = get_user.getuserhash(self='')
		file = get_user.passlist(self='')
		allHash = allhash()
		for i in file:
			sha224 = allHash.SHA224(i)
			if hash_ == sha224:
				print("Your Sha224 hash is:",i)
				return user_hash()
			else:
				print("not found",hash_)
		return user_hash()
	elif hash1 == "Sha256" or hash1 == "sha256" or hash1 == "4":
		hash_ = get_user.getuserhash(self='')
		file = get_user.passlist(self='')
		allHash = allhash()
		for i in file:
			sha256 = allHash.SHA256(i)
			if hash_ == sha256:
				print("Your Sha256 hash is:",i)
				return user_hash()
			else:
				print("not found",hash_)
		return user_hash()
	elif hash1 == "Sha384" or hash1 == "sha384" or hash1 == "5":
		hash_ = get_user.getuserhash(self='')
		file = get_user.passlist(self='')
		allHash = allhash()
		for i in file:
			sha384 = allHash.SHA384(i)
			if hash_ == sha384:
				print("Your Sha384 hash is:",i)
				return user_hash()
			else:
				print("not found",hash_)
		return user_hash()
	elif hash1 == "Sha512" or hash1 == "sha512" or hash1 == "6":
		hash_ = get_user.getuserhash(self='')
		file = get_user.passlist(self='')
		allHash = allhash()
		for i in file:
			sha512 = allHash.SHA512(i)
			if hash_ == sha512:
				print("Your Sha512 hash is:",i)
				return user_hash()
			else:
				print("not found",hash_)
		return user_hash()

	else:
		click.secho("             Use Help commadn to see functions", bg = "red" ,fg = "black", bold= "")
		click.secho("                     IR0Day.Today is Here     ", bg = "red" ,fg = "black", bold="")
		return user_hash()

def get1():
	''' class input :) '''
	a = str(input("XOP4SH4~#: "))

	if a == "help" or a == "info" or a == "1":	
		get_calss.Info()
		return get1()
	elif a == "hash" or a == "Hash" or a == "2":
		# get_calss.hashcrack()
		return user_hash()
	elif a == "Exit" or a == "exit" or a == "3":
		get_calss.Exit()
		exit()
	else:
		print("valu not found !")
		return get1()

p = get1()

