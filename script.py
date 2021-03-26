import json
import sys
import os
import subprocess
from urllib.parse import urlparse


data=None

print("starting script")

url=urlparse(sys.argv[1]).netloc

with open(os.path.abspath("config.json"),encoding="utf-8") as f:
  url=url.lower().replace("https://","").replace("http://","").rstrip("/")
  data = json.load(f)
  v2_path=data["v2rayN-path"]

with open(v2_path+'/guiNConfig.json',encoding="utf-8") as f:
  data = json.load(f)
  s=set()
  s.update(data["userPacRule"])
  s.add(url)
  data["userPacRule"]=list(s)

if(data is not None):
  with open(v2_path+'/guiNConfig.json',"w",encoding="utf-8" ) as f:
    json.dump(data,f, ensure_ascii=False)
    print(f"added url :{url}")
    os.system('taskkill /IM "v2rayN.exe" /F')
    print(f"killed v2rayN")
    subprocess.Popen([os.path.join(v2_path,"v2rayN.exe")])
    print(f"started v2rayN")

