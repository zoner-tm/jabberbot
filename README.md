# jabberbot

Jabberbot is a Telegram bot that loads plugins. That's about it. Check the `plugins/` directory to see some examples.

Jabberbot requires Python 3.5 or higher.

### Install

Adjust the following for your operating system:

    $ sudo dnf install python3-devel ffmpeg
    $ pip install -r requirements.txt
    $ pip install -r requirements-plugins.txt

Now put your Telegram API key in a file in the same directory as `jabberbot.py`. It can be named anything you want, but the default is "token." You're all set. Have fun.

### Run

    $ python3.5 jabberbot.py

Or if you're not using the default filenames for your config and token:

    $ python3.5 jabberbot.py -c my-config.cfg -t my-token

### CLI Switches

    $ python3.5 jabberbot.py --help
    Usage: jabberbot.py [OPTIONS]

    Options:
      -c, --config TEXT  Configuration file for this instance. Default:
                         jabberbot.cfg
      -t, --token TEXT   File containing the API token for the bot. Default: token
      --help             Show this message and exit.

### Features

1. Plugins! And it comes with some cool ones!
    1. cobe - [It's Cobe.](https://github.com/pteichman/cobe) Except it currently uses [my fork](https://github.com/sli/cobe) with more Python 3 fixes. (For now.)
    2. dice - Roll dice using dice notation with [dice](https://github.com/borntyping/python-dice).
    3. fortune - Get your fortune. Also gives Powerball numbers.
    4. github - Link a Github repo by username/reponame.
    5. mediasnag - Download MP3s from YouTube and Soundcloud.
    6. quote - Save quotes from your friends.
    7. talkback - Cobe + Google Speech Recognition + text-to-speech = talkback plugin
    8. hev - See what the HEV suit has to say. (Requires the fvox audio files from Half-Life.)
2. Hot reloading action! Reload the bot on the fly with `/reload`! (Not sure if this is working properly, yet.)
3. Autogenerated `/help` stuff for stupid people!
4. Written almost entirely under the influence of some substance or another!


### Plugins

Want to write one? [Go write one!](https://github.com/sli/jabberbot/wiki/Writing-Plugins)

### Training cobe

To train cobe, simply place a file named `train.txt` containing your training text in `data/cobe/`. This file will be used to train cobe then renamed (to something similar to `train.txt.0`). Only a file named `train.txt` will be used to train cobe, so don't worry about these backups.

Training can be invoked manually with `/reload`.