# jabberbot

Jabberbot is a Telegram bot that loads plugins. That's about it. Check the `plugins/` directory to see some examples.

Jabberbot requires Python 3.5 or higher.

### Install

Adjust the following for your operating system:

    $ sudo dnf install python3-devel libav-tools libavcodec-extra-53
    $ pip install -r requirements.txt
    $ pip install -r requirements-plugins.txt

Now put your Telegram API key in a file in the same directory as `jabberbot.py`. It can be named anything you want, but the default is "token." Set your bot's username in the config, and the admin user's user ID if you want (not required, it just enables `/reload` for that user).

You're all set. Have fun.

### Windows

Jabberbot works just fine on Windows, but the setup will be _slightly_ different. You can skip installing development headers, instead you'll need to install PyStemmer and libav manually. Not big deal.

* PyStemmer: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pystemmer
* Libav: http://builds.libav.org/windows/release-gpl/

Installing the PyStemmer [wheel file](http://pythonwheels.com/) is done with pip in the following fashion:

    $ pip install PyStemmer-1.3.0-cp35-none-win32.whl

Libav is used by the pydub module in the `talkback` plugin, and as such you should follow [pydub's install instruction for libav](https://github.com/jiaaro/pydub#getting-ffmpeg-set-up). Windows is at the bottom. If you're not sure how to add a directory to your PATH, you can read instructions [here](http://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/).

### Run

    $ python3.5 jabberbot.py

Or if you're not using the default filenames for your config and/or token:

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

### Setting up the HEV plugin

If you have Half-Life installed (not Half-Life 2), you can simply copy the audio from the resources and into `data/hev/fvox/`. The locations of these files are:

* Windows: `C:\Program Files (x86)\Steam\steamapps\common\Half-Life\valve\sound\fvox`
* Linux: `~/.steam/steam/SteamApps/common/Half-Life/valve/sound/fvox`
* OS X: `~/Library/Application Support/Steam/steamapps/common/Half-Life/valve/sound/fvox`

If you only have Half-Life 2, you'll need to use [GCFScape](http://nemesis.thewavelength.net/index.php?p=26) to extract the audio from `hl2_sound_misc_dir.vpk` in the Half-Life 2 resources. You can also do the same with Half-Life: Source.

No, I'm not going to commit the audio to the repository, so don't bother asking. Half-Life goes on sale for $2.50 constantly, just buy it. You ought to own it already, anyway. [I'll even link it for you.](http://store.steampowered.com/app/70/)

I'd definitely recommend springing for the Half-Life Bundle instead, though.