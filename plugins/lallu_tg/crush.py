import os
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging

PHOTO1 = "https://telegra.ph/file/70f9918fad55aea9b43fe.jpg"

@Client.on_message(filters.command("owner"))
async def aboutow(client, message):
        buttons= [[
            InlineKeyboardButton('♥️ 𝐅𝐚𝐭𝐡𝐢𝐦𝐚 ♥️', url='https://t.me/File_store_MsT_Bot')
            ],[
            InlineKeyboardButton('🏠 𝙷𝙾𝙼𝙴 🏠', callback_data='start'),
            InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴 🔐', callback_data='close_data')
       ]]
       reply_markup = InlineKeyboardMarkup(buttons)
       await message.reply_photo(
           photo=(PHOTO1),
           caption=script.OWNER1_TXT.format(message.from_user.mention),
           reply_markup=reply_markup,
           parse_mode='html'
      )
       

                 
        
       
        
 
            
