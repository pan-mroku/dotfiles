#!/bin/bash

SOCKETS_DIR=~/.tmux_sockets

if [ "$#" -lt 1 ]; then
		ls "$SOCKETS_DIR"
		exit
fi

if [ -e "$SOCKETS_DIR/$1" ]; then
		tmux -S "$SOCKETS_DIR/$1" attach
else
		tmux -S "$SOCKETS_DIR/$1"
fi

rm "$SOCKETS_DIR/$1"
killall -10 tmux
