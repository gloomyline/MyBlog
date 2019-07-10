# -*- coding: utf-8 -*-
# @Author:              AlanWang
# @Date:                2019-07-10 08:37:22
# @Last Modified by:    AlanWang
# @Last Modified time:  2019-07-10 11:50:04
from datetime import datetime
from board import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)