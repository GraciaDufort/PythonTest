import subprocess

javaCmdResult = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT).decode("utf-8")
cmdResultString = javaCmdResult.partition('\n')[0]


def checkJavaExists():
	if "not recognized" not in cmdResultString:
		return "Yes"
	else:
		return "No"

def checkJavaVersion():
	return cmdResultString


isJavaInstalled = checkJavaExists()
finalResult = "Is Java Installed: " + isJavaInstalled + "\n"

if isJavaInstalled == "Yes":
	finalResult += "Java Version: "+checkJavaVersion() + "\n"

print(finalResult)