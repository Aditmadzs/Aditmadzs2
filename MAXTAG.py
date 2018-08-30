from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

nadya = LINE()
nadya.log("Auth Token : " + str(nadya.authToken))
channelToken = nadya.getChannelResult()
nadya.log("Channel Token : " + str(channelToken))

nadyaMID = nadya.profile.mid
nadyaProfile = nadya.getProfile()
lineSettings = nadya.getSettings()
oepoll = OEPoll(nadya)
Rfu = [nadya]
RfuBot=[nadyaMID]
admin=['u4862fe4b182b2fd194a3108e2f3662e8',nadyaMID]
Family=["u4862fe4b182b2fd194a3108e2f3662e8",nadyaMID]
RfuFamily = RfuBot + Family
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)
#==============================================================================#
wait = {
   'acommentOn':False,
   'bcommentOn':False,
   'autoLeave':False,
   'autoJoin':True,
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = nadyaProfile.displayName
myProfile["statusMessage"] = nadyaProfile.statusMessage
myProfile["pictureStatus"] = nadyaProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    nadya.sendMessage(to, '', contentMetadata, 7)

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            nadya.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def waktu(secs):
        mins, secs = divmod(secs,60)
        hours, mins = divmod(mins,60)
        days,hours = divmod(hours,24)
        return '%02d วัน %02d ชั่วโมง %02d นาที %02d วินาที' % (days, hours, mins, secs)

def logError(text):
    nadya.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        nadya.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def helpmessage():
    helpMessage =  """╔════════════════╗
╠❂➣【さัএπัஞ✵ບิथℓℓҨतΩ】
╠════════════════╝
╠❂➣ คท  (@)
╠❂➣ มิด  (@)
╠❂➣ ชื่อ  (@)
╠❂➣ ตัส  (@)
╠❂➣ รูป  (@)
╠❂➣ ปก  (@)
╠❂➣ กลุ่ม (@)
╠❂➣ ข้อมูล (@)
╠❂➣ ไวรัส
╠❂➣ สปีด
╠❂➣ แทค
╠❂➣ ของขวัญ
╠❂➣ OA - แทคล่องหน
╠❂➣ OB - ไอดีล่องหน
╠❂➣ OC - คทล่องหน
╠❂➣ สแปม on [จำนวน] [ข้อความ]
╠❂➣ พูด [ข้อความ]
╠❂➣ โทร [จำนวน]
╠❂➣ ปฏิทิน
╠❂➣ ไอดีไลน์ [ตามด้วยไอดี]
╠❂➣ เขียน [ข้อความ]
╠❂➣ แอด
╠❂➣ ชื่อกลุ่ม
╠❂➣ รูปกลุ่ม
╠❂➣ ไอดีกลุ่ม
╠❂➣ รายชื่อสมาชิก
╠❂➣ รายชื่อกลุ่ม
╠❂➣ เปิดลิ้ง/ปิดลิ้ง
╠❂➣ ลิ้งกลุ่ม
╠❂➣ เตะ (@)
╠❂➣ บอทออก
╠❂➣ แม็ค
╠❂➣ youtube [ข้อความ]
╠❂➣ google [ข้อความ]
╠❂➣ แอพ [ข้อความ]
╚════════════════╝
By:【さัএπัஞ✵ບิथℓℓҨतΩ】"""
    return helpMessage

def helptexttospeech():
    helpTextToSpeech =   """
"""
    return helpTextToSpeech
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            nadya.findAndAddContactsByMid(op.param1)
            nadya.sendMessage(op.param1, "สวัสดีครับ\n【さัএπัஞ✵ບิथℓℓҨतΩ】 :\nList opsi\n🤖 Pasangan Hidup :\n🔰 Only Status ⏩ 180K/Bulan\n\n🤖 Systim Contract :\n🔰 Only Curhat ⏩ 100K/Bulan\n🔰 Zona Friend + TTM\n🔰 Zona Nyaman + Full Care + On 5day + 2 day free ⏩ 300K/Bulan\n\n✍️ Bisa Requests Mau Berapa Lama Durasi Buat Debay.\nChat Ke : http://line.me/ti/p/~max_pv\n\n📃\n* Always on 24 Jam\n* Keuntungan Banyak\n* Durasi min 0.25month\n* max no limit")
            nadya.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")

        if op.type == 13:
            group = nadya.getGroup(op.param1)
            nadya.acceptGroupInvitation(op.param1)
            nadya.sendMessage(op.param1, "มีการเชิญสมาชิกเข้าร่วมกลุ่ม")

        if op.type == 17:
             dan = nadya.getContact(op.param2)
             tgb = nadya.getGroup(op.param1)
             nadya.sendMessage(op.param1,"🙏 สวัสดี 🙏 {}\n\nยินดีต้อนรับสู่กลุ่ม[ {} ]\n\n【さัএπัஞ✵ບิथℓℓҨतΩ】 :\nList opsi\n🤖 Pasangan Hidup :\n🔰 Only Status ⏩ 180K/Bulan\n\n🤖 Systim Contract :\n🔰 Only Curhat ⏩ 100K/Bulan\n🔰 Zona Friend + TTM\n🔰 Zona Nyaman + Full Care + On 5day + 2 day free ⏩ 300K/Bulan\n\n✍️ Bisa Requests Mau Berapa Lama Durasi Buat Debay.\nChat Ke : http://line.me/ti/p/~max_pv\n\n📃\n* Always on 24 Jam\n* Keuntungan Banyak\n* Durasi min 0.25month\n* max no limit".format(str(dan.displayName),str(tgb.name)))
             nadya.sendContact(op.param1, op.param2)
             nadya.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))

        if op.type == 15:
             dan = nadya.getContact(op.param2)
             tgb = nadya.getGroup(op.param1)
             nadya.sendMessage(op.param1,"😭 ลาก่อน 😭 {}\n\nGood bye![ {} ]\n\nNAH LOH BAPER KHAAAN".format(str(dan.displayName),str(tgb.name)))
             nadya.sendContact(op.param1, op.param2)
             nadya.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))

        if op.type == 19:
                group = nadya.getGroup(op.param1)
                contact = nadya.getContact(op.param2)
                msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
                if "{gname}" in settings['welcomePesan'].lower():
                    gName = group.name
                    msg = settings['welcomePesan'].replace("{gname}", gName)
                    if "@!" in msg:
                        msg = msg.split("@!")
                        return sendMention(op.param1, op.param2, msg[0], msg[1])
                    sendMention(op.param1, op.param2, "สวัสดีครับ", msg)
                else:
                    sendMention(op.param1, op.param2, "สวัสดีครับ","\n{}".format(str(settings['welcomePesan'])))
                    contact = nadya.getContact(op.param2)
                    nadya.sendImageWithURL(op.param1,image)
                    arg = "   Group Name : {}".format(str(group.name))
                    arg += "\n   User Join : {}".format(str(contact.displayName))
                    print (arg)

        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#                    nadya.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        nadya.sendMessage(msg.to,text)
#==============================================================================#
                if msg.text in ["คำสั่ง","Help","help"]:
                    helpMessage = helpmessage()
                    nadya.sendMessage(to, str(helpMessage))
                    nadya.sendContact(to, "u4862fe4b182b2fd194a3108e2f3662e8")
                if text.lower() == 'ออน':
                    eltime = time.time() - mulai
                    van = "「 ระยะเวลาการทำงานของบอท 」\n"+waktu(eltime)
                    nadya.sendMessage(receiver,van)
                if text.lower() == 'ของขวัญ':
                        nadya.sendGift(msg.to,'3534677','sticker')
                if msg.text.lower().startswith("เตะ "):
                  if msg._from in admin:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                  for target in targets:
                        try:
                            nadya.kickoutFromGroup(msg.to,[target])
                        except:
                            nadya.sendText(msg.to,"Error")
                if "cancelall" == msg.text.lower():
                  if msg._from in admin:
                         if msg.toType == 2:
                             group = nadya.getGroup(msg.to)
                             gMembMids = [contact.mid for contact in group.invitee]
                         for _mid in gMembMids:
                             nadya.cancelGroupInvitation(msg.to,[_mid])
                             nadya.sendMessage(to,"ยกเลิกค้างเชิญเสร็จสิ้น(。-`ω´-)")
                if msg.text.lower().startswith("ไอดีไลน์ "):
                    id = msg.text.lower().replace("ไอดีไลน์ ","")
                    conn = nadya.findContactsByUserid(id)
                    if True:
                        nadya.sendMessage(to,"http://line.me/ti/p/~" + id)
                        nadya.sendContact(to,conn.mid)
                if 'แอพ ' in msg.text.lower():
                        tob = msg.text.lower().replace('แอพ ',"")
                        nadya.sendMessage(msg.to,"กรุณารอสักครู่...")
                        nadya.sendMessage(msg.to,"ผลจากการค้นหา : "+tob+"\nจาก : Google Play\nลิ้งโหลด : https://play.google.com/store/search?q=" + tob)
                        nadya.sendMessage(msg.to,"👆กรุณากดลิ้งเพื่อทำการโหลดแอพ👆")
                if "youtube " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "ผลการค้นหาจาก Youtube:\n"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n\n{}".format(str(data["title"]))
                            ret_ += "\nhttps://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n\nจำนวนที่ค้นพบ {} ".format(len(datas))
                        nadya.sendMessage(to, str(ret_))
                if "เขียน " in msg.text.lower():
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    path = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    nadya.sendImageWithURL(msg.to,path)
                if "google " in msg.text.lower():
                    spl = re.split("google ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        nadya.sendMessage(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    else:
                                        nadya.sendMessage(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
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
                                        nadya.sendMessage(msg.to,str(text))
                                    else:
                                        nadya.sendMessage(msg.from_,str(text))
                                except Exception as e:
                                    print(e)
                if "สแปม " in msg.text.lower():
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("สแปม "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                             nadya.sendMessage(msg.to, teks)
                        else:
                           nadya.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            nadya.sendMessage(msg.to, tulisan)
                        else:
                            nadya.sendMessage(msg.to, "Out Of Range!")
                if "โทร " in msg.text.lower():
                  if msg._from in admin:
                      if msg.toType == 2:
                          sep = text.split(" ")
                          strnum = text.replace(sep[0] + " ","")
                          num = int(strnum)
                          nadya.sendMessage(to, "เชิญเข้าร่วมการโทร(。-`ω´-)")
                      for var in range(0,num):
                          group = nadya.getGroup(to)
                          members = [mem.mid for mem in group.members]
                          nadya.acquireGroupCallRoute(to)
                          nadya.inviteIntoGroupCall(to, contactIds=members)
                if text.lower() == 'บอทออก':
                  if msg._from in admin:
                      if msg.toType == 2:
                          ginfo = nadya.getGroup(to)
                          try:
                              nadya.sendMessage(to, "ไปแล้วนะ บ้ายบาย 😭")
                              nadya.leaveGroup(to)
                          except:
                             pass
                if msg.text in ["Speed","speed","Sp","sp",".Sp",".sp",".Speed",".speed","\Sp","\sp","\speed","\Speed","สปีด"]:
                    start = time.time()
                    nadya.sendMessage(msg.to, "กำลังทดสอบ(｀・ω・´)")
                    elapsed_time = time.time() - start
                    nadya.sendMessage(msg.to, "[sᴘᴇᴇᴅ ᴛᴇsᴛ]\n[ %s sᴇᴄᴏɴᴅs ]\n[ ᴘɪɴɢ : " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                if msg.text in ["Tag","tagall","แทค","แทก","Tagall","tag","!แทค"]:
                    group = nadya.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        nadya.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                if msg.text.lower().startswith("คท "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendContact(msg.to, mi_d)
                if msg.text.lower().startswith("มิด "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "ไอดีของ:"
                        for ls in lists:
                            ret_ += "\n" + ls
                        nadya.sendMessage(msg.to, str(ret_))
                if msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, "ชื่อของ:\n" + contact.displayName)
                if msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendMessage(msg.to, "ตัสของ:\n" + contact.statusMessage)
                if msg.text.lower().startswith("รูป "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + nadya.getContact(ls).pictureStatus
                            nadya.sendImageWithURL(msg.to, str(path))
                if msg.text.lower().startswith("ปก "):
                    if nadya != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = nadya.getProfileCoverURL(ls)
                                nadya.sendImageWithURL(msg.to, str(path))
                if msg.text.lower().startswith("ดึงหมด "):
                    if nadya != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                me = nadya.getContact(ls)
                                path = nadya.getProfileCoverURL(ls)
                                path = str(path)
                                if settings["server"] == "VPS":
                                    nadya.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                    nadya.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                    nadya.sendMessage(msg.to,"「 MID 」\n" +  to)
                                    nadya.sendMessage(to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    nadya.sendImageWithURL(to, str(path))
                                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                else:
                                    nadya.sendMessage(msg.to,"「 Display Name 」\n" + me.displayName)
                                    nadya.sendMessage(msg.to,"「 Status Message 」\n" + me.statusMessage)
                                    nadya.sendMessage(msg.to,"「 MID 」\n" + ls)
                                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                if "ข้อมูล " in msg.text.lower():
                    spl = re.split("ข้อมูล ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = nadya.getContact(uid)
                            try:
                                nadya.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net{}".format(userData.picturePath))
                            except:
                                pass
                            nadya.sendText(msg.to,"「 Display Name 」\n"+userData.displayName)
                            nadya.sendText(msg.to,"「 Status Message 」\n"+userData.statusMessage)
                            nadya.sendText(msg.to,"「 MID 」\n"+userData.mid)
                            nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+userData.pictureStatus)
                            nadya.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net"+userData.picturePath)
                if "กลุ่ม " in msg.text.lower():
                    nadya.sendMessage(to, "กำลังตรวจสอบข้อมูล...")
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        G = nadya.getGroupIdsJoined()
                        cgroup = nadya.getGroups(G)
                        ngroup = ""
                        for mention in mentionees:
                         for x in range(len(cgroup)):
                           gMembMids = [contact.mid for contact in cgroup[x].members]
                           if mention['M'] in gMembMids:
                                ngroup += "\n➢ " + cgroup[x].name + " | สมาชิก: " +str(len(cgroup[x].members))
                        if ngroup == "":
                             nadya.sendMessage(to, "ไม่พบ")
                        else:
                             nadya.sendMessage(to, "➢ตรวจพบอยู่ในกลุ่ม %s"%(ngroup))
                if msg.text.lower().startswith("แทค "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
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
                                contact = nadya.getContact(receiver)
                                RhyN_(to, contact.mid)
                if text.lower() == 'oa':
                    gs = nadya.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendMessage(to, "ไม่มีคนใส่ชื่อร่องหน(。-`ω´-)")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        nadya.sendMessage(to, mc)
                if text.lower() == 'ob':
                    gs = nadya.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        nadya.sendMessage(to, "ไม่มีคนใส่ชื่อร่องหน(。-`ω´-)")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "- " + mi_d + "\n"
                        nadya.sendMessage(to,mc)
                if text.lower() == 'oc':
                    gs = nadya.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        nadya.sendMessage(to, "ไม่มีคนใส่ชื่อร่องหน(。-`ω´-)")
                    else:
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendContact(to, mi_d)
#==============================================================================#
                if "ตั้งชื่อกลุ่ม " in msg.text.lower():
                    if msg.toType == 2:
                        X = nadya.getGroup(msg.to)
                        X.name = msg.text.replace("ตั้งชื่อกลุ่ม ","")
                        nadya.updateGroup(X)
                    else:
                        nadya.sendMessage(msg.to,"ไม่สามารถใช้ภายนอกกลุ่มได้")
                if text.lower() == 'แอด':
                    group = nadya.getGroup(to)
                    GS = group.creator.mid
                    nadya.sendContact(to, GS)
                if text.lower() == 'ไอดีกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "ไอดีกลุ่ม:\n" + gid.id)
                if text.lower() == 'รูปกลุ่ม':
                    group = nadya.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    nadya.sendImageWithURL(to, path)
                if text.lower() == 'ชื่อกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendMessage(to, "ชื่อกลุ่ม:\n" + gid.name)
                if text.lower() == 'ลิ้งกลุ่ม':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = nadya.reissueGroupTicket(to)
                            nadya.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                if text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nadya.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = False
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                if text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nadya.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = True
                            nadya.updateGroup(group)
                            nadya.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                if text.lower() == 'รายชื่อสมาชิก':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        ret_ = "╔══[ รายชื่อสมชิกกลุ่ม ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวนสมาชิก {} คน(。-`ω´-) ]".format(str(len(group.members)))
                        nadya.sendMessage(to, str(ret_))
                if text.lower() == 'รายชื่อกลุ่ม':
                        groups = nadya.groups
                        ret_ = "╔══[ รายชื่อกลุ่ม ]"
                        no = 0 + 1
                        for gid in groups:
                            group = nadya.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวนกลุ่ม {} กลุ่ม(。-`ω´-)]".format(str(len(groups)))
                        nadya.sendMessage(to, str(ret_))
                if msg.text.lower().startswith("พูด "):
                       sep = text.split(" ")
                       say = text.replace(sep[0] + " ","")
                       lang = 'th'
                       tts = gTTS(text=say, lang=lang)
                       tts.save("hasil.mp3")
                       nadya.sendAudio(msg.to,"hasil.mp3")
                if text.lower() == 'เปิดอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                nadya.sendMessage(msg.to,"เปิดหาคนซุ่ม 😗")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            nadya.sendMessage(msg.to, "Set reading point:\n" + readTime)
                if text.lower() == 'อ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            nadya.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = nadya.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            nadya.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        nadya.sendMessage(receiver,"ก่อนจะพิมคำสั่งนี้กรุณา (เปิดอ่าน) ก่อนลงคำสั่งนี้ 😗")
                elif text.lower() == 'ปฏิทิน':
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
                    readTime = "🌴ปฏิทินโดย ™ധู้ざຣ้ণს✚ປิʨℓℓҨබମ™ 🌴\n\n🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\n🍁 " + hasil + "\n🍁 วันที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\n🍁 เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]" + "\n\n🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\nBY:【さัএπัஞ✵ບิथℓℓҨतΩ】\nhttp://line.me/ti/p/~max_pv"
                    nadya.sendMessage(msg.to, readTime)
#==============================================================================#
                if msg.text in ["ไวรัส"]:
                        nadya.sendContact(to, "0'.")
                if msg.text in ["แม็ค","แม็ค","ที่รัก"]:
                        nadya.sendMessage(to, "มีไรหรึป่าว??")
                        nadya.sendContact(to, "u4862fe4b182b2fd194a3108e2f3662e8")
                if msg.text in ["Me","me","คท",".me",".Me",".คท","/Me","/me","!me","Mybot","mybot","Myme"]:
                        nadya.sendMentionFooter(to, 'CONTACT', sender, "http://line.me/ti/p/~max_pv", "http://dl.profile.line-cdn.net/"+nadya.getContact(sender).pictureStatus, nadya.getContact(sender).displayName);nadya.sendMessage(to, nadya.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+nadya.getContact(sender).pictureStatus, 'i-installUrl': 'http://line.me/ti/p/~max_pv', 'type': 'mt', 'subText': " ", 'a-installUrl': 'http://line.me/ti/p/~max_pv', 'a-installUrl': ' http://line.me/ti/p/~max_pv', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'http://line.me/ti/p/~max_pv', 'i-linkUri': 'http://line.me/ti/p/~max_pv', 'id': 'mt000000000a6b79f9', 'text': ' ', 'linkUri': 'http://line.me/ti/p/~max_pv'}, contentType=19)
                if msg.text in ["555","5555","55555","555555","5555555","55555555","555555555","5555555555","5555555555","5555+","55555+","555555+"]:
                        nadya.sendMessage(to, "ขำไรกัน กูขำด้วยคน 55555555555+")
                        nadya.sendMessage(msg.to, None, contentMetadata={"STKID":"51626504","STKPKGID":"11538","STKVER":"1"}, contentType=7)
                if msg.text in ["สัส","ควาย","เหี้ย","ไอสัส","ไอควาย","ไอเหี้ย","หน้าหี","หี","ควย","ไอควย","ไอหน้าหี","แม่เย็ด","สาส","ไอสาส","ไอสาสส","ไอสาสสส","ควย"]:
                        nadya.sendMessage(to, "ไม่เอา ไม่พูดคำหยาบสิ 😱")
                        nadya.sendMessage(msg.to, None, contentMetadata={"STKID":"118","STKPKGID":"1","STKVER":"100"}, contentType=7)
                if msg.text in ["bot","Bot","บอท"]:
                        nadya.sendMessage(to, "เรียกบอท มีอาไรหรือป่าว??")
                        nadya.sendMessage(msg.to, None, contentMetadata={"STKID":"52002744","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                if msg.text in ["-.-","TT","-_-","^^","--","==","*-*","•^•",":)",":("]:
                        nadya.sendMessage(to, "ทำไม ทำหน้ากวนตีนจังอะ *(￣３￣)*")
                        nadya.sendMessage(msg.to, None, contentMetadata={"STKID":"52002770","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                if msg.text in ["ฝันดี","ฝรรดี","ฝันค่ะ","ฝันดีคะ","ฝันดีคับ","ฝันดีครับ","ฝรรดีคับ","ฝรรดีครับ","ฝรรดีค่ะ","ฝรรดีคะ"]:
                        nadya.sendMessage(to, "ฝันดีคับผม กูยังไม่นอนหลอก กูดีด 555+")
                        nadya.sendMessage(msg.to, None, contentMetadata={"STKID":"52114120","STKPKGID":"11539","STKVER":"1"}, contentType=7)
                if msg.text in ["มอนิ่ง","นิ่ง","นิ่งๆ","นิ่งๆๆ","มอนิ่งค่ะะ","มอนิ่งคับ","มอนิ่งคะ","มอนิ่งครับ","นิ่งคะ","นิ่งคับ","นิ่งค่ะ","นิ่งครับ"]:
                        nadya.sendMessage(to, "มอนิ่งคับผม 😍")
                if "." in msg.text:
                    spl = msg.text.split(".")
                    if spl[len(spl)-1] == "":
                       nadya.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)
#==============================================================================#
                if msg.contentType == 13:
                        contact = nadya.getContact(msg.contentMetadata["mid"])
                        if nadya != None:
                            cover = nadya.getProfileCoverURL(msg.contentMetadata["mid"])
                        else:
                            cover = "Tidak dapat masuk di line channel"
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            nadya.sendImageWithURL(to, str(path))
                        except:
                            pass
                        ret_ = "「 รายการทั้งหมดจากการสำรวจด้วย คท 」"
                        ret_ += "\n────────────────────"
                        ret_ += "\n❂ ชื่อ : {}".format(str(contact.displayName))
                        ret_ += "\n❂ ไอดี : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n❂ ตัส :"
                        ret_ += "\n────────────────────"
                        ret_ += "\n{}".format(str(contact.statusMessage))
                        ret_ += "\n────────────────────"
                        ret_ += "\n❂ ลิ้งรูปโปรไฟล์ :\nhttp://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n❂ ลิ้งรูปปก :\n{}".format(str(cover))
                        ret_ += "\n────────────────────"
                        nadya.sendMessage(to, str(ret_))
                if msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        ret_ = "Sticker Info"
                        ret_ += "\nSTICKER ID : {}".format(stk_id)
                        ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                        ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                        nadya.sendMessage(to, text=None, contentMetadata={'STKID':'107', 'STKVER':'100', 'STKPKGID':'1'}, contentType=7)
#                    elif msg.contentType == 1:
                        nadya.sendMessage(to, text=None, contentMetadata={"STKID": "190", "STKVER": "100", "STKPKGID": "3"}, contentType=7)
#                    else:
                        if text is not None:
                            txt = text
                            nadya.sendMessage(msg.to,txt)
                if msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        stk_ver = msg.contentMetadata['STKVER']
                        pkg_id = msg.contentMetadata['STKPKGID']
                        ret_ = "「 Check Sticker 」\n"
                        ret_ += "\nSTKID : {}".format(stk_id)
                        ret_ += "\nSTKPKGID : {}".format(pkg_id)
                        ret_ += "\nSTKVER : {}".format(stk_ver)
                        ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                        print(msg)
                        nadya.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                        nadya.sendMessage(to, str(ret_))
                if msg.contentType == 16:
                    msg.contentType = 0
                    msg.text = "ลิ้งโพส\n" + msg.contentMetadata["postEndUrl"]
                    nadya.sendMessage(msg.to,msg.text)
                    if "/ti/g/" in msg.text.lower():
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = nadya.findGroupByTicket(ticket_id)
                                nadya.acceptGroupInvitationByTicket(group.id,ticket_id)
                                nadya.sendMessage(to, "มุดลิ้งเข้าไปในกลุ่ม👉 %s 👈 เรียบร้อยแล้ว" % str(group.name))
#!=================================================================================
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
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
def khieMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    nadya.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#========================================================================
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
