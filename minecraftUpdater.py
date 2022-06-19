from importlib.resources import Package
import os
from posixpath import split
from urllib.parse import urlencode
from urllib.request import urlopen, urlretrieve
import zipfile
import hashlib
import shutil

try:

    def DoHash(filePath):
        hash_md5 = hashlib.md5()
        with open(filePath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    tempFolder="mcUpdaterTemp"
    manifestURL='UUURRRLLL' #Replace whit your own address
    manifestU=urlopen(manifestURL)
    print("正在取得模組包裹名稱")#fetching mod package name/
    manifest=manifestU.read().decode('utf-8')

    package=""
    print("正在建立暫存資料夾")#Creating tmp folder
    if not os.path.exists(tempFolder):
        os.makedirs(tempFolder)

    manifest=manifest.split("\n")
    for v in manifest:
        t=v.split(":")
        if t[0]=="package":
            package=t[1]
            break

    print(f"準備下載模組包：{package}")    #prepare to download {package}
    packageFolder=os.path.join(tempFolder,f"{package}") 
    urlretrieve(f"https://raw.githubusercontent.com/ncuouo/mcPatch/main/{package}.zip",f"{packageFolder}.zip")


    # if not os.path.exists(packageFolder):
    #     os.makedirs(packageFolder)
    print("正在解壓縮") #uncompressing
    with zipfile.ZipFile(f"{packageFolder}.zip", 'r') as zip_ref:
        zip_ref.extractall(tempFolder)

    updateList={}

    print("正在進行雜湊運算") #hashing
    #hash updates
    for filename in os.listdir(packageFolder):
        f = os.path.join(packageFolder, filename)
        # checking if it is a file
        if os.path.isfile(f):
            hashs=DoHash(f)
            if hash!=-1:            
                updateList[f]=hashs

    currentList={}
    #hash existed
    modsFolder="..\mods"
    for filename in os.listdir(modsFolder):
        f = os.path.join(modsFolder, filename)
        # checking if it is a file
        if os.path.isfile(f):
            hashs=DoHash(f)
            if hash!=-1:            
                currentList[f]=hashs


    deleteList={}
    tmpUpdateList={}
    flagFoundSame=False
    deleteList=currentList.copy()
    for kv,vv in updateList.items():
        for kt,vt in  currentList.items():
            if vv ==vt:
                flagFoundSame=True
                deleteList={key:val for key, val in deleteList.items() if val != vv}
               
                
                break
        if not flagFoundSame:
            tmpUpdateList[kv]=vv
            print(f"即將新增：{kv}") #Going to add: 
        flagFoundSame=False


    for delKey,delHash in deleteList.items():
        print(f"正在移除:{delKey}") #Removing {delkey}
        os.remove(delKey)
    for updKey,updHash in tmpUpdateList.items():
        print(f"正在複製:{updKey}") #Copying {updKey}
        shutil.copy(updKey,modsFolder)
    print(f"正在移除暫存檔案")
    shutil.rmtree(tempFolder)
    if  len(deleteList)==0 and len(tmpUpdateList)==0:
        print(f"沒有東西需要修改R？關起來8") #nothing needs to be changed.
    print(f"更新完畢，<3") #All things done 
    input()


    

    if __name__ == '__main__':
        main()
except Exception as e:
    print(str(e))
    input()
