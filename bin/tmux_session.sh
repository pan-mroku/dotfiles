#!/bin/bash

SOCKETS_DIR=~/.tmux_sockets

killall -10 -q tmux

if [ "$#" -lt 1 ]; then
		ls "$SOCKETS_DIR"
		exit
fi

if [ -e "$SOCKETS_DIR/$1" ]; then
		if ! tmux -S "$SOCKETS_DIR/$1" attach
		then
				rm "$SOCKETS_DIR/$1"
				tmux -S "$SOCKETS_DIR/$1" new-session -s "$1"
		fi
else
		tmux -S "$SOCKETS_DIR/$1" new-session -s "$1"
fi

