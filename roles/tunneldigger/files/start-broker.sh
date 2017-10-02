#!/bin/bash

WDIR=/opt/freifunk/tunneldigger
VIRTUALENV_DIR=/opt/freifunk/tunneldigger

cd $WDIR
source $VIRTUALENV_DIR/bin/activate

bin/python broker/l2tp_broker.py broker/l2tp_broker.cfg
