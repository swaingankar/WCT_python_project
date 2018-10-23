import shutil
import os
import sys
try:
	try:
		os.environ["JENKINS_WORKSPACE"]
	except KeyError:
		print("Please set the environment variable ")
		sys.exit(1)
	direc = os.environ.get("JENKINS_WORKSPACE")
	print(direc)
	if not os.path.exists(direc+"/WCT_jenkins_pytest/allure-results/history"):
		os.mkdir(direc+"/WCT_jenkins_pytest/allure-results/history")
		
	files = os.listdir(direc+"/WCT_jenkins_pytest/allure-report/history")
	print(files)
	for f in files:
		shutil.copy(direc+"/WCT_jenkins_pytest/allure-report/history/"+f,direc+"/WCT_jenkins_pytest/allure-results/history",follow_symlinks=True)
except Exception as e:
	print("Error message : " + format(e))	