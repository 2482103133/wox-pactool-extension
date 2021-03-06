import json
import sys
import os
import subprocess
from urllib.parse import urlparse


data=None

print("starting script")
url=sys.argv[1]

if url.lower().startswith("http:") or url.lower().startswith("https:"):
  url=urlparse(sys.argv[1]).netloc

print(url)
# url=sys.argv[1]
with open(os.path.abspath("config.json"),encoding="utf-8") as f:

  data = json.load(f)
  v2_path=data["v2rayN-path"]

with open(v2_path+'/guiNConfig.json',encoding="utf-8") as f:
  data = json.load(f)
  s=set()
  s.update(data["userPacRule"])
  s.add(url)
  
  l=list(s)
  if l.__contains__(""):
    l.remove("")
  data["userPacRule"]=l

if(data is not None):
  with open(v2_path+'/guiNConfig.json',"w",encoding="utf-8" ) as f:
    json.dump(data,f, ensure_ascii=False)
    print(f"added url :{url}")
    os.system('taskkill /IM "v2rayN.exe" /F')
    print(f"killed v2rayN")
    subprocess.Popen([os.path.join(v2_path,"v2rayN.exe")])
    print(f"started v2rayN")

