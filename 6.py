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

cl!= LineClient()
#cl = LineClient(authToken='')
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient()
#ki = LineClient(authToken='')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))

kk = LineClient()
#kk = LineClient(authToken='')
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))

kc = LineClient()
#kc = LineClient(authToken='')
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))

km = LineClient()
#km = LineClient(authToken='')
km.log("Auth Token : " + str(km.authToken))
channel4 = LineChannel(km)
km.log("Channel Access Token : " + str(channel4.channelAccessToken))

kb = LineClient()
#kb = LineClient(authToken='')
kb.log("Auth Token : " + str(kb.authToken))
channel5 = LineChannel(kb)
kb.log("Channel Access Token : " + str(channel5.channelAccessToken))

cxb = LineClient()
#cxb = LineClient(authToken='')
cxb.log("Auth Token : " + str(cxb.authToken))
channel8 = LineChannel(cxb)
cxb.log("Channel Access Token : " + str(channel8.channelAccessToken))

poll = LinePoll(cl)
creator = ["u4862fe4b182b2fd194a3108e2f3662e8"]
owner = ["u4862fe4b182b2fd194a3108e2f3662e8"]
admin = ["u4862fe4b182b2fd194a3108e2f3662e8"]
staff = ["u4862fe4b182b2fd194a3108e2f3662e8"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = km.getProfile().mid
Emid = kb.getProfile().mid
Zmid = cxb.getProfile().mid
KAC = [cl,ki,kk,kc]
ABC = [ki,kk,kc,km,kb]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Zmid]
Saints = owner + admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = km.getProfile().displayName
responsename5 = kb.getProfile().displayName

helpMessage ="""╔═══════════════
╠❂➣【さัএπัஞ✵ບิथℓℓҨतΩ】
╚═══════════════
╔═══════════════
╠❂➣ Me
╠❂➣ Mid
╠❂➣ Mid [@]
╠❂➣ Like [@]
╠❂➣ Url
╠❂➣ Open
╠❂➣ Close
╠❂➣ Ginfo
╠❂➣ Kiss
╠❂➣ Creator
╠❂➣ Settings
╠❂➣ Speed
╠❂➣ Spb
╠❂➣ Join
╠❂➣ Byeall
╠❂➣ Leave all
╠❂➣ Me leave
╠❂➣ Responsename
╚═══════════════
╔═══════════════
╠❂➣ ᴀᴅᴍɪɴ ᴍᴇɴᴜ 
╚═══════════════
╔═══════════════
╠❂➣ Kick [@]
╠❂➣ Kamu [@]
╠❂➣ Mayhem
╠❂➣ Blc
╠❂➣ Ban [@]
╠❂➣ Unban [@]
╠❂➣ Ban:on/off
╠❂➣ Unban:on/off
╠❂➣ Banlist
╠❂➣ Clearban
╠❂➣ Glist
╠❂➣ Friendlist
╠❂➣ B1: [Text]
╠❂➣ B2: [Text]
╠❂➣ B3: [Text]
╠❂➣ B4: [Text]
╠❂➣ B5: [Text]
╠❂➣ Myname: [Text]
╠❂➣ Restart
╠❂➣ Informasi
╠❂➣ Bot upicture
╠❂➣ Group upicture
╠❂➣ Me upicture
╠❂➣ Remove
╚═══════════════
╔══════╬╬═══════
╠❂➣ sᴇᴛᴛɪɴɢ ᴍᴇɴᴜ 
╚══════╬╬═══════
╔══════╬╬═══════
╠❂➣ Sider on/off
╠❂➣ Lurking on/off
╠❂➣ Lurkers
╠❂➣ Cek sider
╠❂➣ Cek spam
╠❂➣ Cek pesan
╠❂➣ Cek respon
╠❂➣ Cek welcome
╠❂➣ Set sider: [Text]
╠❂➣ Set spam: [Text]
╠❂➣ Set pesan: [Text]
╠❂➣ Set respon: [Text]
╠❂➣ Set welcome: [Text]
╠❂➣ Sticker on/off
╠❂➣ Contact on/off
╠❂➣ Autojoin on/off
╠❂➣ Autoadd on/off
╠❂➣ Autoleave on/off
╠❂➣ Welcome on/off
╠❂➣ Autorespon on/off
╠❂➣ Gift: [Mid] [Jumlah]
╠❂➣ Spam: [Mid] [Jumlah]
╚═══════════════
"""

setowner ="""╔═══════════════
╠❂➣【さัএπัஞ✵ບิथℓℓҨतΩ】
╚═══════════════
╔═══════════════
╞☪ Me
╞☪ Mid
╞☪ Mid [@]
╞☪ Like [@]
╞☪ Info [@]
╞☪ Url
╞☪ Open
╞☪ Close
╞☪ Ginfo
╞☪ Kiss
╞☪ Creator
╞☪ Settings
╞☪ Speed
╞☪ Responsp
╞☪ Join
╞☪ Byeall
╞☪ Leave all
╞☪ Me leave
╞☪ Responsename
╞☪ Kick [@]
╞☪ Kamu [@]
╞☪ Mayhem
╰═══════════════
╭═══════════════
╞☪ ᴄᴏᴍᴍᴀɴᴅ ʙʟᴀᴄᴋʟɪsᴛ
╰═══════════════
╭═══════════════
╞☪ Blc
╞☪ Ban [@]
╞☪ Unban [@]
╞☪ Ban:on/off
╞☪ Unban:on/off
╞☪ Banlist
╞☪ Clearban
╞☪ Glist
╞☪ Friendlist
╞☪ Restart
╰═══════════════
╭═══════════════
╞☪ ɪɴғᴏ ᴍᴇɴᴜ βΩT
╰═══════════════
╭═══════════════
╞☪ Informasi
╞☪ Bot upicture
╞☪ Group upicture
╞☪ Me upicture
╞☪ Remove
╞☪ Sider on/off
╞☪ Lurking on/off
╞☪ Lurkers
╞☪ Cek spam
╞☪ Cek pesan
╞☪ Cek respon
╞☪ Cek welcome
╞☪ Set spam: [Text]
╞☪ Set pesan: [Text]
╞☪ Set respon: [Text]
╞☪ Set welcome: [Text]
╞☪ Sticker on/off
╞☪ Contact on/off
╞☪ Autojoin on/off
╞☪ Autoadd on/off
╞☪ Autoleave on/off
╞☪ Welcome on/off
╞☪ Autorespon on/off
╰═══════════════
"""

setadmin ="""╭═══════════════
╞☪ ᴍᴇɴᴜ sᴘᴇsɪᴀʟ
╰═══════════════
╭═══════════════
╞☪ Staff:on/off
╞☪ Staff add [@]
╞☪ Staff dell [@]
╞☪ Admin:on/off
╞☪ Admin add [@]
╞☪ Admin dell [@]
╞☪ Bot:on
╞☪ Bot:repeat
╞☪ Bot add [@]
╞☪ Bot dell [@]
╞☪ Botlist
╞☪ Contact bot
╞☪ Talk on/off
╞☪ Talklist
╞☪ Talkban:on/off
╞☪ Talkban [@]
╞☪ Talkdell [@]
╞☪ Refresh
╞☪ Adminlist
╰═══════════════
╭═══════════════
╞☪【さัএπัஞ✵ບิथℓℓҨतΩ】
╰═══════════════
╭═══════════════
╞☪ Ntag on/off
╞☪ Nkick on/off
╞☪ Njoin on/off
╞☪ Ncancel on/off
╞☪ Block url on/off
╞☪ Allprotect on/off
╞☪ Listpro
╰═══════════════
╭═══════════════
╞☪【さัএπัஞ✵ບิथℓℓҨतΩ】
╰═══════════════
╭═══════════════
╞☪ .cek grup [@]
╞☪ .ginfo: [Nomer]
╞☪ .listmem: [Nomer]
╞☪ .ig: [Nama] 
╞☪ .jumlah: [Angka]
╞☪ .spamtag [@]
╞☪ .cek date: [Tgl-bln-thn]
╞☪ .searchid [IDLine]
╞☪ .broadcast: [Text]
╞☪ .mp3: [Penyanyi - judul]
╞☪ .video: [Penyanyi - judul]
╞☪ .cek cuaca: [Nama kota]
╞☪ .jadwal sholat [Nama kota]
╰═══════════════
"""
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
    "Limit": 5,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"Masuk kuy awas dingin",
    "Respontag":"Njirrr tag pc napa",
    "welcome":"Wellcome to",
    "comment":"Like By : 【さัএπัஞ✵ບิथℓℓҨतΩ】",
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

#with open('creator.json', 'r') as fp:
    #creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
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
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
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
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
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
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def addMembers(to, mid):
    try:
        arrData = ""
        textx = "Total User「{}」\nHello  ".format(str(len(mid)))
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
            textx += mention+wait["message"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if km.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            km.reissueGroupTicket(op.param1)
                                            X = km.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            km.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kb.reissueGroupTicket(op.param1)
                                                X = kb.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                kb.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        km.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        km.leaveGroup(op.param1)
                    else:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        km.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	kb.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1, wait["message"])
                        cl.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
                        ki.sendText(op.param1, wait["message"])
                        ki.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
                        kk.sendText(op.param1, wait["message"])
                        kk.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
                        kc.sendText(op.param1, wait["message"])
                        kc.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
                        km.sendText(op.param1, wait["message"])
                        km.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
                        kb.sendText(op.param1, wait["message"])
                        kb.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                km.kickoutFromGroup(op.param1,[op.param2])
                                km.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            km.kickoutFromGroup(op.param1,[op.param2])
                            km.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return 

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        km.kickoutFromGroup(op.param1,[op.param2])
                        km.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = km.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                    km.updateGroup(G)
                                    Ticket = km.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = km.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    km.updateGroup(G)
                                    Ticket = km.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        km.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            km.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                km.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        km.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            km.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            km.kickoutFromGroup(op.param1,[op.param2])
                                            km.inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if op.param1 in Setmain["RAreadPoint"]:
                if op.param2 in Setmain["RAreadMember"][op.param1]:
                    pass
                else:
                    Setmain["RAreadMember"][op.param1][op.param2] = True
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                        siderMembers(op.param1, [op.param2])

        if op.type == 26:
           msg = op.message
           if msg.to in Setmain["RAreadPoint"]:
               if msg._from in Setmain["RAreadMember"][msg.to]:
                   pass
               else:
                   Setmain["RAreadMember"][msg.to][msg._from] = True
           else:
               pass

        if op.type == 25:
           msg = op.message
           text = msg.text
           msg_id = msg.id
           receiver = msg.to
           sender = msg._from
           if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                   to = sender
               elif msg.toType == 2:
                   to = receiver
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
                        if mention ['M'] in admin:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"7839705","STKPKGID":"1192862","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Jangan tag saya....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
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
                        cl.sendMessage(msg.to,"۞➢ Nama : " + msg.contentMetadata["displayName"] + "\n۞➢ MID : " + msg.contentMetadata["mid"] + "\n۞➢ Status Msg : " + contact.statusMessage + "\n۞➢ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in Saints:
                   if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"succes")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"succes")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"succes")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"succes")
#ADD STAFF
                 if msg._from in Saints:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"succes")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"succes add staff\nplease check stafflist")
                  if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"succes")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact no staff")
#ADD ADMIN
                 if msg._from in Saints:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"succes add admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"succes add admin\nplease chek listadmin ")
                  if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"succes")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact no admin")
#ADD BLACKLIST
                 if msg._from in Saints:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact list blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"succes add blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"succes delete blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact no list blacklist")
#TALKBAN
                 if msg._from in Saints:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact list Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"succes add Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"succes dellete Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact no list Talkban")
#UPDATE FOTO
               if msg.toType == 2:
                 if msg._from in Saints:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "succes change pic group")
               if msg.contentType == 1:
                 if msg._from in Saints:
                   if settings["Picture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["Picture"] = False
                     cl.updateProfilePicture(path)
                     cl.sendMessage(msg.to, "succes channge profile")
               if msg.contentType == 1:
                 if msg._from in Saints:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = km.downloadObjectMsg(msg_id)
                     path5 = kb.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "succes change pic")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "succes change pic")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "succes change pic")
                     km.updateProfilePicture(path4)
                     km.sendMessage(msg.to, "succes change pic")
                     kb.updateProfilePicture(path5)
                     kb.sendMessage(msg.to, "succes change pic")
               if text is None:
                   return
               elif msg.text.lower() == "help":
                 if msg._from in owner or msg._from in admin or msg._from in group:
                     cl.sendMessage(msg.to, helpMessage)
                     cl.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
               elif msg.text.lower() == "help2":
                 if msg._from in owner or msg._from in admin or msg._from in group:
                     cl.sendMessage(msg.to, setowner)
                     cl.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
               elif msg.text.lower() == "help3":
                 if msg._from in owner or msg._from in admin or msg._from in group:
                     cl.sendMessage(msg.to, setadmin)
                     cl.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
               elif "Mid" == msg.text:
                   cl.sendMessage(msg.to, msg._from)
               elif ("Mid " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
               elif text.lower() == 'informasi':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                    name_ = cl.getContact(mid).displayName
                    foto_ = cl.getContact(mid).picturePath
                    mid_ = cl.getContact(mid).mid
                    msg_ = cl.getContact(mid).statusMessage
                    eltime = time.time() - mulai
                    bot = " Allways on " +waktu(eltime)
                    cl.sendMessage(msg.to, '۞➢ Nama : '+name_+'\n۞➢ MID : '+mid_+'\n۞➢ Runtime : '+bot+'\n۞➢ Status Msg : '+msg_+'\n۞➢ Picture : http://dl.profile.line.naver.jp'+foto_)
                    if "videoProfile='{" in str(cl.getContact(mid)):
                        cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+foto_+'/vp.small')
                    else:
                        cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+foto_)
               elif text.lower() == 'status':
                 if msg._from in owner or msg._from in admin or msg._from in group:
                   md = "╭══════╬╬══════╮\n╞☪ sᴇᴛᴛɪɴɢ ᴘʀᴏ ʙᴏᴛ\n╰══════╬╬══════╯\n╭══════╬╬══════╮\n"
                   if wait["sticker"] == True: md+="╞☪ Sticker「⚫」\n"
                   else: md+="╞☪ Sticker「⚪」\n"
                   if wait["contact"] == True: md+="╞☪ Contact「⚫」\n"
                   else: md+="╞☪ Contact「⚪」\n"
                   if wait["talkban"] == True: md+="╞☪ Talkban「⚫」\n"
                   else: md+="╞☪ Talkban「⚪」\n"
                   if wait["Mentionkick"] == True: md+="╞☪ No tag「⚫」\n"
                   else: md+="╞☪ No tag「⚪」\n"
                   if msg.to in protectkick: md+="╞☪ No kick「⚫」\n"
                   else: md+="╞☪ No kick「⚪」\n"
                   if msg.to in protectjoin: md+="╞☪ No join「⚫」\n"
                   else: md+="╞☪ No join「⚪」\n"
                   if msg.to in protectqr: md+="╞☪ Block url「⚫」\n"
                   else: md+="╞☪ Block url「⚪」\n"
                   if msg.to in protectcancel: md+="╞☪ No cancel「⚫」\n"
                   else: md+="╞☪ No cancel「⚪」\n"
                   if msg.to in welcome: md+="╞☪ Welcome「⚫」\n"
                   else: md+="╞☪ Welcome「⚪」\n"
                   if wait["autoJoin"] == True: md+="╞☪ Autojoin「⚫」\n"
                   else: md+="╞☪ Autojoin「⚪」\n"
                   if wait["autoAdd"] == True: md+="╞☪ Autoadd「⚫」\n"
                   else: md+="╞☪ Autoadd「⚪」\n"
                   if wait["autoLeave"] == True: md+="╞☪ Autoleave「⚫」\n"
                   else: md+="╞☪ Autoleave「⚪」\n"
                   if wait["detectMention"] == True: md+="╞☪ Autorespon「⚫」"
                   else: md+="╞☪ Autorespon「⚪」\n╰══════╬╬══════╯\n╭══════╬╬══════╮\n╞☪ sᴇᴛᴛɪɴɢ ᴘʀᴏᴛeᴄᴛɪᴏɴ\n╰══════╬╬══════╯"
                   cl.sendMessage(msg.to, md)
                   cl.sendContact(op.param1, "u4862fe4b182b2fd194a3108e2f3662e8")
               elif text.lower() == 'listpro':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ma = ""
                   a = 0
                   mb = ""
                   b = 0
                   mc = ""
                   c = 0
                   md = ""
                   d = 0
                   gid = protectqr
                   for group in gid:
                       G = cl.getGroup(group)
                       a = a + 1
                       end = "\n"
                       ma += str(a) + ". " +G.name+ "\n"
                   gid = protectkick
                   for group in gid:
                       G = cl.getGroup(group)
                       b = b + 1
                       end = "\n"
                       mb += str(b) + ". " +G.name+ "\n"
                   gid = protectjoin
                   for group in gid:
                       G = cl.getGroup(group)
                       c = c + 1
                       end = "\n"
                       mc += str(c) + ". " +G.name+ "\n"
                   gid = protectcancel
                   for group in gid:
                       G = cl.getGroup(group)
                       d = d + 1
                       end = "\n"
                       md += str(d) + ". " +G.name+ "\n"
                   cl.sendMessage(msg.to,"[ LIST PROTECTION ]\n\n [ PROTECT URL : ]\n"+ma+"\n [ PROTECT KICK : ]\n"+mb+"\n [ PROTECT JOIN : ]\n"+mc+"\n  [ PROTECT CANCEL : ]\n"+md)
               elif text.lower() == "adminlist":
                       if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"[ LIST ADMIN ]\n\n Owner:\n"+ma+"\n Admin:\n"+mb+"\n Staff:\n"+mc+"\n「%s」TΣΔM SLΔCҜβΩT" %(str(len(owner)+len(admin)+len(staff))))
               elif text.lower() == 'creator':
                 if msg._from in Saints:
                   if creator == []:
                        cl.sendMessage(msg.to,"Kosong")
                   else:
                        cl.sendMessage(msg.to, "【さัএπัஞ✵ບิथℓℓҨतΩ】")
                        h = ""
                        for i in creator:
                             h = cl.getContact(i)
                             cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
               elif text.lower() == 'friendlist':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ma = ""
                   a = 0
                   gid = cl.getAllContactIds()
                   for i in gid:
                       G = cl.getContact(i)
                       a = a + 1
                       end = "\n"
                       ma += str(a) + ". " +G.displayName+ "\n"
                   cl.sendMessage(msg.to,"۞➢ [ LIST FRIEND ]\n\n"+ma+"\n۞➢Total Friend「"+str(len(gid))+"」")
               elif text.lower() == 'glist':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ma = ""
                   a = 0
                   gid = cl.getGroupIdsJoined()
                   for i in gid:
                       G = cl.getGroup(i)
                       a = a + 1
                       end = "\n"
                       ma += "╠ " + str(a) + ". " +G.name+ "\n"
                   cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
               elif text.lower() == 'glist1':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ma = ""
                   a = 0
                   gid = ki.getGroupIdsJoined()
                   for i in gid:
                       G = ki.getGroup(i)
                       a = a + 1
                       end = "\n"
                       ma += "╠ " + str(a) + ". " +G.name+ "\n"
                   ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
               elif text.lower() == 'glist2':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ma = ""
                   a = 0
                   gid = kk.getGroupIdsJoined()
                   for i in gid:
                       G = kk.getGroup(i)
                       a = a + 1
                       end = "\n"
                       ma += "╠ " + str(a) + ". " +G.name+ "\n"
                   kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
               elif text.lower() == 'glist3':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ma = ""
                   a = 0
                   gid = kc.getGroupIdsJoined()
                   for i in gid:
                       G = kc.getGroup(i)
                       a = a + 1
                       end = "\n"
                       ma += "╠ " + str(a) + ". " +G.name+ "\n"
                   kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
               elif text.lower() == 'glist4':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ma = ""
                   a = 0
                   gid = km.getGroupIdsJoined()
                   for i in gid:
                       G = kc.getGroup(i)
                       a = a + 1
                       end = "\n"
                       ma += "╠ " + str(a) + ". " +G.name+ "\n"
                   km.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
               elif text.lower() == 'glist5':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ma = ""
                   a = 0
                   gid = kb.getGroupIdsJoined()
                   for i in gid:
                       G = kb.getGroup(i)
                       a = a + 1
                       end = "\n"
                       ma += "╠ " + str(a) + ". " +G.name+ "\n"
                   kb.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
               elif text.lower() == 'grup list':
                    if msg._from in owner or msg._from in admin or msg._from in staff:
                            groups = cl.getGroupIdsJoined()
                            ret_ = "╔══[ Group List ]\n║"
                            no = 0
                            for gid in groups:
                                group = cl.getGroup(gid)
                                ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n║\n╚══[ Total {} Groups ]".format(str(len(groups)))
                            cl.sendMessage(to, str(ret_))
               elif ".ginfo: " in text.lower():
                    if msg._from in owner or msg._from in admin or msg._from in staff:
                            separate = text.split(":")
                            number = text.replace(separate[0] + ":","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Error"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Nothing"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "۞➢[ lIST GRUP INFO ]\n"
                                ret_ += "\n۞➢ Nama Group : {}".format(G.name)
                                ret_ += "\n۞➢ ID Group : {}".format(G.id)
                                ret_ += "\n۞➢ Pembuat : {}".format(gCreator)
                                ret_ += "\n۞➢ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n۞➢ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n۞➢ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n۞➢ Group Qr : {}".format(gQr)
                                ret_ += "\n۞➢ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass
               elif ".listmem: " in text.lower():
                    if msg._from in owner or msg._from in admin or msg._from in staff:
                            separate = msg.text.split(":")
                            number = msg.text.replace(separate[0] + ":","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"۞➢Group Name : [ " + str(G.name) + " ]\n\n۞➢   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass
               elif msg.text.lower() == "group upicture":
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if msg.toType == 2:
                    settings["groupPicture"] = True
                    cl.sendMessage(msg.to, "Send pict")
               elif msg.text.lower() == 'bot upicture':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                    settings["changePicture"] = True
                    cl.sendMessage(msg.to, "Send pict")
               elif msg.text.lower() == 'me upicture':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                    settings["Picture"] = True
                    cl.sendMessage(msg.to, "Send pict")
               elif msg.text.lower() == 'kiss':
                     if msg._from in admin:
                            if msg.toType == 0:
                                mentionMembers(to, to)
                            elif msg.toType == 2:
                                group = cl.getGroup(to)
                                contact = [mem.mid for mem in group.members]
                                mentionMembers(to, contact)
               elif msg.text.lower() == 'kiss':
                     if msg._from in admin:
                            if msg.toType == 0:
                                mentionMembers(to, to)
                            elif msg.toType == 2:
                                group = cl.getGroup(to)
                                contact = [mem.mid for mem in group.members]
                                mentionMembers(to, contact)
               elif cmd == "tagall":
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

               elif 'allprotect ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   spl = msg.text.replace('Mode protection ','')
                   if spl == 'on':
                      if msg.to in protectqr:
                           msgs = ""
                      else:
                           protectqr.append(msg.to)
                      if msg.to in protectkick:
                           msgs = ""
                      else:
                           protectkick.append(msg.to)
                      if msg.to in protectcancel:
                           msgs = ""
                      else:
                           protectcancel.append(msg.to)
                      if msg.to in protectjoin:
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Allprotection Mode on\n Group : " +str(ginfo.name)
                      else:
                           protectjoin.append(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Succes Mode on Allprotection\n Group : " +str(ginfo.name)
                      cl.sendMessage(msg.to, "「ENABLE」\n" + msgs)
                   elif spl == 'off':
                        if msg.to in protectqr:
                           protectqr.remove(msg.to)
                        else:
                           msgs = ""
                        if msg.to in protectkick:
                           protectkick.remove(msg.to)
                        else:
                           msgs = ""
                        if msg.to in protectcancel:
                           protectcancel.remove(msg.to)
                        else:
                           msgs = ""
                        if msg.to in protectjoin:
                           protectjoin.remove(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Succes Mode Off Allprotection\n Group : " +str(ginfo.name)
                        else:
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Allprotection succes Mode off\n Group : " +str(ginfo.name)
                        cl.sendMessage(msg.to, "「DISABLE」\n" + msgs)
               elif 'Welcome ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   spl = msg.text.replace('Welcome ','')
                   if spl == 'on':
                      if msg.to in welcome:
                           msgs = "Wellcome Allready on"
                      else:
                           welcome.append(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Wellcome mode on grup " +str(ginfo.name)
                      cl.sendMessage(msg.to, "「Massage Welcome」\n" + msgs)
                   elif spl == 'off':
                        if msg.to in welcome:
                           welcome.remove(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Massage wellvom mode off grup " +str(ginfo.name)
                        else:
                           msgs = "Massage wellcome succes mode off "
                        cl.sendMessage(msg.to, "「Massage Welcome」\n" + msgs)
               elif 'Block url ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   spl = msg.text.replace('Block url ','')
                   if spl == 'on':
                      if msg.to in protectqr:
                           msgs = "Protect URL already on"
                      else:
                           protectqr.append(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Protect URL set on in " +str(ginfo.name)
                      cl.sendMessage(msg.to, "「Protect URL」\n" + msgs)
                   elif spl == 'off':
                        if msg.to in protectqr:
                           protectqr.remove(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Protect URL set off in " +str(ginfo.name)
                        else:
                           msgs = "Protect URL already off"
                        cl.sendMessage(msg.to, "「Protect URL」\n" + msgs)
               elif 'Nkick ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   spl = msg.text.replace('No kick ','')
                   if spl == 'on':
                       if msg.to in protectkick:
                           msgs = "Protect Kick already on"
                       else:
                           protectkick.append(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Protect Kick set on in " +str(ginfo.name)
                       cl.sendMessage(msg.to, "「Protect Kick」\n" + msgs)
                   elif spl == 'off':
                       if msg.to in protectkick:
                           protectkick.remove(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Protect Kick set off in " +str(ginfo.name)
                       else:
                           msgs = "Protect Kick already off"
                       cl.sendMessage(msg.to, "「Protect Kick」\n" + msgs)
               elif 'Njoin ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   spl = msg.text.replace('No join ','')
                   if spl == 'on':
                       if msg.to in protectjoin:
                           msgs = "Protect Join already on"
                       else:
                           protectjoin.append(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Protect Join set on in " +str(ginfo.name)
                       cl.sendMessage(msg.to, "「Protect Join」\n" + msgs)
                   elif spl == 'off':
                       if msg.to in protectjoin:
                           protectjoin.remove(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Protect Join set off in " +str(ginfo.name)
                       else:
                           msgs = "Protect Join already off"
                       cl.sendMessage(msg.to, "「Protect Join」\n" + msgs)
               elif 'Ncancel ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   spl = msg.text.replace('No cancel ','')
                   if spl == 'on':
                       if msg.to in protectcancel:
                           msgs = "Protect cancel already on"
                       else:
                           protectcancel.append(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Protect cancel set on in " +str(ginfo.name)
                       cl.sendMessage(msg.to, "「Protect Cancel」\n" + msgs)
                   elif spl == 'off':
                       if msg.to in protectcancel:
                           protectcancel.remove(msg.to)
                           ginfo = cl.getGroup(msg.to)
                           msgs = "Protect cancel set off in " +str(ginfo.name)
                       else:
                           msgs = "Protect cancel already off"
                       cl.sendMessage(msg.to, "「Protect Cancel」\n" + msgs)
               elif 'Sider on' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   try:
                       cl.sendMessage(msg.to, "Sider check mode on")
                       del cctv['point'][msg.to]
                       del cctv['sidermem'][msg.to]
                       del cctv['cyduk'][msg.to]
                   except:
                       pass
                   cctv['point'][msg.to] = msg.id
                   cctv['sidermem'][msg.to] = ""
                   cctv['cyduk'][msg.to]=True
               elif 'Sider off' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if msg.to in cctv['point']:
                       cctv['cyduk'][msg.to]=False
                       cl.sendMessage(msg.to, "Sider check mode off")
                   else:
                       cl.sendMessage(msg.to, "Check sider allways off")
               elif '.cek cuaca: ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                            separate = text.split(":")
                            location = text.replace(separate[0] + ":","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "۞➢ Location : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n۞➢ Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n۞➢ Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n۞➢ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n۞➢ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\n۞➢Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n۞➢Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))
               elif '.jadwal sholat ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
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
                           ret_ = "۞➢「Jadwal Sholat」"
                           ret_ += "\n۞➢ Lokasi : " + data[0]
                           ret_ += "\n۞➢ " + data[1]
                           ret_ += "\n۞➢ " + data[2]
                           ret_ += "\n۞➢ " + data[3]
                           ret_ += "\n۞➢ " + data[4]
                           ret_ += "\n۞➢ " + data[5]
                           ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                           ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                       cl.sendMessage(msg.to, str(ret_))
               elif '.cek date: ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to, "۞➢ Lahir tanggal : "+lahir+"\n۞➢ Umurnya : "+usia+"\n◆ Ultah : "+ultah+"\n۞➢ Zodiak : "+zodiak)
               elif '.video: ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   try:
                       textToSearch = (msg.text).replace('Yt-video: ', "").strip()
                       query = urllib.parse.quote(textToSearch)
                       url = "https://www.youtube.com/results?search_query=" + query
                       response = urllib.request.urlopen(url)
                       html = response.read()
                       soup = BeautifulSoup(html, "html.parser")
                       results = soup.find(attrs={'class':'yt-uix-tile-link'})
                       dl=('https://www.youtube.com' + results['href'])
                       vid = pafy.new(dl)
                       stream = vid.streams
                       for s in stream:
                           start = timeit.timeit()
                           vin = s.url
                           hasil = vid.title
                           hasil += '\n\n۞➢Penulis : ' + str(vid.author)
                           hasil += '\n۞➢Durasi : ' + str(vid.duration) +' (' +s.quality+ ') '
                           hasil += '\n۞➢Rating : ' + str(vid.rating)
                           hasil += '\n۞➢Ditonton : ' + str(vid.viewcount)+ 'x '
                           hasil += '\n۞➢Diterbitkan : ' + vid.published
                           hasil += '\n۞➢Time Taken : %s' % (start)
                           hasil += '\n\n۞➢Tunggu beberapa saat\nVideo sedang di proses...'
                       cl.sendMessage(msg.to,hasil)
                       cl.sendVideoWithURL(msg.to,vin)
                       cl.sendMessage(msg.to, "Wait encoding proses")
                   except Exception as e:
                       cl.sendMessage(msg.to,str(e))
               elif '.mp3: ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   try:
                       textToSearch = (msg.text).replace('Yt-mp3: ', "").strip()
                       query = urllib.parse.quote(textToSearch)
                       url = "https://www.youtube.com/results?search_query=" + query
                       response = urllib.request.urlopen(url)
                       html = response.read()
                       soup = BeautifulSoup(html, "html.parser")
                       results = soup.find(attrs={'class':'yt-uix-tile-link'})
                       dl=('https://www.youtube.com' + results['href'])
                       vid = pafy.new(dl)
                       stream = vid.streams
                       for s in stream:
                           start = timeit.timeit()
                           vin = s.url
                           hasil = vid.title
                           hasil += '\n\n۞➢Penulis : ' + str(vid.author)
                           hasil += '\n۞➢Durasi : ' + str(vid.duration) +' (' +s.quality+ ') '
                           hasil += '\n۞➢Rating : ' + str(vid.rating)
                           hasil += '\n۞➢Ditonton : ' + str(vid.viewcount)+ 'x '
                           hasil += '\n۞➢Diterbitkan : ' + vid.published
                           hasil += '\n۞➢Time Taken : %s' % (start)
                           hasil += '\n\n۞➢Tunggu beberapa saat\nAudio & Video sedang di proses...'
                       cl.sendMessage(msg.to,hasil)
                       cl.sendVideoWithURL(msg.to,vin)
                       cl.sendAudioWithURL(msg.to,vin)
                       cl.sendMessage(msg.to, "Wait encoding proses....")
                   except Exception as e:
                       cl.sendMessage(msg.to,str(e))
               elif 'Like ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   try:
                       typel = [1001,1002,1003,1004,1005,1006]
                       key = eval(msg.contentMetadata["MENTION"])
                       u = key["MENTIONEES"][0]["M"]
                       a = cl.getContact(u).mid
                       s = cl.getContact(u).displayName
                       hasil = channel.getHomeProfile(mid=a)
                       st = hasil['result']['feeds']
                       for i in range(len(st)):
                           test = st[i]
                           result = test['post']['postInfo']['postId']
                           channel.like(str(sender), str(result), likeType=random.choice(typel))
                           channel.comment(str(sender), str(result), str(wait["comment"]))
                       cl.sendMessage(msg.to, 'Like & Commant succes '+str(len(st))+' Post From ' + str(s))
                   except Exception as e:
                       cl.sendMessage(msg.to, str(e))
               elif 'Info ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   try:
                       key = eval(msg.contentMetadata["MENTION"])
                       u = key["MENTIONEES"][0]["M"]
                       cname = cl.getContact(u).displayName
                       cmid = cl.getContact(u).mid
                       cstatus = cl.getContact(u).statusMessage
                       cpic = cl.getContact(u).picturePath
                       #print(str(a))
                       cl.sendMessage(msg.to, '۞➢Nama : '+cname+'\n۞➢MID : '+cmid+'\n۞➢Status Msg : '+cstatus+'\n۞➢Picture : http://dl.profile.line.naver.jp'+cpic)
                       cl.sendMessage(msg.to, None, contentMetadata={'mid': cmid}, contentType=13)
                       if "videoProfile='{" in str(cl.getContact(u)):
                           cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                       else:
                           cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+cpic)
                   except Exception as e:
                       cl.sendMessage(msg.to, str(e))
               elif text.lower() == 'ginfo':
                 if msg._from in owner or msg._from in admin or msg._from in group:
                   try:
                       cname = cl.getGroup(msg.to)
                       cpic = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gCreator = ginfo.creator.displayName
                       if ginfo.preventedJoinByTicket == False:
                           gQr = "Opened"
                       else:
                           gQr = "Closed"
                           grup = cl.getGroup(msg.to)
                           if grup.invitee is None:
                               sinvitee = "No Panding"
                           else:
                               sinvitee = str(len(grup.invitee))
                           #print(str(a))
                           cl.sendMessage(msg.to, '۞➢ Nama : '+str(cname.name)+'\n۞➢ Grup ID : '+msg.to+'\n۞➢ Creator group : '+gCreator+'\n۞➢ Status URL : '+str(gQr)+'\n۞➢ Status pendingan : '+str(sinvitee)+'\n۞➢ Picture : http://dl.profile.line-cdn.net'+str(cpic.pictureStatus))
                           cl.sendMessage(msg.to, None, contentMetadata={'mid': ginfo.creator.mid}, contentType=13)
                           cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+cpic.pictureStatus)
                   except Exception as e:
                       cl.sendMessage(msg.to, str(e))
               elif text.lower() == 'open':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                  if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                   X.preventedJoinByTicket = False
                   cl.updateGroup(X)
                   cl.sendMessage(msg.to, "Url Opened")
               elif text.lower() == 'close':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                  if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                   X.preventedJoinByTicket = True
                   cl.updateGroup(X)
                   cl.sendMessage(msg.to, "Url Closed")
               elif text.lower() == 'url':
                 if msg._from in owner or msg._from in admin or msg._from in group:
                  if msg.toType == 2:
                   x = cl.getGroup(msg.to)
                   ginfo = cl.getGroup(msg.to)
                   if x.preventedJoinByTicket == True:
                      x.preventedJoinByTicket = False
                      cl.updateGroup(x)
                   gurl = cl.reissueGroupTicket(msg.to)
                   cl.sendMessage(msg.to,"Nama grup : " + str(ginfo.name) + "\nUrl Group : line://ti/g/" + gurl)
#===================BOT NAME====================#
               elif "Myname: " in msg.text:
                    if msg._from in admin:
                        string = msg.text.replace("Myname: ","")
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Update name " + string + " done")
               elif "B1: " in msg.text:
                    if msg._from in admin:
                        string = msg.text.replace("B1: ","")
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"Update name " + string + " done")
               elif "B2: " in msg.text:
                    if msg._from in admin:
                        string = msg.text.replace("B2: ","")
                        profile = kk.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        kk.sendText(msg.to,"Update name " + string + " done")
               elif "B3: " in msg.text:
                    if msg._from in admin:
                        string = msg.text.replace("B3: ","")
                        profile = kc.getProfile()
                        profile.displayName = string
                        kc.updateProfile(profile)
                        kc.sendText(msg.to,"Update name " + string + " done")
               elif "B4: " in msg.text:
                    if msg._from in admin:
                        string = msg.text.replace("B4: ","")
                        profile = km.getProfile()
                        profile.displayName = string
                        km.updateProfile(profile)
                        km.sendText(msg.to,"Update name " + string + " done")
               elif "B5: " in msg.text:
                    if msg._from in admin:
                        string = msg.text.replace("B5: ","")
                        profile = kb.getProfile()
                        profile.displayName = string
                        kb.updateProfile(profile)
                        kb.sendText(msg.to,"Update name " + string + " done")
#===================BOT NAME====================#
               elif "/ti/g/" in msg.text.lower():
                 if msg._from in owner or msg._from in admin or msg._from in group:
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
                        cl.sendMessage(msg.to, "Succes : %s" % str(group.name))
                        group1 = ki.findGroupByTicket(ticket_id)
                        ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                        ki.sendMessage(msg.to, "Succes : %s" % str(group.name))
                        group2 = kk.findGroupByTicket(ticket_id)
                        kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                        kk.sendMessage(msg.to, "Succes : %s" % str(group.name))
                        group3 = kc.findGroupByTicket(ticket_id)
                        kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                        kc.sendMessage(msg.to, "Succes : %s" % str(group.name))
                        group4 = km.findGroupByTicket(ticket_id)
                        km.acceptGroupInvitationByTicket(group4.id,ticket_id)
                        km.sendMessage(msg.to, "Succes : %s" % str(group.name))
                        group5 = kb.findGroupByTicket(ticket_id)
                        kb.acceptGroupInvitationByTicket(group5.id,ticket_id)
                        kb.sendMessage(msg.to, "Succes : %s" % str(group.name))
               elif 'Sticker: ' in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   try:
                       query = msg.text.replace("Sticker: ", "")
                       query = int(query)
                       if type(query) == int:
                           cl.sendImageWithURL(msg.to, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                           cl.sendMessage(msg.to, 'https://line.me/S/sticker/'+str(query))
                       else:
                           cl.sendMessage(msg.to, 'Pakai key sticker angka bukan huruf')
                   except Exception as e:
                       cl.sendMessage(msg.to, str(e))
               elif ".searchid " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   msgs = msg.text.replace(".searchid ","")
                   conn = cl.findContactsByUserid(msgs)
                   if True:
                       cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                       cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
               elif "Gift: " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in group:
                   korban = msg.text.replace("Gift: ","")
                   korban2 = korban.split()
                   midd = korban2[0]
                   jumlah = int(korban2[1])
                   if jumlah <= 1000:
                       for var in range(0,jumlah):
                            cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                            ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                            kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                            kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                            km.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                            kb.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
               elif "Spam: " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in group:
                   korban = msg.text.replace("Spam: ","")
                   korban2 = korban.split()
                   midd = korban2[0]
                   jumlah = int(korban2[1])
                   if jumlah <= 1000:
                       for var in range(0,jumlah):
                           ki.sendMessage(midd,str(Setmain["RAmessage1"]))
                           kk.sendMessage(midd,str(Setmain["RAmessage1"]))
                           kc.sendMessage(midd,str(Setmain["RAmessage1"]))
                           km.sendMessage(midd,str(Setmain["RAmessage1"]))
                           kb.sendMessage(midd,str(Setmain["RAmessage1"]))
               elif text.lower() == 'crash':
                 if msg._from in Saints:
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': "12345,'"}, contentType=13)
               elif text.lower() == 'me':
                 if msg._from in owner or msg._from in admin or msg._from in group:
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': sender}, contentType=13)
               elif text.lower() == 'mybot':
                 if msg._from in owner or msg._from in admin or msg._from in group:
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': Amid}, contentType=13)
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': Bmid}, contentType=13)
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': Cmid}, contentType=13)
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': Dmid}, contentType=13)
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': Emid}, contentType=13)
                   cl.sendMessage(msg.to, None, contentMetadata={'mid': Zmid}, contentType=13)
               elif text.lower() == 'responsename':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ki.sendMessage(msg.to,responsename1)
                   kk.sendMessage(msg.to,responsename2)
                   kc.sendMessage(msg.to,responsename3)
                   km.sendMessage(msg.to,responsename4)
                   kb.sendMessage(msg.to,responsename5)
               elif text.lower() == 'leave all':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   gid = cl.getGroupIdsJoined()
                   gid = ki.getGroupIdsJoined()
                   gid = kk.getGroupIdsJoined()
                   gid = kc.getGroupIdsJoined()
                   gid = km.getGroupIdsJoined()
                   gid = kb.getGroupIdsJoined()
                   for i in gid:
                       ki.sendMessage(i, "Sorry, SLΔCҜβΩT dipaksa keluar oleh owner\nSilahkan hubungi owner ")
                       ki.leaveGroup(i)
                       kk.leaveGroup(i)
                       kc.leaveGroup(i)
                       km.leaveGroup(i)
                       kb.leaveGroup(i)
                       cl.sendMessage(msg.to, "Bot sudah dikeluarkan dari semua grup")
               elif text.lower() == 'me leave':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ginfo = cl.getGroup(msg.to)
                   cl.sendMessage(msg.to, "Bye bye " +str(ginfo.name))
                   cl.leaveGroup(msg.to)
               elif text.lower() == 'bye':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   sw.leaveGroup(msg.to)
               elif text.lower() == 'byeall.':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   ki.sendMessage(msg.to, "Bye bye " +str(ginfo.name))
                   ki.leaveGroup(msg.to)
                   kk.leaveGroup(msg.to)
                   kc.leaveGroup(msg.to)
                   km.leaveGroup(msg.to)
                   kb.leaveGroup(msg.to)
               elif text.lower() == 'kicker':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   G = cl.getGroup(msg.to)
                   ginfo = cl.getGroup(msg.to)
                   G.preventedJoinByTicket = False
                   cl.updateGroup(G)
                   invsend = 0
                   Ticket = cl.reissueGroupTicket(msg.to)
                   cxb.acceptGroupInvitationByTicket(msg.to,Ticket)
                   G = cxb.getGroup(msg.to)
                   G.preventedJoinByTicket = True
                   cxb.updateGroup(G)
               elif text.lower() == 'x1':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   G = cl.getGroup(msg.to)
                   ginfo = cl.getGroup(msg.to)
                   G.preventedJoinByTicket = False
                   cl.updateGroup(G)
                   invsend = 0
                   Ticket = cl.reissueGroupTicket(msg.to)
                   ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                   G = ki.getGroup(msg.to)
                   G.preventedJoinByTicket = True
                   ki.updateGroup(G)
               elif text.lower() == 'x2':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   G = cl.getGroup(msg.to)
                   ginfo = cl.getGroup(msg.to)
                   G.preventedJoinByTicket = False
                   cl.updateGroup(G)
                   invsend = 0
                   Ticket = cl.reissueGroupTicket(msg.to)
                   kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                   G = kk.getGroup(msg.to)
                   G.preventedJoinByTicket = True
                   kk.updateGroup(G)
               elif text.lower() == 'x3':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   G = cl.getGroup(msg.to)
                   ginfo = cl.getGroup(msg.to)
                   G.preventedJoinByTicket = False
                   cl.updateGroup(G)
                   invsend = 0
                   Ticket = cl.reissueGroupTicket(msg.to)
                   kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                   G = kc.getGroup(msg.to)
                   G.preventedJoinByTicket = True
                   kc.updateGroup(G)
               elif text.lower() == 'x4':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   G = cl.getGroup(msg.to)
                   ginfo = cl.getGroup(msg.to)
                   G.preventedJoinByTicket = False
                   cl.updateGroup(G)
                   invsend = 0
                   Ticket = cl.reissueGroupTicket(msg.to)
                   km.acceptGroupInvitationByTicket(msg.to,Ticket)
                   G = km.getGroup(msg.to)
                   G.preventedJoinByTicket = True
                   km.updateGroup(G)
               elif text.lower() == 'x5':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   G = cl.getGroup(msg.to)
                   ginfo = cl.getGroup(msg.to)
                   G.preventedJoinByTicket = False
                   cl.updateGroup(G)
                   invsend = 0
                   Ticket = cl.reissueGroupTicket(msg.to)
                   kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                   G = kb.getGroup(msg.to)
                   G.preventedJoinByTicket = True
                   kb.updateGroup(G)
               elif text.lower() == 'join':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   G = cl.getGroup(msg.to)
                   ginfo = cl.getGroup(msg.to)
                   G.preventedJoinByTicket = False
                   cl.updateGroup(G)
                   invsend = 0
                   Ticket = cl.reissueGroupTicket(msg.to)
                   ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                   kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                   kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                   km.acceptGroupInvitationByTicket(msg.to,Ticket)
                   kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                   G = kb.getGroup(msg.to)
                   G.preventedJoinByTicket = True
                   kb.updateGroup(G)
               elif text.lower() == 'mayhem':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                  if msg.toType == 2:
                   ginfo = cl.getGroup(msg.to)
                   cl.sendMessage(msg.to, "「 Mayhem 」\nMayhem Is Starting♪\n abort to abort♪")
                   cl.sendMessage(msg.to, "「 Mayhem 」\nmember : " +str(len(ginfo.members)) + " \nSave m pict your grup")
                   G = cl.getGroup(msg.to)
                   ginfo = cl.getGroup(msg.to)
                   G.preventedJoinByTicket = False
                   cl.updateGroup(G)
                   invsend = 0
                   Ticket = cl.reissueGroupTicket(msg.to)
                   ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                   kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                   kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                   km.acceptGroupInvitationByTicket(msg.to,Ticket)
                   kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                   _name = text.lower().replace('mayhem','')
                   gs = ki.getGroup(msg.to)
                   gs = kk.getGroup(msg.to)
                   gs = kc.getGroup(msg.to)
                   gs = km.getGroup(msg.to)
                   gs = kb.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                   if targets == []:
                       cl.sendMessage(msg.to, "Nothing member")
                   else:
                       for target in targets:
                         if target not in Bots or target not in owner or target not in admin or target not in staff:
                             try:
                                  random.choice(ABC).kickoutFromGroup(msg.to,[target])
                                  G = cl.getGroup(msg.to)
                                  G.preventedJoinByTicket = True
                                  cl.updateGroup(G)
                                  G.preventedJoinByTicket(G)
                                  cl.updateGroup(G)
                             except:
                                  pass
               elif text.lower() == 'responsp':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "۞➢[ ResponSpeed ]\n\n - ۞➢Speed Profile\n   %.10f\n - ۞➢Speed Contact\n   %.10f\n - ۞➢Speed Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))
               elif text.lower() == 'sp':
                 if msg._from in owner or msg._from in admin or msg._from in group:
                    speed = "0.00072476863861083984 Detik","0.00066165924072265625 Detik","0.0006737709045410156 Detik","0.0005425930023193359 Detik","0.006354093551635742 Detik","0.00064165592193603516 Detik","0.000640559196472168 Detik","0.0007369041442871094 Detik","0.0017087697982788086 Detik","0.00075762271881103516 Detik","0.00069200992584228516 Detik","0.0011708498001098633 Detik"
                    text = random.choice(speed)
                    cl.sendMessage(msg.to, "Proges speed...")
                    cl.sendMessage(msg.to, str(text))
               elif text.lower() == 'speed':
                 if msg._from in owner or msg._from in admin or msg._from in group:
                    speed = "0.00072476863861083984 Detik","0.00066165924072265625 Detik","0.0006737709045410156 Detik","0.0005425930023193359 Detik","0.0006354093551635742 Detik","0.00064165592193603516 Detik","0.000640559196472168 Detik","0.0007369041442871094 Detik","0.0017087697982788086 Detik","0.00075762271881103516 Detik","0.00069200992584228516 Detik","0.0011708498001098633 Detik"
                    text = random.choice(speed)
                    cl.sendMessage(msg.to, "Progres speed...")
                    cl.sendMessage(msg.to, str(text))
               elif text.lower() == 'spb':
                 if msg._from in owner or msg._from in admin or msg._from in group:
                    speed = "0.00072476863861083984 Detik","0.00066165924072265625 Detik","0.0006737709045410156 Detik","0.0005425930023193359 Detik","0.0006354093551635742 Detik","0.00064165592193603516 Detik","0.000640559196472168 Detik","0.0007369041442871094 Detik","0.0017087697982788086 Detik","0.00075762271881103516 Detik","0.00069200992584228516 Detik","0.011708498001098633 Detik","0.0006253678219877442 Detik","0.0007625273849272546 Detik","0.0086472849755484988 Detik","0.00067263637228007213 Detik","0.001087462546489230 Detik","0.000673728994432870 Detik","0.000609286451538291 Detik","0.001087462684911508 Detik"
                    speed1 = "0.0007153511047363281 Detik","0.0007079362869262695 Detik","0.0075762271881103516 Detik","0.0069200992584228516 Detik","0.00862581973667200 Detik","0.007203102111816406 Detik","0.008542300881153976 Detik","0.007643579108376799 Detik","0.006739908765524177 Detik","0.007546262829033837 Detik","0.017087697982788086 Detik","0.019716978073120117 Detik","0.0072476863861083984 Detik","0.0066165924072265625 Detik","0.006737709045410156 Detik","0.005425930023193359 Detik","0.006354093551635742 Detik","0.0064165592193603516 Detik","0.00640559196472168 Detik","0.007369041442871094 Detik","0.017087697982788086 Detik","0.0075762271881103516 Detik","0.0069200992584228516 Detik","0.011708498001098633 Detik"
                    speed2 = "0.006253678219877442 Detik","0.007625273849272546 Detik","0.0086472849755484988 Detik","0.0067263637228007213 Detik","0.01087462546489270 Detik","0.006737289944328470 Detik","0.006092864515382911 Detik","0.010874626849115083 Detik","0.007274839010557822 Detik","0.0072476863861083984 Detik","0.0066165924072265625 Detik","0.006737709045410156 Detik","0.005425930023193359 Detik","0.006354093551635742 Detik","0.0064165592193603516 Detik","0.00640559196472168 Detik","0.007369041442871094 Detik","0.017087697982788086 Detik","0.0075762271881103516 Detik","0.0069200992584228516 Detik","0.011708498001098633 Detik"
                    speed3 = "0.007153511047363281 Detik","0.007079362869262695 Detik","0.0075762271881103516 Detik","0.0069200992584228516 Detik","0.00862581973667200 Detik","0.007203102111816406 Detik","0.008542300881153976 Detik","0.007643579108376799 Detik","0.006739908765524177 Detik","0.007546262829033837 Detik","0.017087697982788086 Detik","0.019716978073120117 Detik","0.0072476863861083984 Detik","0.0066165924072265625 Detik","0.006737709045410156 Detik","0.005425930023193359 Detik","0.006354093551635742 Detik","0.0064165592193603516 Detik","0.00640559196472168 Detik","0.007369041442871094 Detik","0.017087697982788086 Detik","0.0075762271881103516 Detik","0.0069200992584228516 Detik","0.011708498001098633 Detik"
                    speed4 = "0.006253678219877442 Detik","0.007625273849272546 Detik","0.0086472849755484988 Detik","0.0067263637228007213 Detik","0.01087462546489270 Detik","0.006737289944328470 Detik","0.006092864515382911 Detik","0.010874626849115083 Detik","0.007274839010557822 Detik","0.0072476863861083984 Detik","0.0066165924072265625 Detik","0.006737709045410156 Detik","0.005425930023193359 Detik","0.006354093551635742 Detik","0.0064165592193603516 Detik","0.00640559196472168 Detik","0.007369041442871094 Detik","0.017087697982788086 Detik","0.0075762271881103516 Detik","0.0069200992584228516 Detik","0.011708498001098633 Detik"
                    text = random.choice(speed)
                    text1 = random.choice(speed1)
                    text2 = random.choice(speed2)
                    text3 = random.choice(speed3)
                    text4 = random.choice(speed4)
                    ki.sendMessage(msg.to, "Progres speed...")
                    ki.sendMessage(msg.to, str(text))
                    kk.sendMessage(msg.to, str(text1))
                    kc.sendMessage(msg.to, str(text2))
                    km.sendMessage(msg.to, str(text3))
                    kb.sendMessage(msg.to, str(text4))
               elif "Kick" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                    if target not in Bots:
                     try:
                         G = cl.getGroup(msg.to)
                         G.preventedJoinByTicket = False
                         cl.updateGroup(G)
                         invsend = 0
                         Ticket = cl.reissueGroupTicket(msg.to)
                         cxb.acceptGroupInvitationByTicket(msg.to,Ticket)
                         cxb.kickoutFromGroup(msg.to, [target])
                         cxb.leaveGroup(msg.to)
                         X = cl.getGroup(msg.to)
                         X.preventedJoinByTicket = True
                         cl.updateGroup(X)
                     except:
                         pass
               elif "Kamu" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                    if target not in Bots:
                     try:
                         random.choice(ABC).kickoutFromGroup(msg.to, [target])
                     except:
                        pass
               elif "Copy " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                    if target not in Bots:
                     try:
                         cl.cloneContactProfile(target)
                         cl.sendMessage(msg.to,"Succes copy")
                     except:
                        pass
               elif "Talkban " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                    if target not in Bots:
                     try:
                         wait["Talkblacklist"][target] = True
                         cl.sendMessage(msg.to,"Succes add Talkban")
                     except:
                        pass
               elif "Talkdell " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                     try:
                         del wait["Talkblacklist"][target]
                         cl.sendMessage(msg.to,"Succes dellete Talkban")
                     except:
                        pass
               elif "Staff add " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                     try:
                         staff.append(target)
                         cl.sendMessage(msg.to,"Succes add staff")
                     except:
                        pass
               elif "Staff dell " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                      try:
                         staff.remove(target)
                         cl.sendMessage(msg.to,"Succes dellete staff")
                      except:
                         pass
               elif "Admin add " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                     try:
                         admin.append(target)
                         cl.sendMessage(msg.to,"Succes add admin")
                     except:
                        pass
               elif "Admin dell " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                      try:
                         admin.remove(target)
                         cl.sendMessage(msg.to,"Succes dellete admin")
                      except:
                         pass
               elif text.lower() == 'admin:on':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["addadmin"] = True
                   cl.sendMessage(msg.to,"Send contact")
               elif text.lower() == 'admin:off':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["delladmin"] = True
                   cl.sendMessage(msg.to,"Send contact")
               elif text.lower() == 'staff:on':
                 if msg._from in owner or msg._from in admin:
                   wait["addstaff"] = True
                   cl.sendMessage(msg.to,"Send contact")
               elif text.lower() == 'staff:off':
                 if msg._from in owner or msg._from in admin:
                   wait["dellstaff"] = True
                   cl.sendMessage(msg.to,"Send contact")
               elif "Bot add " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                     try:
                         Bots.append(target)
                         cl.sendMessage(msg.to,"Succes")
                     except:
                        pass
               elif "Bot dell " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                      try:
                         Bots.remove(target)
                         cl.sendMessage(msg.to,"Succes")
                      except:
                         pass
               elif text.lower() == 'botlist':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if Bots == []:
                     cl.sendMessage(msg.to,"Bots kosong")
                   else:
                       cl.sendMessage(msg.to,"Wait...")
                       mc = "[【さัএπัஞ✵ບิथℓℓҨतΩ】 List ]\n"
                       num=1
                       ragets = cl.getContacts(Bots)
                       for mi_d in ragets:
                           mc += "\n%i. %s" % (num, mi_d.displayName)
                           num=(num+1)
                       mc += "\n\n۞➢「%i」" % len(ragets)
                       cl.sendMessage(msg.to, mc)
               elif text.lower() == 'contact bot':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                     if Bots == []:
                         cl.sendMessage(msg.to, "Bot kosong")
                     else:
                         h = ""
                         for i in Bots:
                             h = cl.getContact(i)
                             cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
               elif text.lower() == 'bot:on':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["addbots"] = True
                   cl.sendMessage(msg.to,"Send contact")
               elif text.lower() == 'bot:repeat':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["dellbots"] = True
                   cl.sendMessage(msg.to,"Send contact")
               elif text.lower() == 'refresh':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["addadmin"] = False
                   wait["delladmin"] = False
                   wait["addbots"] = False
                   wait["dellbots"] = False
                   wait["addstaff"] = False
                   wait["dellstaff"] = False
                   wait["wblacklist"] = False
                   wait["dblacklist"] = False
                   wait["Talkwblacklist"] = False
                   wait["Talkdblacklist"] = False
                   cl.sendMessage(msg.to,"Succes refresh")
               elif "Ban " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                     try:
                         wait["blacklist"][target] = True
                         cl.sendMessage(msg.to,"Succes add blacklist")
                     except:
                        pass
               elif "Unban " in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   targets = []
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                      try:
                         del wait["blacklist"][target]
                         cl.sendMessage(msg.to,"Succes dellete blacklist")
                      except:
                         pass
               elif text.lower() == 'clearban':
                 if msg._from in owner or msg._from in admin:
                   wait["blacklist"] = {}
                   ragets = cl.getContacts(wait["blacklist"])
                   mc = "۞➢「%i」User Blacklist" % len(ragets)
                   cl.sendMessage(msg.to,"Succes Clearban " +mc)
                   ki.sendMessage(msg.to,"Succes Clearban " +mc)
                   kk.sendMessage(msg.to,"Succes Clearban " +mc)
                   kc.sendMessage(msg.to,"Succes Clearban " +mc)
                   km.sendMessage(msg.to,"Succes Clearban " +mc)
                   kb.sendMessage(msg.to,"Succes Clearban " +mc)
               elif text.lower() == 'talkban:on':
                 if msg._from in owner or msg._from in admin:
                   wait["Talkwblacklist"] = True
                   cl.sendMessage(msg.to,"Send contact")
               elif text.lower() == 'talkban:off':
                 if msg._from in owner or msg._from in admin:
                   wait["Talkdblacklist"] = True
                   cl.sendMessage(msg.to,"Send contact")
               elif text.lower() == 'talklist':
                 if msg._from in owner or msg._from in admin:
                   if wait["Talkblacklist"] == {}:
                     cl.sendMessage(msg.to,"No Talkban user")
                   else:
                       cl.sendMessage(msg.to,"Wait...")
                       mc = "۞➢「Talkban User」\n"
                       num=1
                       ragets = cl.getContacts(wait["Talkblacklist"])
                       for mi_d in ragets:
                           mc += "\n%i. %s" % (num, mi_d.displayName)
                           num=(num+1)
                       mc += "\n\n۞➢「%i」User Talkban" % len(ragets)
                       cl.sendMessage(msg.to, mc)
               elif text.lower() == 'ban:on':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["wblacklist"] = True
                   cl.sendMessage(msg.to,"Send contact")
               elif text.lower() == 'ban:off':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["wblacklist"] = False
                   cl.sendMessage(msg.to,"Succes mode off")
               elif text.lower() == 'unban:on':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["dblacklist"] = True
                   cl.sendMessage(msg.to,"s0Send contact")
               elif text.lower() == 'unban:off':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["dblacklist"] = False
                   cl.sendMessage(msg.to,"Succes mode off")
               elif text.lower() == 'banlist':
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if wait["blacklist"] == {}:
                       cl.sendMessage(msg.to,"No blacklist")
                   else:
                       cl.sendMessage(msg.to,"Wait...")
                       mc = "۞➢「Blacklist User」\n"
                       num=1
                       ragets = cl.getContacts(wait["blacklist"])
                       for mi_d in ragets:
                           mc += "\n%i. %s" % (num, mi_d.displayName)
                           num=(num+1)
                       mc += "\n\n۞➢「%i」User Blacklist" % len(ragets)
                       cl.sendMessage(msg.to, mc)
               elif text.lower() == 'blc':
                 if msg._from in owner or msg._from in admin or msg._from in group:
                     if wait["blacklist"] == {}:
                         cl.sendMessage(msg.to, "No blacklist")
                     else:
                         h = ""
                         for i in wait["blacklist"]:
                             h = cl.getContact(i)
                             cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
               elif "Talk on" in msg.text:
                 if msg._from in owner or msg._from in admin:
                   wait["talkban"] = True
                   cl.sendMessage(msg.to,"Succes mode on Talkban")
               elif "Talk off" in msg.text:
                 if msg._from in owner or msg._from in admin:
                   wait["talkban"] = False
                   cl.sendMessage(msg.to,"Succes mode off Talkban")
               elif "No tag on" in msg.text:
                 if msg._from in owner or msg._from in admin:
                   wait["Mentionkick"] = True
                   cl.sendMessage(msg.to,"Berhasil mengaktifkan mention kick")
               elif "No tag off" in msg.text:
                 if msg._from in owner or msg._from in admin:
                   wait["Mentionkick"] = False
                   cl.sendMessage(msg.to,"Berhasil menonaktifkan mention kick")
               elif "Jointicket on" in msg.text:
                 if msg._from in owner or msg._from in admin:
                   settings["autoJoinTicket"] = True
                   cl.sendMessage(msg.to,"Berhasil mengaktifkan auto join by URL")
               elif "Jointicket off" in msg.text:
                 if msg._from in owner or msg._from in admin:
                   settings["autoJoinTicket"] = False
                   cl.sendMessage(msg.to,"Berhasil menonaktifkan auto join by URL")
               elif "Sticker on" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["sticker"] = True
                   cl.sendMessage(msg.to,"Berhasil mengaktifkan sticker deteksi")
               elif "Sticker off" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["sticker"] = False
                   cl.sendMessage(msg.to,"Berhasil dinonaktifkan")
               elif "Contact on" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["contact"] = True
                   cl.sendMessage(msg.to,"Berhasil mengaktifkan deteksi contact")
               elif "Contact off" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["contact"] = False
                   cl.sendMessage(msg.to,"Berhasil dinonaktifkan")
               elif "Autojoin on" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["autoJoin"] = True
                   cl.sendMessage(msg.to,"Berhasil mengaktifkan auto join")
               elif "Autojoin off" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["autoJoin"] = False
                   cl.sendMessage(msg.to,"Berhasil menonaktifkan auto join")
               elif "Autoadd on" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["autoAdd"] = True
                   cl.sendMessage(msg.to,"Berhasil mengaktifkan auto add")
               elif "Autoadd off" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["autoAdd"] = False
                   cl.sendMessage(msg.to,"Berhasil menonaktifkan auto add")
               elif "Autoleave on" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["autoLeave"] = True
                   cl.sendMessage(msg.to,"Berhasil mengaktifkan auto leave\nBot cuma bisa diundang oleh Owner, Admin & Staff")
               elif "Autoleave off" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["autoLeave"] = False
                   cl.sendMessage(msg.to,"Berhasil menonaktifkan auto leave")
               elif "Leave on" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["autoLeave1"] = True
                   cl.sendMessage(msg.to,"Berhasil mengaktifkan auto leave\nBot cuma bisa diundang oleh Owner, Admin & Staff")
               elif "Leave off" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["autoLeave1"] = False
                   cl.sendMessage(msg.to,"Berhasil menonaktifkan auto leave")
               elif "Autorespon on" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["detectMention"] = True
                   cl.sendMessage(msg.to,"Berhasil mengaktifkan respon tag")
               elif "Autorespon off" in msg.text:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   wait["detectMention"] = False
                   cl.sendMessage(msg.to,"Berhasil menonaktifkan respon tag")
               elif text.lower() == 'restart':
                 if msg._from in owner or msg._from in admin:
                   cl.sendMessage(msg.to, "Succes restart")
                   restart_program()
               elif msg.text in ["Runtime"]:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   eltime = time.time() - mulai
                   bot = "Allways on " +waktu(eltime)
                   cl.sendMessage(msg.to,bot)
               elif text.lower() == 'cek spam':
                 if msg._from in owner or msg._from in admin:
                    cl.sendMessage(msg.to, "Pesan spam kamu⤵\n\n" +str(Setmain["RAmessage1"]))
               elif text.lower() == 'cek pesan':
                 if msg._from in owner or msg._from in admin:
                    cl.sendMessage(msg.to, "Pesan kamu kalo di add⤵\n\n" +str(wait["message"]))
               elif text.lower() == 'cek respon':
                 if msg._from in Saints:
                    cl.sendMessage(msg.to, "Respon kamu kalo di tag⤵\n\n" +str(wait["Respontag"]))
               elif text.lower() == 'cek welcome':
                 if msg._from in Saints:
                    cl.sendMessage(msg.to, "Pesan kamu kalo ada\norang masuk grup⤵\n\n" +str(wait["welcome"]))
               elif text.lower() == 'cek sider':
                 if msg._from in Saints:
                    cl.sendMessage(msg.to, "Pesan kamu kalo ada yg sider⤵\n\n" +str(wait["mention"]))
               elif 'Set pesan: ' in msg.text:
                 if msg._from in Saints:
                    m = msg.text.replace('Set pesan: ','')
                    if m in [""," ","\n",None]:
                       cl.sendMessage(msg.to, "Gagal mengganti pesan, silahkan coba lagi")
                    else:
                       wait["message"] = m
                       cl.sendMessage(msg.to, "Pesan kamu diganti menjadi⤵\n\n" + m)
               elif 'Set welcome: ' in msg.text:
                 if msg._from in Saints:
                    m = msg.text.replace('Set welcome: ','')
                    if m in [""," ","\n",None]:
                       cl.sendMessage(msg.to, "Gagal mengganti pesan welcome, silahkan coba lagi")
                    else:
                       wait["welcome"] = m
                       cl.sendMessage(msg.to, "Pesan welcome kamu diganti menjadi⤵\n\n" + m)
               elif 'Set respon: ' in msg.text:
                 if msg._from in Saints:
                    m = msg.text.replace('Set respon: ','')
                    if m in [""," ","\n",None]:
                       cl.sendMessage(msg.to, "Gagal mengganti respon, silahkan coba lagi")
                    else:
                       wait["Respontag"] = m
                       cl.sendMessage(msg.to, "Respon kamu diganti menjadi⤵\n\n" + m)
               elif 'Set spam: ' in msg.text:
                 if msg._from in Saints:
                    m = msg.text.replace('Set spam: ','')
                    if m in [""," ","\n",None]:
                       cl.sendMessage(msg.to, "Gagal mengganti spam, silahkan coba lagi")
                    else:
                       Setmain["RAmessage1"] = m
                       cl.sendMessage(msg.to, "Spam kamu diganti menjadi⤵\n\n" + m)
               elif 'Set sider: ' in msg.text:
                 if msg._from in Saints:
                    m = msg.text.replace('Set sider: ','')
                    if m in [""," ","\n",None]:
                       cl.sendMessage(msg.to, "Gagal mengganti pesan sider, silahkan coba lagi")
                    else:
                       wait["mention"] = m
                       cl.sendMessage(msg.to, "Pesan sider kamu diganti menjadi⤵\n\n" + m)
               elif '.broadcast: ' in msg.text:
                 if msg._from in Saints:
                     pesan = msg.text.replace('.broadcast: ','')
                     saya = cl.getGroupIdsJoined()
                     for group in saya:
                         cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))
               elif text.lower() == 'remove chat':
                 if msg._from in Saints:
                     try:
                         cl.removeAllMessages(op.param2)
                     except:
                         cl.sendMessage(msg.to, "Berhasil membersihkan chat")
                     pass
               elif text.lower() == "lurking on": 
                   if msg._from in Saints:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            Setmain['RAreadPoint'][msg.to] = msg_id
                            Setmain['RAreadMember'][msg.to] = {}
                            cl.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
               elif text.lower() == "lurking off": 
                   if msg._from in Saints:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            del Setmain['RAreadPoint'][msg.to]
                            del Setmain['RAreadMember'][msg.to]
                            cl.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\n۞➢Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n۞➢Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
               elif text.lower() == "lurkers":
                   if msg._from in Saints:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
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
                                            textx += mention+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "aktifkan lastseen")
               elif ".ig: " in text.lower():
                   if msg._from in Saints:
                        proses = text.split(": ")
                        instagram = text.replace(proses[0] + ": ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        cl.sendMessage(msg.to, "Profile Name : "+namaIG+"\nUser Name : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link)
                        cl.sendImageWithURL(msg.to, profileIG)
               elif ".jumlah: " in text.lower():
                            if msg._from in Saints:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                cl.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)
               elif ".spamtag" in text.lower():
                            if msg._from in Saints:
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
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
               elif ".cek grup " in text.lower():
                       if msg._from in owner:
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                G = cl.getGroupIdsJoined()
                                cgroup = cl.getGroups(G)
                                ngroup = ""
                                for mention in mentionees:
                                  for x in range(len(cgroup)):
                                    gMembMids = [contact.mid for contact in cgroup[x].members]
                                    if mention['M'] in gMembMids:
                                        ngroup += "\n۞➢ " + cgroup[x].name + " | Members: " + str(len(cgroup[x].members))    
                                if ngroup == "":
                                      cl.sendMessage(to, "CONTACT NOT FOUND")
                                else:
                                    cl.sendMessage(to, "【さัএπัஞ✵ບิथℓℓҨतΩ】Group\n%s\n"%(ngroup))
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
