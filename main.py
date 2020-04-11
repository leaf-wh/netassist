# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, session, request, copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
import json
from threading import Lock

import socket_client
import socket_server


app = Flask(__name__)  # 实例化app对象
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
testInfo = {}

sc = socket_client.socket_client()
ss = socket_server.socket_server()


@app.route('/')
@app.route('/index')
def index():
    return render_template('test.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    # socket_send.server_send('testtest')
    if request.method == 'POST':
        protocol = request.form['porttype']
        rev = request.form['data']
        status = protocol
        if (status == "TCP Server"):
            #result = ss.send(rev) + "\n"
            ss.send(rev)
        elif (status == "TCP Client"):
            #result = sc.send(rev) + "\n" 
            sc.send(rev)   
        #return jsonify(result)
    else:
        return render_template('test.html')


@app.route('/init', methods=['GET', 'POST'])
def init():
    if request.method == 'POST':
        protocol = request.form['porttype']
        address = request.form['portaddress']
        port = request.form['portNO']
        if (protocol == "TCP Server"):
            ss.initport(address, port)
            print("server mode")
        elif (protocol == "TCP Client"):
            sc.initport(address, port)
            print("client mode")
        return jsonify(True)
    else:
        return render_template('test.html')

@socketio.on('imessage', namespace='/test_conn')
def test_message(porttype):
    while True:
        if (porttype == "TCP Server"):
            data = ss.recv() + "\n"
            emit('message', data, broadcast=True)
            print("server mode")
        elif (porttype == "TCP Client"):
            data = sc.recv() + "\n"
            emit('message', data, broadcast=True)
            print("client mode")      
    

@app.route('/close', methods=['GET', 'POST'])
def close():
    if request.method == 'POST':
        protocol = request.form['porttype']
        if (protocol == "TCP Server"):
            ss.closeport()
            print("close server mode")
        elif (protocol == "TCP Client"):
            sc.closeport()
            print("close client mode")
        return jsonify(True)
    else:
        return render_template('test.html')


if __name__ == '__main__':
    socketio.run(app, debug=False)
