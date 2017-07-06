import DecodeManifestXml
import subprocess
import GetPid
import time
def super_fuzz(apk_file):
    xml=DecodeManifestXml.get_androidmanifest(apk_file)
    package_name='"'+DecodeManifestXml.get_package_name(xml)+'"'
    activity_name_list=DecodeManifestXml.get_activities(xml)
    cmd1 = "adb shell am start -n sdk.apigw.jcloud.com.fuzz_ofo/.MainActivity"
    cmd1_l=cmd1.split(" ")
    p1=subprocess.Popen(cmd1_l,shell=True)
    p1.wait()
    for activity in activity_name_list:
        wocao = GetPid.get_result(apk_file)
        pid = GetPid.get_pid(wocao, apk_file)
        new_activity='"'+activity+'"'
        cmd2='adb shell am broadcast -a android.intent.action.MY_BROADCAST --es packagename '+package_name+' --es classname '+new_activity
        cmd3="adb shell kill "+pid
        cmd2_l=cmd2.split(" ")
        p2=subprocess.Popen(cmd2_l,shell=True)
        p2.wait()
        time.sleep(5)
        cmd3_l=cmd3.split(" ")
        p3=subprocess.Popen(cmd3_l,shell=True)
    time.sleep(5)
    wocao1 = GetPid.get_result(apk_file)
    pid1 = GetPid.get_pid(wocao1, apk_file)
    cmd4 = "adb shell kill " + pid1
    cmd4_l = cmd4.split(" ")
    p4 = subprocess.Popen(cmd4_l, shell=True)
    p4.wait()
if __name__=="__main__":
    apk_file=r"C:\Users\yixianglin\Desktop\ofo.apk"
    super_fuzz(apk_file)