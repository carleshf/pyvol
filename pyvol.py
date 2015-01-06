#!/usr/bin/env python
# econding: utf-8

from argparse import ArgumentParser
from colorama import init, Fore
from commands import getstatusoutput

def print_status( status, nchr=10, plain=False) :
    dchr = int( status[ 'vol' ] ) * nchr / 100
    if plain:
        print( status[ 'vol' ] )
    else:
        disp = '{0:>3}% [{1}{2}] {3}'.format(
            status[ 'vol' ],
            '#' * dchr,
            ' ' * ( nchr - dchr ),
            Fore.RED + 'mute' + Fore.RESET if status[ 'status' ] == 'off' else ''
        )
        print( disp )


def get_status():
    _, output = getstatusoutput( 'amixer -D pulse' )
    output    = output.split( '\n' )
    output    = [ line 
                     for line in output 
                     if 'Front Left: Playback' in line 
                ][ 0 ]
    output    = [ nn.strip( ' ' ).strip( ']' ).strip( '%' )
                      for nn in output.split( '[' )[ 1: ] 
                ]
    return { 'vol': output[ 0 ], 'status': output[ 1 ] }


def set_volume( action ):
    if action not in ( 'up', 'down', 'mute' ):
         return
    if action == 'up':
         _, output = getstatusoutput( 'amixer -D pulse set Master 3276+' )
    if action == 'down':
         _, output = getstatusoutput( 'amixer -D pulse set Master 3276-' )
    if action == 'mute':
         _, output = getstatusoutput( 'amixer -D pulse set Master toggle' )
    return output


def main():
    parser = ArgumentParser()
    parser.add_argument( 'action', help = 'up, down, mute or ask', type = str )

    args = parser.parse_args()
    args.action = args.action.lower()
    init()

    if args.action != 'ask':
        set_volume( args.action )
    
    if args.action == 'txt':
        print_status( get_status(), plain=True)
    else:
        print_status( get_status() )


if __name__ == '__main__':
    main()
