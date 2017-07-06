import subprocess
import DecodeManifestXml
def get_result(apk_file):
    pid=""
    results=[]
    xml=DecodeManifestXml.get_androidmanifest(apk_file)
    package_name=DecodeManifestXml.get_package_name(xml)
    cmd=["adb","shell","ps","|","grep",package_name]
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE)
    if p.stdout.readline!="":
        for line in iter(p.stdout.readline,b""):
            result=line.split(" ")
            results.append(result)
            for i in range(1,len(result)):
                if result[i]!="" and package_name==result[len(result)-1]:
                    pid=result[i]
                    break
    return results
def get_pid(results,apk_file):
    pid=""
    xml=DecodeManifestXml.get_androidmanifest(apk_file)
    package_name = DecodeManifestXml.get_package_name(xml)
    for result in results:
        for i in range(1,len(result)):
            result_pac=result[-1]
            #print result_pac
            if result_pac.strip()==package_name:
                #print result_pac
                if result[i] != "" :
                    pid = result[i]
                    break
    return pid



if __name__=="__main__":
    apk_file=r"C:\Users\yixianglin\Desktop\ofo.apk"
    results=get_result(apk_file)
    pid=get_pid(results,apk_file)
    print pid