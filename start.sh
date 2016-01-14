#!/bin/bash

set -e

python pingpongbot.py tf3 game 9090 &>> log/game.log &
echo $! >> .pids
