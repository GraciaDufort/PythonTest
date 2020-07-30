import subprocess
from urllib.request import urlopen, Request


def checkJavaExists():
	if "not recognized" not in cmdResultString:
		return "Yes"
	else:
		return "No"

def checkJavaVersion():
	return cmdResultString
	
def download(url, filename):
    print(url)
    print(filename)
    javaFile = urlopen(url)
    with open(filename, 'wb+') as save:
        save.write(javaFile.read())



javaCmdResult = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT).decode("utf-8")
cmdResultString = javaCmdResult.partition('\n')[0]

isJavaInstalled = checkJavaExists()
finalResult = "Is Java Installed: " + isJavaInstalled + "\n"

if isJavaInstalled == "Yes":
	finalResult += "Java Version: "+checkJavaVersion() + "\n"
	

if isJavaInstalled == "No":
	url = 'http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-windows-x64.exe'
	filename = 'jdk-8u131-windows-x64.exe'
	download(url, filename)

print(finalResult)