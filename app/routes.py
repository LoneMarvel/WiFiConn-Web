from flask import Flask, render_template, url_for, redirect, request, flash
import sys
import subprocess
from app import app
from app.forms import PasswdFrm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():    
    wlanList = subprocess.getoutput("nmcli dev wifi list | awk '{print $1}'").split('\n')
    del wlanList[0]
    passwdFrm = PasswdFrm()
    if passwdFrm.validate_on_submit():
        print(f'Form Was Submitted {passwdFrm.wifiPasswd.data}')        

    pageCont = {'title':'WiFi Connection', 'wlanList':wlanList, 'passwdFrm':passwdFrm}
    return render_template('layout.html', pageCont=pageCont)