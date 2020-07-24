import subprocess

def checkJavaVersion():
	return subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)

version = checkJavaVersion()	
print(version)