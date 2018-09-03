# -*- coding: utf-8 -*-
import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#BOT INI BUAT KALIAN YANG MEMANG MEMBUTUHKAN
#cl = LineClient()
cl = LineClient(authToken='')
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(cl)
call = cl

mid = cl.getProfile().mid

admin = ["u4862fe4b182b2fd194a3108e2f3662e8"]

KAC = [cl]
Bots = ["u4862fe4b182b2fd194a3108e2f3662e8"]
Phie = admin

welcome = []
simisimi = []
translateen = []
translatetr = []
translateid = []
translateth = []
translatetw = []
translatear = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

phieProfile = cl.getProfile()
myProfile["displayName"] = phieProfile.displayName
myProfile["statusMessage"] = phieProfile.statusMessage
myProfile["pictureStatus"] = phieProfile.pictureStatus

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":True,
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
    ]
}

wait = {
    "limit": 1,
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentiongift":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "unsend":True,
    "mention":"Hayoo ngintip ,ketuaan kan..ngaku hayoo",
    "Respontag":"มีไรคะ...!!",
    "welcome":"Nah Calon Tikungan Baru",
    "leave":"NAH LOH BAPER KHAAAN KHAAAN ,KEBANYAKAN DRAMA SIHH..😂",
    "comment":"Like by【さัএπัஞ✵ບิथℓℓҨतΩ】",
    "message":"【さัএπัஞ✵ບิथℓℓҨतΩ】 :\nList opsi\n🤖 Pasangan Hidup :\n🔰 Only Status ⏩ 180K/Bulan\n\n🤖 Systim Contract :\n🔰 Only Curhat ⏩ 100K/Bulan\n🔰 Zona Friend + TTM\n🔰 Zona Nyaman + Full Care + On 5day + 2 day free ⏩ 300K/Bulan\n\n✍️ Bisa Requests Mau Berapa Lama Durasi Buat Debay.\nChat Ke : http://line.me/ti/p/~max_pv\n\n📃\n* Always on 24 Jam\n* Keuntungan Banyak\n* Durasi min 0.25month\n* max no limit",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))


def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)
            time.sleep(0.1)
            page = page[end_content:]
    return items

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Kamu yanke「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╰━━[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╰━━[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider「{}」\nTercyduk ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╰━━[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╰━━[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Nah ketemu lagi「{}」\nHemm  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\ndi Grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╰━━[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╰━━[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Hemm korban Bapeerr lg pasti「{}」\nByee gosah balik2 lagi ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nke Grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╰━━[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╰━━[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🔰 Group : "+str(len(gid))+"\n🔰 Teman : "+str(len(teman))+"\n🔰 Expired : In "+hari+"\n🔰 Version :  Premium\n🔰 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔰 Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    key2 = Setmain["namecreator"]
    key2 = key2.title()
    helpMessage = "🔰 【さัএπัஞ✵ບิथℓℓҨतΩ】: "+ key2 +" 🔰" + "\n" + \
                  "🔥 Help Message 🔥" + "\n" + \
                  "     Gunakan「 " + key + " 」Di Depannya\n" + \
                  "\n🔵 Menu" + "\n" + \
                  "🔰 " + key + "Help\n" + \
                  "🔰 " + key + "Help bot\n" + \
                  "🔰 " + key + "Translate\n" + \
                  "🔰 " + key + "Autotrans「en-on/en-off」\n" + \
                  "🔰 " + key + "Autotrans「id-on/id-off」\n" + \
                  "🔰 " + key + "Autotrans「th-on/th-off」\n" + \
                  "🔰 " + key + "Autotrans「tw-on/tw-off」\n" + \
                  "🔰 " + key + "Autotrans「ar-on/ar-off」\n" + \
                  "🔰 " + key + "Info meme\n" + \
                  "🔰 " + key + "Self「on/off」\n" + \
                  "🔰 " + key + "Me\n" + \
                  "🔰 " + key + "Mycopy「@」\n" + \
                  "🔰 " + key + "Mybackup\n" + \
                  "🔰 " + key + "Stealname「@」\n" + \
                  "🔰 " + key + "Stealbio「@」\n" + \
                  "🔰 " + key + "Stealpicture「@」\n" + \
                  "🔰 " + key + "Stealcover「@」\n" + \
                  "🔰 " + key + "Stealvideoprofile「@」\n" + \
                  "🔰 " + key + "Mymid\n" + \
                  "🔰 " + key + "Mid「@」\n" + \
                  "🔰 " + key + "Info 「@」\n" + \
                  "🔰 " + key + "Status\n" + \
                  "🔰 " + key + "About\n" + \
                  "🔰 " + key + "Restart\n" + \
                  "🔰 " + key + "Runtime\n" + \
                  "🔰 " + key + "Creator\n" + \
                  "🔰 " + key + "Respon\n" + \
                  "🔰 " + key + "Speed/Sp\n" + \
                  "🔰 " + key + "Sprespon\n" + \
                  "🔰 " + key + "แทค\n" + \
                  "🔰 " + key + "Byeme\n" + \
                  "🔰 " + key + "Ginfo\n" + \
                  "🔰 " + key + "Open\n" + \
                  "🔰 " + key + "Close\n" + \
                  "🔰 " + key + "Url grup\n" + \
                  "🔰 " + key + "Reject\n" + \
                  "🔰 " + key + "Gruplist\n" + \
                  "🔰 " + key + "Infogrup「angka」\n" + \
                  "🔰 " + key + "Infomem「angka」\n" + \
                  "🔰 " + key + "Remove chat\n" + \
                  "🔰 " + key + "Lurking「on/off」\n" + \
                  "🔰 " + key + "Lurkers\n" + \
                  "🔰 " + key + "Sider「on/off」\n" + \
                  "🔰 " + key + "Updatefoto\n" + \
                  "🔰 " + key + "Updategrup\n" + \
                  "🔰 " + key + "Broadcast:「Text」\n" + \
                  "🔰 " + key + "Setkey「New Key」\n" + \
                  "🔰 " + key + "Mykey\n" + \
                  "🔰 " + key + "Resetkey\n" + \
                  "     Gunakan「 " + key + " 」Di Depannya\n" + \
                  "\n🔵 Hiburan" + "\n" + \
                  "🎭 " + key + "Musik:「Judul Lagu」\n" + \
                  "🎭 " + key + "Musik2:「Judul Lagu」\n" + \
                  "🎭 " + key + "Playlist「Nama Penyanyi」\n" + \
                  "🎭 " + key + "Ytmp3:「Judul Lagu」\n" + \
                  "🎭 " + key + "Ytmp4:「Judul Video\n" + \
                  "🎭 " + key + "Fs:「Nama」\n" + \
                  "🎭 " + key + "cl-telp:「No HP」\n" + \
                  "🎭 " + key + "cl-sms:「No HP」\n" + \
                  "🎭 " + key + "Smsgratis:「Nohp:Pesannya」\n" + \
                  "🎭 " + key + "Meme@Nama@Teks1@Teks2\n" + \
                  "🎭 " + key + "Quotes\n" + \
                  "🎭 " + key + "1cak\n" + \
                  "🎭 " + key + "Profilesmule:「ID Smule」\n" + \
                  "🎭 " + key + "Randomnumber:「Nmor-Nmor」\n" + \
                  "🎭 " + key + "Acaratv:「Nama Channel」\n" + \
                  "🎭 " + key + "Gimage:「Keyword」\n" + \
                  "🎭 " + key + "Img food:「Nama Makanan」\n" + \
                  "🎭 " + key + "Al-quran:「Surah」\n" + \
                  "🎭 " + key + "Sholat:「Nama Kota」\n" + \
                  "🎭 " + key + "Cuaca:「Nama Kota」\n" + \
                  "🎭 " + key + "Lokasi:「Nama Kota」\n" + \
                  "🎭 " + key + "Profileig:「Nama IG」\n" + \
                  "🎭 " + key + "Cekig:「Nama IG」\n" + \
                  "🎭 " + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "🎭 " + key + "Spamtag:「jumlahnya」\n" + \
                  "🎭 " + key + "Spamtag「@」\n" + \
                  "🎭 " + key + "Spamcall:「jumlahnya」\n" + \
                  "🎭 " + key + "Spamcall\n" + \
                  "🎭 " + key + "ID line:「Id Line nya」\n" + \
                  "     Gunakan「 " + key + " 」Di Depannya\n" + \
                  "\n🔵 Settings" + "\n" + \
                  "🎭 " + key + "Unsend「on/off」\n" + \
                  "🎭 " + key + "Jointicket「on/off」\n" + \
                  "🎭 " + key + "Sticker「on/off」\n" + \
                  "🎭 " + key + "Respon「on/off」\n" + \
                  "🎭 " + key + "Respongift「on/off」\n" + \
                  "🎭 " + key + "Contact「on/off」\n" + \
                  "🎭 " + key + "Autojoin「on/off」\n" + \
                  "🎭 " + key + "Autoadd「on/off」\n" + \
                  "🎭 " + key + "Welcome「on/off」\n" + \
                  "🎭 " + key + "Simi「on/off」\n" + \
                  "🎭 " + key + "Autoleave「on/off」\n" + \
                  "     Gunakan「 " + key + " 」Di Depannya\n" + \
                  "\n🔵 Admin" + "\n" + \
                  "🎭 " + key + "Changenamecreator:「Nama」\n" + \
                  "🎭 " + key + "Resetnamecreator\n" + \
                  "🎭 " + key + "Admin:on\n" + \
                  "🎭 " + key + "Admin:repeat\n" + \
                  "🎭 " + key + "Adminadd「@」\n" + \
                  "🎭 " + key + "Admindell「@」\n" + \
                  "🎭 " + key + "Refresh\n" + \
                  "🎭 " + key + "Listadmin\n" + \
                  "     Ketik「 Refresh 」Jika Sudah Menggunakan Command Diatas...\n" + \
                  "\n🔐 USER BY:"+ key2 + "🔐"
    return helpMessage



def helarot():
    key = Setmain["keyCommand"]
    key = key.title()
    key2 = Setmain["namecreator"]
    key2 = key2.title()
    helpMessage1 ="🔰 NAME: "+ key2 +" 🔰" + "\n" + \
                  "🔵 Help Bot" + "\n" + \
                  "     Gunakan「 " + key + " 」Di Depannya\n" + \
                  "\n🔵 Menu" + "\n" + \
                  "🔥 " + key + "Cek sider\n" + \
                  "🔥 " + key + "Cek spam\n" + \
                  "🔥 " + key + "Cek pesan\n" + \
                  "🔥 " + key + "Cek respon\n" + \
                  "🔥 " + key + "Cek welcome\n" + \
                  "🔥 " + key + "Cek leave\n" + \
                  "🔥 " + key + "Set sider:「Text」\n" + \
                  "🔥 " + key + "Set spam:「Text」\n" + \
                  "🔥 " + key + "Set pesan:「Text」\n" + \
                  "🔥 " + key + "Set respon:「Text」\n" + \
                  "🔥 " + key + "Set welcome:「Text」\n" + \
                  "🔥 " + key + "Set leave:「Text」\n" + \
                  "🔥 " + key + "Myname:「Nama」\n" + \
                  "🔥 " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "🔥 " + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "     Ketik「 Refresh 」Jika Sudah Menggunakan Command Diatas...\n" + \
                  "\n🔐 USER:"+ key2 + "🔐"
    return helpMessage1

def infomeme():
    helpMessage2 = """         🔰 Meme List 🔰

✍ Buzz
✍ Spongebob
✍ Patrick
✍ Doge
✍ Joker
✍ Xzibit
✍ You_tried
✍ cb
✍ blb
✍ wonka
✍ keanu
✍ cryingfloor
✍ disastergirl
✍ facepalm
✍ fwp
✍ grumpycat
✍ captain
✍ mmm
✍ rollsafe
✍ sad-obama
✍ sad-clinton
✍ aag
✍ sarcasticbear
✍ sk
✍ sparta
✍ aag

🎓 by:【さัএπัஞ✵ບิथℓℓҨतΩ】🎓
line.me/ti/p/~max_pv"""
    return helpMessage2
def listharga():
    helpMessage3 = """
#Price List【さัএπัஞ✵ບิथℓℓҨतΩ】:

🤖 Jasa bikin 2anak :
🔰 Male/Female Only ⏩ 150K/Minggu

🤖 Jasa Madu3 :
🔰 Private Only ⏩ 100K/Minggu
🔰 Private + Publik ⏩ 200K/Minggu
🔰 Private + Publik + Legal + Certifikasi ⏩ 250K/Minggu

✍️ Bisa Requests Mau Berapa Lama Buat Debay.
Chat Ke : http://line.me/ti/p/~max_pv

📃
* Always on 24 Jam
* Sensasi Banyak
* Long Duration
* Free Request
# Buat Gadis, Dari Kami Harga Beda Lagi.
"""

def translate():
    helpTranslate =     "✍ T R A N S L A T E " + "\n" + \
                       "📝 af : afrikaans" + "\n" + \
                       "📝 sq : albanian" + "\n" + \
                       "📝 am : amharic" + "\n" + \
                       "📝 ar : arabic" + "\n" + \
                       "📝 hy : armenian" + "\n" + \
                       "📝 az : azerbaijani" + "\n" + \
                       "📝 eu : basque" + "\n" + \
                       "📝 be : belarusian" + "\n" + \
                       "📝 bn : bengali" + "\n" + \
                       "📝 bs : bosnian" + "\n" + \
                       "📝 bg : bulgarian" + "\n" + \
                       "📝 ca : catalan" + "\n" + \
                       "📝 ceb : cebuano" + "\n" + \
                       "📝 ny : chichewa" + "\n" + \
                       "📝 zh-cn : chinese (simplified)" + "\n" + \
                       "📝 zh-tw : chinese (traditional)" + "\n" + \
                       "📝 co : corsican" + "\n" + \
                       "📝 hr : croatian" + "\n" + \
                       "📝 cs : czech" + "\n" + \
                       "📝 da : danish" + "\n" + \
                       "📝 nl : dutch" + "\n" + \
                       "📝 en : english" + "\n" + \
                       "📝 eo : esperanto" + "\n" + \
                       "📝 et : estonian" + "\n" + \
                       "📝 tl : filipino" + "\n" + \
                       "📝 fi : finnish" + "\n" + \
                       "📝 fr : french" + "\n" + \
                       "📝 fy : frisian" + "\n" + \
                       "📝 gl : galician" + "\n" + \
                       "📝 ka : georgian" + "\n" + \
                       "📝 de : german" + "\n" + \
                       "📝 el : greek" + "\n" + \
                       "📝 gu : gujarati" + "\n" + \
                       "📝 ht : haitian creole" + "\n" + \
                       "📝 ha : hausa" + "\n" + \
                       "📝 haw : hawaiian" + "\n" + \
                       "📝 iw : hebrew" + "\n" + \
                       "📝 hi : hindi" + "\n" + \
                       "📝 hmn : hmong" + "\n" + \
                       "📝 hu : hungarian" + "\n" + \
                       "📝 is : icelandic" + "\n" + \
                       "📝 ig : igbo" + "\n" + \
                       "📝 id : indonesian" + "\n" + \
                       "📝 ga : irish" + "\n" + \
                       "📝 it : italian" + "\n" + \
                       "📝 ja : japanese" + "\n" + \
                       "📝 jw : javanese" + "\n" + \
                       "📝 kn : kannada" + "\n" + \
                       "📝 kk : kazakh" + "\n" + \
                       "📝 km : khmer" + "\n" + \
                       "📝 ko : korean" + "\n" + \
                       "📝 ku : kurdish (kurmanji)" + "\n" + \
                       "📝 ky : kyrgyz" + "\n" + \
                       "📝 lo : lao" + "\n" + \
                       "📝 la : latin" + "\n" + \
                       "📝 lv : latvian" + "\n" + \
                       "📝 lt : lithuanian" + "\n" + \
                       "📝 lb : luxembourgish" + "\n" + \
                       "📝 mk : macedonian" + "\n" + \
                       "📝 mg : malagasy" + "\n" + \
                       "📝 ms : malay" + "\n" + \
                       "📝 ml : malayalam" + "\n" + \
                       "📝 mt : maltese" + "\n" + \
                       "📝 mi : maori" + "\n" + \
                       "📝 mr : marathi" + "\n" + \
                       "📝 mn : mongolian" + "\n" + \
                       "📝 my : myanmar (burmese)" + "\n" + \
                       "📝 ne : nepali" + "\n" + \
                       "📝 no : norwegian" + "\n" + \
                       "📝 ps : pashto" + "\n" + \
                       "📝 fa : persian" + "\n" + \
                       "📝 pl : polish" + "\n" + \
                       "📝 pt : portuguese" + "\n" + \
                       "📝 pa : punjabi" + "\n" + \
                       "📝 ro : romanian" + "\n" + \
                       "📝 ru : russian" + "\n" + \
                       "📝 sm : samoan" + "\n" + \
                       "📝 gd : scots gaelic" + "\n" + \
                       "📝 sr : serbian" + "\n" + \
                       "📝 st : sesotho" + "\n" + \
                       "📝 sn : shona" + "\n" + \
                       "📝 sd : sindhi" + "\n" + \
                       "📝 si : sinhala" + "\n" + \
                       "📝 sk : slovak" + "\n" + \
                       "📝 sl : slovenian" + "\n" + \
                       "📝 so : somali" + "\n" + \
                       "📝 es : spanish" + "\n" + \
                       "📝 su : sundanese" + "\n" + \
                       "📝 sw : swahili" + "\n" + \
                       "📝 sv : swedish" + "\n" + \
                       "📝 tg : tajik" + "\n" + \
                       "📝 ta : tamil" + "\n" + \
                       "📝 te : telugu" + "\n" + \
                       "📝 th : thai" + "\n" + \
                       "📝 tr : turkish" + "\n" + \
                       "📝 uk : ukrainian" + "\n" + \
                       "📝 ur : urdu" + "\n" + \
                       "📝 uz : uzbek" + "\n" + \
                       "📝 vi : vietnamese" + "\n" + \
                       "📝 cy : welsh" + "\n" + \
                       "📝 xh : xhosa" + "\n" + \
                       "📝 yi : yiddish" + "\n" + \
                       "📝 yo : yoruba" + "\n" + \
                       "📝 zu : zulu" + "\n" + \
                       "📝 fil : Filipino" + "\n" + \
                       "📝 he : Hebrew" + "\n" + \
                       "\n🔊🔊🔊 Jangan Typo 🔊🔊🔊" + "\n" + "\n" + \
                         "Contoh : tr-en Lagi Syantik "
    return helpTranslate
groupParam = ""
def SiriGetOut(targ):
    cl.kickoutFromGroup(groupParam,[targ])
    #ki.kickoutFromGroup(groupParam,[targ])
    #kk.kickoutFromGroup(groupParam,[targ])
def byuh(targ):
    random.choice(KAC).kickoutFromGroup(groupParam,[targ])
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal Semuanya yg ada di\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai Semuanya yg ada di " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hallo all members " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"ดีจ้าา 😄 " + str(ginfo.name))

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in admin:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])
                        cl.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
                        cl.blockContact(op.param1)

        if op.type == 55:
            try:
                if op.param1 in Setmain["phreadPoint"]:
                   if op.param2 in Setmain["phreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["phreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)


        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ariftj = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ariftj.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ariftj.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ariftj = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ariftj.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ariftj = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ariftj.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.gq/simi.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               cl.sendMessage(msg.to, str(data["answer"]))
                   except Exception as error:
                       pass

               if msg.to in translatetr:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='tr')
                           A = hasil.text
                           cl.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           cl.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           cl.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           cl.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           cl.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           cl.sendMessage(msg.to, A)
                   except Exception as error:
                       pass

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"7839705","STKPKGID":"1192862","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           cl.sendMessage(msg.to, "Yang suka ngetag aku gift aja ya,\nsilahkan Cek di PM, udah aku gift tuh silahkan klik unduh,tp ingt klo belom berteman masa berlaku tikel akan kadaluarsa...")
                           cl.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, "Jangan tag saya dong....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n🔰 STKID : " + msg.contentMetadata["STKID"] + "\n🔰 STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n🔰 STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"☬ Nama : " + msg.contentMetadata["displayName"] + "\n🔰 MID : " + msg.contentMetadata["mid"] + "\n🔰 Status Msg : \n🔰" + contact.statusMessage + "\n🔰 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}

            if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"✍ Nama : " + msg.contentMetadata["displayName"] + "\n🔰 MID : " + msg.contentMetadata["mid"] + "\n🔰 Status Msg : " + contact.statusMessage + "\n🔰 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["phfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["phfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "คำสั่ง":
                          if wait["selfbot"] == True:
                            if msg._from in group:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                               cl.sendContact(to, "u4862fe4b182b2fd194a3108e2f3662e8")
 
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Selfbot diaktifkan")

                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Selfbot dinonaktifkan")

                        elif cmd == "คำสั่ง2":
                          if wait["selfbot"] == True:
                            if msg._from in group:
                               helpMessage1 = helarot()
                               cl.sendMessage(msg.to, str(helpMessage1))
                               cl.sendContact(to, "u4862fe4b182b2fd194a3108e2f3662e8")
 
                        elif cmd == "โปร":
                          if wait["selfbot"] == True:
                            if msg._from in group:
                               helpMessage2 = infomeme()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "คำสั่งแปล":
                          if wait["selfbot"] == True:
                            if msg._from in group:
                               helpTranslate = translate()
                               cl.sendMessage(msg.to, str(helpTranslate))

                        if cmd == "เปิดยกเลิก":
                            if msg._from in admin:
                                wait["unsend"] = True
                                cl.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")

                        if cmd == "ปิดยกเลิก":
                            if msg._from in admin:
                                wait["unsend"] = False
                                cl.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")

                        elif cmd == "เชคค่า":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "-▬▬▬▬▬▬▬▬▬▬▬▬\n          🔰 S T A T U S 🔰\n-▬▬▬▬▬▬▬▬▬▬▬▬\n"
                                if wait["unsend"] == True: md+="🔊 ยกเลิก「เปิด」\n"
                                else: md+="🔇 ยกเลิก「ปิด」\n"
                                if wait["sticker"] == True: md+="🔊 สติกเกอร์「เปิด」\n"
                                else: md+="🔇 สติกเกอร์「ปิด」\n"
                                if wait["contact"] == True: md+="🔊 คท「เปิด」\n"
                                else: md+="🔇 คท「ปิด」\n"
                                if wait["Mentionkick"] == True: md+="🔊 แตะแทค「เปิด」\n"
                                else: md+="🔇 เตะแทค「ปิด」\n"
                                if wait["detectMention"] == True: md+="🔊 แทค「เปิด」\n"
                                else: md+="🔇 แทค「ปิด」\n"
                                if wait["Mentiongift"] == True: md+="🔊 ของขวัญ「เปิด」\n"
                                else: md+="🔇 ของขวัญ「ปิด」\n"
                                if wait["autoJoin"] == True: md+="🔊 เข้ากลุ่ม「เปิด」\n"
                                else: md+="🔇 เข้ากลุ่ม「ปิด」\n"
                                if settings["autoJoinTicket"] == True: md+="🔊 มุดลิ้ง「เปิด」\n"
                                else: md+="🔇 มุดลิ้ง「ปิด」\n"
                                if msg.to in simisimi: md+="🔊 Simisimi「ON」\n"
                                else: md+="🔇 Simisimi「OFF」\n"
                                if wait["autoAdd"] == True: md+="🔊 บล็อค「เปิด」\n"
                                else: md+="🔇 บล็อค「ปิด」\n"
                                if msg.to in welcome: md+="🔊 คนเข้า「เปิด」\n"
                                else: md+="🔇 คนเข้า「ปิด」\n"
                                if wait["autoLeave"] == True: md+="🔊 คนออก「เปิด」\n"
                                else: md+="🔇 คนออก「ปิด」\n"
                                cl.sendMessage(msg.to, md+"-▬▬▬▬▬▬▬▬▬▬▬▬\n☬ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n☬ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n-▬▬▬▬▬▬▬▬▬▬▬▬")
                                cl.sendContact(to, "u4862fe4b182b2fd194a3108e2f3662e8")
      
                        elif cmd == "เชคค่า แปล":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "-▬▬▬▬▬▬▬▬▬▬▬▬\n🔰 STATUS TRANSLATE 🔰\n-▬▬▬▬▬▬▬▬▬▬▬▬\n"
                                if msg.to in translatetr: md+="🔊 Turkish「ON」\n"
                                else: md+="🔇 Turkish 「OFF」\n"
                                if msg.to in translateen: md+="🔊 English「ON」\n"
                                else: md+="🔇 English「OFF」\n"
                                if msg.to in translateid: md+="🔊 Indonesia「ON」\n"
                                else: md+="🔇 Indonesia「OFF」\n"
                                if msg.to in translateth: md+="🔊 Thailand「ON」\n"
                                else: md+="🔇 Thailand「OFF」\n"
                                if msg.to in translatetw: md+="🔊 Taiwan「ON」\n"
                                else: md+="🔇 Taiwan「OFF」\n"
                                if msg.to in translatear: md+="🔊 Arab「ON」\n"
                                else: md+="🔇 Arab「OFF」\n"
                                cl.sendMessage(msg.to, md+"-▬▬▬▬▬▬▬▬▬▬▬▬\n☬ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n☬ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n-▬▬▬▬▬▬▬▬▬▬▬▬")

                        elif cmd == "ผส" or text.lower() == 'creator':
                            if msg._from in group:
                                cl.sendMessage(msg.to,"Creator Bot")
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "ข้อมูล" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「【さัএπัஞ✵ບิथℓℓҨतΩ】」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "คท" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               cl.sendMessage1(msg)

                        elif text.lower() == "ไอดี":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("ไอดี " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("ข้อมูล " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "☬ Nama : "+str(mi.displayName)+"\n🔰 Mid : " +key1+"\n🔰 Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif text.lower() == "ลบแชท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif cmd.startswith("ชื่อ "):
                          if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = cl.getContact(ls)
                                      cl.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)

                        elif cmd.startswith("ตัส "):
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = cl.getContact(ls)
                                      cl.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)

                        elif cmd.startswith("รูป "):
                            if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                                        cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ปก "):
                            if msg._from in admin:
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
                                            path = cl.getProfileCoverURL(ls)
                                            cl.sendImageWithURL(msg.to, str(path))
                        elif cmd.startswith("วิดีโอ "):
                            if msg._from in admin:
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            contact = cl.getContact(target)
                                            path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                                            cl.sendVideoWithURL(msg.to, path)
                                        except Exception as e:
                                            pass

                        elif cmd.startswith("ก็อป "):
                            if msg._from in admin:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        for mention in mentionees:
                                            contact = mention["M"]
                                            break
                                        try:
                                            cl.cloneContactProfile(contact)
                                            cl.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                        except:
                                            cl.sendMessage(msg.to, "Gagal clone member")

                        elif cmd.startswith("คืนร่าง"):
                            if msg._from in admin:
                                try:
                                    PhieProfile.displayName = str(myProfile["displayName"])
                                    PhieProfile.statusMessage = str(myProfile["statusMessage"])
                                    PhieProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    cl.updateProfileAttribute(8, arifProfile.pictureStatus)
                                    cl.updateProfile(PhieProfile)
                                    cl.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except:
                                            cl.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("ประกาศ: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"ประกาศ\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")

                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd.startswith("changenamecreator: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti nama creator")
                               else:
                                   Setmain["namecreator"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Change name creator」\nNama creator diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetnamecreator":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["namecreator"] = "【さัএπัஞ✵ບิथℓℓҨतΩ】"
                               cl.sendMessage(msg.to, "「Change name creator」\nNama creator kembali ke awal")

                        elif cmd == "รีบูส":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["restartPoint"] = msg.to
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               time.sleep(3)
                               cl.sendMessage(msg.to, "3...")
                               time.sleep(2)
                               cl.sendMessage(msg.to, "2...")
                               time.sleep(2)
                               cl.sendMessage(msg.to, "1...")
                               time.sleep(2)
                               cl.sendMessage(msg.to, "Restart Sukses...")
                               restartBot()

                        elif cmd == "ออน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)

                        elif cmd == "ข้อมูลกลุ่ม":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "💻 BOT Grup Info\n\n 💻 Nama Group : {}".format(G.name)+ "\n🔰 ID Group : {}".format(G.id)+ "\n🔰 Pembuat : {}".format(G.creator.displayName)+ "\n🔰 Waktu Dibuat : {}".format(str(timeCreated))+ "\n🔰 Jumlah Member : {}".format(str(len(G.members)))+ "\n🔰 Jumlah Pending : {}".format(gPending)+ "\n🔰 Group Qr : {}".format(gQr)+ "\n🔰 Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "🖥 BOT Grup Info\n"
                                ret_ += "\n🖥 Nama Group : {}".format(G.name)
                                ret_ += "\n🖥 ID Group : {}".format(G.id)
                                ret_ += "\n🖥 Pembuat : {}".format(gCreator)
                                ret_ += "\n🖥 Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n🖥 Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n🖥 Jumlah Pending : {}".format(gPending)
                                ret_ += "\n🖥 Group Qr : {}".format(gQr)
                                ret_ += "\n🖥 Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "💻 "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"💻 Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except:
                                pass

                        elif cmd == "เพื่อนกู":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╭━━[ FRIEND LIST ]\n┃\n"+ma+"┃\n╰━━[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "กลุ่มกู":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "┃ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╭━━[ GROUP LIST ]\n┃\n"+ma+"┃\n╰━━[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "เปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "ปิดลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "ลิ้งกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "spaminvid":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                dan = msg.text.split("|")
                                userid = dan[1]
                                namagrup = dan[2]
                                jumlah = int(dan[3])
                                grups = cl.groups
                                tgb = cl.findContactsByUserid(userid)
                                if jumlah <= 10000:
                                    for var in range(0,jumlah):
                                        try:
                                            cl.createGroup(str(namagrup), [tgb.mid])
                                            for i in grups:
                                                grup = cl.getGroup(i)
                                                if grup.name == namagrup:
                                                    cl.inviteIntoGroup(grup.id, [tgb.mid])
                                                    cl.leaveGroup(grup.id)
                                                    sendMention(msg.to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                        except Exception as Nigga:
                                            cl.sendMessage(msg.to, str(Nigga))
                                else:
                                    sendMention(msg.to, "@! kebanyakan njer!!", [sender])

                        elif cmd == "ลบรัน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "Tidak ada undangan yang tertunda")

#===========BOT UPDATE============#
                        elif cmd == "เปลี่ยนรูปกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "เปลี่ยนรูป":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendMessage(msg.to,"ส่งรูปภาพ.....")

                        elif cmd.startswith("เปลี่ยนชื่อ: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "แทค":
                          if wait["selfbot"] == True:
                            group = cl.getGroup(msg.to)
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
                                cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                cl.sendMessage(to, "Hello {} Mention".format(str(len(nama)))) 

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"💻 BOT admin\n\nAdmin:\n"+mb+"\nTotal「%s」Admin" %(str(len(admin))))

                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, " 💻 BOT Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "สปีท" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "เปิดอ่าน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['phreadPoint'][msg.to] = msg_id
                                 Setmain['phreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "ปิดอ่าน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['phreadPoint'][msg.to]
                                 del Setmain['phreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "อ่าน":
                          if msg._from in admin:
                            if msg.to in Setmain['phreadPoint']:
                                if Setmain['phreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['phreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['phreadPoint'][msg.to]
                                        del Setmain['phreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['phreadPoint'][msg.to] = msg.id
                                    Setmain['phreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "cctv on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "cctv off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n💻 Lokasi : " + data[0]
                                         ret_ += "\n💻 " + data[1]
                                         ret_ += "\n💻 " + data[2]
                                         ret_ += "\n💻 " + data[3]
                                         ret_ += "\n💻 " + data[4]
                                         ret_ += "\n💻 " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n🌎 Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n🌦 Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n🌦 Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n🌦 Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n🌦 Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n🌎 Location : " + data[0]
                                    ret_ += "\n🔎 Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("musik: "):
                          if msg._from in admin:
                            try:
                                search = msg.text.replace("musik: ","")
                                r = requests.get("https://farzain.xyz/api/premium/joox.php?apikey=al11241519&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                cl.sendImageWithURL(msg.to, str(data["gambar"]))
                                cl.sendMessage(msg.to, str(hasil))
                                cl.sendMessage(msg.to, "Downloading...")
                                cl.sendMessage(msg.to, "「 Result MP3 」")
                                cl.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                cl.sendMessage(msg.to, "「 Result M4A 」")
                                cl.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                cl.sendMessage(msg.to, str(data["lirik"]))
                                cl.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	cl.sendMessage(msg.to, "「 Result Error 」\n" + str(error))

                        elif cmd.startswith("playlist "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━[ List Lagu ]━━━"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n🎙「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    ret_ += "\n🎙「 {}Lirik {}:nomor 」 ".format(str(),str(search))
                                    cl.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╭━━━━[ Detail Musik ]━━━━"
                                            ret_ += "\n┃ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n┃ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n┃ Size : {}".format(str(data["result"]["size"]))
                                            #ret_ += "\n┃ Link : {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╰━━[ Tunggu Audionya ]━━━"
                                            cl.sendMessage(msg.to, str(ret_))
                                            cl.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass

                        elif cmd.startswith("lirik "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lirik ]━━━━"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n🎙「 {}Lirik {}:nomor 」".format(str(),str(search))
                                    ret_ += "\n🎙「 {}Playlist {}:nomor 」 ".format(str(),str(search))
                                    cl.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        cl.sendMessage(msg.to, str(lyric))
                            except Exception as error:
                                pass

                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                cl.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                cl.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass

                        elif cmd.startswith("randomnumber: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                angka = msg.text.replace(separate[0] + " ","")
                                tgb = angka.split("-")
                                num1 = tgb[0]
                                num2 = tgb[1]
                                r = requests.get("https://farzain.xyz/api/random.php?min="+num1+"&max="+num2)
                                data = r.json()
                                cl.sendMessage(msg.to,"Hasil : "+str(data["url"]))

                        elif cmd.startswith("1cak"):
                          if msg._from in admin:
                              r=requests.get("https://api-1cak.herokuapp.com/random")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "Result :\n"
                              hasil += "\nID : " +str(data["id"])
                              hasil += "\nTitle : " + str(data["title"])
                              hasil += "\nUrl : " + str(data["url"])
                              hasil += "\nVotes : " + str(data["votes"])
                              cl.sendImageWithURL(msg.to, str(data["img"]))
                              cl.sendMessage(msg.to, str(hasil))

                        elif cmd.startswith("musik2: "):
                          if msg._from in admin:
                            try:
                                dan = msg.text.replace("musik2: ","")
                                r = requests.get("https://corrykalam.gq/joox.php?song="+urllib.parse.quote(dan))
                                data = r.json()
                                l = data["lyric"].replace("ti:","Judul: ")
                                i = l.replace("ar:","Penyanyi: ")
                                r = i.replace("al:","Album: ")
                                ii = r.replace("[by:]","")
                                k = ii.replace("[offset:0]","")
                                lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                                cl.sendImageWithURL(msg.to, data["image"])
                                t = "[ Music ]"
                                t += "\n\nJudul: "+str(data["title"])
                                t+="\nPenyanyi: "+str(data["singer"])
                                t+="\n\n[ Finish ]\n\n"+str(lirik)
                                cl.sendMessage(msg.to, str(t))
                                cl.sendAudioWithURL(msg.to, data["url"])
                            except Exception as error:
                                pass

                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        cl.sendImageWithURL(msg.to, str(food["url"]))

                        elif cmd.startswith("fs: "):
                          if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                nama = msg.text.replace(separate[0] + " ","")
                                nmor = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]
                                plih = random.choice(nmor)
                                nmor2 = ["1","2","3","4","5","6","7"]
                                plih2 = random.choice(nmor2)
                                url = ("https://farzain.xyz//api//premium//fansign//fs%20("+plih+").php?text="+nama+"&apikey=al11241519","http://farzain.xyz/api/premium/fansign/cos/cos%20("+plih2+").php?text="+nama+"&apikey=al11241519")
                                plihurl = random.choice(url)
                                cl.sendImageWithURL(msg.to, plihurl)
                            except Exception as error:
                                pass

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                keyword = msg.text.replace(separate[0] + " ","")
                                r = requests.get("https://farzain.xyz/api/gambarg.php?id="+keyword)
                                data = r.text
                                data = json.loads(data)
                                cl.sendImageWithURL(msg.to, str(data["url"]))
                            except Exception as error:
                            	pass

                        elif cmd.startswith("quotes"):
                          if msg._from in admin:
                            try:
                                r = requests.get("https://farzain.xyz/api/quotes.php")
                                data = r.text
                                data = json.loads(data)
                                cl.sendMessage(msg.to, str(data["result"]))
                            except Exception as error:
                            	pass

                        elif cmd.startswith("acaratv: "):
                          if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                channel = msg.text.replace(separate[0] + " ","")
                                r = requests.get("https://farzain.xyz/api/premium/acaratv.php?apikey=al11241519&id="+channel)
                                data = r.text
                                data = json.loads(data)
                                cl.sendMessage(msg.to, "Acara TV Di "+channel+ ":\n" + str(data["url"]))
                            except Exception as error:
                            	pass

                        elif cmd.startswith("cl-telp: "):
                          if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                nohp = msg.text.replace(separate[0] + " ","")
                                r = requests.get("https://farzain.xyz/api/cl.php?id="+nohp+"&type=2")
                                cl.sendMessage(msg.to, "「 cl Telepon 」\n💻 Status : Success!!!\n💻 No Tujuan : "+nohp)
                            except Exception as error:
                                pass

                        elif cmd.startswith("cl-sms: "):
                          if msg._from in admin:
                            try:
                                separate = msg.text.split(" ")
                                nohp = msg.text.replace(separate[0] + " ","")
                                r = requests.get("https://farzain.xyz/api/cl.php?id="+nohp+"&type=1")
                                cl.sendMessage(msg.to, "「 cl Sms 」\n💻 Status : Success!!!\n💻 No Tujuan : "+nohp)
                            except Exception as error:
                                pass

                        elif cmd.startswith("smsgratis: "):
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                pesan = msg.text.replace(separate[0] + " ","")
                                tgb = pesan.split(":")
                                num1 = tgb[0]
                                num2 = tgb[1]
                                r = requests.get("https://corrykalam.gq/sms.php?no="+num1+"&text="+num2)
                                data = r.json()
                                cl.sendMessage(msg.to, "「 Sms Gratis 」\n💻 Status : "+str(data["status"])+"!!!\n💻 No Tujuan : "+num1+"\n💻 Pesannya : "+num2+"\n💻 Detail : "+str(data["detail"]))

                        elif cmd.startswith("cl call: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            nomor = msg.text.replace(sep[0] + " ","")
                            r = requests.get("http://apisora2.herokuapp.com/cl/call/?no={}".format(urllib.parse.quote(nomor)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = "「 Prangked Telpon 」"
                            ret_ += "\n• Status : {}".format(str(data["status"]))
                            ret_ += "\n• Tujuan "+str(data["result"])
                            cl.sendMessage(msg.to, str(ret_))


                        elif cmd.startswith("meme"):
                          if msg._from in admin:
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            cl.sendImageWithURL(msg.to, image)

                        elif cmd.startswith("al-quran:"):
                            if msg._from in admin:
                                try:
                                    sep = msg.text.split(" ")
                                    search = msg.text.replace(sep[0] + " ","")
                                    with requests.session() as web:
                                        r = requests.get("http://api.alquran.cloud/surah/{}/ar.alafasy".format(str(search)))
                                        data = r.text
                                        data = json.loads(data)
                                        no = 0
                                        ret_ = "Quran Surah {}/{}\nSurah Ke-{}".format(str(data["data"]["englishName"]),str(data["data"]["name"]),str(data["data"]["number"]))
                                        for quran in data["data"]["ayahs"]:
                                            no += 1
                                            ret_ += "\n{}. {}".format(str(no),quran["text"])
                                        cl.sendMessage(msg.to, str(ret_))
                                except Exception as error:
                                     pass

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🎥 Author : ' + str(vid.author)
                                    durasi = '\n🎥 Duration : ' + str(vid.duration)
                                    suka = '\n🎥 Likes : ' + str(vid.likes)
                                    rating = '\n🎥 Rating : ' + str(vid.rating)
                                    deskripsi = '\n🎥 Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n📽 Author : ' + str(vid.author)
                                    durasi = '\n📽 Duration : ' + str(vid.duration)
                                    suka = '\n📽 Likes : ' + str(vid.likes)
                                    rating = '\n📽 Rating : ' + str(vid.rating)
                                    deskripsi = '\n📽 Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                tj = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                cl.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                cl.sendImageWithURL(msg.to, tj)
                            except Exception as njer:
                                cl.sendMessage(msg.to, str(njer))

                        elif cmd.startswith("cekig:"):
                            if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHtJIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "╭━━[ Profile Instagram ]"
                                        ret_ += "\n┃ Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\n┃ Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\n┃ Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\n┃ URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\n┃ Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃ Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\n┃ Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\n╰━━[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        cl.sendMessage(to, str(ret_))
                                        cl.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"🔰 I N F O R M A S I 🔰\n\n"+"🔰 Date Of Birth : "+lahir+"\n🔰 Age : "+usia+"\n🔰 Ultah : "+ultah+"\n🔰 Zodiak : "+zodiak)

                        elif cmd.startswith("แทค: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ARlimit"] = num
                                cl.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("แสปมคลอ: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("แทค "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ARlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")

                        elif cmd == "แสปมคลอ":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["ARmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#==============================================================================#
                        elif msg.text.lower().startswith("tr-af "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='af')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sq "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sq')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-am "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='am')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ar "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ar')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hy')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-az "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='az')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-eu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='eu')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-be "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='be')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bn')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bs "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bs')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bg')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ca "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ca')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ceb "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ceb')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ny "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ny')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-cn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-cn')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-tw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-tw')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-co "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='co')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hr')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-cs "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='cs')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-da "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='da')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-nl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='nl')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-en "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='en')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-et "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='et')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fi')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fr')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fy')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gl')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ka "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ka')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-de "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='de')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-el "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='el')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gu')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ht "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ht')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ha "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ha')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-haw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='haw')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-iw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='iw')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hi')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hmn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hmn')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hu')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-is "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='is')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ig "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ig')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-id "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='id')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ga "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ga')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-it "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='it')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ja "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ja')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-jw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='jw')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-kn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='kn')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-kk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='kk')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-km "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='km')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ko "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ko')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ku "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ku')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ky "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ky')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lo "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lo')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-la "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='la')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lv "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lv')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lt')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lb "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lb')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mk')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mg')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ms "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ms')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ml "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ml')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mt')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mi')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mr')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mn')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-my "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='my')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ne "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ne')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-no "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='no')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ps "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ps')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fa "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fa')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pl')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pt')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pa "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pa')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ro "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ro')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ru "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ru')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sm "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sm')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gd "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gd')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sr')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-st "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='st')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sn')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sd "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sd')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-si "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='si')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sk')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sl')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-so "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='so')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-es "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='es')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-su "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='su')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sw')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sv "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sv')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-tg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='tg')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ta "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ta')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-te "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='te')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-th "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='th')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-tr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='tr')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-uk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='uk')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ur "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ur')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-uz "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='uz')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-vi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='vi')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-cy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='cy')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-xh "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='xh')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-yi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='yi')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-yo "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='yo')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zu')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fil "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fil')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-he "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='he')
                            A = hasil.text
                            cl.sendMessage(msg.to, A)

#===========Settings============#
                        elif 'Simi ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Autotrans tr-' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Autotrans tr-','')
                              if spl == 'on':
                                  if msg.to in translateth:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateth.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateth:
                                         translateth.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Autotrans th-' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Autotrans th-','')
                              if spl == 'on':
                                  if msg.to in translateth:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateth.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateth:
                                         translateth.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Autotrans en-' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Autotrans en-','')
                              if spl == 'on':
                                  if msg.to in translateen:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateen.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateen:
                                         translateen.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif 'Autotrans id-' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Autotrans id-','')
                              if spl == 'on':
                                  if msg.to in translateid:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateid.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateid:
                                         translateid.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Autotrans tw-' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Autotrans tw-','')
                              if spl == 'on':
                                  if msg.to in translatetw:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatetw.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatetw:
                                         translatetw.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Autotrans ar-' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Autotrans ar-','')
                              if spl == 'on':
                                  if msg.to in translatear:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatear.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatear:
                                         translatear.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========Protection============#
                        elif 'ต้อนรับ ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'เปิด':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'ปิด':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                        elif ("ปลิว " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                            cl.kickoutFromGroup(msg.to,[target])
                                       except:
                                           pass

                        elif ("Selam canım" in msg.text):
                            if wait["selfbot"] == True:
                                if msg.toType == 2:
                                    if msg._from in admin:
                                        #print "ok"
                                        _name = msg.text.replace("Selam canım","")
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    if _name in g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    cl.sendText(msg.to,"Error")
                                else:
                                    for target in targets:
                                        try:
                                            cl.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                            cl.sendText(msg.to,"Done")
                        elif text.lower() == 'fuck@sirichan':
                            if msg._from in admin:
                                gs = cl.getGroup(msg.to)
                            gs = cl.getGroup(msg.to)
                            gs = cl.getGroup(msg.to)
                            sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん","0","1","2","3","4","5","6","7","8","9"])]
                            if sirilist != []:
                                groupParam = msg.to
                                try:
                                    p = Pool(40)
                                    p.map(SiriGetOut,sirilist)
                                    p.close()
                                except:
                                    p.close()
                        elif text.lower() == 'nuke all':
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                #gs = ar1.getGroup(msg.to)
                                #gs = ar2.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendText(msg.to,"kayak nya limit")
                                else:
                                    for target in targets:
                                      if target not in Bots:
                                        try:
                                            klist=[cl]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                           pass
                        elif text.lower() == 'broken':
                            if msg._from in admin:
                                if msg.toType == 2:
                                    gs = cl.getGroup(msg.to)
                                gs.preventedJoinByTicket = False
                                cl.updateGroup(gs)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.1)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendText(msg.to,"DRAG KICK OUT BYE")
                                else:
                                    for target in targets:
                                      if target not in Bots:
                                        try:
                                            klist=[cl,cl,cl]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                           pass
                        elif msg.text in ['ยกเลิก']:
                            if msg.toType == 2:
                                #if msg._from in admin:
                                group = cl.getGroup(msg.to)

                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                    cl.cancelGroupInvitation(msg.to,[_mid])

                        elif msg.text in ["ยกเลิกทั้งหมด"]:
                            if msg._from in admin:
                                gid = cl.getGroupIdsInvited()
                                for i in gid:
                                    cl.rejectGroupInvitation(i)
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Success menolak semua undangan")
                            else:
                                cl.sendText(msg.to,"He declined all invitations")
#===========ADMIN ADD============#
                        elif ("ตั้งแอดมิน " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("ลบแอดมิน " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   #if target not in Arif:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "ตั้งคทแอด" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"● ส่งคท ●...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "ปิดตั้งแอด" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                cl.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "คท แอดมิน" or text.lower() == 'virüs':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': 'sezer'}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "เปิดเตะแทค" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"แทคมามีเจ็บ 😈")

                        elif cmd == "ปิดเตะแทค" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                cl.sendMessage(msg.to,"ปิดแล้ว เดี๋ยวมึงหัวร้อน 😈")

                        elif cmd == "เปิดคท" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"เปิดเชค คท แล้ว 😈")

                        elif cmd == "ปิดคท" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"ปิดเชค คท แล้ว 😈")

                        elif cmd == "เปิดแทค" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"เปิดแทคแล้ว 😈")

                        elif cmd == "ปิดแทค" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"ปิดแทคแล้ว 😈")

                        elif cmd == "เปิดของขวัญ" or text.lower() == 'respongift on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                cl.sendMessage(msg.to,"เปิดแทคส่งของขวัญ 😈")

                        elif cmd == "ปิดของขวัญ" or text.lower() == 'respongift off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                cl.sendMessage(msg.to,"ปิดแทคส่งของขวัญ 😈")

                        elif cmd == "เปิดเข้ากลุ่ม" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"เปิดเข้ากลุ่มออโต้แล้ว 😈")

                        elif cmd == "ปิดเข้ากลุ่ม" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"ปิดเข้ากลุ่มออโต้แล้ว 😈")

                        elif cmd == "เปิดคนออก" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"เปิดข้อความคนออก 😈")

                        elif cmd == "ปิดคนออก" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"ปิดข้อความคนออก 😈")

                        elif cmd == "เปิดบล็อค" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"เปิดบล็อค 😈")

                        elif cmd == "ปิดบล็อค" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"ปิดบล็อค 😈")

                        elif cmd == "เปิดสติกเกอร์" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "ปิดสติกเกอร์" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "เปิดมุด" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"เปิดมุดลิ้ง 😈")

                        elif cmd == "ปิดมุด" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"ปิดมุดลิ้ง 😈")

#===========COMMAND SET============#
                        elif 'ตั้งข้อความ: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'ตั้งคนเข้า: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'ตั้งคนออก: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  wait["leave"] = spl
                                  cl.sendMessage(msg.to, "「Leave Msg」\nLeave Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'ตั้งแทค: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'ตั้งแสปม: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'ตั้งคนแอบ: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "เชคข้อความ":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "เชคคนเข้า":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "เชคคนออก":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Leave Msg」\nLeave Msg mu :\n\n「 " + str(wait["leave"]) + " 」")

                        elif text.lower() == "เชคแทค":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "เชคแสปม":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["ARmessage1"]) + " 」")

                        elif text.lower() == "เชคคนแอบ":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "● มุดเรียบร้อย ● : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
