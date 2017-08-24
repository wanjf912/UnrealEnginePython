#ue.exec('pip2.py')

import subprocess
import sys
import os
import unreal_engine as ue
import _thread as thread

#ue.log(sys.path)

#define some convenience paths
def PythonHomePath():
	for path in sys.path:
		if ('UnrealEnginePython' in path and
			path.endswith('Binaries/Win64')):
			return path
	
	#return sys.path[1]
	return "not found"

def PythonHomeScriptsPath():
	home = PythonHomePath()
	return home + "/Scripts"

def PythonPluginScriptPath():
	tempPath = "not found"

	for path in sys.path:
		if ('UnrealEnginePython' in path and
			path.endswith('Content/Scripts')):
			tempPath = path
			break

	return tempPath

def PythonProjectScriptPath():
	relativePath = PythonPluginScriptPath() + "/../../../../Content/Scripts";
	return os.path.abspath(relativePath);

def AsAbsPath(path):
	return os.path.abspath(path)

_PythonHomePath = PythonHomePath()

def FolderCommand(folder):
	#replace backslashes
	folder = folder.replace('/','\\')

	changefolder = "cd /d \"" + folder + "\" & "
	return changefolder

#main public function
def run(process, path=_PythonHomePath, verbose=True):
	#todo: change folder
	fullcommand = FolderCommand(path) + process
	if verbose:
		ue.log("Started cmd <" + fullcommand + ">")
	stdoutdata = subprocess.getstatusoutput(fullcommand)
	if verbose:
		ue.log("cmd Result: ")
		ue.log(stdoutdata[1])
	return stdoutdata[1] #return the data for dependent functions

#convenience override
def runLogOutput(process, path=_PythonHomePath):
	fullcommand = FolderCommand(path) + process
	stdoutdata = subprocess.getstatusoutput(fullcommand)
	ue.log(stdoutdata[1])
	return stdoutdata[1]

#convenience wrappers
def dir(path=_PythonHomePath):
	run('dir', path)

def ls(path=_PythonHomePath):
	dir(path)

def md(folder, path=_PythonHomePath):
	run('md ' + folder, path)

def mkdir(folder, path=_PythonHomePath):
	md(folder, path)