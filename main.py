import asyncio
import requests
 
from pyrogram import *
from pyrogram.types import * 
from pyrogram.errors import *
from pyromod import listen
from pyrogram import (
   __version__ as v, Client,
   filters, idle
)
import requests
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from pyrogram.errors import SessionPasswordNeeded, PhoneCodeExpired
from pyrogram.errors.exceptions.bad_request_400 import PasswordHashInvalid
from pyrogram.errors.exceptions.not_acceptable_406 import PhoneNumberInvalid
from pyrogram.errors.exceptions.bad_request_400 import PhoneCodeInvalid

from telethon import TelegramClient
from telethon import __version__ as v2
from telethon.sessions import StringSession
from telethon.errors import (
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


api_hash = "" #ايبي هاش هنا
api_id =  #ايبي اي دي هنا
token = "" #توكن البوت هنا

app = Client(
  name="@q444x - @N0040 - stringsession",
  api_id=api_id, api_hash=api_hash,
  bot_token=token, in_memory=True
)
CHANNEL = "Y8840" # قناه الاشتراك 
bot_token = "" # بوت التوكن المستخدم في الاشتراك
@app.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
       m = message.chat.id
       user = message.from_user.mention
       do = requests.get(f"https://api.telegram.org/bot{bot_token}/getChatMember?chat_id=@{CHANNEL}&user_id={message.from_user.id}").text
       if do.count("left") or do.count("Bad Request: user not found"):
          await message.reply_text(f"**Join [this channel](t.me/{CHANNEL}) first to be able to use the bot**", disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "Join Channel",
                        url=f'https://t.me/{CHANNEL}'),
                        ],])) 
       else:
         await app.send_message(
      chat_id = message.chat.id,
      text=f"Hi {message.from_user.mention} \n\n𝐭𝐡𝐢𝐬 𝐛𝐨𝐭 𝐟𝐨𝐫 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐩𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 \n\n- 𝐨𝐰𝐧𝐞𝐫 : @N0040",
      reply_to_message_id=message.id,
      disable_web_page_preview = True,
      reply_markup = ReplyKeyboardMarkup(
                [[
                    KeyboardButton ("«𝐩𝐲𝐫𝐨𝐠𝐫𝐚𝐦»"), KeyboardButton ("«𝐭𝐞𝐥𝐞𝐭𝐡𝐨𝐧»")
                ],[
                    KeyboardButton ("«𝐚𝐛𝐨𝐮𝐭»")
                ]], resize_keyboard=True, placeholder='@N0040'
            )
         )

@app.on_message(filters.text & filters.private)
async def generator_and_about(app,m):



   if m.text == "«𝐚𝐛𝐨𝐮𝐭»":
      text = ''
      text += "𝐩𝐫𝐨𝐠𝐫𝐚𝐦𝐦𝐢𝐧𝐠 𝐥𝐚𝐧𝐠𝐮𝐚𝐠𝐞: 𝐩𝐲𝐭𝐡𝐨𝐧"
      text += f"\n 𝐩𝐲𝐫𝐨𝐠𝐫𝐚𝐦 {v}"
      text += f"\n 𝐭𝐞𝐥𝐞𝐭𝐡𝐨𝐧 {v2}"
      text += f"\n\n 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 : [𝐦𝐲 𝐥𝐨𝐯𝐞](t.me/N0040)"
      await m.reply(text, quote=True)
   
   
   
   if m.text == "«𝐩𝐲𝐫𝐨𝐠𝐫𝐚𝐦»":
       rep = await m.reply(
       "**⏳ 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠..**", reply_markup=ReplyKeyboardRemove ()
       ,quote=True)
       c = Client(
       f"pyro{m.from_user.id}",api_id,api_hash,
       device_model="Elmasry", in_memory=True)
       await c.connect()
       await rep.delete()
       phone_ask = await app.ask(
       m.chat.id, "**𝐞𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝐩𝐡𝐨𝐧𝐞 𝐧𝐮𝐦𝐛𝐞𝐫:\n +201111111111**",
       reply_to_message_id=m.id, filters=filters.text
       )
       phone = phone_ask.text
       
       try:
         send_code = await c.send_code(phone)
       except PhoneNumberInvalid:
         return await phone_ask.reply("𝐩𝐡𝐨𝐧𝐞 𝐧𝐮𝐦𝐛𝐞𝐫 𝐢𝐧𝐯𝐚𝐥𝐢𝐝\n/start", quote=True)
       except Exception:
         return await phone_ask.reply("𝐚𝐧 𝐞𝐫𝐫𝐨𝐫! 𝐩𝐥𝐞𝐚𝐬𝐞 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐥𝐚𝐭𝐞𝐫 🤠\n/start",quote=True)
       
       hash = send_code.phone_code_hash
       
       code_ask = await app.ask(
       m.chat.id, "**𝐧𝐨𝐰 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐜𝐨𝐝𝐞 𝐲𝐨𝐮 𝐫𝐞𝐜𝐢𝐯𝐞𝐝 𝐰𝐢𝐭𝐡 𝐭𝐡𝐢𝐬 𝐭𝐲𝐩𝐞 :**\n`1 2 3 4 5` ✔️\n12345 ✖️**",filters=filters.text)
       
       code = code_ask.text
       
       try:
         await c.sign_in(phone, hash, code)
       except SessionPasswordNeeded:
         password_ask = await app.ask(m.chat.id, "**𝐞𝐧𝐭𝐞𝐫 2FA password**", filters=filters.text)
         password = password_ask.text
         try:
           await c.check_password(password)
         except PasswordHashInvalid:
           return await password_ask.reply("Password hash invalid\n/start", quote=True)
       
       except (PhoneCodeInvalid, PhoneCodeExpired):
         return await code_ask.reply("Phone code invalid!", quote=True)
         
       try:
         await c.sign_in(phone, hash, code)
       except:
         pass
       
       rep = await m.reply("**⏳ 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ..**", quote=True)
       get = await c.get_me()
       text = '** 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐥𝐨𝐠𝐠𝐞𝐝 𝐢𝐧\n'
       text += f' 𝐟𝐢𝐫𝐬𝐭𝐧𝐚𝐦𝐞 : {get.first_name}\n'
       text += f' 𝐢𝐝 : {get.id}\n'
       text += f' 𝐩𝐡𝐨𝐧𝐞𝐧𝐮𝐦𝐛𝐞𝐫: {phone}\n'
       text += f' 𝐩𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐢𝐧 𝐬𝐚𝐯𝐞𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬\n'
       text += '\n/start'
       
       string_session = await c.export_session_string()
       await rep.delete()
       
       await c.send_message('me', f' 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐩𝐲𝐫𝐨𝐠𝐫𝐚𝐦 {v} 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧\n\n`{string_session}`\n\n 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 : [𝐦𝐲 𝐥𝐨𝐯𝐞](t.me/N0040)\n 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐛𝐲 : @N0040')
       await c.disconnect()
       
       await app.send_message(
       m.chat.id, text)
   
   
   
   if m.text == "«𝐭𝐞𝐥𝐞𝐭𝐡𝐨𝐧»":
       rep = await m.reply(
       "**⏳ 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠..**", reply_markup=ReplyKeyboardRemove ()
       ,quote=True)
       c = TelegramClient(StringSession(), api_id, api_hash)
       await c.connect()
       await rep.delete()
       phone_ask = await app.ask(
       m.chat.id, "**𝐞𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝐩𝐡𝐨𝐧𝐞 𝐧𝐮𝐦𝐛𝐞𝐫:\n +201111111111**",
       reply_to_message_id=m.id, filters=filters.text
       )
       phone = phone_ask.text
       
       try:
         send_code = await c.send_code_request(phone)
       except PhoneNumberInvalidError:
         return await phone_ask.reply("𝐩𝐡𝐨𝐧𝐞 𝐧𝐮𝐦𝐛𝐞𝐫 𝐢𝐧𝐯𝐚𝐥𝐢𝐝\n/start", quote=True)
       except Exception:
         return await phone_ask.reply("𝐚𝐧 𝐞𝐫𝐫𝐨𝐫! 𝐩𝐥𝐞𝐚𝐬𝐞 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐥𝐚𝐭𝐞𝐫 🤠\n/start",quote=True)
       
       code_ask = await app.ask(
       m.chat.id, "**𝐧𝐨𝐰 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐜𝐨𝐝𝐞 𝐲𝐨𝐮 𝐫𝐞𝐜𝐢𝐯𝐞𝐝 𝐰𝐢𝐭𝐡 𝐭𝐡𝐢𝐬 𝐭𝐲𝐩𝐞 :**\n`1 2 3 4 5` ✔️\n12345 ✖️**",filters=filters.text)
       
       code = code_ask.text.replace(" ","")
       
       try:
         await c.sign_in(phone, code, password=None)
       except SessionPasswordNeededError:
         password_ask = await app.ask(m.chat.id, "**𝐞𝐧𝐭𝐞𝐫 2FA password**", filters=filters.text)
         password = password_ask.text
         try:
           await c.sign_in(password=password)
         except PasswordHashInvalidError:
           return await password_ask.reply("Password hash invalid\n/start", quote=True)
       
       except (PhoneCodeExpiredError, PhoneCodeInvalidError):
         return await code_ask.reply("Phone code invalid!", quote=True)
      
       await c.start(bot_token=phone)
       
       rep = await m.reply("**⏳ 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ..**", quote=True)
       get = await c.get_me()
       text = '** 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐥𝐨𝐠𝐠𝐞𝐝 𝐢𝐧\n'
       text += f' 𝐟𝐢𝐫𝐬𝐭𝐧𝐚𝐦𝐞 : {get.first_name}\n'
       text += f' 𝐢𝐝 : {get.id}\n'
       text += f' 𝐩𝐡𝐨𝐧𝐞𝐧𝐮𝐦𝐛𝐞𝐫: {phone}\n'
       text += f' 𝐭𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐢𝐧 𝐬𝐚𝐯𝐞𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬\n'
       text += '\n/start'
       
       string_session = c.session.save()
       await rep.delete()
       
       await c.send_message('me', f' 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐠𝐞𝐧??𝐫𝐚𝐭𝐞𝐝 𝐭𝐞𝐥𝐞𝐭𝐡𝐨𝐧 {v2} 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧\n\n`{string_session}`\n\n 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 : [𝐦𝐲 𝐥𝐨𝐯𝐞](t.me/N0040)\n 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐛𝐲 : @N0040 ')
       await c.disconnect()
       
       await app.send_message(
       m.chat.id, text)
   
   
       

app.start()
print("VerY Good This BoT \n\n Is Successful Live Now")
idle()
