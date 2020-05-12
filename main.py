import os
global file
file = "nothing"

while True:
	try:
		gelen = raw_input("file:"+file+" >")
		if "file" in gelen:
			file = gelen.split(" ")[1]
		elif gelen == "run":
			if file != "nothing":
				os.system("alti "+file)
			else:
				print "File not found."
				pass
		elif gelen == "debug":
	                 if file != "nothing":
	                         os.system("alti "+file+" d")
	                 else:
	                         print "File not found."
	                         pass
		elif gelen == "cgibi":
	                 if file != "nothing":
	                         os.system("alti "+file+" a")
	                 else:
	                         print "File not found."
	                         pass
		elif gelen == "edit":
			if file != "nothing":
				os.system("nano "+file)
			else:
				print "File not found"
				pass
		elif "new" in gelen:
			print "yeni dosya"
			os.system("echo bits 64 >> "+gelen.split(" ")[1])
		elif "search" in gelen:
			print ""
			print os.popen("locate "+gelen.split(" ")[1]).read()
		elif gelen == "exit":
			break
		elif gelen == "help":
			print "newfile dosya.asm\nrun\ndebug\nedit\ncgibi\nsearch\nfile"
		else:
			print "hatali komut. help yazarak komulari gorebilirsiniz"
			pass
	except:
		print ""
