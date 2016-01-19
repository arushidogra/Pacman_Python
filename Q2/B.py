import os
import colorama
from colorama import Fore
import stat
import grp
import pwd
import time
import shutil
colorama.init()
i=1

print "ENTER THE COMMAND NAME"
command=raw_input()
if command=='ls':
	'''
	class hello:
		x=0
	p=sorted(os.listdir('.'))
	#print p
	for a,b,c in os.walk('.'):
		if(i==1):
			q= b
			w= c
			i=i+1
		if(i>1):
			break

		 	
	for f in p:
		if f[0]!='.':
	
			try:
				if q.index(f):
					print(Fore.BLUE + f) + ' ',
					continue
			except ValueError:
		  		pass
	
			try:
				if w.index(f):
					print (Fore.WHITE + f) + ' ',
					continue
			
			except ValueError:
				 pass

			print (Fore.WHITE+f)+' ',
	''' 
	for i in sorted(os.listdir('.')):
		if os.path.isdir(os.path.join(".",i)):
			print(Fore.BLUE + i) ,
		else:
			print(Fore.WHITE + i) ,
elif command=='cp':
	q=raw_input()
	w=raw_input()


	for a,b,c in os.walk('.'):
		break



	while 1:
			try :
				if b.index(q)>=0:#first is a dict in the list
					print "cp: omitting directory " + q
					break
			except ValueError:
				try:
					if c.index(q)>=0: # first is a file in the list
						try :
							if b.index(w)>=0: #second is a directory present
								a=open(q,"r")
								p=a.read()
								os.chdir(w)
								b=open(q,"w")
								b.write(p)
								a.close()
								b.close()
								break
						except ValueError: #second is a file
							a=open(q,"r")
							p=a.read()
							b=open(w,"w")
							b.write(p)
							a.close()
							b.close()
							break
				except ValueError:
					print "cp: cannot stat "+ "'" +q +"'" +": No such file or directory "
					break
elif command=="dirstr":
	def count(folder):
		p=0
		for i in os.listdir(folder):
			if i[0]!='.':
			    p=p+1
		return p
	def fun(folder,n,y):
	#print folder

		if n==0:
		    print "             (EMPTY FOLDER)"
		    y=y-1
		    return
		else:
			for i in sorted(os.listdir(folder)):
	#y=y+1
				if i[0]!='.':
				
			    		if os.path.isdir(os.path.join(folder,i)):
						p=y
						q=y
						r=y
						while q:
						    print ' ',
						    q=q-1
						print '|'
						while p:
						      print " ",
						      p=p-1
				    		print "#----------  Folder Name:" + i +"/  ----------#"
						while r:
						      print " ",
						      r=r-1
				  		print '|'
					
						os.chdir(folder)
						y=y+1
						q=count(i)
	
						fun(i,q,y)
						os.chdir("..")
						y=y-1
				
			    		else:
						p=y
						q=y
						r=y
						while q:
						    print ' ',
						    q=q-1
						print '|'
						while p:
						      print " ",
						      p=p-1
				     		print "#-"+i
						while r:
						      print " ",
						      r=r-1
						print '|'
					
		

	def main():
		folder="folder"
		n=count(folder)
		#print n
		y=0
		fun(folder,n,y)

	main()
elif command=="ls-l":
	a=open("chmod","r")
	n=777
	dic={}
	while n:
		n=n-1
		q=a.readline()
		w=a.readline()
		dic[q[6:-1]]=w.strip()[1:]

	Months={}
	Months={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
	j=os.listdir('.')
	k=0


	for p in j:
		b = str(os.path.getsize(p))
		if(len(b)>k):
			k=len(b)


	for i in sorted(os.listdir('.')):
		if os.path.isdir(os.path.join(".",i)):
			print 'd'+ dic[oct(stat.S_IMODE(os.lstat(i).st_mode))[1:]],
		else:
		 	print '-'+ dic[oct(stat.S_IMODE(os.lstat(i).st_mode))[1:]],
		stat_info = os.stat(i)
		uid = stat_info.st_uid
		gid = stat_info.st_gid

		user = pwd.getpwuid(uid)[0]
		group = grp.getgrgid(gid)[0]
		print user, group,
		b = os.path.getsize(i)
		print b,
		gh=len(str(b))
		gh=k-gh
		while gh:
			print '' ,
			gh=gh-1
		print Months[time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(i)))[0:2]],
		print time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(i)))[3:5],


		if(time.strftime("%p",time.localtime(os.path.getmtime(i)))!="PM"):
			print time.strftime("%I:%M",time.localtime(os.path.getmtime(i))),
		else:

			print int(time.strftime("%I",time.localtime(os.path.getmtime(i))))+12,
			print time.strftime(":%M",time.localtime(os.path.getmtime(i))),


		if os.path.isdir(os.path.join(".",i)):
			print(Fore.BLUE + i)
		else:
			print(Fore.WHITE + i)
	
elif command=="mv":
	for a,b,c in os.walk('.'):
		break
		'''
	try:	
		if b.index(inp1):#imp1 is a directory
			try :
				if c.index(inp2)>=0:# i2 is a file
				     print "mv: cannot overwrite non-directory '"+ inp2 + "' with directory '" + inp1
			except ValueError:#imp1 is not a directory
				#copy i1 into i2
				try:
					if c.index(inp1)>=0:#if imp1 is a file
						try :#if imp2 is a directory
							if b.index(inp2)>=0:
								shutil.move(inp1,inp2)
						except ValueError:	#inp2 is not a directory
						
				excpet 

	'''


	if os.path.isdir(os.path.join(".",inp1)):
		if os.path.isfile(os.path.join(".",inp2)):
			print "mv: cannot overwrite non-directory " + inp2 + "' with directory '" + inp1 + "'"
		elif os.path.isdir(os.path.join(".",inp2)):
			shutil.move(inp1,inp2)
		else:
			os.mkdir(inp2)
			shutil.move(inp1,inp2)

	elif os.path.isfile(os.path.join(".",inp1)):
		if os.path.isfile(os.path.join(".",inp2)):
			q=open(inp1,"r")
			w=q.read()
			e=open(inp2,"w")
			e.write(w)
			q.close()
			os.remove(inp1)
			e.close()
		elif os.path.isdir(os.path.join(".",inp2)):
			shutil.move(inp1,inp2)

		else :
			os.rename(inp1,inp2)
	else:
		print "mv: cannot stat " + inp1 + "': No such file or directory"

elif command=="rm":

	a=raw_input()
	for q,b,c in os.walk("."):
		break
	if os.path.isdir(os.path.join(".",a)): #it is a directory
		#shutil.rmtree(a)
		print "cannot remove" + a +" Is a directory."
	else:
		try:
			if c.index(a) >=0:#it is a file
				os.remove(a)
		except:
			print "rm: cannot remove '"+a +"': No such file or directory"

elif command=="rm-r":

	a=raw_input()
	for q,b,c in os.walk("."):
		break
	if os.path.isdir(os.path.join(".",a)): #it is a directory
		shutil.rmtree(a)
	
	else:
		try:
			if c.index(a) >=0:#it is a file
				os.remove(a)
		except:
			print "rm: cannot remove '"+a +"': No such file or directory"
	

elif command=="ls>>":
	print "Enter the name of the file you want to redirect to"
	file1=raw_input()
	q=open(file1,"w")
	a=" "
	for i in sorted(os.listdir('.')):
		a=a+i+ " "
	q.write(a)
	q.close()
	#print 
	#print dic.sort()

	


