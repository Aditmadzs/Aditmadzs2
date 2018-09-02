#===========================================x
from LINEPY import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata,GACSender
_session = requests.session()
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#===============================================================================#
line = LINE()
#Line = LINE("เมล","พาส")
#line = LINE("")
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

ki = LINE("")
ki.log("Auth Token : " + str(ki.authToken))
ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

kk = LINE("")
kk.log("Auth Token : " + str(kk.authToken))
kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

kc = LINE("")
kc.log("Auth Token : " + str(kc.authToken))
kc.log("Timeline Token : " + str(kc.tl.channelAccessToken))

ke = LINE("")
ke.log("Auth Token : " + str(ke.authToken))
ke.log("Timeline Token : " + str(ke.tl.channelAccessToken))

kf = LINE("")
kf.log("Auth Token : " + str(kf.authToken))
kf.log("Timeline Token : " + str(kf.tl.channelAccessToken))

kg = LINE("")
kg.log("Auth Token : " + str(kg.authToken))
kg.log("Timeline Token : " + str(kg.tl.channelAccessToken))

kh = LINE("")
kh.log("Auth Token : " + str(kh.authToken))
kh.log("Timeline Token : " + str(kh.tl.channelAccessToken))

kj = LINE("")
kj.log("Auth Token : " + str(kj.authToken))
kj.log("Timeline Token : " + str(kj.tl.channelAccessToken))

print ("BY:【さัএπัஞ✵ບิथℓℓҨतΩ】")

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()
oepoll = OEPoll(line)
Rfu = [line,ki,kk,kc,ke,kf,kg,kh,kj]
Exc = [ki,kk,kc,ke,kf,kg,kh,kj]
lineMID = line.getProfile().mid
kiMID = ki.getProfile().mid
kkMID = kk.getProfile().mid
kcMID = kc.getProfile().mid
keMID = ke.getProfile().mid
kfMID = kf.getProfile().mid
kgMID = kg.getProfile().mid
khMID = kh.getProfile().mid
kjMID = kj.getProfile().mid
RfuBot=[lineMID,kiMID,kkMID,keMID,kfMID,kgMID,khMID,kjMID]
Family=["u4862fe4b182b2fd194a3108e2f3662e8",lineMID,kiMID,kkMID,keMID,kfMID,kgMID,khMID,kjMID]
admin=['u4862fe4b182b2fd194a3108e2f3662e8',lineMID,kiMID,kkMID,keMID,kfMID,kgMID,khMID,kjMID]
RfuFamily = RfuBot + Family
msg_dict = {}
msg_image={}
msg_video={}
msg_sticker={}
unsendchat = {}
temp_flood = {}
wbanlist = []
wblacklist = []
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#

settings = {
    "autoAdd": True,
    "autoBlock": False,
    "autoJoin": True,
    'autoCancel':{"on":True,"members":10},	
    "autoLeave": True,
    "autoRead": False,
    "autoReply": False,
    "botcancel": False,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "checkContact": False,
    "checkPost": False,
    "kickMention": False,
    "potoMention": True,
    "delayMention": False,
    "lang":"JP",
    "Wc": True,
    "Lv": True,
    "Nk": False,
    "Api": False,
    "Aip": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "detectMentionPM": False,
    "dwhitelist": False,
    "gift": False,
    "likeOn": False,
    "timeline": False,
    "commentOn":True,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "changeGroupPicture": [],
    "changePictureProfile": False,    
    "changeVideo": False,
    "chatMessage": "dih",
    "unsendMessage": False,
    "autoJoinTicket": False,
    "welcome":"Welcome to group ",
    "kick":"เก่ง เก่ง",
    "bye":"Good bye 😑",
    "Respontag":"จะแทคทำไมนักหนา 😠",
    "eror":"คุณใช้คำสั่งผิด กรุณาศึกษาวิธีใช้ หรือสอบถามกับผู้สร้าง โดยพิมคำสั่ง *.ผส*เพื่อแสดง คท ของผู้สร้าง",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "notag": False,
    "pcancel": False,
    "pinvite": False,
    "pmMessage": "ไอชิปหาย ~_~",
    "qrp": False,
    "readerPesan": " แอบทมายเดะจิ้มตาบอด",
    "replyPesan": "Sorry , i'm busy right now.",
    "responGc": True,
    "responcall": False,
    "responcallgc": False,
    "restartPoint": "ca1f5f9361386320256158f49bda4bb7e",
    "server": "VPS",
    "ksticker": False,
    "timeRestart": "18000",   
    "phu":"SPAM BY XAEL",
    "me":"MAX SELF BOT",
    "icon":"MAX SELF BOT ",
    "message":"【さัএπัஞ✵ບิथℓℓҨतΩ】 :\nList opsi\n🤖 Pasangan Hidup :\n🔰 Only Status ⏩ 180K/Bulan\n\n🤖 Systim Contract :\n🔰 Only Curhat ⏩ 100K/Bulan\n🔰 Zona Friend + TTM\n🔰 Zona Nyaman + Full Care + On 5day + 2 day free ⏩ 300K/Bulan\n\n✍️ Bisa Requests Mau Berapa Lama Durasi Buat Debay.\nChat Ke : http://line.me/ti/p/~max_pv\n\n📃\n* Always on 24 Jam\n* Keuntungan Banyak\n* Durasi min 0.25month\n* max no limit",
    "comment":"【さัএπัஞ✵ບิथℓℓҨतΩ】 :\nList opsi\n🤖 Pasangan Hidup :\n🔰 Only Status ⏩ 180K/Bulan\n\n🤖 Systim Contract :\n🔰 Only Curhat ⏩ 100K/Bulan\n🔰 Zona Friend + TTM\n🔰 Zona Nyaman + Full Care + On 5day + 2 day free ⏩ 300K/Bulan\n\n✍️ Bisa Requests Mau Berapa Lama Durasi Buat Debay.\nChat Ke : http://line.me/ti/p/~max_pv\n\n📃\n* Always on 24 Jam\n* Keuntungan Banyak\n* Durasi min 0.25month\n* max no limit",
   "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "addPesan": "【さัএπัஞ✵ບิथℓℓҨतΩ】 :\nList opsi\n🤖 Pasangan Hidup :\n🔰 Only Status ⏩ 180K/Bulan\n\n🤖 Systim Contract :\n🔰 Only Curhat ⏩ 100K/Bulan\n🔰 Zona Friend + TTM\n🔰 Zona Nyaman + Full Care + On 5day + 2 day free ⏩ 300K/Bulan\n\n✍️ Bisa Requests Mau Berapa Lama Durasi Buat Debay.\nChat Ke : http://line.me/ti/p/~max_pv\n\n📃\n* Always on 24 Jam\n* Keuntungan Banyak\n* Durasi min 0.25month\n* max no limit",
    "addSticker": {
        "name": "",
        "status": False,
    },
    "mentionPesan": " ว่าไง ที่รัก ^ω^",
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "addSticker": {
                "STKID": "52002736",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "leaveSticker": {
                "STKID": "51626516",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "kickSticker": {
                "STKID": "51626501",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "readerSticker": {
                "STKID": "13188540",
                "STKPKGID": "1327110",
                "STKVER": "1"
            },
            "responSticker": {
                "STKID": "51626504",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "sleepSticker": "",
            "welcomeSticker": {
                "STKID": "52002738",
                "STKPKGID": "11537",
                "STKVER": "1"
            }
        }
    },
    "mimic": {
       "copy": False,
       "status": False,
       "target": {}
    }
}
RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": True,
    "autoBlock": False,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
mulai = time.time() 

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#==============================================================================================================
                        
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        line.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+line.getContact(lineMID).pictureStatus, line.getContact(lineMID).displayName)
                    except Exception as error:
                        logError(error)
                        
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
        
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    line.sendMessage(to, '', contentMetadata, 7)

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            line.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

def waktu(secs):
	mins, secs = divmod(secs,60)
	hours, mins = divmod(mins,60)
	days,hours = divmod(hours,24)
	return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))                        
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = line.genOBSParams({'oid': lineMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        line.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)
def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def myhelp():
    myHelp = """╔═══════════════╗
║【さัএπัஞ✵ບิथℓℓҨतΩ】║
╚═══════════════╝
╔═════════════════╗
╠★→ คท
╠★→ สปีด
╠★→ ไอดีเรา
╠★→ ชื่อเรา
╠★→ ตัสเรา
╠★→ ดิสเรา
╠★→ ปกเรา
╠★→ เชคค่า
╠★→ ข้อมูล
╠★→ บอท
╠★→ ออน
╠★→ รีบอท
╠★→ ผู้สร้าง
╠★→ สุดหล่อ
╠★→ อัพชื่อ: 「ชื่อที่ต้องการ」
╠★→ อัพตัส: 「ตัสที่ต้องการ」
╠★→ ก็อป「@」
╠★→ พูด「ข้อความ」
╠★→ ยกเลิก「จำนวน」
╠★→ สแปม on「จำนวน ข้อความ」
╠★→ แทค
╠★→ เพิ่มเลียนแบบ「@」
╠★→ ลบเลียนแบบ「@」
╠★→ เชคเลียนแบบ
╠★→ เลียนแบบ เปิด/ปิด
╠★→ ดึง「ส่งคอนแทคลง」
╠★→ ยกเชิญ
╠★→ แอดมิน
╠★→ ชื่อกลุ่ม
╠★→ ไอดีกลุ่ม
╠★→ รูปกลุ่ม
╠★→ สมาชิกกลุ่ม
╠★→ ข้อมูลกลุ่ม
╠★→ เช็คบล็อค
╠★→ เช็คบล็อค
╠★→ ไอดีเพื่อน
╠★→ ลิ้งกลุ่ม
╠★→ เปิดลิ้ง/ปิดลิ้ง
╠★→ เปิดแอด/ปิดแอด
╠★→ เปิดบล็อค/ปิดบล็อค
╠★→ เปิดรี/ปิดรี
╠★→ เปิดเตะ/ปิดเตะ
╠★→ เปิดพูด/ปิดพูด
╠★→ เปิดคท/ปิดคท
╠★→ เปิดเตะคท/ปิดเตะคท
╠★→ เปิดมุด/ปิดมุด
╠★→ เปิดเข้า/ปิดเข้า
╠★→ เปิดออก/ปิดออก
╠★→ เปิดอ่าน/ปิดอ่าน
╠★→ เปิดโพส/ปิดโพส
╠★→ เปิดแอบ/ปิดแอบ
╠★→ เปิดหมด/ปิดหมด
╠★→ เปิดติก/ปิดติก
╠★→ เปิดทักเข้า/ปิดทักเข้า
╠★→ เปิดทักออก/ปิดทักออก
╠★→ เปิดแทค/ปิดแทค
╠★→ เปิดแทค2/ปิดแทค2
╠★→ เปิดแทค3/ปิดแทค3
╠★→ เปิดแทคแชท/ปิดแทคแชท
╠★→ ตั้งแทค:「ข้อความที่ต้องการ」
╠★→ ตั้งติกแทค
╠★→ ตั้งเข้า:「ข้อความที่ต้องการ」
╠★→ ตั้งติกเข้า
╠★→ ตั้งออก:「ข้อความที่ต้องการ」
╠★→ ตั้งติกออก
╠★→ ตั้งเตะ:「ข้อความที่ต้องการ」
╠★→ ตั้งติกเตะ
╠★→ แทคแชท:「ข้อความที่ต้องการ」
╠★→ ดึงหมด「@」
╠★→ ดึงหมด แชท.สต
╠★→ กลุ่ม「@」
╠★→ เตะ「@」คำสั่งเตะ
╠★→ ล้อเล่น「@」คำสั่งเตะ
╠★→ ปลิว「@」คำสั่งเตะ
╠★→ แตก1「@」คำสั่งเตะ
╠★→ ทัก「จำนวน」แชท.สต
╠★→ แทค「จำนวน」@
╠★→ ไวรัส「จำนวน」@
╠★→ ส่วนตัว「จำนวน」@
╠★→ ส่วนตัว:「ข้อความที่ต้องการ」
╠★→ ไอคอน:「ข้อความที่ต้องการ」
╠★→ คำห้ามพิม「@」
╠★→ ล้างคำห้ามพิม「@」
╠★→ เช็คคำห้ามพิม
╠★→ เปลี่ยนดิส「ส่งรูปภาพ」
╠★→ เปลี่ยนรูปกลุ่ม「ส่งรูปภาพ」
╚═════════════════╝"""
    return myHelp
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.sendMessage(op.param1,str(settings["message"]))
                line.findAndAddContactsByMid(op.param1)
                ki.findAndAddContactsByMid(op.param1)
                kk.findAndAddContactsByMid(op.param1)
                kc.findAndAddContactsByMid(op.param1)
                ke.findAndAddContactsByMid(op.param1)
            if settings["autoBlock"] == True:
                line.sendMessage(op.param1,str(settings["message"]))
                line.blockContact(op.param1)
                ki.blockContact(op.param1)
                kk.blockContact(op.param1)
                kc.blockContact(op.param1)
                ke.blockContact(op.param1)
            msgSticker = settings["messageSticker"]["listSticker"]["addSticker"]
            if msgSticker != None:
                sid = msgSticker["STKID"]
                spkg = msgSticker["STKPKGID"]
                sver = msgSticker["STKVER"]
                sendSticker(op.param1, sver, spkg, sid)        
        if op.type == 13:
            print(op.param1)
            print(op.param2)
            print(op.param3)
            if mid in op.param3:
                G = line.getGroup(op.param1)
                if setting["autoJoin"] == True:
                    if setting["autoCancel"]["on"] == True:
                        if len(G.members) <= setting["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif setting["autoCancel"]["on"] == True:
                    if len(G.members) <= setting["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in setting["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 15:
          #  print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            if settings["Lv"] == True:
                group = line.getGroup(op.param1)
                contact = line.getContact(op.param2)
                msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
        if op.type == 19:
            #print ("[ 15 ]  NOTIFIED LEAVE GROUP")
            if settings["Nk"] == True:
                if "{gname}" in settings['kick']:
                    gName = line.getGroup(op.param1).name
                    msg = settings['kick'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                    if "@!" in settings['kick']:
                        msg = msg.split("@!")
                        return sendMention(op.param2, op.param2, msg[0], msg[1])
                    return sendMention(op.param2, op.param2, "Hallo ", msg)
                msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
                #sendMention(op.param1, op.param2, "อุ๊ต๊ะ", "\n{}".format(str(settings['kick'])))
        if op.type == 17:
            print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            if settings["Wc"] == True:
                group = line.getGroup(op.param1)
                contact = line.getContact(op.param2)
                msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
#      if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
        if op.type == 24:
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)                      
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if settings["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = line.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 line.sendText(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 line.sendText(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 line.sendText(msg.to,"ใช้คำสั่ง!, \n➡ล้างดำ➡ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     line.findAndAddContactsByMid(target)
                                     line.inviteIntoGroup(msg.to,[target])
                                     line.sendText(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         line.findAndAddContactsByMid(invite)
                                         line.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         line.sendText(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         settings["winvite"] = False
                                         break
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendText(msg.to,"รับทราบ")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendText(msg.to,"decided not to comment")

               elif settings["dblack"] == True:
                   if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"ลบจากรายการที่ถูกแบนแล้ว")
                        settings["dblack"] = False

                   else:
                        settings["dblack"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Daftar Blacklist")
               elif settings["wblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendText(msg.to,"Sudah Ada")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")

               elif settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว")
                        settings["dblacklist"] = False

                   else:
                        settings["dblacklist"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
       # if op.type == 26:
#            if settings ["mutebot2"] == True:
           # msg = op.message
           # try:
               # if msg.toType == 0:
                  #  line.log("[%s]"%(msg._from)+str(msg.text))
               # else:
                  #  group = line.getGroup(msg.to)
                    #contact = line.getContact(msg._from)
                  #  line.log("[%s]"%(msg.to)+"\nGroupname: "+str(group.name)+"\nNamenya: "+str(contact.displayName)+"\nPesannya: "+str(msg.text))
               # if msg.contentType == 0:
            #Save message to dict
                    #msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                #if msg.contentType == 7:
                    #stk_id = msg.contentMetadata['STKID']
                    #stk_ver = msg.contentMetadata['STKVER']
                   # pkg_id = msg.contentMetadata['STKPKGID']
                    #ret_ = "="
                    #ret_ += "\nSTICKER ID : {}".format(stk_id)
                  #  ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                    #ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                    #ret_ += "\nSTICKER URL : line://shop/detail/{}".format(pkg_id)
                    #ret_ += "\n"
                    #msg_dict[msg.id] = {"text":str(ret_),"from":msg._from,"createdTime":msg.createdTime}
            #except Exception as e:
                #print(e) 
#==============================================================================================================
                 if msg.contentType == 0:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"lokasi":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                 if msg.contentType == 1:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                 if msg.contentType == 2:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                 if msg.contentType == 3:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                 if msg.contentType == 7:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                 if msg.contentType == 13:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                 if msg.contentType == 14:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = line.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
#==============================================================================================================                   
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if "ควย " in msg.text.lower():
                    spl = re.split("ควย ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == 'คำสั่ง':
                    contact = line.getContact(msg._from)
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    link = "http://line.me/ti/p/~max_pv"
                    name = "ชุดใบคำสั่ง"
                    myHelp = myhelp()
                    line.sendFooter(to, str(myHelp),link ,icon,name)
#==============================================================================#
                elif text.lower() == 'บอท':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความตอบกลับอัตโนมัติ"
                    link = "http://line.me/ti/p/~xael.py"
                    ki.sendFooter(msg.to, "BOT 1",link ,icon,name)
                    kk.sendFooter(msg.to, "BOT 1",link ,icon,name)
                    kc.sendFooter(msg.to, "BOT 1",link ,icon,name)
                    ke.sendFooter(msg.to, "BOT 4",link ,icon,name)
                    kf.sendFooter(msg.to, "BOT 1",link ,icon,name)
                    kg.sendFooter(msg.to, "BOT 1",link ,icon,name)
                    kh.sendFooter(msg.to, "BOT 1",link ,icon,name)
                    kj.sendFooter(msg.to, "BOT 1",link ,icon,name)
                elif text.lower() == 'คิกสปีด':
                    start = time.time()
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                    elapsed_time = time.time() - start
                    ki.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                    elapsed_time = time.time() - start
                    kk.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                    elapsed_time = time.time() - start
                    kc.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                    elapsed_time = time.time() - start
                    ke.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'เทส':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความเทสอัตโมมัติ"
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "กำลังโหลด:▒...0%",link ,icon,name)
                    line.sendFooter(to, "█▒... 10.0%" ,link ,icon,name)
                    ki.sendFooter(to, "██▒... 20.0%" ,link ,icon,name)
                    ki.sendFooter(to, "███▒... 30.0%" ,link ,icon,name)
                    ki.sendFooter(to, "████▒... 40.0%" ,link ,icon,name)
                    ki.sendFooter(to, "█████▒... 50.0%" ,link ,icon,name)
                    kk.sendFooter(to, "██████▒... 60.0%" ,link ,icon,name)
                    kk.sendFooter(to, "██████▒... 70.0%" ,link ,icon,name)
                    kk.sendFooter(to, "████████▒... 80.0%" ,link ,icon,name)
                    kk.sendFooter(to, "█████████▒... 90.0%" ,link ,icon,name)
                    kk.sendFooter(to, "███████████..100.0%" ,link ,icon,name)
                elif text.lower() == 'แจก':
                        line.sendGift(msg.to,'1002077','sticker')
                        ki.sendGift(msg.to,'1002077','sticker')
                        kk.sendGift(msg.to,'1002077','sticker')
                        kc.sendGift(msg.to,'1002077','sticker')
                        ke.sendGift(msg.to,'1002077','sticker')
                        kf.sendGift(msg.to,'1002077','sticker')
                        kg.sendGift(msg.to,'1002077','sticker')
                        kh.sendGift(msg.to,'1002077','sticker')
                        kj.sendGift(msg.to,'1002077','sticker')						
                elif 'ยกเลิก ' in msg.text:
                    args = msg.text.replace("ยกเลิก ","")
                    mes = 0
                    try:
                        mes = int(args[1])
                    except:
                        mes = 1
                    M = line.getRecentMessagesV2(to, 101)
                    MId = []
                    for ind,i in enumerate(M):
                        if ind == 0:
                            pass
                        else:
                            if i._from == line.profile.mid:
                                MId.append(i.id)
                                if len(MId) == mes:
                                    break
                    def unsMes(msg_id):
                      line.unsendMessage(msg_id)
                    for i in MId:
                      thread1 = threading.Thread(target=unsMes, args=(i,))
                      thread1.start()
                      thread1.join()
                    line.sendMessage(msg.to, ' 「 กำลังยกเลิกข้อความ 」\nยกเลิกข้อความทั้งหมด {} ข้อความ'.format(len(MId)))         
                elif 'มาดิ' in text.lower():
                    if msg.toType == 2:
                        G = line.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ki.acceptGroupInvitationByTicket(to, Ti)
                            kk.acceptGroupInvitationByTicket(to, Ti)
                            kc.acceptGroupInvitationByTicket(to, Ti)
                            ke.acceptGroupInvitationByTicket(to, Ti)
                            kf.acceptGroupInvitationByTicket(to, Ti)
                            kg.acceptGroupInvitationByTicket(to, Ti)
                            kh.acceptGroupInvitationByTicket(to, Ti)
                            kj.acceptGroupInvitationByTicket(to, Ti)							
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            line.updateGroup(G)
                            invsend = 0
                            Ti = line.reissueGroupTicket(to)
                            ki.acceptGroupInvitationByTicket(to, Ti)
                            kk.acceptGroupInvitationByTicket(to, Ti)
                            kc.acceptGroupInvitationByTicket(to, Ti)
                            ke.acceptGroupInvitationByTicket(to, Ti)
                            kf.acceptGroupInvitationByTicket(to, Ti)
                            kg.acceptGroupInvitationByTicket(to, Ti)
                            kh.acceptGroupInvitationByTicket(to, Ti)
                            kj.acceptGroupInvitationByTicket(to, Ti)	
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                elif text.lower() == 'แอลถอย':
                    if msg.toType == 2:
                        ginfo = line.getGroup(to)
                        try:
                            ki.leaveGroup(to)
                            kk.leaveGroup(to)
                            kc.leaveGroup(to)
                            ke.leaveGroup(to)
                            kf.leaveGroup(to)
                            kg.leaveGroup(to)
                            kh.leaveGroup(to)
                            kj.leaveGroup(to)							
                        except:
                            pass

                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                elif text.lower() == 'Sp':
                    start = time.time()
                    line.sendMessage(to, "TEAM CLOWN OF DEAYH")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                if text.lower() == 'ออน':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "เวลาการใช้งานบอท"                   
                    link = "http://line.me/ti/p/~xael.py"
                    eltime = time.time() - mulai
                    van = "「 ระยะเวลาการทำงานของบอท 」\n"+waktu(eltime)
                    line.sendFooter(receiver,van ,link ,icon,name)
                elif text.lower() == 'รีบอท':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "รีสตาร์ทบอท"                   
                    link = "http://line.me/ti/p/~xael.py"                    
                    line.sendFooter(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ .." ,link ,icon,name)
                    line.sendFooter(to, "เริ่มใหม่สำเร็จแล้ว",link ,icon,name)
                    restartBot()                                  
                elif text.lower() == 'บอท':
                    try:
                        arr = []
                        owner = "u09bc8f258afebdc8dc54122b1b5ac565"                        
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ TEAM CLOWN OF DEAYH ]"
                        ret_ += "\n╠🎤 ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠🎤 กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠🎤 เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠🎤 บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠🎤 สถานะ ═ {}".format(contact.statusMessage)
                        ret_ += "\n╠🎤 ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[ TEAM CLOWN OF DEAYH ]"
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "เกี่ยวกับเรา"                   
                        link = "http://line.me/ti/p/~xael.py"
                        line.sendContact(to, owner)
                        line.sendFooter(to, str(ret_),link ,icon,name)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                        
                if text.lower() == 'กลุ่ม ':
#                    line.sendMessage(to, "กำลังตรวจสอบข้อมูล...")
                    G = line.getGroupIdsJoined()
                    cgroup = line.getGroups(G)
                    ngroup = ""
                    for x in range(len(cgroup)):
                        gMembMids = [contact.mid for contact in cgroup[x].members]
                        if receiver in gMembMids:
                            ngroup += "\n➢ " + cgroup[x].name + " | สมาชิก: " + str(len(cgroup[x].members))    
                    if ngroup == "":
                         line.sendMessage(to, "ไม่พบคุณอยู่ในกลุ่ม")
                    else:
                         line.sendMessage(to, "➢ตรวจพบอยู่ในกลุ่ม %s\n"%(ngroup))

                elif "กลุ่ม " in text.lower():
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        G = line.getGroupIdsJoined()
                        cgroup = line.getGroups(G)
                        ngroup = ""
                        for mention in mentionees:
                         for x in range(len(cgroup)):
                           gMembMids = [contact.mid for contact in cgroup[x].members]
                           if mention['M'] in gMembMids:
                                ngroup += "\n➢ " + cgroup[x].name + " | สมาชิก: " +str(len(cgroup[x].members))    
                        if ngroup == "":
                             line.sendMessage(to, "ไม่พบ")
                        else:
                             line.sendMessage(to, "➢ตรวจพบอยู่ในกลุ่ม %s"%(ngroup))
#==============================================================================#
                   
                if text.lower() == 'ยกเชิญ':
                                if msg._from in bot1:
                                
                                    if msg.toType == 2:
                                        group = line.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//30
                                        line.sendMessage(msg.to,"[ ยกค้างเชิญ จำนวน {} คน] \nรอสักครู่...".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*30 : (i+1)*30]:
                                                time.sleep(random.uniform(0.5,0.4))
                                                line.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            line.sendMessage(receiver,"พัก 10-15 วินาที แล้ว จะทำการ ยกต่อ 30 คน\nผู้สร้างบอทสนใจใช้บอทกรุณาติดต่อ≧∇≦\n☆➣ http://line.me/ti/p/~botline2034 \n☆➣ http://line.me/ti/p/~l581-1")
                                            time.sleep(random.uniform(15,10))
                                        line.sendMessage(receiver,"[ ยกค้างเชิญ จำนวน {} คน เรียบร้อยแล้ว]".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        line.sendMessage(receiver, None, contentMetadata={"STKID": "119","STKPKGID": "1","STKVER": "100" }, contentType=7)
                                        gname = line.getGroup(receiver).name
                                        line.sendMessage(Notify,"[ ยกค้างเชิญ >> "+gname+"  <<] \n จำนวน {} คน เรียบร้อยแล้ว\nผู้สร้างบอทสนใจใช้บอทกรุณาติดต่อ≧∇≦\n║͜͡☆➣ http://line.me/ti/p/~botline2034 \n☆➣ http://line.me/ti/p/~l581-1".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        line.leaveGroup(receiver)
                                								
                                    line.sendMessage(receiver,"[ไม่มีคนให้ผมยกเชิญ ลาก๋อย]")
                                    line.sendMessage(receiver, None, contentMetadata={"STKID": "120","STKPKGID": "1","STKVER": "100" }, contentType=7)
                                    line.leaveGroup(receiver)
#=================================
#==============================================================================#                             
#==============================================================================#
                elif text.lower() == 'เชคค่า':
                    try:
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ระบบตั้งค่า"                    
                        link = "http://line.me/ti/p/~xael.py"                      
                        ret_ = "╔════[ สถานะบอท ]═════╗"
                        if settings["autoAdd"] == True: ret_ += "\n╠✴️ ออโต้แอด ✅"
                        else: ret_ += "\n╠✴️ ออโต้แอด ❌"
                        if settings["autoBlock"] == True: ret_ += "\n╠✴️ ออโต้บล็อค ✅"
                        else: ret_ += "\n╠✴️ ออโต้บล็อค ❌"
                        if settings["autoJoinTicket"] == True: ret_ += "\n╠✴️ มุดลิ้ง ✅"
                        else: ret_ += "\n╠✴️ มุดลิ้ง ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠✴️ เข้าห้องออโต้ ✅"
                        else: ret_ += "\n╠✴️ เข้าห้องออโต้ ❌"
                        if settings["Api"] == True: ret_ += "\n╠✴️ บอท api ✅"
                        else: ret_ += "\n╠✴️ บอท api ❌"
                        if settings["Aip"] == True: ret_ += "\n╠✴️ แสกนคำพูด+คำสั่งบิน ✅"
                        else: ret_ += "\n╠✴️ แสกนคำพูด+คำสั่งบ ิน❌"
                        if settings["Wc"] == True: ret_ += "\n╠✴️ ข้อความต้อนรับสมาชิก ✅"
                        else: ret_ += "\n╠✴️ ข้อความต้อนรับสมาชิก ❌"
                        if settings["Lv"] == True: ret_ += "\n╠✴️ ข้อความอำลาสมาชิก ✅"
                        else: ret_ += "\n╠✴️ ข้อความอำลาสมาชิก ❌"
                        if settings["Nk"] == True: ret_ += "\n╠✴️ ข้อความแจ้งเตือนคนลบ ✅"
                        else: ret_ += "\n╠✴️ ข้อความแจ้งเตือนคนลบ ❌"
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠✴️ ปฏิเสธกลุ่มเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"]) + " → ✅"
                        else: ret_ += "\n╠✴️ ปฏิเสธกลุ่มเชิญ ❌"						
                        if settings["autoLeave"] == True: ret_ += "\n╠✴️ ออกแชทรวม ✅"
                        else: ret_ += "\n╠✴️ ออกแชทรวม ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠✴️ อ่านออโต้ ✅"
                        else: ret_ += "\n╠✴️ อ่านออโต้ ❌"				
                        if settings["checkContact"] == True: ret_ += "\n╠✴️ อ่านคท ✅"
                        else: ret_ += "\n╠✴️ อ่านคท ❌"
                        if settings["checkPost"] == True: ret_ += "\n╠✴️ เช็คโพส ✅"
                        else: ret_ += "\n╠✴️ เช็คโพส ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠✴️ Sticker ✅"
                        else: ret_ += "\n╠✴️ Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠✴️ ตอบกลับคนแทค ✅"
                        else: ret_ += "\n╠✴️ ตอบกลับคนแทค ❌"
                        if settings["potoMention"] == True: ret_ += "\n╠✴️ แสดงภาพคนแทค ✅"
                        else: ret_ += "\n╠✴️ แสดงภาพคนแทค ❌"
                        if settings["kickMention"] == True: ret_ += "\n╠✴️ เตะคนแทค ✅"
                        else: ret_ += "\n╠✴️ เตะคนแทค ❌"
                        if settings["delayMention"] == True: ret_ += "\n╠✴️ แทคกลับคนแทค ✅"
                        else: ret_ += "\n╠✴️ แทคกลับคนแทค ❌"
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠✴️ กันเชิญ ✅"
                        else: ret_ += "\n╠✴️ กันเชิญ ❌"
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠✴️ กันยกเชิญ ✅"
                        else: ret_ += "\n╠✴️ กันยกเชิญ ❌"
                        if RfuProtect["protect"] == True: ret_ += "\n╠✴️ ป้องกัน ✅"
                        else: ret_ += "\n╠✴️ ป้องกัน ❌"
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠✴️ ป้องกันเปิดลิ้ง ✅"
                        else: ret_ += "\n╠✴️ ป้องกันเปิดลิ้ง ❌"
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠✴️ ป้องกันสมาชิก ✅"
                        else: ret_ += "\n╠✴️ ป้องกันสมาชิก ❌"
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠✴️ ป้องกันเข้ากลุ่ม ✅"
                        else: ret_ += "\n╠✴️ ป้องกันเข้ากลุ่ม ❌"						
                        ret_ += "\n╚════[ สถานะบอท ]═════╝"
                        line.sendFooter(to, str(ret_),link ,icon,name)
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == 'เปิดแอด':
                    settings["autoAdd"] = True
                    settings["autoBlock"] = False
                    RfuProtect["autoAdd"] == True
                    RfuProtect["autoBlock"] == False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "เปิดรับแอดออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดบล็อค':
                    settings["autoBlock"] = True
                    settings["autoAdd"] = False
                    RfuProtect["autoBlock"] == True
                    RfuProtect["autoAdd"] == False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "เปิดบล็อคแอดออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดแอด':
                    settings["autoAdd"] = False
                    RfuProtect["autoAdd"] == False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ปิดรับแอดออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดบล็อค':
                    settings["autoBlock"] = False
                    RfuProtect["autoBlock"] == False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ปิดบล็อคแอดออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดเข้า':
                    settings["autoJoin"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "เปิดเข้าห้องออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดเข้า':
                    settings["autoJoin"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ปิดเข้าห้องออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดรี':
                    settings["unsendMessage"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "เปิดรีข้อความที่ยกเลิกแล้ว",link ,icon,name)
                elif text.lower() == 'ปิดรี':
                    settings["unsendMessage"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ปิดรีข้อความที่ยกเลิกแล้ว",link ,icon,name)
                elif "gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,"ปิดใช้งานระบบปฏิเสธคำเชิญตามจำนวนสมาชิก")
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to, " สมาชิกในกลุ่มที่ไม่ถึง" + strnum + "จะถูกปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,str(settings["eror"]))
                        else:
                                line.sendText(msg.to,"Bizarre ratings")					
                elif text.lower() == 'เปิดออก':
                    settings["autoLeave"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "เปิดออกแชทรวมออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดออก':
                    settings["autoLeave"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ปิดออกแชทรวมออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดอ่าน':
                    settings["autoRead"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "เปิดอ่านออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'ปิดอ่าน':
                    settings["autoRead"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ปิดอ่านออโต้แล้ว",link ,icon,name)
                elif text.lower() == 'เปิดติก':
                    settings["checkSticker"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "เปิดเชคติ๊กแล้ว",link ,icon,name)
                elif text.lower() == 'ปิดติก':
                    settings["checkSticker"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ปิดเชคติ๊กแล้ว",link ,icon,name)
                elif text.lower() == 'เปิดมุด':
                    settings["autoJoinTicket"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "เปิดมุดลิ้งแล้ว",link ,icon,name)
                elif text.lower() == 'ปิดมุด':
                    settings["autoJoinTicket"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ปิดมุดลิ้งแล้ว",link ,icon,name)
                elif text.lower() == 'เปิดเตะคท':
                    settings["kickContact"] = True
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "เปิดเตะคทแล้ว",link ,icon,name)
                elif text.lower() == 'ปิดเตะคท':
                    settings["kickContact"] = False
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "TEAM BOT CLOWN OF DEAYH"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ปิดเตะคทแล้ว",link ,icon,name)
#==============================================================================#
                elif text.lower() == 'คิก':
                    line.sendContact(to, kiMID)
                    line.sendContact(to, kkMID)
                    line.sendContact(to, kcMID)
                    line.sendContact(to, keMID)
                elif text.lower() == "คท" or text.lower()  == "me":
                    line.sendMentionFooter(to, str(settings["me"]), sender, "https://line.me/ti/p/~xael.py", "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName);line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installrl': 'https://line.me/ti/p/~xael.py', 'type': 'mt', 'subText': str(settings["icon"]), 'a-installUrl': 'https://line.me/ti/p/~xael.py', 'a-installUrl': ' https://line.me/ti/p/~xael.py', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~xael.py', 'i-linkUri': 'https://line.me/ti/p/~xael.py', 'id': 'mt000000000a6b79f9', 'text': 'XAEL', 'linkUri': 'https://line.me/ti/p/~xael.py'}, contentType=19)
                    ki.sendMentionFooter(to, str(settings["me"]), sender, "https://line.me/ti/p/~xael.py", "http://dl.profile.line-cdn.net/"+ki.getContact(sender).pictureStatus, ki.getContact(sender).displayName);ki.sendMessage(to, ki.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+ki.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~xael.py', 'type': 'mt', 'subText': str(settings["icon"]), 'a-installUrl': 'https://line.me/ti/p/~xael.py', 'a-installUrl': ' https://line.me/ti/p/~xael.py', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~xael.py', 'i-linkUri': 'https://line.me/ti/p/~xael.py', 'id': 'mt000000000a6b79f9', 'text': 'XAEL', 'linkUri': 'https://line.me/ti/p/~xael.py'}, contentType=19)
                elif text.lower() == "ไอดีเรา":
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendFooter(to, "MID :\n"+str(sender), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif text.lower() == "555":
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "555แอลขำ"
                    link = "http://line.mr/ti/p/~xael.py"
                    line.sendMessage(msg.to, None, contentMetadata={"STKID":"51626512","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                    line.sendFooter(to, "พูด 5 5 5 แอล ขำ",link ,icon,name)
                elif text.lower() == "สปีด":
                   contact = line.getContact(msg._from)
                   icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                   name = "SPEED TEST BOT BY. XAEL"
                   name2 = "SPEED TEST BOT..."
                   link = "http://line.me/ti/p/~xael.py"
                   start = time.time()
                   line.sendFooter(to, "ꜱᴩᴇᴇᴅ ᴛᴇꜱᴛ...  ",link ,icon,name)
                   elapsed_time = time.time() - start
                   line.sendFooter(to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]",link ,icon,name2)
                elif text.lower() == "ชื่อเรา":
                     h = line.getContact(lineMID)
                     userid = "https://line.me/ti/p/~" + line.profile.userid
                     line.sendFooter(to, "ชื่อเรา :\n"+str(h.displayName), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif text.lower() == "ตัสเรา":
                    h = line.getContact(lineMID)
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendFooter(to, "ตัสเรา :\n"+str(h.statusMessage), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif text.lower() == "สุดหล่อ":
                    contact = line.getContact(lineMID)
                    cu = line.getProfileCoverURL(lineMID)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendImageWithFooter(to, image, userid, image, line.getContact(sender).displayName)
                    line.sendImageWithFooter(to, path, userid, path, line.getContact(sender).displayName)
                    line.sendFooter(to, "ดิส\nมิด : "+str(sender)+"\nชื่อ : "+str(contact.displayName)+"\nตัส :\n"+str(contact.statusMessage), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif text.lower() == "ดิสเรา":
                    h = line.getContact(lineMID)
                    image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendImageWithFooter(to, image, userid, image, line.getContact(sender).displayName)
                elif text.lower() == "ปกเรา":
                    h = line.getContact(lineMID)
                    cu = line.getProfileCoverURL(lineMID)
                    image = str(cu)
                    userid = "https://line.me/ti/p/~" + line.profile.userid
                    line.sendImageWithFooter(to, image, userid, image, line.getContact(sender).displayName)                            
                elif text.lower() == 'ผู้สร้าง':                   
                    line.sendContact(to, "u09bc8f258afebdc8dc54122b1b5ac565")
                    line.sendContact(to, "uf70dcd1cf3349a7f3d8d05e99a5fb081")                
                elif text.lower() == 'คอมเม้น':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความที่ตั้งไว้"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(msg.to,str(settings["comment"]),link ,icon,name) 
                elif text.lower() == 'ทักคท':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความที่ตั้งไว้"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(msg.to,str(settings["me"]),link ,icon,name)                
                elif text.lower() == 'ส่วนตัว':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความที่ตั้งไว้"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(msg.to, str(settings["phu"]),link ,icon,name)
                elif text.lower() == 'ทักเข้า':
               	    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความที่ตั้งไว้"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(msg.to, str(settings["welcome"]),link ,icon,name)
                elif text.lower() == 'ทักออก':
               	    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความที่ตั้งไว้"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(msg.to, str(settings["bye"]),link ,icon,name)
                elif text.lower() == 'ทักเตะ':
               	    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความที่ตั้งไว้"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(msg.to, str(settings["kick"]),link ,icon,name)
                elif text.lower() == 'คนแอด':
               	    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความที่ตั้งไว้"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(msg.to, str(settings["message"]),link ,icon,name)
                elif text.lower() == 'คนแทค':
               	    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความที่ตั้งไว้"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(msg.to, str(settings["Respontag"]),link ,icon,name)
                elif text.lower() == 'แทคล่อง':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "ม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == 'ไอดีล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีmidคนใส่ร่องหน🤗")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == 'คทล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)


                elif text.lower() == 'ดึงหมด':
                    if line != None:
                        me = line.getContact(to)
                        path = line.getProfileCoverURL(to)
                        path = str(path)
                        if settings["server"] == "VPS":
                            line.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                            line.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                            line.sendMessage(msg.to,"「 MID 」\n" +  to)
                            line.sendMessage(to, text=None, contentMetadata={'mid': to}, contentType=13)
                            line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                            line.sendImageWithURL(to, str(path))
                            line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                        else:
                            line.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                            line.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                            line.sendMessage(msg.to,"「 MID 」\n" +  to)
                            line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            line.sendImageWithURL(to, str(path))
                    else:
                        line.sendMessage(to, "Talk Exception")
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("ไอดี "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)                          
                elif msg.text.lower().startswith("เพิ่มเพื่อน "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                           if mention["M"] not in lists:
                               lists.append(mention["M"])
                        for ls in lists:                           
                            line.findAndAddContactsByMid(ls)
                        line.sendMessage(to, "เพิ่ม " + str(contact.displayName) + " เป็นเพื่อนสำเร็จแล้ว")
                elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("วีดีโอ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))             

                elif msg.text.lower().startswith("ดึงหมด "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                me = line.getContact(ls)
                                path = line.getProfileCoverURL(ls)
                                path = str(path)
                                if settings["server"] == "VPS":
                                    line.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                    line.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                    line.sendMessage(msg.to,"「 MID 」\n" +  to)
                                    line.sendMessage(to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    line.sendImageWithURL(to, str(path))
                                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                else:
                                    line.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                    line.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                    line.sendMessage(msg.to,"「 MID 」\n" + ls)
                                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                    line.sendImageWithURL(to, str(path))

                elif msg.text in ["โหลด"]:
                    if msg._from in admin:
                        wek = line.getContact(lineMID)
                        a = wek.pictureStatus
                        r = wek.displayName
                        i = wek.statusMessage
                        s = open('mydn.txt',"w")
                        s.write(r)
                        s.close()
                        t = open('mysm.txt',"w")
                        t.write(i)
                        t.close()
                        u = open('myps.txt',"w")
                        u.write(a)
                        u.close()
                        line.sendText(msg.to, "backup has been active")
                        print (wek)
                        print (a)
                        print (r)
                        print (i)
                
                elif "ก็อป " in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = line.getContact(target)
                            X = contact.displayName
                            profile = line.getProfile()
                            profile.displayName = X
                            line.updateProfile(profile)
                            line.sendMessage(msg.to, "Success...")
                        #---------------------------------------
                            Y = contact.statusMessage
                            lol = line.getProfile()
                            lol.statusMessage = Y
                            line.updateProfile(lol)
                        #---------------------------------------
                            settings["changePictureProfile"] = True
                            me = line.getContact(target)     
                            line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                        except Exception as e:
                            line.sendMessage(msg.to, "Failed!")
                            print (e)

                elif "คืนร่าง" in msg.text:
                    if msg._from in admin:
                            try:
                                h = open('mydn.txt',"r")
                                name = h.read()
                                h.close()
                                x = name
                                profile = line.getProfile()
                                profile.displayName = x
                                line.updateProfile(profile)
                                i = open('mysm.txt',"r")
                                sm = i.read()
                                i.close()
                                y = sm
                                cak = line.getProfile()
                                cak.statusMessage = y
                                line.updateProfile(cak)
                                line.sendMessage(msg.to, "คืนได้แค่ชื่อกับตัสนะ😂😂")
                            except Exception as e:
                                line.sendText(msg.to,"การคืนร่างล้มเหลว!")
                                print (e)

                elif text.lower() == 'คืน':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(nadyaProfile)
                        line.sendMessage(msg.to, "เสร๋จ")
                    except:
                        line.sendMessage(msg.to, "Gagal restore profile")

                elif msg.text in ["Allprotect on","เปิดกันห้อง"]:
                        settings["kickMention"] = True
                        settings["Aip"] = False
                        RfuProtect["protect"] = True
                        RfuProtect["cancelprotect"] = True
                        RfuProtect["inviteprotect"] = True 
                        RfuProtect["linkprotect"] = True 
                        RfuProtect["Protectguest"] = True
                        RfuProtect["Protectjoin"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด เปิด👌")
						
                elif msg.text in ["Allprotect off","ปิดกันห้อง"]:
                        settings["kickMention"] = False
                        settings["Aip"] = False
                        RfuProtect["protect"] = False
                        RfuProtect["cancelprotect"] = False
                        RfuProtect["inviteprotect"] = False 
                        RfuProtect["linkprotect"] = False 
                        RfuProtect["Protectguest"] = False
                        RfuProtect["Protectjoin"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด ปิด👌")
                        
                elif msg.text in ["Allmsg on","เปิดข้อความ"]:
                        settings["Wc"] = True
                        settings["Lv"] = True
                        settings["Nk"] = True
                        settings["autoRead"] = True
                        settings["checkSticker"] = True 
                        settings["checkContact"] = True 
                        settings["checkPost"] = True
                        settings["potoMention"] = True
                        settings["detectMention"] = True
                        settings["delayMention"] = True
                        settings["Api"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด เปิด👌")
						
                elif msg.text in ["Allmsg off","ปิดข้อความ"]:
                        settings["Wc"] = False
                        settings["Lv"] = False
                        settings["Nk"] = False
                        settings["autoRead"] = True
                        settings["checkSticker"] = False 
                        settings["checkContact"] = False 
                        settings["checkPost"] = False
                        settings["detectMention"] = False
                        settings["potoMention"] = False
                        settings["delayMention"] = False
                        settings["Api"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด ปิด👌")
#==============================================================================#
                elif msg.text.lower().startswith("เพิ่มเลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("ลบเลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'เชคเลียนแบบ':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "เลียนแบบ" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "เปิด":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "ปิด":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")
                elif 'แอพ ' in msg.text.lower():
                        tob = msg.text.lower().replace('แอพ ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : Google Play\nลิ้งโหลด : https://play.google.com/store/search?q=" + tob)
                        line.sendText(msg.to,"👆กรุณากดลิ้งเพื่อทำการโหลดแอพ👆")
                elif 'ขอเพลง ' in msg.text.lower():
                        tob = msg.text.lower().replace('ขอเพลง ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : ยูทูป\nลิ้งรับชม : https://m.youtube.com/results?search_query=เพลง" + tob)
                        line.sendText(msg.to,"👆กรุณากดลิ้งเพื่อทำการโหลดแอพ👆")
                elif 'กิ๊ฟ ' in msg.text.lower():
                        tob = msg.text.lower().replace('กิ๊ฟ ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : GitHub\nลิ้ง : https://github.com/search?q=" + tob)
                        line.sendText(msg.to,"👆ค้นหาสำเร็จแล้ว👆")
                elif 'ค้น ' in msg.text.lower():
                        tob = msg.text.lower().replace('ค้น ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : กูเกิ้ล\nลิ้ง : https://www.google.co.th/search?q=" + tob)
                        line.sendText(msg.to,"👆ค้นหาสำเร็จแล้ว👆")
                elif 'เฟส ' in msg.text.lower():
                        tob = msg.text.lower().replace('เฟส ',"")
                        line.sendText(msg.to,"กรุณารอสักครู่...")
                        line.sendText(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : เฟสบุค\nลิ้ง : https://m.facebook.com/search/top/?q=" + tob)
                        line.sendText(msg.to,"👆ค้นหาสำเร็จแล้วเชิญกดลิ้งเพื่อเข้าไปดูรายละเอียด👆")
                elif "คท:" in msg.text:
                    mmid = msg.text.replace("คท:","")
                    line.sendMessage(to, text=None, contentMetadata={'mid': mmid}, contentType=13)
                elif msg.text.lower().startswith("ไลน์ "):
                    id = msg.text.lower().replace("ไลน์ ","")
                    conn = line.findContactsByUserid(id)
                    if True:                                      
                        line.sendMessage(to,"http://line.me/ti/p/~" + id)
                        line.sendContact(to,conn.mid)
                elif "สแปม " in msg.text:                
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ระบบรัวข้อความตามที่เราสั่ง"                   
                    link = "http://line.me/ti/p/~botline2034"                    
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("สแปม "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                             line.sendFooter(msg.to, teks ,link ,icon,name)
                        else:
                           line.sendFooter(msg.to, "Out of Range!" ,link ,icon,name)
                    elif txt[1] == "พอ":
                        if jmlh <= 100000:
                            line.sendFooter(msg.to, tulisan ,link ,icon,name)
                        else:
                            line.sendFooter(msg.to, "Out Of Range!" ,link ,icon,name)
                elif msg.text.lower().startswith("อัพชื่อ: "):
                    string = msg.text.lower().replace("อัพชื่อ: ", "")
                    if len(string) <= 10000000000:
                        pname =  line.getContact(sender).displayName
                        profile = line.getProfile()
                        profile.displayName = string
                        line.updateProfile(profile)
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        line.sendFooter(to, "Status : เปลี่ยนแล้ว\nชื่อเก่า : "+str(pname)+"\nเปลี่ยนเป็น : "+str(string), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif msg.text.lower().startswith("อัพตัส: "):
                    string = msg.text.lower().replace("อัพตัส: ", "")
                    if len(string) <= 10000000000:
                        pname = line.getContact(sender).statusMessage
                        profile = line.getProfile()
                        profile.statusMessage = string
                        line.updateProfile(profile)
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        line.sendFooter(to, "Status : เปลี่ยนแล้ว\nตัสเก่า : "+str(pname)+"\nเปลั่ยนเป็น : "+str(string), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
#==============================================================================#
                elif text.lower() == 'แอดมิน':
                    group = line.getGroup(to)
                    GS = group.creator.mid                    
                    line.sendContact(to, GS)
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ใช้ได้แต่ในกลุ่มเท่านั้น"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "☝คนนี้แหล่ะคนสร้างกลุ่มนี้" ,link ,icon,name)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ใช้ได้แต่ในกลุ่มเท่านั้น"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ไอดีกลุ่ม \n" + gid.id ,link ,icon,name)
                elif text.lower() == 'รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ใช้ได้แต่ในกลุ่มเท่านั้น"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, "ชื่อกลุ่ม -> \n" + gid.name ,link ,icon,name)
                elif text.lower() == 'ลิ้งกลุ่ม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "ลิ้งของกลุ่ม\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "คนนี้คือผู้สร้างกลุ่มนี้"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม👉 : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ใช้ได้แต่ในกลุ่มเท่านั้น"                   
                    link = "http://line.me/ti/p/~xael.py"
                    line.sendFooter(to, str(ret_),link ,icon,name)
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'สมาชิกกลุ่ม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'เช็คกลุ่ม':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))				                                     
                elif msg.text.lower().startswith("ถาม "):
                    kata = msg.text.lower().replace("ถาม ", "")
                    sch = kata.replace(" ","+")
                    with _session as web:
                        urlz = "http://lmgtfy.com/?q={}".format(str(sch))
                        r = _session.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
                        data = r.text
                        data = json.loads(data)
                        url = data["shorturl"]
                        ret_ = "「Ask」"
                        ret_ += "\n\nLink : {}".format(str(url))
                        line.sendMessage(to, str(ret_))
                elif msg.text.lower().startswith("บล็อคไอดี "):
                    user = msg.text.lower().replace("บล็อคไอดี ","")
                    line.blockContact(user)
                    line.sendMessage(to, "ทำการบล็อคไอดีนั้นแล้ว")        
                elif "ข้อมูล " in msg.text.lower():
                    spl = re.split("ข้อมูล ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = line.getContact(uid)
                            try:
                                line.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net{}".format(userData.picturePath))
                            except:
                                pass
                            line.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            line.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            line.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)                
                elif "xael" in msg.text:
                    spl = msg.text.split("xael")
                    if spl[len(spl)-1] == "":
                        line.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)

                elif "ล้อเล่น " in msg.text:
                        vkick0 = msg.text.replace("ล้อเล่น ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = nadya.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    line.kickoutFromGroup(msg.to,[target])
                                    line.findAndAddContactsByMid(target)
                                    line.inviteIntoGroup(msg.to,[target])
                                except:
                                    pass
                elif "แตก1" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                            line.sendMessage(msg.to,"แตก1สวยพี่สวย")
                elif "เตะ" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif "ปลิว" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)
                elif "มุด " in msg.text.lower():
                    spl = re.split("มุด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendText(msg.to,str(e))
                elif msg.text.lower().startswith("โทร "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        members = [mem.mid for mem in group.members]
                        line.acquireGroupCallRoute(to)
                        line.inviteIntoGroupCall(to, contactIds=members)
                    else:
                        line.sendMessage(to, "เชิญแล้วฮ่าๆ".format(str(jml)))


                elif msg.text.lower().startswith("แทค "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = line.getContact(receiver)
                                RhyN_(to, contact.mid)

                elif msg.text.lower().startswith("แอลแทค "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = ki.getContact(receiver)
                                RhyN_(to, contact.mid)

                elif msg.text.lower().startswith("แจก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver, text=None, contentMetadata={'sticker':'1002077'}, contentType=9)
                                line.sendMessage(to, "ส่งของขวัญใน ส.ต แล้ว".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith("ไวรัส "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver, ".God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                line.sendMessakge(to, "ไปดูแชทด้วยนะด้วยความหวังดี".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith("ส่วนตัว "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = line.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                line.sendMessage(receiver, str(settings["phu"]))
                                line.sendMessage(to, "ไปดูแชทด้วยนะครับ")
                            else:
                                pass
                elif msg.text.lower().startswith("ทัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    for x in range(jml):
                        name = line.getContact(to)
                        RhyN_(to, name.mid)
                elif msg.text.lower() == ".":
                    if msg.toType == 0:
                        sendMention(to, to, "", "")
                    elif msg.toType == 2:
                        group = line.getGroup(to)
                        contact = [mem.mid for mem in group.members]
                        mentionMembers(to, contact)

                elif msg.text.lower().startswith("คำห้ามพิม "):
                    wban = msg.text.lower().split()[1:]
                    wban = " ".join(wban)
                    wbanlist.append(wban)
                    line.sendMessage(to,"%s พิมคำนี้อาจมีปลิวนะ."%wban)
                elif msg.text.lower().startswith("ล้างคำห้ามพิม "):
                    wunban = msg.text.lower().split()[1:]
                    wunban = " ".join(wunban)
                    if wunban in wbanlist:
                        wbanlist.remove(wunban)
                        line.sendMessage(to,"%s ล้างออกจากคำสั่งห้ามพิมแล้ว."%wunban)
                    else:
                        line.sendMessage(to,"%s is not blacklisted."%wunban)
                elif msg.text.lower() == 'เช็คคำห้ามพิม':
                    tst = "คำห้ามพิม:\n"
                    if len(wbanlist) > 0:
                        for word in wbanlist:
                            tst += "- %s"%word
                        line.sendMessage(msg.to,tst)
                    else:
                        line.sendMessage(msg.to,"คำที่ห้ามพิมทั้งหมด")               
                elif text.lower() == 'แทค':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//2
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*2 : (a+1)*2]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += "@Alin \n"
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "จำนวนคนที่เราแทค"                   
                        link = "http://line.me/ti/p/~xael.py"
                        line.sendFooter(to,"\n[ จำนวนแทคทั้งหมด {} คน]".format(str(len(nama))),link ,icon,name)
                elif text.lower() == 'แท็ค':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = ''
                        txt = "╔══[ชื่อกลุ่ม {} ]\n╠ ".format(str(line.getGroup(to).name))
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += "╠ " + "@Alin \n"
                        else:
                            try:
                                tex += "╚══[ชื่อกลุ่ม   {} ]".format(str(line.getGroup(to).name))
                            except:
                                pass
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)                
                        
                elif "ประกาศ " in msg.text:                	
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความประกาศ"
                    link = "http://line.me/ti/p/~xael.py"
                    bc = msg.text.replace("ประกาศ ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendFooter(i,"••••••[ข้อความประกาศแชท]••••••\n\n"+bc+"\n\n『◉⊰ᎢᎬᎪᎷ ᏴØᎢ ᎠᎬᏞᎬᎢ⊱◉』",link ,icon,name)
                elif "ประกาศแชท " in msg.text:
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ข้อความประกาศ"
                    link = "http://line.me/ti/p/~xael.py"
                    bc = msg.text.replace("ประกาศแชท ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendFooter(i,"======[ข้อความประกาศแชท]======\n\n"+bc+"\n\n『◉⊰ᎢᎬᎪᎷ ᏴØᎢ ᎠᎬᏞᎬᎢ⊱◉』",link ,icon,name)
                    
                elif "ส่งรูปภามตามแชท: " in msg.text:
                    bc = msg.text.replace("ส่งรูปภาพตามแชท: ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendImageWithURL(i, bc)
                elif "ส่งเสียงกลุ่ม " in msg.text:
                    bctxt = msg.text.replace("ส่งเสียงกลุ่ม ", "")
                    bc = ("บาย...ภู...เป็ด...เซลบอท...ไลน์")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "ส่งเสียงแชท " in msg.text:
                    bctxt = msg.text.replace("ส่งเสียงแชท ", "")
                    bc = ("บาย...ภู...เป็ด...เซลบอท...ไลน์")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')
                    
                elif text.lower() == '/ปฏิทิน':
                    icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                    name = "ปฏิทิน"
                    link = "http://line.me/ti/p/~botline2034"
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "🌀ปฏิทิน🌀\n\n❄️⚡🎃❄️⚡🎃❄️⚡🎃❄️⚡🎃🌀" + "\n\n🐼" + hasil + "\n🐼 ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\n🐼 เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]" + "🌀❄️⚡❄️⚡❄️⚡❄️⚡❄️⚡🌀" + "\n\nBY: PHU SELF BOT LINE"
                    line.sendFooter(msg.to, readTime ,link ,icon,name)

                elif "รูปมา " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "กาตูน " in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
      
                elif "ยูทูป " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "ค้น " in msg.text.lower():
                    spl = re.split("ค้น ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        line.sendText(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    else:
                                        line.sendText(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                    text = "ผลการค้นหาจาก Google:\n\n"
                                    for el in resp.findAll("h3",attrs={"class":"r"}):
                                        try:
                                                tmp = el.a["class"]
                                                continue
                                        except:
                                                pass
                                        try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                        except:
                                                continue
                                        text += el.a.text+"\n"
                                        text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                    text = text[:-2]
                                    if msg.toType != 0:
                                        line.sendText(msg.to,str(text))
                                    else:
                                        line.sendText(msg.from_,str(text))
                                except Exception as e:
                                    print(e)
                        
                elif "วีดีโอ " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "วีดีโอ ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "หนัง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "หนัง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "เพลง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "เพลง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif msg.text in ["เปิดแอบ"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"เปิดระบบแสกนคนอ่านอัตโนมัติ")
                elif msg.text in ["ปิดแอบ"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "ปิดระบบแสกนคนอ่านแล้ว")

                elif text.lower() == 'ปิดเชล':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)
                elif text.lower() == "ลบแชท":
                        if msg._from in lineMID:
                            try:
                                line.removeAllMessages(op.param2)
                                line.sendMessage(msg.to,"ลบทุกการแชทเรียบร้อย")
                            except:
                                pass
                                print ("/ลบแชท")
                elif text.lower() == 'เพื่อน':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="🎎รายชื่อเพื่อนทั้งหมด🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎รายชื่อเพื่อนทั้งหมด🎎\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["เช็คบล็อค"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════ไม่มีรายการบัญชีที่ถูกบล็อค═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════รายการบัญชีที่ถูกบล็อค════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["ไอดีเพื่อน"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════รายการไอดีเพื่อน═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════รายการ ไอดีเพื่อน═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text.lower() == 'gurl':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link Groupnya Tanpa Buka Qr\n╚══════════════┛")

                elif msg.text == "เว็บโป๊":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")
                elif msg.text == "/ประกาศ":
                	line.sendMessage(msg.to,str(settings["message1"]))
                elif msg.text.lower() == '/ดึงแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Type👉 Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["?ไม่รับเชิญ"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)							
                        except:
                            pass
                elif msg.text in ["/เช็คไอดี"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="TEAM CLOWN OF DEAYH"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\nจำนวน  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)
                    
                elif msg.text in ["เปิดเตะแทค"]:
                    settings["kickMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบเตะคนแท็ก(○ﾟεﾟ○)")
                
                elif msg.text in ["ปิดเตะแทค"]:
                    settings["kickMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบเตะคนแท็ก(○ﾟεﾟ○)")
                    
                elif msg.text in ["เปิดแทค","Tag on"]:
                        settings['detectMention'] = True
                        line.sendMessage(msg.to,"เปิดระบบตอบกลับคนแทค(○ﾟεﾟ○)")
                
                elif msg.text in ["ปิดแทค","Tag off"]:
                        settings['detectMention'] = False
                        line.sendMessage(msg.to,"ปิดระบบตอบกลับคนแทค(○ﾟεﾟ○)")

                elif msg.text in ["เปิดแทค2","Tag2 on"]:
                    settings["potoMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบส่งรูปคนแทค(○ﾟεﾟ○)")
                
                elif msg.text in ["ปิดแทค2","Tag2 off"]:
                    settings["potoMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบส่งรูปคนแทค(○ﾟεﾟ○)")
                    
                elif msg.text in ["เปิดแทค3","Tag3 on"]:
                    settings["delayMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบแทคกลับคนแทค(○ﾟεﾟ○)")
                
                elif msg.text in ["ปิดแทค3","Tag3 off"]:
                    settings["delayMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบแทคกลับคนแทค(ˉ(∞)ˉ)")
                elif msg.text.lower() == "เปิดแทคแชท":
                    settings["detectMentionPM"] = True
                    line.sendMessage(msg.to,"เปิดแทคแชทเรียบร้อยครับ")
                elif msg.text.lower() == "ปิดแทคแชท":
                    settings["detectMentionPM"] = False
                    line.sendMessage(msg.to,"ปิดแทคแชทเรียบร้อยครับ")
                elif msg.text.lower().startswith("แทคแชท: "):
                    text = msg.text.lower().replace("แทคแชท: ","")                    
                    settings["pmMessage"] = text
                    line.sendMessage(msg.to, "คำแทคแชท สต คือ : {}".format(str(settings["pmMessage"])))
                elif msg.text.lower().startswith("setrespongroup: "):
                    text = msg.text.lower().replace("setrespongroup: ","")
                    settings["respMessage"] = text
                    line.sendMessage(msg.to, "Success Update Response Group to : {}".format(str(settings["respMessage"])))
                    
                elif msg.text in ["เปิดกันบิน"]:
                    settings["Aip"] = True
                    line.sendMessage(msg.to,"เปิดระบบตรวจสอบคำหยาบกับบอทบิน^ω^")
                
                elif msg.text in ["ปิดกันบิน"]:
                    settings["Aip"] = False
                    line.sendMessage(msg.to,"ปิดระบบตรวจสอบคำหยาบกับบอทบินแล้วʕ•ﻌ•ʔ")
                    
                elif msg.text in ["เปิดพูด"]:
                    settings["Api"] = True
                    line.sendMessage(msg.to,"เปิดระบบApiข้อความ")
                
                elif msg.text in ["ปิดพูด"]:
                    settings["Api"] = False
                    line.sendMessage(msg.to,"ปิดระบบApiข้อความแล้ว")
                    
                elif 'ตั้งแอด: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแอด: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["message"] = spl
                         line.sendMessage(msg.to, "👇ตั้งข้อความตอบโต้เมื่อมีคนแอดแล้ว ดังนี้👇\n\n👉{}".format(str(spl)))
         
                elif 'ไอคอน: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ไอคอน: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["icon"] = spl
                         line.sendMessage(msg.to, "👇ตั้งข้อความตอบโต้เมื่อมีคนแอดแล้ว ดังนี้👇\n\n👉{}".format(str(spl)))
 
                elif 'ตั้งคท: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งคท: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["me"] = spl
                         line.sendMessage(msg.to, "👇ตั้งข้อความตอบโต้เมื่อมีคนแอดแล้ว ดังนี้👇\n\n👉{}".format(str(spl)))
               
                elif 'คอมเม้น: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('คอมเม้น: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["comment"] = spl
                         line.sendMessage(msg.to, "👇ตั้งข้อความคอมเม้นของคุณแล้ว ดังนี้👇\n\n👉{}".format(str(spl))) 

                elif 'ส่วนตัว: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ส่วนตัว: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["phu"] = spl
                         line.sendMessage(msg.to, "👇ตั้งข้อความคอมเม้นของคุณแล้ว ดังนี้👇\n\n👉{}".format(str(spl))) 
                    
                elif 'ตั้งแทค: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแทค: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย")
                     else:
                         settings["Respontag"] = spl
                         line.sendMessage(msg.to, "ข้อความคนแทค\n\n➠{}".format(str(spl)))
                         
                elif 'ตั้งเตะ: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งเตะ: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความคนคนลบสมาชิดเรียบร้อย")
                     else:
                          settings["kick"] = spl
                          line.sendMessage(msg.to, "ข้อความเตะออกกลุ่ม\n\n➠{}".format(str(spl)))

                elif 'ตั้งออก: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งออก: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความคนออกเรียบร้อย")
                     else:
                          settings["bye"] = spl
                          line.sendMessage(msg.to, "ข้แความคนออกกลุ่ม\n\n➠{}".format(str(spl)))

                elif 'ตั้งเข้า: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งเข้า: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความคนเข้าเรียบร้อยแล้ว")
                     else:
                          settings["welcome"] = spl
                          line.sendMessage(msg.to, "ข้อความคนเข้ากลุ่ม\n\n➠{}".format(str(spl)))
                elif msg.text.lower() == "เปิดเตะติก":
                        settings["sticker"] = True
                        line.sendMessage(to,"เปิดเตะคนรันสติกเกอรแล้ว")
                elif msg.text.lower() == "ปิดเตะติก":
                        settings["sticker"] = False
                        line.sendMessage(to,"ปิดเตะคนรันสติกเกอรแล้ว")
                elif msg.text.lower() == "sleepmode":
                    if settings["replyPesan"] is not None:
                        line.sendMessage(to,"Your Sleepmode is : " + str(settings["replyPesan"]))
                        msgSticker = settings["messageSticker"]["listSticker"]["sleepSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                    else:
                        line.sendMessage(to,"My Sleepmode : No messages are set")
                elif msg.text.lower() == "addsleepmodesticker":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "sleepSticker"
                    line.sendMessage(to, "โปรดส่งสติ๊กเกอร์ที่คุณต้องการเพิ่ม")
                elif msg.text.lower() == "delsleepmodesticker":
                    settings["messageSticker"]["listSticker"]["sleepSticker"] = None
                    line.sendMessage(to, "ลบรายการสติ๊กเกอร์เรียบร้อย")
                elif msg.text.lower().startswith("setsleepmode: "):
                    text_ = msg.text.lower().replace("setsleepmode:", "")
                    try:
                        settings["replyPesan"] = text_
                        line.sendMessage(to,"Sleep mode changed to : " + text_)
                    except:
                        line.sendMessage(to,"SleepMode \nFailed to replace message")
                elif msg.text.lower() == "ติกออก":
                        msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติกออก":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "leaveSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติกคนออก":
                    settings["messageSticker"]["listSticker"]["leaveSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว")
                elif msg.text.lower() == "ติกเตะ":
                        msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติกเตะ":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "kickSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติกเตะ":
                    settings["messageSticker"]["listSticker"]["kickSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเตะแล้ว")
                elif msg.text.lower() == "ติกเข้า":
                        msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติกเข้า":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "welcomeSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะตั้งลงมา")
                elif msg.text.lower() == "ลบติกเข้า":
                    settings["messageSticker"]["listSticker"]["welcomeSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนเข้าแล้ว")
                elif msg.text.lower()== "ติกแอด":
                        msgSticker = settings["messageSticker"]["listSticker"]["addSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower()== "ตั้งติกแอด":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "addSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติกแอด":
                    settings["messageSticker"]["listSticker"]["addSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนแทคแล้ว")
                elif msg.text.lower() == "ติกแทค":
                        msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif msg.text.lower() == "ตั้งติกแทค":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "responSticker"
                    line.sendMessage(to, "ส่งสติกเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "/ลบติ๊กคนแทค":
                    settings["messageSticker"]["listSticker"]["responSticker"] = None
                    line.sendMessage(to, "ลบสติกเกอรคนแทคแล้ว")
                elif msg.text.lower() == "ตั้งติกแอบ":
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "readerSticker"
                    line.sendMessage(to, "ส่งสติ๊กเกอรที่จะใช่ลงมา")
                elif msg.text.lower() == "ลบติกแอบ":
                    settings["messageSticker"]["listSticker"]["readerSticker"] = None
                    line.sendMessage(to, "ลบสติ๊กเกอรคนแอบอ่านแล้ว")
                elif msg.text.lower() == "ติกแอบ":
                        msgSticker = settings["messageSticker"]["listSticker"]["readerSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                elif "/kedip " in msg.text:
                    txt = msg.text.replace("kedip ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    line.sendMessage(msg.to, t1 + txt + t2)						
                elif msg.text in ["ดึง"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"ลงคทคนที่จะดึงเข้าห้องเลยครับ")                            
                elif msg.text.lower() == "ยกเลิก":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == "บอทยก":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
#=============COMMAND KICKER===========================#
                elif msg.text in ["ดำ"]:
                  if msg._from in admin: 
                    settings["wblacklist"] = True
                    line.sendText(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["ขาว"]:
                  if msg._from in admin: 
                    settings["dblacklist"] = True
                    line.sendText(msg.to,"กรุณาส่งคอทแทค")
                elif msg.text in ["ล้างดำ"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลบัญชีดำทั้งหมดเรียร้อย")
                    print ("Clear Ban")
                elif msg.text.lower() == "คทดำ":
                    if msg._from in lineMID:
                        if settings["blacklist"] == []:
                            line.sendMessage(to, "Nothing boss")
                        else:
                            for bl in settings["blacklist"]:
                                line.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif 'ลาก่อย' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")

                elif 'บาย' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kk.kickoutFromGroup(msg.to,[target])             
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'เชิญ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "Type👉 Invite Succes")
                           except:
                               line.sendMessage(msg.to,"Type👉 Limit Invite")
                elif "บล็อค @" in msg.text:
                    if msg.toType == 2:
                        print ("[block] OK")
                        _name = msg.text.replace("บล็อค @","")
                        _nametarget = _name.rstrip('  ')
                        gs = line.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                               targets.append(g.mid)
                        if targets == []:
                            sendMassage(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                   line.blockContact(target)
                                   sendMessage(msg.to, "Success block contact~")
                                except Exception as e:
                                   print (e)
                elif msg.text.lower() == 'บล็อค':
                    blockedlist = line.getBlockedContactIds()
                    sendMessage(msg.to, "Please wait...")
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="User Blocked List\n"
                    for ids in kontak:
                        msgs+="\n%i. %s" % (num, ids.displayName)
                        num=(num+1)
                        msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                        sendMessage(msg.to, msgs)
                elif "ปวดตับ" in msg.text:
                	if msg.toType == 2:
                         _name = msg.text.replace("ปวดตับ","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"Just some casual cleansing ô")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"Not found.")
                         else:
                             for target in targets:
                             	if not target in Rfu:
                                     try:
                                         klist=[line]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"Group cleanse")
                                         print ("Cleanse Group")

                elif msg.text in ["ไล่ดำ"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"Nots in Blacklist")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")



                elif "คิก1: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        ki.updateProfile(profile_A)
                        ki.sendMessage(msg.to,"เปลี่ยนชื่อคิกแล้ว " + string)
                        print ("Update Name")

                elif "คิก2: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        kk.updateProfile(profile_A)
                        kk.sendMessage(msg.to,"เปลี่ยนชื่อคิกแล้ว" + string)
                        print ("Update Name")

                elif "คิก3: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        kc.updateProfile(profile_A)
                        kc.sendMessage(msg.to,"เปลี่ยนชื่อคิกแล้ว " + string)
                        print ("Update Name")

                elif "คิก4: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        ke.updateProfile(profile_A)
                        ke.sendMessage(msg.to,"เปลี่ยนชื่อคิกแล้ว " + string)
                        print ("Update Name")

                elif "ตัส1: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        ki.updateProfile(profile_A)
                        ki.sendMessage(msg.to,"เปลี่ยนตัสคิกแล้ว " + string)
                        print ("Update Bio Succes")

                elif "ตัส2: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        kk.updateProfile(profile_A)
                        kk.sendMessage(msg.to,"เปลี่ยนตัสคิกแล้ว " + string)
                        print ("Update Bio Succes")

                elif "ตัส3: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        kc.updateProfile(profile_A)
                        ke.sendMessage(msg.to,"เปลี่ยนตัสคิกแล้ว " + string)
                        print ("Update Bio Succes")

                elif "ตัส4: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        ke.updateProfile(profile_A)
                        ke.sendMessage(msg.to,"เปลี่ยนตัสคิกแล้ว " + string)
                        print ("Update Bio Succes")


#                elif "ชื่อ: " in text.lower():
#                    if msg._from in Family:
#                        proses = text.split(":")
#                        string = text.replace(proses[0] + ": ","")
#                        profile_A = line.getProfile()
#                        profile_A.displayName = string
#                        line.updateProfile(profile_A)
#                        line.sendMessage(msg.to,"Update to " + string)
#                        print ("Update Name")

#                elif "ตัส: " in msg.text.lower():
#                    if msg._from in Family:
#                        proses = text.split(":")
#                        string = text.replace(proses[0] + ": ","")
#                        profile_A = line.getProfile()
#                        profile_A.statusMessage = string
#                        line.updateProfile(profile_A)
#                        line.sendMessage(msg.to,"Succes Update 👉 " + string)
#                        print ("Update Bio Succes")

#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == 'เปิดกัน':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")

                elif msg.text.lower() == 'ปิดกัน':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")

                elif msg.text.lower() == 'กันยก':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'ปิดกันยก':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'กันเชิญ':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'ปิดกันเชิญ':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'กันลิ้ง':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'ปิดกันลิ้ง':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'กันกลุ่ม':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'ปิดกันกลุ่ม':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'กันเข้า':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'ปิดกันเข้า':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'เปิดหมด':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

                elif msg.text.lower() == 'ปิดหมด':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == 'เปิดทักเข้า':
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม(○ﾟεﾟ○)")
                elif msg.text.lower() == 'ปิดทักเข้า':
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับเมื่อมีสมาชิกเข้ากลุ่ม(○ﾟεﾟ○)")
                                
                elif msg.text.lower() == 'เปิดเตะ':
                        if settings["Nk"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Nk"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่ม(○ﾟεﾟ○)")
                                
                elif msg.text.lower() == 'ปิดเตะ':
                        if settings["Nk"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว(○ﾟεﾟ○)")
                        else:
                            settings["Nk"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความแจ้งเตือนเมื่อมีคนลบสมาชิกในกลุ่มแล้ว(○ﾟεﾟ○)")

                elif msg.text.lower() == 'เปิดทักออก':
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม(○ﾟεﾟ○)")
                elif msg.text.lower() == 'ปิดทักออก':
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม(○ﾟεﾟ○)")
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความอำลาเมื่อมีสมาชิกออกกลุ่ม(○ﾟεﾟ○)")
                                
                elif msg.text.lower() == 'เปิดคท':
                        if settings["checkContact"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบอ่านข้อมูลด้วยคอนแทค(○ﾟεﾟ○)")
                        else:
                            settings["checkContact"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบอ่านข้อมูลด้วยคอนแทคไว้อยู่แล้ว(○ﾟεﾟ○)")
                elif msg.text.lower() == 'ปิดคท':
                        if settings["checkContact"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบอ่านข้อมูลด้วยคอนแทค(○ﾟεﾟ○)")
                        else:
                            settings["checkContact"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบอ่านข้อมูลด้วยคอนแทคไว้อยู่แล้ว(○ﾟεﾟ○)")
                elif msg.text.lower() == 'เปิดโพส':
                        if settings["checkPost"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบเช็คโพสบนทามไลน์(○ﾟεﾟ○)")
                        else:
                            settings["checkPost"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดระบบเช็คโพสบนทามไลน์อยู่แล้ว(○ﾟεﾟ○)")
                elif msg.text.lower() == 'ปิดโพส':
                        if settings["checkPost"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบเช็คโพสบนทามไลน์(○ﾟεﾟ○)")
                        else:
                            settings["checkPost"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดระบบเช็คโพสบนทามไลน์ไว้อยู่แล้ว(○ﾟεﾟ○)")
                elif text.lower() == "เปลี่ยนดิส":
                    settings["changePictureProfile"] = True
                    line.sendMessage(to, "ส่งรูปภาพลงมาได้เลยครับผม(○ﾟεﾟ○)")
                elif text.lower() == "เปลี่ยนรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                        line.sendMessage(to, "ส่งรูปภาพลงมาไดเเลยครับผม(○ﾟεﾟ○)")
                elif text.lower() == "ดับไฟ":
                    line.sendContact(to, 'u1f41296217e740650e0448b96851a3e2','')

                elif text.lower() == 'ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบรันเสร็จแล้วขอรับ")
                    line.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))
			
                elif "ลงดำ" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace(".ลงดำ","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"แบนสมาชิกทุกคนในห้องนี้แล้ว＼（○＾ω＾○）／")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
#                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")
										   
                elif 'แบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
#                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes added for the blacklist ")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

                elif 'ล้างแบน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
#                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes unban from the blacklist. ")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")
                
                elif msg.text in ["เช็คดำ"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่พบ") 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ติดดำ")
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))

            elif msg.contentType == 13:
                if settings["checkContact"] == True:
                    try:
                        contact = line.getContact(msg.contentMetadata["mid"])
                        if line != None:
                            cover = line.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            line.sendImageWithURL(to, str(path))
                        except:
                            pass
                        ret_ = "[ รายการทั้งหมดจากการสำรวจด้วย คท ]"
                        ret_ += "\n ชื่อ : {}".format(str(contact.displayName))
                        ret_ += "\n ไอดี : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n ตัส : {}".format(str(contact.statusMessage))
                        ret_ += "\n รูปโปรไฟล : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n  รูปปก : {}".format(str(cover))
                        ret_ += "\n[ สิ้นสุดการสำรวจ ]"
                        line.sendMessage(to, str(ret_))
                    except:
                        line.sendMessage(to, "เกิดข้อผิดพลาดในการสำรวจ")
                #for image in images:
                    #if text.lower() == image:
                        #line.sendImage(to, images[image])
                #for sticker in stickers:
                    #if text.lower() == sticker:
                        #sid = stickers[sticker]["STKID"]
                       # spkg = stickers[sticker]["STKPKGID"]
                       # sver = stickers[sticker]["STKVER"]
                        #sendSticker(to, sver, spkg, sid)
            elif msg.contentType == 1:
                if settings["changePictureProfile"] == True:
                    path = line.downloadObjectMsg(msg_id)
                    settings["changePictureProfile"] = False
                    line.updateProfilePicture(path)
                    line.sendMessage(to, "ทำการแปลงโฉมเสร็จเรียบร้อย")
                if msg.toType == 2:
                    if to in settings["changeGroupPicture"]:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changeGroupPicture"].remove(to)
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "เปลี่ยนรูปโปรสำเร็จแล้วครับ"                   
                        link = "http://line.me/ti/p/~xael.py"
                        line.updateGroupPicture(to, path)
                        line.sendFooter(to, "เปลี่ยนรูปภาพกลุ่มเรียบร้อยแล้ว" ,link ,icon,name)
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "Success Added " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "ตั้งติ๊ก {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
                   
#            elif msg.contentType == 7:
#                if settings["checkSticker"] == True:
#                    stk_id = msg.contentMetadata['STKID']
#                    stk_ver = msg.contentMetadata['STKVER']
#                    pkg_id = msg.contentMetadata['STKPKGID']
#                    ret_ = "╔══[ Sticker Info ]"
#                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
#                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
#                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
#                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
#                    ret_ += "\n╚══[ Finish ]"
#                    line.sendMessage(to, str(ret_))
#==============================================================================#
        if op.type == 19:
          if op.param2 in Family:
            pass
          if op.param2 in RfuBot:
          	pass
          else:
            if op.param3 in lineMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kk.getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)		  
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in kiMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kk.getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in kkMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kk.getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in kcMID:
              if op.param2 not in Family:
                try:
                  G = kc.getGroup(op.param1)
                  G = ke.getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
  #                json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in keMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kc.getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


            if op.param3 in kfMID:
              if op.param2 not in Family:
                try:
                  G = kk.getGroup(op.param1)
                  G = ke.getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in kgMID:
              if op.param2 not in Family:
                try:
                  G = kc.getGroup(op.param1)
                  G = ki.getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)


            if op.param3 in khMID:
              if op.param2 not in Family:
                try:
                  G = kj.getGroup(op.param1)
                  G = kf.getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in kjMID:
              if op.param2 not in Family:
                try:
                  G = line.getGroup(op.param1)
                  G = ke.getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  invlist = RfuBot
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(Rfu).inviteIntoGroup(op.param1,[invlist])
                  line.acceptGroupInvitation(op.param1)
                  ki.acceptGroupInvitation(op.param1)
                  kk.acceptGroupInvitation(op.param1)
                  kc.acceptGroupInvitation(op.param1)
                  ke.acceptGroupInvitation(op.param1)			  
                  kf.acceptGroupInvitation(op.param1)
                  kg.acceptGroupInvitation(op.param1)
                  kh.acceptGroupInvitation(op.param1)
                  kj.acceptGroupInvitation(op.param1)	
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
#                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#==============================================================================#          
#==============================================================================#
        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)    
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)
                kf.leaveRoom(op.param1)  
                kg.leaveRoom(op.param1)  
                kh.leaveRoom(op.param1)  
                kj.leaveRoom(op.param1)
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)     
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)
                kf.leaveRoom(op.param1)  
                kg.leaveRoom(op.param1)  
                kh.leaveRoom(op.param1)  
                kj.leaveRoom(op.param1)               
#-------------------------------------------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in lineMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)							
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                                                
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True                       

                elif op.param3 in kiMID:
                    if op.param2 in lineMID:
                        G = kk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)					
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in kkMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in kcMID:
                    if op.param2 in kkMID:
                        G = kk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)							
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                elif op.param3 in keMID:
                    if op.param2 in kcMID:
                        G = ke.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ke.updateGroup(G)
                        ticket = ke.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                    else:
                        G = ke.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ke.updateGroup(G)
                        ticket = ke.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ke.updateGroup(G)
                        settings["blacklist"][op.param2] = True
						
                elif op.param3 in kfMID:
                    if op.param2 in keMID:
                        G = kf.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kf.updateGroup(G)
                        ticket = kf.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                    else:
                        G = kf.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kf.updateGroup(G)
                        ticket = kf.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kf.updateGroup(G)
                        settings["blacklist"][op.param2] = True	

                elif op.param3 in kgMID:
                    if op.param2 in kfMID:
                        G = kg.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kg.updateGroup(G)
                        ticket = kg.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kg.updateGroup(G)
                    else:
                        G = kg.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kg.updateGroup(G)
                        ticket = kg.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kg.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in khMID:
                    if op.param2 in kgMID:
                        G = kh.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kh.updateGroup(G)
                        ticket = kh.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kg.updateGroup(G)
                    else:
                        G = kh.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kh.updateGroup(G)
                        ticket = kh.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kh.updateGroup(G)
                        settings["blacklist"][op.param2] = True		

                elif op.param3 in kjMID:
                    if op.param2 in khMID:
                        G = kj.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kj.updateGroup(G)
                        ticket = kj.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kj.updateGroup(G)
                    else:
                        G = kj.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kj.updateGroup(G)
                        ticket = kj.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kf.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kg.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kh.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)	
                        kj.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kh.updateGroup(G)
                        settings["blacklist"][op.param2] = True								
            except:
                pass
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])
        
        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])

        if op.type == 5:
            if RfuProtect["autoBlock"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["comment"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))
                    ki.sendMessage(op.param1,str(settings["message"]))
                    kk.sendMessage(op.param1,str(settings["message"]))
                    kc.sendMessage(op.param1,str(settings["message"]))
                    ke.sendMessage(op.param1,str(settings["message"]))
                    kf.sendMessage(op.param1,str(settings["message"]))
                    kg.sendMessage(op.param1,str(settings["message"]))
                    kh.sendMessage(op.param1,str(settings["message"]))
                    kj.sendMessage(op.param1,str(settings["message"]))					
        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 17:
            if op.param2 in settings["blacklist"] == {}:
                line.kickoutFromGroup(op.param1,[op.param2])
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                ki.sendMessage(op.param1,"สมาชิกที่ถูกแบนไม่ได้รับอนุญาตให้เข้าร่วมกลุ่ม （´・ω・｀）"+tm)
        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")
        if op.type == 25:
#            if settings ["mutebot2"] == True:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if settings["messageSticker"]["addStatus"] == True:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            line.sendMessage(to, "Success Added " + name)
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                    if settings["addSticker"]["status"] == True:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
        if op.type in [25,26]:
            msg = op.message
            if msg.contentType == 16:
                if settings["checkPost"] == True:
                        try:
                            ret_ = "[ ข้อมูลของโพสนี้ ]"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = line.getContact(msg._from)
                                auth = "\n  ผู้เขียนโพส : {}".format(str(contact.displayName))
                            else:
                                auth = "\n  ผู้เขียนโพส : {}".format(str(msg.contentMetadata["serviceName"]))
                            purl = "\n  ลิ้งโพส : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                            ret_ += auth
                            ret_ += purl
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n  Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n  Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n  Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "text" in msg.contentMetadata:
                                text = "\n ข้อความโดยย่อ : {}".format(str(msg.contentMetadata["text"]))
                                ret_ += text
                            ret_ += "\n[ สิ้นสุดการเช็คโพส ]"
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "เกิดข้อผิดะลาดในการเช็คโพสนี้")
                            
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if settings ["Aip"] == True:
            	    if msg.text in ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ",".","ปลิว"]:
                        line.kickoutFromGroup(receiver,[sender])
                        line.sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)")
                if settings ["Api"] == True:
            	    if msg.text in ["แอล"]:                  	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~xael.py"
                        line.sendFooter(msg.to,"มีอะไรรึปล่าวครับถ้าสนใจเชลบอททักแชทมาเลยครับ",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["บอท","เซล","เซลบอท","selfbot","คนรึบอท","Help","help",".help","/help","คำสั่ง"]:                   	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~xael.py"
                        line.sendFooter(msg.to,"XAEL SELF BOT LINE สนใจเชลบอทรึบอทต่างแอดมาทักสอบถามได้ http://line.me/ti/p/~xael.py",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["55","555","5555","55555","55+","555+","5555+","ขำ",".ขำ"]:                    	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~xael.py"
                        line.sendFooter(msg.to,"ฮ่าๆๆๆ..ขำไร...ถถถ...บ้าอ่อ",link ,icon,name)
                        line.sendMessage(msg.to, None, contentMetadata={"STKID":"56618796","STKPKGID":"11637","STKVER":"1"}, contentType=7)
                if settings ["Api"] == True:
                    if msg.text in ["คท",".คท","me","!me",".me","/me",".โย่ว","!โย่ว","!คท"]:                    	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~xael.py"
                        line.sendFooter(msg.to,"เช็คจัง...กลัวหลุดมากอ่อ",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["แทค",".แทค",".แจ๊ะ","tag","tagall","!แทค","!แจ๊ะ"]:                   	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~toeyc.py"
                        line.sendFooter(msg.to,"แทคไรหนักหนาครับ...กำ",link ,icon,name)
                        line.sendMessage(msg.to, None, contentMetadata={"STKID":"147","STKPKGID":"2","STKVER":"100"}, contentType=7)
                if settings ["Api"] == True:
                    if msg.text in [".วัดรอบ","sp","speed",".สปีด","สปีด","ความเร็ว","!speed","!สปีด"]:                   	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~toeyc.py"
                        line.sendFooter(msg.to,"ไวเกินมองไม่ทั้นขออีกทีได้ปะ😁😁",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["@","แอด","แอดมิน","แอดกลุ่ม"]:                 	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~toeyc.py"
                        line.sendFooter(msg.to,"Siriv10:groupcreator",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["อย","อยู่ไหม","อยู่บ่"]:                    	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~toeyc.py"
                        line.sendFooter(msg.to,"ว่าวอยุ่อย่ากวนสิ",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["@@","แอดรอง","รองแอด"]:                    	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~toeyc.py"
                        line.sendFooter(msg.to,"Siriv10:予備作成者",link ,icon,name)
                if settings ["Api"] == True:
                    if msg.text in ["ล๊อก","ล็อค","ชุดล็อค","ล็อคบ้าน"]:       	
                        icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                        name = "ข้อความอัติโนมัติ"                   
                        link = "http://line.me/ti/p/~toeyc.py"
                        line.sendFooter(msg.to,"ให้แอดมินก๊อปคำสั่งวางทีละอัน",link ,icon,name)
                        line.sendFooter(msg.to,"Set:iconlock:on",link ,icon,name)
                        line.sendFooter(msg.to,"Set:ownerlock:on",link ,icon,name)
                        line.sendFooter(msg.to,"Set:changenamelock:on",link ,icon,name)
                        line.sendFooter(msg.to,"Set:blockinvite:on",link ,icon,name)
                if settings["autoRead"] == True:
                        line.sendChatChecked(to, msg_id)				
                if to in read["readPoint"]:
                   if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    if msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        ret_ = "Sticker Info"
                        ret_ += "\nSTICKER ID : {}".format(stk_id)
                        ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                        ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                        line.sendMessage(to, text=None, contentMetadata={'STKID':'107', 'STKVER':'100', 'STKPKGID':'1'}, contentType=7)
                    elif msg.contentType == 1:
                        line.sendMessage(to, text=None, contentMetadata={"STKID": "190", "STKVER": "100", "STKPKGID": "3"}, contentType=7)
                    else:
                        if text is not None:
                            txt = text
                            line.sendMessage(msg.to,txt)
                elif msg.contentType == 7:
                    if settings["checkSticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            line.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                            name = "ข้อมูลสติกเกอร์"
                            link = "http://line.me/ti/p/~xael.py"
                            line.sendFooter(to, str(ret_),link ,icon,name)
                        except Exception as error:
                            line.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in lineMID:
                            try:
                                line.kickoutFromGroup(msg.to,[sender])
                                line.sendMessage("คุณพูดคำต้องห้าม จำเป็นต้องนำออก sorry(╯°□°）╯︵ ┻━┻")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = line.findGroupByTicket(ticket_id)
                                line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                line.sendMessage(to, "มุดลิ้งเข้าไปในกลุ่ม👉 %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.toType == 0 and settings["autoReply"] and sender != lineMID:
                    contact = line.getContact(sender)
                    rjct = ["auto", "ngetag"]
                    validating = [a for a in rjct if a.lower() in text.lower()]
                    if validating != []: return
                    if contact.attributes != 32:
                        msgSticker = settings["messageSticker"]["listSticker"]["sleepSticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                        if "@!" in settings["replyPesan"]:
                            msg_ = settings["replyPesan"].split("@!")
                            sendMention(to, sender, "Sleep Mode :\n" + msg_[0], msg_[1])
                        sendMention(to, sender, "Sleep Mode :\nจ๊ะเอ๋", settings["replyPesan"])
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    if settings["detectMentionPM"] == True:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                                sendMention(sender, sender, "「ตอบแทคอัตโนมัติ」\n", "\n" + str(settings["pmMessage"]))
                                break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in msg.contentMetadata.keys() != None:
        	             if settings['kickMention'] == True:
        		             contact = line.getContact(msg._from)
        		             cName = contact.displayName
        		             balas = ["เนื่องจากตอนนี้ผมเปิดระบบเตะคนแทคไว้ " + "\n👉" + cName + "\n🙏ต้องขออภัยด้วยจริงๆ🙏Bye!!!"]
        		             ret_ = "" + random.choice(balas)                     
        		             name = re.findall(r'@(\w+)', msg.text)
        		             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
        		             mentionees = mention["MENTIONEES"]
        		             for mention in mentionees:
        			               if mention['M'] in admin:
        				                  line.sendText(msg.to,ret_)
        				                  random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
        				                  break                                  
        			               if mention['M'] in lineMID:
        				                  line.sendText(msg.to,ret_)
        				                  random.choice(Rfu).kickoutFromGroup(msg.to,[msg._from])
        				                  break
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             mi_d = contact.mid
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          line.sendContact(msg.to, mi_d)
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:                    
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = [ cName ]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
                                          name = "ข้อความคนแทค"
                                          link = "http://line.me/ti/p/~xael.py"
                                          line.sendFooter(to,ret_ ,link ,icon,name)
                                          line.sendFooter(to,str(settings["Respontag"]),link ,icon,name)
                                          msgSticker = settings["messageSticker"]["listSticker"]["responSticker"]
                                          if msgSticker != None:
                                              sid = msgSticker["STKID"]
                                              spkg = msgSticker["STKPKGID"]
                                              sver = msgSticker["STKVER"]
                                              sendSticker(to, sver, spkg, sid)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['delayMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          sendMessageWithMention(to, contact.mid)                                          
                                          break
        if op.type == 17:
           print ("ต้อนรับคนเข้ากลุ่ม")
           if settings["Wc"] == True:
             if op.param2 in lineMID:
                 return            
             icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
             name = "ข้อความต้อนรับ"                   
             link = "http://line.me/ti/p/~xael.py"
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendFooter(op.param1,"สวัสดี {} ".format(str(dan.displayName),str(tgb.name)) + str(settings["welcome"]),link ,icon,name)
             line.sendContact(op.param1, op.param2)
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 19:
           print ("ข้อความคนเตะกัน")
           if settings["Nk"] == True:
             if op.param2 in lineMID:
                 return
             icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
             name = "ข้อความคนเตะกัน"                   
             link = "http://line.me/ti/p/~xael.py"
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,"วู้วเท่ไปเลย".format(str(dan.displayName)) + str(settings["kick"]),link ,icon,name)
             line.sendContact(op.param1, op.param2)             
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 15:
           print ("ข้อความอำลาคนออก")
           if settings["Lv"] == True:
             if op.param2 in lineMID:
                 return
             icon = "http://dl.profile.line.naver.jp/"+lineProfile.pictureStatus
             name = "ข้อความคนออก"                   
             link = "http://line.me/ti/p/~xael.py"
             dan = line.getContact(op.param2)
             tgb = line.getGroup(op.param1)
             line.sendMessage(op.param1,"บาย {} ".format(str(dan.displayName),str(tgb.name)) + str(settings["bye"]),link ,icon,name)
             line.sendContact(op.param1, op.param2)
             line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath)) 
#==============================================================================================================
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                at = op.param1
                msg_id = op.param2
                if msg_id in msg_dict:
                    ah = time.time()
                    ikkeh = line.getContact(msg_dict[msg_id]["from"])
                    if "text" in msg_dict[msg_id]:
                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                        waktumsg = format_timespan(waktumsg)
                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                        rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                        sendMention(at, ikkeh.mid, " ** Resend Message **\n\nMaker :\n", str(rat_))
                        del msg_dict[msg_id]
                    else:
                        if "image" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nImage :\nBelow"
                            sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                            line.sendImage(at, msg_dict[msg_id]["image"])
                            del msg_dict[msg_id]
                        else:
                            if "video" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nVideo :\nBelow"
                                sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                line.sendVideo(at, msg_dict[msg_id]["video"])
                                del msg_dict[msg_id]
                            else:
                                if "audio" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nAudio :\nBelow"
                                    sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                    line.sendAudio(at, msg_dict[msg_id]["audio"])
                                    del msg_dict[msg_id]
                                else:
                                    if "sticker" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nSticker :\nBelow"
                                        sendMention(at, ikkeh.mid, " ** Resend Message **\n\nMaker :\n", str(rat_))
                                        line.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "mid" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n~ {} ago".format(waktumsg)
                                            rat_ += "\nContact :\nBelow"
                                            sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                            line.sendContact(at, msg_dict[msg_id]["mid"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "lokasi" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nLocate :\nBelow"
                                                sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                                line.sendLocation(at, msg_dict[msg_id]["lokasi"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "file" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nFile :\nBelow"
                                                    sendMention(at, ikkeh.mid, "** Resend Message **\n\nMaker :\n", str(rat_))
                                                    line.sendFile(at, msg_dict[msg_id]["file"])
                                                    del msg_dict[msg_id]
                else:
                    line.sendMessage(at, "Unsend Message Detected\n\nMessage not in log")
#==============================================================================================================
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=['จ๊ะเอ๋','รู้นะว่าแอบอยู่','เล่นซ่อนแอบกันเหรอ','คิดว่าเป็นนินจารึไง','ว่าไง','อ่านอย่างเดียวเลยนะ','ออกมาคุยหน่อย','ออกมาเดี๋ยวนี้']
                            sendMessageWithMention(op.param1, op.param2)
                            line.sendMessage(op.param1, str(random.choice(pref)) + '\n♪ ♬ ヾ(´︶`♡)ﾉ ♬ ♪')
                            line.sendContact(op.param1, op.param2)
                            msgSticker = settings["messageSticker"]["listSticker"]["readerSticker"]
                            if msgSticker != None:
                                sid = msgSticker["STKID"]
                                spkg = msgSticker["STKPKGID"]
                                sver = msgSticker["STKVER"]
                                sendSticker(op.param1, sver, spkg, sid)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print (" [ทีมงานสาสเต้ย ตัวตลกแห่งความตาย]  ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        

while True:
    try:
        ops = oepoll.singleTrace(count=5)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
