# Installation list

1. networkmanager;nm-applet and editor
2. xorg-server;~~xf86_video-~~*; xorg-xwininfo
3. i3-wm; 
4. qtile
5. lightDM;[lightdm-gtk-greeter](https://www.archlinux.org/packages/?name=lightdm-gtk-greeter)
6. rofi
7. ~~CLI xbacklight~~
8. pavucontrol; CLI pulsemixer
9. pacmanfm; gvfs for trash support
10. maim: Copy desktop 
11. ~~copyq~~
12. picom

### Internet

1. firefox
2. wget
3. filezilla
4. ~~**RSS**  Liferea~~
5. **Cloud service FUSE**
6. openconnect
7. rclone (CLI)
8. sshfs
9. ~~**neomutt**~~

### Multimedia

  1. nitrogen
2. **vimiv**
  3. maim 
  4. vlc
5. ~~viewnoir~~

### Utilities

1. terminator
2. ~~st colormap and configuration file~~
3. alacritty  to replace st
4. tmux
5. pacmanfm (gvfs)
6. ranger    (_there are several package..._)
7. xarchiver (p7zip,unrar)
8. **File Serching**?
9. git
10. zeal ?
11. **Back up tools**?
12. conky
13. neofetch
14. pacmanlogviewer
15. **cron** what is that conky? Cronies
16. arandr (_configuration_!!!!!)
 17. bluez; bluez-utils; gnome-bluetooth
18. acpid _Configuration_
19. pass
20. taskwarrior
21. w3m
22. cups; cpus-pdf
23. mlocate

### Document

1. gedit
2. ~~mupdf~~
3. ~~zim~~
4. Typora
5. atril
6. Inkscape
7. gimp

### Security

​	~~1. keepassxc (**extension**)~~

1. pass

### Others

1. ohmyzsh

 	2. powerline; powerline-fonts(for zsh vim and other useages)


3. man 
4.  tldr
5. fcitx;fcitx-configtool;fcitx-im
6. anki
7. mpv(required by anki)
8. kite [link](https://kite.com/download/?utm_expid=.sq9uDK0ERlShfoLd6G7rqw.0&utm_referrer=)
9. stardict, [The dictionary is in the link](http://download.huzheng.org/zh_CN/)

### Font

1. nerd font https://github.com/ryanoasis/nerd-fonts
2. otf-lartin-modern; otf-lartinmodern-math
3. wqy font
4. Font Awesome
5. powerline font; powerline-font-git
6. fontviewer

### Python

1. anaconda (Requirement pacman -Sy libxau libxi libxss libxtst libxcursor libxcomposite libxdamage libxfixes libxrandr libxrender mesa-libgl alsa-lib libglvnd: )
2. sudo pacman -S pip
3. sudo pacman -S python-virtualenv
4. sudo pacman -S python-pipenv
6. pip instrall --user flake8

### Sqlite

1. sqlitebrowser

### Vim

1. ctags



----------------

#### Set default input/output  in PulseAudio

[This link](https://wiki.archlinux.org/index.php/PulseAudio/Examples#Set_default_input_source)

```bash
$ pacmd list-sinks | grep -e 'name:' -e 'index:'

  * index: 0
	name: <alsa_output.pci-0000_04_01.0.analog-stereo>
    index: 1
	name: <combined>
    
    
    
$ vim /etc/pulse/default.pa

...
set-default-sink alsa_output.pci-0000_04_01.0.analog-stereo
...
```

#### Set about the GunPG

This [link](https://wiki.archlinux.org/index.php/GnuPG#See_also)  and this [one](https://riseup.net/en/security/message-security/openpgp/gpg-best-practices)

#### Set about Mutt

1. ~~msmtp~~
2. ~~isync~~
3. ~~abook~~

Check the configuration file.



Replace by:

1.  Thunderbird

#### Mathematica

Please check this two links [Zlib](https://stackoverflow.com/questions/48306849/lib-x86-64-linux-gnu-libz-so-1-version-zlib-1-2-9-not-found) and [post](https://mathematica.stackexchange.com/questions/189306/cant-launch-mathematica-11-on-fedora-29)

After the installation:

```bash
. /usr/local/Wolfram/Mathematica/11.X/SystemFiles/FrontEnd/Binaries/Linux-x86-64/Mathematica: symbol lookup error: /usr/lib/libfontconfig.so.1: undefined symbol: FT_Done_MM_Var
```

```bash
cp /usr/lib/libfreetype.so.6 /usr/local/Wolfram/Mathematica/11.X/SystemFiles/FontEnd/Binaries/Linux-x86-64/Mathematica/

tar -xvf ~/Downloads/zlib-1.2.9.tar.gz
cd zlib-1.2.9
sudo./configure
sudo make
make install

cd /usr/local/Wolfram/Mathematica/11.0/SystemFiles/Libraries/Linux-x86-64

sudo ln -s -f /usr/local/lib/libz.so.1.2.9 libz.so.1


```

#### Fcitx input in some application

[Fcitx link](https://fcitx-im.org/wiki/FAQ#Only_one_specific_app_has_problem.3F)

For Gtk apps configure the DBus.

```bash
exec --no-startup-id fcitx -d
```

For Qt apps

```bash
pacman -S fcitx-qt5
```

### Julia

1. julia
2. juno



### Power manager related

1. acpid

2. screensaver? Dpms

	Problem is screen will black in Zoom

k