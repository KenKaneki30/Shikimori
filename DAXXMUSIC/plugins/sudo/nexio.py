import requests
import random
from DAXXMUSIC import app, userbot
from DAXXMUSIC.misc import SUDOERS
from pyrogram import * 
from pyrogram.types import *
from DAXXMUSIC.utils.daxx_ban import admin_filter






Yumikoo_text = [
"hey please don't disturb me.",
"who are you",    
"aap kon ho",
"aap mere owner to nhi lgte ",
"hey tum mera name kyu le rhe ho mujhe sone do",
"ha bolo kya kaam hai ",
"dekho abhi mai busy hu ",
"hey i am busy",
"aapko smj nhi aata kya ",
"leave me alone",
"dude what happend",    
]

strict_txt = [
"i can't go against my besties",
"are you serious? i am not restrict to my friends",
"fuck you bsdk, mai apne dosto ko kyu kru",
"hey stupid admin ", 
"han ye krlo phele chutiya harkatein",  
"i can't he's my closest friend",
"i love him... I can't do it... "
]


 
ban = ["ban","boom","udade"]
unban = ["unban","wapis"]
mute = ["mute","silent","shut","chup"]
unmute = ["unmute","speak","free","bolnede"]
kick = ["kick", "out","nikaal","nikal","punch"]
promote = ["promote","adminship","admin"]
fullpromote = ["fullpromote","fulladmin"]
demote = ["demote","lelo","downpromote"]
group = ["group"]
channel = ["channel"]



# ========================================= #


@app.on_message(filters.command(["hiki","hikimori"], prefixes=["s", "S"]) & admin_filter)
async def restriction_app(app :app, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if len(message.text) < 2:
        return await message.reply(random.choice(Yumikoo_text))
    bruh = message.text.split(maxsplit=1)[1]
    data = bruh.split(" ")
    
    if reply:
        user_id = reply.from_user.id
        for banned in data:
            print(f"present {banned}")
            if banned in ban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))          
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await message.reply("OK, Ban krdia maderchod ko rand tha apko tang kar rha tha !")
                    
        for unbanned in data:
            print(f"present {unbanned}")
            if unbanned in unban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))          
                else:
                    await app.unban_chat_member(chat_id, user_id)
                    await message.reply(f"Ok, aapke kehne pr unban kr rhi hun") 
                
        for kicked in data:
            print(f"present {kicked}")
            if kicked in kick:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await app.unban_chat_member(chat_id, user_id)
                    await message.reply("get lost! laat mardia bhosdike ko") 
                    
        for muted in data:
            print(f"present {muted}") 
            if muted in mute:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"muted successfully! chup kar chutiye.") 
                    
        for unmuted in data:
            print(f"present {unmuted}")            
            if unmuted in unmute:
                if user_id in SUDOERS:
                 await message.reply(random.choice(strict_txt))
                
                else:
                    permissions = ChatPermissions(can_send_messages=True)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"muted successfully! chup kar chutiye.") 
 


        for promoted in data:
            print(f"present {promoted}")            
            if promoted in promote:
                if user_id in SUDOERS:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                       )
                     )
                await message.reply("promoted !")

        for demoted in data:
            print(f"present {demoted}")            
            if demoted in demote:
                if user_id in SUDOERS:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                       )
                     )
                await message.reply("demoted !")


#async def your_function():
    for fullpromoted in data:
        print(f"present {fullpromoted}")            
        if fullpromoted in fullpromote:
                if user_id in SUDOERS:
            await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                can_change_info=True,
                can_invite_users=True,
                can_delete_messages=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True,
               )
             )
            await message.reply("fullpromoted !")
