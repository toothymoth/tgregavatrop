from redis import Redis
import time
from aiogram import Bot, Dispatcher, executor, types
import string
import random


def random_string(string_length=20):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(string_length))

def getPass():
    developer = "tg: @rnbw0q ; vk: @lonelyhurricane ; github: @qwikks"
    return chr(ord(developer[51:])+222) + random_string(17)



TOKEN = "5272186159:AAHwvr0Iiwi3-0oPWgTBOnVXFL_7olEWsPE" # token of bot from @BotFather


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
r = Redis(decode_responses=True)


@dp.message_handler(commands=["start"])
async def newacc(message: types.Message):
    passwd = r.get(f"tg:{message.from_user.id}")
    if passwd:
        await message.reply(f"PASS-WORD: {passwd}")
        return
    else:
        uid = r.incrby("uids", 1)
        passwd = getPass()
        r.set(f"uid:{uid}:slvr", 10000)
        r.set(f"uid:{uid}:gld", 10000)
        r.set(f"uid:{uid}:enrg", 150)
        r.set(f"uid:{uid}:exp", 250)
        r.set(f"uid:{uid}:emd", 0)
        r.set(f"uid:{uid}:lvt", 0)
        r.set(f"uid:{uid}:role", 0)
        r.set(f"uid:{uid}:password", passwd)
        r.set(f"tg:{message.from_user.id}", passwd)
        r.set(f"uid:{passwd}", uid)
    await message.reply(f"PASS-WORD: {passwd}")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
