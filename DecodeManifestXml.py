#coding:utf-8
from androguard.core.bytecodes import apk
from androguard.util import read
from xml.dom.minidom import parseString
import zipfile
NS_ANDROID_URI = 'http://schemas.android.com/apk/res/android'
"""
parse AndroidManifest.xml
"""
def get_androidmanifest(apk_file):
    z=zipfile.ZipFile(apk_file,"r")
    for i in z.namelist():
        if i=="AndroidManifest.xml":
            ap=apk.AXMLPrinter(z.read(i))
            xml=parseString(ap.get_buff())
    return xml
"""
get exported activity,receiver,service
"""
def get_exported_activity(xml):
    exported_activies=[]
    find_tags = ["activity", "activity-alias"]
    for tag in find_tags:
        for ac in xml.getElementsByTagName(tag):
            exported=str(ac.getAttributeNS(NS_ANDROID_URI,"exported"))
            if exported=="true":
                exported_activies.append(str(ac.getAttributeNS(NS_ANDROID_URI,"name")))
    return exported_activies

def get_exported_receiver(xml):
    exported_receivers=[]
    for rv in xml.getElementsByTagName("receiver"):
        exported=str(rv.getAttributeNS(NS_ANDROID_URI,"exported"))
        if exported=="true":
            exported_receivers.append(str(rv.getAttributeNS(NS_ANDROID_URI,"name")))
    return exported_receivers

def get_exported_service(xml):
    exported_services=[]
    for sv in xml.getElementsByTagName("service"):
        exported=str(sv.getAttributeNS(NS_ANDROID_URI,"exported"))
        if exported=="true":
            exported_services.append(str(sv.getAttributeNS(NS_ANDROID_URI,"name")))
    return exported_services
"""
get intent-filter activity,receiver,service
"""
def get_intent_filter_activities(xml):
    #xml = get_manifestxml(apk_path)
    name_list=[]
    action_list=[]
    for item in xml.getElementsByTagName("activity"):
        exported=str(item.getAttributeNS(NS_ANDROID_URI,"exported"))
        if exported!="false":
            for filter_item in item.getElementsByTagName("intent-filter"):
                for action_item in filter_item.getElementsByTagName("action"):
                    action=str(action_item.getAttributeNS(NS_ANDROID_URI,"name"))
                    if action!="":
                        activity_name=str(item.getAttributeNS(NS_ANDROID_URI,"name"))
                        name_list.append(activity_name)
    return list(set(name_list))
def get_intent_filter_receiver(xml):
    name_list=[]
    action_list=[]
    for item in xml.getElementsByTagName("receiver"):
        exported=str(item.getAttributeNS(NS_ANDROID_URI,"exported"))
        if exported!="false":
            for filter_item in item.getElementsByTagName("intent-filter"):
                for action_item in filter_item.getElementsByTagName("action"):
                    action=str(action_item.getAttributeNS(NS_ANDROID_URI,"name"))
                    action_list.append(action)
                    if action!="":
                        activity_name=str(item.getAttributeNS(NS_ANDROID_URI,"name"))
                        name_list.append(activity_name)
    return list(set(name_list))
def get_intent_filter_service(xml):
    name_list=[]
    action_list=[]
    for item in xml.getElementsByTagName("service"):
        exported=str(item.getAttributeNS(NS_ANDROID_URI,"exported"))
        if exported!="false":
            for filter_item in item.getElementsByTagName("intent-filter"):
                for action_item in filter_item.getElementsByTagName("action"):
                    action=str(action_item.getAttributeNS(NS_ANDROID_URI,"name"))
                    action_list.append(action)
                    if action!="":
                        activity_name=str(item.getAttributeNS(NS_ANDROID_URI,"name"))
                        name_list.append(activity_name)

    return list(set(name_list))

"""
coolect activity,receiver,service
"""
def get_activities(xml):
    ac_ex=get_exported_activity(xml)
    ac_fi=get_intent_filter_activities(xml)
    return list(set(ac_ex+ac_fi))
def get_receivers(xml):
    rec_ex=get_exported_receiver(xml)
    rec_fi=get_intent_filter_receiver(xml)
    return list(set(rec_ex+rec_fi))
def get_services(xml):
    se_ex=get_exported_service(xml)
    se_fi=get_intent_filter_service(xml)
    return list(set(se_ex+se_fi))
"""
get Main Activity
"""
def get_main_activity(xml):
    for ac in xml.getElementsByTagName("activity"):
        for intent_filter in ac.getElementsByTagName("intent-filter"):
            for action in intent_filter.getElementsByTagName("action"):
                for category in intent_filter.getElementsByTagName("category"):
                    if str(action.getAttributeNS(NS_ANDROID_URI,"name"))=="android.intent.action.MAIN" and str(category.getAttributeNS(NS_ANDROID_URI,"name"))=="android.intent.category.LAUNCHER":
                        main_activity=str(ac.getAttributeNS(NS_ANDROID_URI,"name"))
    return main_activity
"""
get package name
"""
def get_package_name(xml):
    return xml.documentElement.getAttribute("package")

if __name__=="__main__":
    apk_file = r"C:\Users\yixianglin\Desktop\ofo.apk"
    xml=get_androidmanifest(apk_file)
    print get_activities(xml)
    print get_receivers(xml)
    print get_services(xml)
    print get_main_activity(xml)
    print get_package_name(xml)
