import subprocess,commands,time
import DecodeManifestXml
def read_log(apk_file):
    xml=DecodeManifestXml.get_androidmanifest(apk_file)
    package_name=DecodeManifestXml.get_package_name(xml)
    cmd="adb logcat -c"
    cmd_l=cmd.split(" ")
    pp=subprocess.Popen(cmd_l,shell=True)
    pp.wait()
    cmd_str="adb logcat"
    cmd_l=cmd_str.split(" ")
    p=subprocess.Popen(cmd_l,stdout=subprocess.PIPE,shell=True)
    for line in iter(p.stdout.readline,b""):
        if "Unable to start activity" in line.strip():
            start=line.index("{")+1
            end=line.index("}")
            activity=line[start:end]
            activity_l=activity.split("/")
            if activity_l[0]==package_name:
                print activity

if __name__=="__main__":
    apk_file = r"C:\Users\yixianglin\Desktop\ofo.apk"
    print read_log(apk_file)
