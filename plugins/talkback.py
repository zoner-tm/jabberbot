import time
import requests
import subprocess
import speech_recognition as sr
from telepot import glance
from gtts import gTTS

__author__ = 'sli'
__version__ = '0.1'
__doc__ = '''A talkative feature. Reacts automatically to voice messages.'''


class TalkBackPlugin(object):
    def __init__(self) -> None:
        self._recog = sr.Recognizer()

    def setup(self, bot) -> None:
        pass

    async def run(self, msg: dict, bot) -> None:
        content_type, chat_type, chat_id = glance(msg)
        m_id = msg['message_id']
        file_id = msg['voice']['file_id']
        path = self.getFile(file_id)['file_path']
        audio_url = 'https://api.telegram.org/file/bot{}/{}'
        audio_url = audio_url.format(self._token, path)
        message_audio = 'voice/{}.ogg'.format(file_id)

        with open(message_audio, 'wb') as f:
            r = requests.get(audio_url)
            f.write(r.content)

        of = message_audio.replace('.ogg', '.flac')
        subprocess.check_call(['ffmpeg', '-i', message_audio, of],
                              stdout=open('stdout.log', 'w'),
                              stderr=open('stderr.log', 'w'),
                              close_fds=True)

        with sr.AudioFile(message_audio) as source:
            audio = self._recog.record(source)

        incoming_message = self._recog.recognize_google(audio)

        get_reply = bot.plugins['cobe'].exports['self'].get_reply
        reply_text = '{}, {}'.format(msg['from']['first_name'],
                                     get_reply(incoming_message, bot))
        reply_audio = gTTS(text=reply_text, lang='en')
        audio_file = '{}-reply.ogg'.format(time.time())
        reply_audio.save(audio_file)

        with open(audio_file, 'wb') as f:
            await bot.sendVoice(chat_id, f, reply_to_message_id=m_id)

p = TalkBackPlugin()

exports = {
    'self': p,
    'audio': p.run
}
