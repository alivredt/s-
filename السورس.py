import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","زد إي","السورس", "سورس زد إي"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/41a777f089288f7ad2571.jpg",
        caption=f"""**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ . .
 [🔱 سورس علي احمد 🔱](https://t.me/zlz1zl)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/TFFF_F"), 
                    
                
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/TFFF_F"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/zlz1zl"),
                
        ],

            ]

        ),

    )

