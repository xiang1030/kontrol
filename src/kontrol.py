#!/usr/bin/env python3
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtWidgets import QTableWidgetItem, QDesktopWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QTextDocument, QImage, QPixmap, QIcon
from PyQt5.QtMultimedia import QSound
from main import Ui_MainWindow
from datetime import datetime, date
from threading import Thread
import paho.mqtt.client as mqtt
import cv2
import mysql.connector
import os
import sys
import getpass
import random
import string
import time

user = getpass.getuser()

# declare paths
if sys.platform == 'win32':
    messages_dir = 'C:/Users/{}/AppData/Local/kontrol'.format(user)
    messages_path = 'C:/Users/{}/AppData/Local/kontrol/messages'.format(user)
    alarms_path = 'C:/Users/{}/AppData/Local/kontrol/alarms'.format(user)
    audio_path = os.path.dirname(os.path.realpath(__file__)) + '\\alarm.wav'
    videos_dir = 'C:/Users/{}/Videos/Surveillance'.format(user)
elif sys.platform == 'linux':
    messages_dir = os.path.relpath(
        '/home/{}/.local/share/kontrol'.format(user))
    messages_path = os.path.relpath(
        '/home/{}/.local/share/kontrol/messages'.format(user))
    alarms_path = os.path.relpath(
        '/home/{}/.local/share/kontrol/alarms'.format(user))
    audio_path = os.path.dirname(os.path.realpath(__file__)) + '/alarm.wav'
    videos_dir = os.path.relpath(
        '/home/{}/Videos/Surveillance'.format(user))


def on_message(client, userdata, message):
    msg = str(message.payload.decode('utf-8'))
    if message.topic == 'alarm_cb':
        op = open(alarms_path, 'w')
        op.write(msg + '\n')
        op.close()
    else:
        op = open(messages_path, 'w')
        op.write(msg + message.topic + '\n')
        op.close()


class GetMessage(QThread):

    signal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(GetMessage, self).__init__(parent)

    def run(self):
        while True:
            op = open(messages_path, 'r')
            message = op.readlines()
            op.close()
            for line in message:
                if 'indoor_light_cb' in line:
                    topic = 'indoor_light_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'indoor_fan_cb' in line:
                    topic = 'indoor_fan_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'indoor_air_cb' in line:
                    topic = 'indoor_air_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'indoor_curtain_cb' in line:
                    topic = 'indoor_curtain_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'indoor_door_cb' in line:
                    topic = 'indoor_door_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)

                elif 'indoor_temp_cb' in line:
                    topic = 'indoor_temp_cb'
                    msg = line.replace('indoor_temp_cb', '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)

                elif 'indoor_alarm_cb' in line:
                    topic = 'indoor_alarm_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)

                elif 'outdoor_light_cb' in line:
                    topic = 'outdoor_light_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'irrigation' in line:
                    topic = 'irrigation_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'outdoor_temp_cb' in line:
                    topic = 'outdoor_temp_cb'
                    msg = line.replace('outdoor_temp_cb', '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)

                elif 'outdoor_hum_cb' in line:
                    topic = 'outdoor_hum_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)

                elif 'outdoor_alarm_cb' in line:
                    topic = 'outdoor_alarm_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)
            open(messages_path, 'w')
            self.msleep(50)


class FireAlarm(QThread):

    signal = pyqtSignal(str, str)

    def __init__(self):
        super(FireAlarm, self).__init__()
        self.fire = True

    def run(self):
        while True:
            op = open(alarms_path, 'r')
            message = op.readlines()
            op.close()
            for line in message:
                if 'Fire' in line:
                    self.fire = True
                    while self.fire:
                        self.signal.emit('alarm', 'alarm_anime')
                        self.signal.emit('fire_red', 'alarm_anime')
                        self.msleep(500)
                        self.signal.emit('fire_blue', 'alarm_anime')
                        self.msleep(500)
                    self.signal.emit('fire_green', 'alarm_anime')
            self.msleep(50)

    def stop(self):
        open(alarms_path, 'w')
        self.fire = False


class WaterAlarm(QThread):

    signal = pyqtSignal(str, str)

    def __init__(self):
        super(WaterAlarm, self).__init__()
        self.water = True

    def run(self):
        while True:
            op = open(alarms_path, 'r')
            message = op.readlines()
            op.close()
            for line in message:
                if 'Water' in line:
                    self.water = True
                    while self.water:
                        self.signal.emit('alarm', 'alarm_anime')
                        self.signal.emit('water_red', 'alarm_anime')
                        self.msleep(500)
                        self.signal.emit('water_blue', 'alarm_anime')
                        self.msleep(500)
                    self.signal.emit('water_green', 'alarm_anime')
            self.msleep(50)

    def stop(self):
        open(alarms_path, 'w')
        self.water = False


class GasAlarm(QThread):

    signal = pyqtSignal(str, str)

    def __init__(self):
        super(GasAlarm, self).__init__()
        self.gas = True

    def run(self):
        while True:
            op = open(alarms_path, 'r')
            message = op.readlines()
            op.close()
            for line in message:
                if 'Gas' in line:
                    self.gas = True
                    self.signal.emit('alarm', 'alarm_anime')
                    while self.gas:
                        self.signal.emit('gas_red', 'alarm_anime')
                        self.msleep(500)
                        self.signal.emit('gas_blue', 'alarm_anime')
                        self.msleep(500)
                    self.signal.emit('gas_green', 'alarm_anime')
            self.msleep(50)

    def stop(self):
        open(alarms_path, 'w')
        self.gas = False


class MotionAlarm(QThread):

    signal = pyqtSignal(str, str)

    def __init__(self):
        super(MotionAlarm, self).__init__()
        self.motion = True

    def run(self):
        while True:
            op = open(alarms_path, 'r')
            message = op.readlines()
            op.close()
            for line in message:
                if 'Motion' in line:
                    self.motion = True
                    self.signal.emit('alarm', 'alarm_anime')
                    while self.motion:
                        self.signal.emit('motion_red', 'alarm_anime')
                        self.msleep(500)
                        self.signal.emit('motion_blue', 'alarm_anime')
                        self.msleep(500)
                    self.signal.emit('motion_green', 'alarm_anime')
            self.msleep(50)

    def stop(self):
        open(alarms_path, 'w')
        self.motion = False


class LaserAlarm(QThread):

    signal = pyqtSignal(str, str)

    def __init__(self):
        super(LaserAlarm, self).__init__()
        self.laser = True

    def run(self):
        while True:
            op = open(alarms_path, 'r')
            message = op.readlines()
            op.close()
            for line in message:
                if 'Laser' in line:
                    self.laser = True
                    self.signal.emit('alarm', 'alarm_anime')
                    while self.laser:
                        self.signal.emit('laser_red', 'alarm_anime')
                        self.msleep(500)
                        self.signal.emit('laser_blue', 'alarm_anime')
                        self.msleep(500)
                    self.signal.emit('laser_green', 'alarm_anime')
            self.msleep(50)

    def stop(self):
        open(alarms_path, 'w')
        self.laser = False


class Record(QThread):

    signal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(Record, self).__init__(parent)
        self.isRunning = True
        self.out = None

    def run(self):
        self.isRunning = True
        stream_url = 'rtsp://192.168.1.100:554/ucast/11'
        capture = cv2.VideoCapture(stream_url)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video_date = date.strftime(datetime.now(), '%Y%m%d_%H%M%S')
        video_name = '{}.avi'.format(video_date)
        video_dist = videos_dir + '/' + video_name
        if capture.isOpened():
            self.out = cv2.VideoWriter(video_name, fourcc, 10.0, (1280, 720))
            while self.isRunning:
                if date.strftime(datetime.now(), '%H:%M:%S') == '23:59:59':
                    self.signal.emit('restart', 'camera')
                    break
                ret, image = capture.read()
                self.out.write(image)
                self.signal.emit('record', 'camera')
                time.sleep(0.01)
            self.signal.emit('sleep', 'camera')
        else:
            self.signal.emit('nocam', 'camera')
        if sys.platform == 'win32':
            video_src = os.getcwd() + '\\' + video_name
            os.system("move {} {}".format(video_src, video_dist))
        elif sys.platform == 'linux':
            video_src = os.getcwd() + '/' + video_name
            os.system("mv {} {}".format(video_src, video_dist))

    def stop(self):
        try:
            self.out.release()
        except Exception:
            pass
        self.isRunning = False
        self.quit()
        self.wait()


class Stream(QThread):

    signal = pyqtSignal(str, str)
    changePixmap = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        super(Stream, self).__init__(parent)
        self.isRunning = True

    def run(self):
        self.isRunning = True
        stream_url = 'rtsp://192.168.1.100:554/ucast/11'
        capture = cv2.VideoCapture(stream_url)
        geo = QDesktopWidget().availableGeometry()
        if capture.isOpened():
            self.signal.emit('stream', 'camera')
            while self.isRunning:
                ret, image = capture.read()
                if geo.width() <= 1280:
                    screen_w = geo.width()
                else:
                    screen_w = 1280
                r = screen_w / image.shape[1]
                screen_h = int(image.shape[0] * r)
                if screen_h <= geo.height():
                    dim = (screen_w, screen_h)
                else:
                    dim = (screen_w, 720)
                resized = cv2.resize(
                    image, dim, interpolation=cv2.INTER_AREA)
                qformat = QImage.Format_Indexed8
                if len(resized.shape) == 3:
                    if resized.shape[2] == 4:
                        qformat = QImage.Format_RGBA8888
                    else:
                        qformat = QImage.Format_RGB888
                outImage = QImage(
                    resized, resized.shape[1],
                    resized.shape[0], resized.strides[0], qformat)
                outImage = outImage.rgbSwapped()
                outPixmap = QPixmap.fromImage(outImage)
                self.changePixmap.emit(outPixmap)
                time.sleep(0.01)
            self.signal.emit('sleep', 'camera')
        else:
            self.signal.emit('nocam', 'camera')

    def stop(self):
        self.isRunning = False
        self.quit()
        self.wait()


class Camera(QLabel):

    signal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(Camera, self).__init__(parent)
        QLabel.__init__(self)
        self.setFixedSize(1280, 720)
        icon = QIcon()
        icon.addPixmap(
            QPixmap(":/icons/png/kontrol_24.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

    def closeEvent(self, event):
        self.signal.emit('close', 'camera')
        event.accept()

    def viewImage(self, outPixmap):
        self.setPixmap(outPixmap)


class MainApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.make_dirs()
        self.random_id()
        self.conf_ui()
        self.conf_buttons()
        self.conf_sliders()
        # connect to mqtt broker
        self.t = Thread(target=self.connect)
        self.t.start()
        self.quit = False
        # initialize camera
        self.cam = Camera()
        self.cam.signal.connect(self.conf_labels)
        # initialize stream thread
        self.st = Stream()
        self.st.signal.connect(self.conf_labels)
        self.st.changePixmap.connect(self.cam.viewImage)
        # initialize record thread
        self.rec = Record()
        self.rec.signal.connect(self.conf_labels)
        # start message thread
        self.thread = GetMessage()
        self.thread.start()
        self.thread.signal.connect(self.conf_labels)
        # start FireAlarm
        self.falarm = FireAlarm()
        self.falarm.start()
        self.falarm.signal.connect(self.conf_labels)
        # start WaterAlarm
        self.walarm = WaterAlarm()
        self.walarm.start()
        self.walarm.signal.connect(self.conf_labels)
        # start GasAlarm
        self.galarm = GasAlarm()
        self.galarm.start()
        self.galarm.signal.connect(self.conf_labels)
        # start MotionAlarm
        self.malarm = MotionAlarm()
        self.malarm.start()
        self.malarm.signal.connect(self.conf_labels)
        # start LaserAlarm
        self.lalarm = LaserAlarm()
        self.lalarm.start()
        self.lalarm.signal.connect(self.conf_labels)
        self.alarm_status = 'off'

    def keyPressEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        if event.key() == Qt.Key_Space:
            self.button_fire()
            self.button_water()
            self.button_gas()
            self.button_motion()
            self.button_laser()
        if modifiers == Qt.AltModifier:
            if event.key() == Qt.Key_1:
                self.tabWidget.setCurrentIndex(0)
            elif event.key() == Qt.Key_2:
                self.tabWidget.setCurrentIndex(1)
            elif event.key() == Qt.Key_3:
                self.tabWidget.setCurrentIndex(2)
            elif event.key() == Qt.Key_4:
                self.tabWidget.setCurrentIndex(3)
            elif event.key() == Qt.Key_5:
                self.tabWidget.setCurrentIndex(4)

    def closeEvent(self, event):
        self.button_stop_camera()
        self.falarm.quit()
        self.walarm.quit()
        self.galarm.quit()
        self.malarm.quit()
        self.lalarm.quit()
        self.quit = True
        event.accept()

    def make_dirs(self):
        if not os.path.exists(messages_dir):
            os.makedirs(messages_dir)
        if not os.path.exists(videos_dir):
            os.makedirs(videos_dir)
        open(messages_path, 'w')
        open(alarms_path, 'w')

    def random_id(self):
        s = string.ascii_letters + string.digits
        self.client_id = ''.join(random.sample(s, 7))

    def connect(self):
        self.mqttc = mqtt.Client(self.client_id)
        while not self.quit:
            try:
                self.mqttc.connect('192.168.1.10')
            except Exception:
                print('[MQTT]: Connection failed')
                print('[MQTT]: Reconnecting ...')
                time.sleep(5)
            else:
                self.mqttc.on_message = on_message
                self.mqttc.loop_start()
                self.mqttc.subscribe([
                    ('indoor_light_cb', 1), ('indoor_fan_cb', 1),
                    ('indoor_air_cb', 1), ('indoor_curtain_cb', 1),
                    ('indoor_door_cb', 1), ('indoor_alarm_cb', 1),
                    ('indoor_temp_cb', 1), ('outdoor_light_cb', 1),
                    ('irrigation_cb', 1), ('alarm_cb', 1),
                    ('outdoor_temp_cb', 1), ('outdoor_hum_cb', 1),
                    ('outdoor_alarm_cb', 1)])
                break

    def conf_ui(self):
        self.setFixedSize(911, 547)

    def conf_buttons(self):
        # indoor
        self.in_light_on_button.clicked.connect(self.button_in_light_on)
        self.in_light_off_button.clicked.connect(self.button_in_light_off)
        self.in_light_auto_button.clicked.connect(self.button_in_light_auto)
        self.in_fan_on_button.clicked.connect(self.button_in_fan_on)
        self.in_fan_off_button.clicked.connect(self.button_in_fan_off)
        self.in_fan_auto_button.clicked.connect(self.button_in_fan_auto)
        self.in_air_on_button.clicked.connect(self.button_in_air_on)
        self.in_air_off_button.clicked.connect(self.button_in_air_off)
        self.in_air_auto_button.clicked.connect(self.button_in_air_auto)
        self.in_curtain_on_button.clicked.connect(self.button_in_curtain_on)
        self.in_curtain_off_button.clicked.connect(self.button_in_curtain_off)
        self.in_curtain_auto_button.clicked.connect(
            self.button_in_curtain_auto)
        self.in_door_open_button.clicked.connect(self.button_in_door_open)
        self.in_door_close_button.clicked.connect(self.button_in_door_close)
        self.in_open_button.clicked.connect(self.button_in_open)
        self.in_close_button.clicked.connect(self.button_in_close)
        self.in_alarm_button.clicked.connect(self.button_in_alarm)

        # outdoor
        self.out_light_on_button.clicked.connect(self.button_out_light_on)
        self.out_light_off_button.clicked.connect(self.button_out_light_off)
        self.out_light_auto_button.clicked.connect(self.button_out_light_auto)
        self.out_irri_on_button.clicked.connect(self.button_out_irri_on)
        self.out_irri_off_button.clicked.connect(self.button_out_irri_off)
        self.out_irri_auto_button.clicked.connect(self.button_out_irri_auto)
        self.out_open_button.clicked.connect(self.button_out_open)
        self.out_close_button.clicked.connect(self.button_out_close)
        self.out_alarm_button.clicked.connect(self.button_out_alarm)

        # message
        self.message_send_button.clicked.connect(self.button_message_send)
        self.message_clear_button.clicked.connect(self.button_message_clear)

        # database
        self.refresh_button.clicked.connect(self.button_refresh)

        # camera
        self.stream_button.clicked.connect(self.button_stream)
        self.record_button.clicked.connect(self.button_record)
        self.stream_record_button.clicked.connect(self.button_stream_record)
        self.stop_camera_button.clicked.connect(self.button_stop_camera)

        # alarms
        self.fire_button.clicked.connect(self.button_fire)
        self.water_button.clicked.connect(self.button_water)
        self.gas_button.clicked.connect(self.button_gas)
        self.motion_button.clicked.connect(self.button_motion)
        self.laser_button.clicked.connect(self.button_laser)

    # camera
    def button_stream(self):
        self.st.start()

    def button_record(self):
        self.rec.start()

    def button_stream_record(self):
        self.button_stream()
        self.button_record()

    def button_stop_camera(self):
        self.st.stop()
        self.rec.stop()
        self.cam.close()

    # alarms
    def button_fire(self):
        self.falarm.stop()
        self.alarm('stop')

    def button_water(self):
        self.walarm.stop()
        self.alarm('stop')

    def button_gas(self):
        self.galarm.stop()
        self.alarm('stop')

    def button_motion(self):
        self.malarm.stop()
        self.alarm('stop')

    def button_laser(self):
        self.lalarm.stop()
        self.alarm('stop')

    # database
    def button_refresh(self):
        t = Thread(target=self.database)
        t.start()

    # indoor
    def button_in_light_on(self):
        self.mqttc.publish('indoor_light', '01')

    def button_in_light_off(self):
        self.mqttc.publish('indoor_light', '0')
        self.in_light_slider.setValue(0)

    def button_in_light_auto(self):
        self.mqttc.publish('indoor_light', '02')

    def button_in_fan_on(self):
        self.mqttc.publish('indoor_fan', '01')

    def button_in_fan_off(self):
        self.mqttc.publish('indoor_fan', '0')
        self.in_fan_slider.setValue(0)

    def button_in_fan_auto(self):
        self.mqttc.publish('indoor_fan', '02')

    def button_in_air_on(self):
        self.mqttc.publish('indoor_air', '01')

    def button_in_air_off(self):
        self.mqttc.publish('indoor_air', '0')

    def button_in_air_auto(self):
        self.mqttc.publish('indoor_air', '02')

    def button_in_curtain_on(self):
        self.mqttc.publish('indoor_curtain', '01')

    def button_in_curtain_off(self):
        self.mqttc.publish('indoor_curtain', '0')

    def button_in_curtain_auto(self):
        self.mqttc.publish('indoor_curtain', '02')

    def button_in_door_open(self):
        self.mqttc.publish('indoor_door', '01')

    def button_in_door_close(self):
        self.mqttc.publish('indoor_door', '0')

    def button_in_open(self):
        self.button_in_light_on()
        self.button_in_fan_on()
        self.button_in_curtain_on()
        self.button_in_air_on()

    def button_in_close(self):
        self.button_in_light_off()
        self.button_in_fan_off()
        self.button_in_curtain_off()
        self.button_in_air_off()

    def button_in_alarm(self):
        doc = QTextDocument()
        doc.setHtml(self.in_alarm_label.text())
        if doc.toPlainText() == 'Active':
            self.mqttc.publish('indoor_alarm', '0')
        else:
            self.mqttc.publish('indoor_alarm', '01')

    # Outdoor
    def button_out_light_on(self):
        self.mqttc.publish('outdoor_light', '01')

    def button_out_light_off(self):
        self.mqttc.publish('outdoor_light', '0')
        self.out_light_slider.setValue(0)

    def button_out_light_auto(self):
        self.mqttc.publish('outdoor_light', '02')

    def button_out_irri_on(self):
        self.mqttc.publish('irrigation', '01')

    def button_out_irri_off(self):
        self.mqttc.publish('irrigation', '0')
        self.out_irri_slider.setValue(0)

    def button_out_irri_auto(self):
        self.mqttc.publish('irrigation', '02')

    def button_message_send(self):
        self.mqttc.publish('message', self.message_text.toPlainText())

    def button_message_clear(self):
        self.message_text.setText('')

    def button_out_open(self):
        self.button_out_light_on()
        self.button_out_irri_on()

    def button_out_close(self):
        self.button_out_light_off()
        self.button_out_irri_off()

    def button_out_alarm(self):
        doc = QTextDocument()
        doc.setHtml(self.out_alarm_label.text())
        if doc.toPlainText() == 'Active':
            self.mqttc.publish('outdoor_alarm', '0')
        else:
            self.mqttc.publish('outdoor_alarm', '01')

    def conf_sliders(self):
        self.in_light_slider.sliderReleased.connect(self.slider_in_light)
        self.in_fan_slider.sliderReleased.connect(self.slider_in_fan)
        self.out_light_slider.sliderReleased.connect(self.slider_out_light)
        self.out_irri_slider.sliderReleased.connect(self.slider_out_irri)
        self.in_light_slider.valueChanged.connect(self.slider_in_light_)
        self.in_fan_slider.valueChanged.connect(self.slider_in_fan_)
        self.out_light_slider.valueChanged.connect(self.slider_out_light_)
        self.out_irri_slider.valueChanged.connect(self.slider_out_irri_)
        self.in_air_spinbox.valueChanged.connect(self.spin_ra)

    def slider_in_light(self):
        self.mqttc.publish('indoor_light', int(self.in_light_slider.value()))

    def slider_in_light_(self):
        self.in_light_percentage.setText(
            str(self.in_light_slider.value()) + '%')

    def slider_in_fan(self):
        self.mqttc.publish('indoor_fan', int(self.in_fan_slider.value()))

    def slider_in_fan_(self):
        self.in_fan_percentage.setText(str(self.in_fan_slider.value()) + '%')

    def slider_out_light(self):
        self.mqttc.publish('outdoor_light', int(self.out_light_slider.value()))

    def slider_out_light_(self):
        self.out_light_percentage.setText(
            str(self.out_light_slider.value()) + '%')

    def slider_out_irri(self):
        self.mqttc.publish('irrigation', int(self.out_irri_slider.value()))

    def slider_out_irri_(self):
        self.out_irri_percentage.setText(
            str(self.out_irri_slider.value()) + '%')

    def spin_ra(self):
        self.mqttc.publish('indoor_air', self.in_air_spinbox.value())

    def alarm(self, msg):
        self.audio = QSound(audio_path)
        self.audio.setLoops(-1)
        if msg == 'start':
            self.audio.play()
            self.alarm_status = 'on'
        else:
            self.audio.stop()
            self.alarm_status = 'off'

    def conf_labels(self, msg, topic):

        red_style = 'QPushButton {background-color: #C62828;}'
        blue_style = 'QPushButton {background-color: #1565C0;}'
        green_style = 'QPushButton {background-color: #2E7D32;}'

        if topic == 'indoor_light_cb':

            if msg == 'ON':
                self.in_light_label.setText('<p style="color:#2E7D32">ON</p>')
                self.in_light_level_label.setText(
                    '<p style="color:#2E7D32">100%</p>')
            elif msg == 'OFF':
                self.in_light_label.setText('<p style="color:#C62828">OFF</p>')
                self.in_light_level_label.setText('-')
            elif msg == 'AUTO':
                self.in_light_label.setText(
                    '<p style="color:#1565C0">AUTO</p>')
                self.in_light_level_label.setText('-')
            else:
                self.in_light_label.setText('<p style="color:#2E7D32">ON</p>')
                self.in_light_level_label.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'indoor_fan_cb':

            if msg == 'ON':
                self.in_fan_label.setText('<p style="color:#2E7D32">ON</p>')
                self.in_fan_level_label.setText(
                    '<p style="color:#2E7D32">100%</p>')
            elif msg == 'OFF':
                self.in_fan_label.setText('<p style="color:#C62828">OFF</p>')
                self.in_fan_level_label.setText('-')
            elif msg == 'AUTO':
                self.in_fan_label.setText('<p style="color:#1565C0">AUTO</p>')
                self.in_fan_level_label.setText('-')
            else:
                self.in_fan_label.setText('<p style="color:#2E7D32">ON</p>')
                self.in_fan_level_label.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'indoor_air_cb':

            if msg == 'ON':
                self.in_air_label.setText('<p style="color:#2E7D32">ON</p>')
                self.in_air_level_label.setText(
                    '<p style="color:#2E7D32">21°</p>')
            elif msg == 'OFF':
                self.in_air_label.setText('<p style="color:#C62828">OFF</p>')
                self.in_air_level_label.setText('-')
            elif msg == 'AUTO':
                self.in_air_label.setText('<p style="color:#1565C0">AUTO</p>')
                self.in_air_level_label.setText('-')
            else:
                self.in_air_label.setText('<p style="color:#2E7D32">ON</p>')
                self.in_air_level_label.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'indoor_curtain_cb':

            if msg == 'ON':
                self.in_curtain_label.setText(
                    '<p style="color:#2E7D32">ON</p>')
            elif msg == 'OFF':
                self.in_curtain_label.setText(
                    '<p style="color:#C62828">OFF</p>')
            elif msg == 'AUTO':
                self.in_curtain_label.setText(
                    '<p style="color:#1565C0">AUTO</p>')

        elif topic == 'indoor_door_cb':

            if msg == 'ON':
                self.in_door_label.setText('<p style="color:#2E7D32">OPEN</p>')
            elif msg == 'OFF':
                self.in_door_label.setText(
                    '<p style="color:#C62828">CLOSED</p>')

        elif topic == 'indoor_temp_cb':

            msg = int(float(msg))
            if msg > 22 and msg < 28:
                self.in_temp_label.setText(
                    '<p style="color:#2E7D32">{}°</p>'.format(msg))
            elif msg <= 22:
                self.in_temp_label.setText(
                    '<p style="color:#1565C0">{}°</p>'.format(msg))
            elif msg >= 28:
                self.in_temp_label.setText(
                    '<p style="color:#C62828">{}°</p>'.format(msg))

        elif topic == 'indoor_alarm_cb':

            if msg == 'ON':
                self.in_alarm_label.setText(
                    '<p style="color:#2E7D32">Active</p>')
            elif msg == 'OFF':
                self.in_alarm_label.setText(
                    '<p style="color:#C62828">Inactive</p>')

        elif topic == 'outdoor_light_cb':

            if msg == 'ON':
                self.out_light_label.setText('<p style="color:#2E7D32">ON</p>')
                self.out_light_level_label.setText(
                    '<p style="color:#2E7D32">100%</p>')
            elif msg == 'OFF':
                self.out_light_label.setText(
                    '<p style="color:#C62828">OFF</p>')
                self.out_light_level_label.setText('-')
            elif msg == 'AUTO':
                self.out_light_label.setText(
                    '<p style="color:#1565C0">AUTO</p>')
                self.out_light_level_label.setText('-')
            else:
                self.out_light_label_setText('<p style="color:#2E7D32">ON</p>')
                self.out_light_level_label.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'irrigation_cb':

            if msg == 'ON':
                self.out_irri_label.setText('<p style="color:#2E7D32">ON</p>')
                self.out_irri_level_label.setText(
                    '<p style="color:#2E7D32">100%</p>')
            elif msg == 'OFF':
                self.out_irri_label.setText('<p style="color:#C62828">OFF</p>')
                self.out_irri_level_label.setText('-')
            elif msg == 'AUTO':
                self.out_irri_label.setText(
                    '<p style="color:#1565C0">AUTO</p>')
                self.out_irri_level_label.setText('-')
            else:
                self.out_irri_label.setText('<p style="color:#2E7D32">ON</p>')
                self.out_irri_level_label.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'outdoor_temp_cb':

            msg = int(float(msg))
            if msg >= 23 and msg <= 27:
                self.out_temp_label.setText(
                    '<p style="color:#2E7D32">{}°</p>'.format(msg))
            elif msg <= 22:
                self.out_temp_label.setText(
                    '<p style="color:#1565C0">{}°</p>'.format(msg))
            elif msg >= 28:
                self.out_temp_label.setText(
                    '<p style="color:#C62828">{}°</p>'.format(msg))

        elif topic == 'outdoor_hum_cb':

            msg = int(float(msg))
            if msg >= 45 and msg <= 55:
                self.out_hum_label.setText(
                    '<p style="color:#2E7D32">{}</p>'.format(msg))
            else:
                self.out_hum_label.setText(
                    '<p style="color:#C62828">{}</p>'.format(msg))

        elif topic == 'outdoor_alarm_cb':

            if msg == 'ON':
                self.out_alarm_label.setText(
                    '<p style="color:#2E7D32">Active</p>')
            elif msg == 'OFF':
                self.out_alarm_label.setText(
                    '<p style="color:#C62828">Inactive</p>')

        elif topic == 'alarm_anime':
            if msg == 'alarm':
                if self.alarm_status == 'off':
                    self.alarm('start')
            elif msg == 'fire_red':
                self.fire_button.setStyleSheet(red_style)
            elif msg == 'fire_blue':
                self.fire_button.setStyleSheet(blue_style)
            elif msg == 'fire_green':
                self.fire_button.setStyleSheet(green_style)
            elif msg == 'water_red':
                self.water_button.setStyleSheet(red_style)
            elif msg == 'water_blue':
                self.water_button.setStyleSheet(blue_style)
            elif msg == 'water_green':
                self.water_button.setStyleSheet(green_style)
            elif msg == 'gas_red':
                self.gas_button.setStyleSheet(red_style)
            elif msg == 'gas_blue':
                self.gas_button.setStyleSheet(blue_style)
            elif msg == 'gas_green':
                self.gas_button.setStyleSheet(green_style)
            elif msg == 'motion_red':
                self.motion_button.setStyleSheet(red_style)
            elif msg == 'motion_blue':
                self.motion_button.setStyleSheet(blue_style)
            elif msg == 'motion_green':
                self.motion_button.setStyleSheet(green_style)
            elif msg == 'laser_red':
                self.laser_button.setStyleSheet(red_style)
            elif msg == 'laser_blue':
                self.laser_button.setStyleSheet(blue_style)
            elif msg == 'laser_green':
                self.laser_button.setStyleSheet(green_style)

        elif topic == 'camera':

            if msg == 'record':
                self.out_camera_label.setText(
                    '<p style="color:#2E7D32">Recording</p>')
            elif msg == 'stream':
                self.out_camera_label.setText(
                    '<p style="color:#2E7D32">Recording</p>')
                self.cam.show()
            elif msg == 'sleep':
                self.out_camera_label.setText(
                    '<p style="color:#C62828">Sleeping</p>')
            elif msg == 'nocam':
                self.out_camera_label.setText(
                    '<p style="color:#C62828">Not Available</p>')
            elif msg == 'close':
                self.st.stop()
                self.cam.close()
            elif msg == 'restart':
                self.rec.stop()
                self.rec.start()

    def database(self):
        row = 0
        col_name = 0
        col_code = 1
        col_year = 2
        col_uid = 3
        col_s1 = 4
        col_s2 = 5
        col_s3 = 6
        col_s4 = 7
        col_s5 = 8

        try:
            cnx = mysql.connector.connect(
                user='normal', password='itisjustnormal1!',
                host='192.168.1.10', database='assc')
        except Exception:
            print('[MySQL]: Connection Failed')
        else:
            cursor = cnx.cursor()
            get_code = ("""SELECT aname, uid, code, year, s1, s2, s3,
                        s4, s5 FROM students""")
            cursor.execute(get_code)
            for (aname, uid, code, year, s1, s2, s3, s4, s5) in cursor:
                self.table.setItem(row, col_code, QTableWidgetItem(str(code)))
                self.table.setItem(row, col_year, QTableWidgetItem(str(year)))
                self.table.setItem(row, col_uid, QTableWidgetItem(uid))
                self.table.setItem(row, col_name, QTableWidgetItem(aname))
                self.table.setItem(row, col_s1, QTableWidgetItem(s1))
                self.table.setItem(row, col_s2, QTableWidgetItem(s2))
                self.table.setItem(row, col_s3, QTableWidgetItem(s3))
                self.table.setItem(row, col_s4, QTableWidgetItem(s4))
                self.table.setItem(row, col_s5, QTableWidgetItem(s5))
                row = row + 1
            cnx.commit()
            cursor.close()
            cnx.close()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
