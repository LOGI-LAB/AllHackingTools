print("  # \033[1;34m[ 1 ] >> \033[1;36;40mBattareyStatus")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mCalsLogs")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mWifiScanInfo")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mExit")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Web-Hack1Ng: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && termux-battery-status && python3 src/Timer.py && cd && cd AllHackingTools && python2 src/aboutMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && termux-call-log && python3 src/Timer.py && cd && cd AllHackingTools && python2 src/aboutMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && termux-wifi-scaninfo && python3 src/Timer.py && cd && cd AllHackingTools && python2 src/aboutMenu.py")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
