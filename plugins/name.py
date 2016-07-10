import random
from telepot import glance

__author__ = 'sli'
__version__ = '0.1'
__doc__ = '''Generates for you a new fantasy name.

Commands:
  * /name'''


class NamePlugin(object):
    def __init__(self) -> None:
        with open('data/name/nouns', 'r') as f:
            self._nouns = f.read().rstrip().split('\n')
        with open('data/name/adjectives', 'r') as f:
            self._adjectives = f.read().rstrip().split('\n')
        with open('data/name/groups', 'r') as f:
            self._groups = f.read().rstrip().split('\n')
        with open('data/name/locations', 'r') as f:
            self._locations = f.read().rstrip().split('\n')

    def setup(self, bot) -> None:
        pass

    def run(self, msg: dict, bot) -> None:
        content_type, chat_type, chat_id = glance(msg)
        m_id = msg['message_id']
        name = self.generate_name()
        reply = 'Your new name is: {}'.format(name)
        await bot.sendMessage(chat_id, reply, reply_to_message_id=m_id)

    def generate_name(self) -> str:
        nameA = random.choice(self._locations)
        nameB = nameA
        while nameA == nameB:
            nameB = random.choice(self._locations)
        if nameA[-1] == nameB[0]:
            nameB = nameB[1:]
        name = nameA+nameB
        noun = random.choice(self._nouns)
        adj = random.choice(self._adjectives)
        grp = random.choice(self._groups)
        return '%s, %s of the %s %s' % (name.capitalize(), noun, adj, grp)

p = NamePlugin()

exports = {
    'self': p,
    '/name': p.run
}