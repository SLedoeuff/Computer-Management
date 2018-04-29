#!/bin/bash

crontab < <(crontab -l; echo"*/5 * * * * /home/sonde1.py")
crontab < <(crontab -l; echo"*/5 * * * * /home/GetData.py")
crontab < <(crontab -l; echo"*/5 * * * * /home/AlertMachine.py")