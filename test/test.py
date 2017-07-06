from androguard.core.bytecodes import dvm
from androguard.util import read
from androguard.core.analysis import analysis


def test():
    dex=r"C:\Users\yixianglin\Desktop\classes.dex"
    vm=dvm.DalvikVMFormat(read(dex))
    buff=""
    for cla in vm.get_classes():
        for method in cla.get_methods():
            for ins in method.get_instructions():
                if "invoke-virtual" in ins.get_name():
                    if "Landroid/content/Context;->getSharedPreferences" in ins.get_translated_kind():
                        print "******************************************************"
                        buff_tmp=ins.get_operands()
                        print buff_tmp
                        print method.get_class_name()
                        print method.get_name()
                        print "******************************************************"

test()