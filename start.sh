#!/usr/bin/env bash
# -*- coding: utf-8 -*-
if (( $(id -u) == 0 )); then
    echo "Installing packages..."
    pip install requests colorama
    python start.py
else echo "You need root to use this program."
sudo su
pip install requests colorama
python start.py
fi
