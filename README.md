# jabberbot

Jabberbot is a Telegram bot that loads plugins. That's about it. Check the `plugins/` directory to see some examples.

Jabberbot requires Python 3.5 or higher.

### Install

Adjust the following for your operating system:

    $ sudo dnf install python3-devel ffmpeg
    $ pip install -r requirements.txt
    $ pip install -r requirements-plugins.txt

Now put your Telegram API key in a file called `token` in the same directory at `jabberbot.py` and you're all set. Have fun.

### Run

    $ python3.5 jabberbot.py

### Features

1. Plugins! And it comes with some cool ones!
	1. cobe - [It's Cobe.](https://github.com/pteichman/cobe) Except it currently uses [my fork](https://github.com/sli/cobe) with more Python 3 fixes.
	2. dice - Roll dice using dice notation with [dice](https://github.com/borntyping/python-dice).
	3. fortune - Get your fortune. Also gives Powerball numbers.
	4. github - Link a Github repo by username/reponame.
	5. mediasnag - Download MP3s from YouTube.
	6. ~~quote - Save quotes from your friends.~~
	7. ~~talkback - Cobe + Google Speech Recognition + text-to-speech = talkback plugin~~
2. Hot reloading action! Reload the bot on the fly with `/reload`!
3. Autogenerated `/help` stuff for stupid people!
4. Written almost entirely under the influence of some substance or another!


### Plugins

Want to write one? [Go write one!](https://github.com/sli/jabberbot/wiki/Writing-Plugins)

### Training cobe

To train cobe, simply place a file named `train.txt` containing your training text in `data/cobe/`. This file will be used to train cobe then renamed (to something similar to `train.txt.0`). Only a file named `train.txt` will be used to train cobe, so don't worry about these backups.

Training can be invoked manually with `/reload`.