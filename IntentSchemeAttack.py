import DecodeManifestXml
NS_ANDROID_URI = 'http://schemas.android.com/apk/res/android'
def checkScheme(xml):
    category_list=[]
    category_dic={}
    new_dic={}
    find_tags=["activity", "activity-alias"]
    for tag in find_tags:
        for ac in xml.getElementsByTagName(tag):
            for intent_filter in ac.getElementsByTagName("intent-filter"):
                for data in intent_filter.getElementsByTagName("data"):
                    for category in intent_filter.getElementsByTagName("category"):
                        scheme=str(data.getAttributeNS(NS_ANDROID_URI,"scheme"))
                        category_name=str(category.getAttributeNS(NS_ANDROID_URI,"name"))
                        ac_name=str(ac.getAttributeNS(NS_ANDROID_URI,"name"))
                        new_scheme =ac_name+"@"+scheme
                        category_list.append(category_name)
                    if new_scheme!="":
                        category_dic[new_scheme]=list(set(category_list))
    return category_dic
def identify_intent(xml):
    category_dic=checkScheme(xml)
    i_activity=""
    activity_list=[]
    package_name=DecodeManifestXml.get_package_name(xml)
    for key in category_dic.keys():
        flag="android.intent.category.BROWSABLE"
        values=category_dic[key]
        if flag not in values:
            key_list=key.split("@")
            activity=key_list[0]
            if activity.startswith("."):
                i_activity=package_name+activity
                activity_list.append(i_activity)
            else:
                activity_list.append(activity)
    return activity_list

def show(xml):
    activity_list=identify_intent(xml)
    if len(activity_list)>0:
        for activity in activity_list:
            print "%s  exist Intent Scheme URLs attack!!" % activity
    else:
        print "Not exist Intent Scheme URLs attack!! This is OK!!"

if __name__=="__main__":
    apk_file = r"C:\Users\yixianglin\Desktop\v-phone.apk"
    xml = DecodeManifestXml.get_androidmanifest(apk_file)
    #print identify_intent(xml)
    show(xml)

