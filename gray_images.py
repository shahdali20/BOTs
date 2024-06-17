import telepot
import os
from telepot.loop import MessageLoop
import cv2
import tempfile

def handle(msg):
    if msg["photo"]:
        chat_id = msg['chat']['id']
        f = tempfile.NamedTemporaryFile(delete=True).name+".png"
        print(f)
        photo = msg['photo'][-1]['file_id']
        path = bot.getFile(photo)["file_path"]
        print(photo)
        print(path)
        bot.sendMessage(chat_id,"Retrieving %s" % path)
        bot.download_file(photo,f)
        p = cv2.imread(f)
        gray = cv2.cvtColor(p,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f,gray)
        bot.sendPhoto(chat_id,open(f,'rb'))
    else:
        print("no photo")

TOKEN = os.environ['BOT_TOKEN']
bot = telepot.Bot(TOKEN)
MessageLoop(bot,handle).run_forever()