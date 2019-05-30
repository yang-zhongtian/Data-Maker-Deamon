import json
import shutil
import os
import time
import random
import subprocess

def makenewdir(path) :
	if os.path.exists(path):
		shutil.rmtree(path)
	time.sleep(0.01)
	os.mkdir(path)

if __name__ == "__main__" :
	varpool = {}
	jsonfilename = input("JSON File:")
	with open(jsonfilename,"r") as file:
		jsondata = json.loads(file.read())
	makenewdir(jsondata["name"])
	for tests in range(1,int(jsondata["test_count"])+1) :
		current_test_path = jsondata["name"]+".\\"+jsondata["output_file_ext"]+str(tests)
		with open("res.in","w") as file:
			content = []
			for data in jsondata["data_generate"] :
				if data["type"] == "line" :
					line = []
					for cont in data["data"]:
						if cont["type"] == "int":
							rand = random.randint(int(cont["min"]),int(cont["max"]))
							if "var" in cont:
								varpool[cont["var"]] = rand
							line.append(str(rand))
					content.append(" ".join(line)+"\n")
				elif data["type"] == "array" :
					if data["data"][0] == "line" :
						if data["data"][1].find("$") != -1:
							getvar = varpool[data["data"][1].replace("$","")]
						else:
							getvar = data["data"][1]
						for cont in range(1,int(getvar)+1) :
							line = []
							for test in data["data"][2] :
								if test["repeat"].find("$") != -1:
									tmp = varpool[test["repeat"].replace("$","")]
								else:
									tmp = test["repeat"]
								for repeat in range(int(tmp)) :
									if test["type"] == "int":
										rand = random.randint(int(test["min"]),int(test["max"]))
										line.append(str(rand))
							content.append(" ".join(line)+"\n")
			file.writelines(content)
		subprocess.run([jsondata["std_exe"]+"<res.in>res.out"],shell=True)
		shutil.move("res.in",current_test_path+".in")
		shutil.move("res.out",current_test_path+".out")
		varpool.clear()  
		print("finished",tests)