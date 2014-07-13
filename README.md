# DESCRIPTION

Simple script to manage (music) volume. It uses `argparse`, `colorama` and `commands`.

# USAGE

The script's help shows:

     % python pyvol.py -h
     usage: pyvol.py [-h] action

     positional arguments:
       action      up, down, mute or ask

     optional arguments:
       -h, --help  show this help message and exit

Three actions are allowed:

 * up: increase the volume a 5%
 * down: decrease the volume a 5%
 * mute: toggle mute/unmute
 * ask: does nothing and shows the actual status

 __EXAMPLE__:

     % python pyvol.py ask
      35% [###       ] 
     % python pyvol.py mute
      35% [###       ] mute

