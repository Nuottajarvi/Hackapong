#!/bin/bash

set -e

python pingpongbot.py "$@" &>> log/game.log &
echo $! >> .pids
