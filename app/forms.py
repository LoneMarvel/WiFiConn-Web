from app import app
from flask_wtf import FlaskForm
from flask import Flask, render_template, flash, request
from wtforms import PasswordField, HiddenField, SubmitField

class PasswdFrm(FlaskForm):
    wifiPasswd = PasswordField('Password: ')
    wifiName = HiddenField('Wifi Name')
    
