#!/usr/bin/env python3
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem, QDesktopWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QTextDocument, QImage, QPixmap
from PyQt5.QtMultimedia import QSound
from main import Ui_MainWindow as mainWindow
from cam import Ui_MainWindow as camWindow
from datetime import datetime, date
import paho.mqtt.client as mqtt
import cv2
import mysql.connector
import os
import sys
import getpass
import random
import string


user = getpass.getuser()

if sys.platform == 'win32':
    messages_dir = 'C:/Users/{}/AppData/Local/kontrol/'.format(user)
    messages_path = 'C:/Users/{}/AppData/Local/kontrol/messages'.format(user)
elif sys.platform == 'linux':
    messages_dir = os.path.relpath(
        '/home/{}/.local/share/kontrol/'.format(user))
    messages_path = os.path.relpath(
        '/home/{}/.local/share/kontrol/messages'.format(user))

if getattr(sys, 'frozen', False):
    # frozen
    dir_ = os.path.dirname(sys.executable)
else:
    # unfrozen
    dir_ = os.path.dirname(os.path.realpath(__file__))


def on_message(client, userdata, message):
    msg = str(message.payload.decode('utf-8'))
    msg_list = msg.split('!')
    if msg_list[len(msg_list) - 1] == '':
        del msg_list[len(msg_list) - 1]
    with open(messages_path, 'w') as op:
        for l in msg_list:
            op.write(l + message.topic + '\n')
        op.close()


class get_message(QThread):

    signal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(get_message, self).__init__(parent)

    def run(self):
        while True:
            with open(messages_path, 'r') as op:
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

                elif 'alarm_cb' in line:
                    topic = 'alarm_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)
            open(messages_path, 'w')
            self.msleep(250)


class Camera(QMainWindow, camWindow):

    signal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(Camera, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setMaximumSize(1280, 720)
        self.image = None
        self.stream_url = 'rtsp://192.168.1.13:554/ucast/11'
        rect = QDesktopWidget().availableGeometry()
        self.screen_h = rect.height()
        self.screen_w = rect.width()

    def closeEvent(self, event):
        self.stop_camera()
        self.signal.emit('stop', 'camera')
        event.accept()

    def start_stream(self):
        self.capture = cv2.VideoCapture(self.stream_url)
        if self.capture.isOpened():
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(5)
            self.signal.emit('stream', 'camera')
        else:
            self.imgLabel.setText('Camera is not available!')
            self.signal.emit('sleep', 'camera')

    def update_frame(self):
        ret, self.image = self.capture.read()
        if self.screen_w <= 1280:
            screen_w = self.screen_w
        else:
            screen_w = 1280
        r = screen_w / self.image.shape[1]
        screen_h = int(self.image.shape[0] * r)
        if screen_h <= self.screen_h:
            self.dim = (screen_w, screen_h)
        else:
            self.dim = (screen_w, 720)

        self.resized = cv2.resize(
            self.image, self.dim, interpolation=cv2.INTER_AREA)
        self.displayImage(self.resized, 1)
        self.setMinimumSize(self.dim[0], self.dim[1])

    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:

            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(
            img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        if window == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))

    def start_record(self):
        self.capture = cv2.VideoCapture(self.stream_url)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        if self.capture.isOpened():
            self.out = cv2.VideoWriter(
                '{}.avi'.format(date.strftime(
                    datetime.now(), '%Y%m%d_%H%M%S')),
                self.fourcc, 10.0, (1280, 720))
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.save_record)
            self.timer.start(5)
            self.signal.emit('record', 'camera')
        else:
            self.signal.emit('sleep', 'camera')

    def save_record(self):
        ret, image = self.capture.read()
        self.out.write(image)

    def stop_camera(self):
        try:
            self.out.release()
            self.timer.stop()
        except Exception:
            pass


class MainApp(QMainWindow, mainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.file_dir()
        self.random_id()
        self.connect()
        self.conf_ui()
        self.conf_buttons()
        self.conf_sliders()
        self.dialog = Camera()
        self.dialog.signal.connect(self.conf_labels)
        self.thread = get_message()
        self.thread.start()
        self.thread.signal.connect(self.conf_labels)

    def keyPressEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
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
        if sys.platform == 'win32':
            os.system('taskkill /f /im kontrol.exe')
        elif sys.platform == 'linux':
            os.system('pkill kontrol')
        event.accept()

    def file_dir(self):
        if not os.path.exists(messages_dir):
            os.makedirs(messages_dir)
        open(messages_path, 'w')

    def random_id(self):
        s = string.ascii_letters + string.digits
        self.client_id = ''.join(random.sample(s, 10))

    def connect(self):
        self.mqttc = mqtt.Client(self.client_id)
        try:
            self.mqttc.connect('localhost')
        except Exception:
            QMessageBox.information(
                self, 'Information',
                'Can\'t connect to MQTT Broker', QMessageBox.Ok)
        self.mqttc.on_message = on_message
        self.mqttc.loop_start()
        self.mqttc.subscribe([
            ('indoor_light_cb', 1), ('indoor_fan_cb', 1), ('indoor_air_cb', 1),
            ('indoor_curtain_cb', 1), ('indoor_door_cb', 1),
            ('indoor_temp_cb', 1), ('outdoor_light_cb', 1),
            ('irrigation_cb', 1), ('alarm_cb', 1),
            ('outdoor_temp_cb', 1), ('outdoor_hum_cb', 1),
            ('indoor_alarm_cb', 1), ('outdoor_alarm_cb', 1)])

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
        self.refresh_button.clicked.connect(self.db)

        # Camera
        self.stream_button.clicked.connect(self.button_stream)
        self.record_button.clicked.connect(self.button_record)
        self.stream_record_button.clicked.connect(self.button_stream_record)
        self.stop_camera_button.clicked.connect(self.button_stop_camera)

    # Camera
    def button_stream(self):
        self.dialog.start_stream()
        self.dialog.show()

    def button_record(self):
        self.dialog.start_record()

    def button_stream_record(self):
        self.button_stream()
        self.button_record()

    def button_stop_camera(self):
        self.dialog.stop_camera()
        self.dialog.close()

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
        if sys.platform == 'win32':
            song_path = 'C:/Program Files (x86)/kontrol/alarm.wav'
        elif sys.platform == 'linux':
            song_path = '/home/amr/projects/kontrol/alarm.wav'
        song = QSound(song_path)
        song.setLoops(-1)
        song.play()
        reply = QMessageBox.warning(None, 'Alarm', msg, QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            song.stop()

    def conf_labels(self, msg, topic):
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

            if int(msg) > 22 and int(msg) < 28:
                self.in_temp_label.setText(
                    '<p style="color:#2E7D32">{}°</p>'.format(msg))
            elif int(msg) <= 22:
                self.in_temp_label.setText(
                    '<p style="color:#1565C0">{}°</p>'.format(msg))
            elif int(msg) >= 28:
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

            if int(msg) >= 23 and int(msg) <= 27:
                self.out_temp_label.setText(
                    '<p style="color:#2E7D32">{}°</p>'.format(msg))
            elif int(msg) <= 22:
                self.out_temp_label.setText(
                    '<p style="color:#1565C0">{}°</p>'.format(msg))
            elif int(msg) >= 28:
                self.out_temp_label.setText(
                    '<p style="color:#C62828">{}°</p>'.format(msg))

        elif topic == 'outdoor_hum_cb':

            if int(msg) >= 45 and int(msg) <= 55:
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

        elif topic == 'alarm_cb':
            self.alarm(msg)

        elif topic == 'camera':

            if msg == 'stream':
                self.out_camera_label.setText(
                    '<p style="color:#2E7D32">Streaming</p>')
            elif msg == 'record':
                self.out_camera_label.setText(
                    '<p style="color:#2E7D32">Recording</p>')
            elif msg == 'sleep':
                self.out_camera_label.setText(
                    '<p style="color:#C62828">Sleeping</p>')
            elif msg == 'stop':
                self.button_stop_camera()

    def db(self):
        row = 0
        col_aname = 0
        col_code = 1
        col_year = 2
        col_uid = 3
        col_s1 = 4
        col_s2 = 5
        col_s3 = 6
        col_s4 = 7
        col_s5 = 8

        cnx = mysql.connector.connect(
            user='amr', password='nowayout',
            host='192.168.1.11', database='assc')
        cursor = cnx.cursor()
        get_code = ("""SELECT aname, uid, code, year, s1, s2, s3,
                    s4, s5 FROM students""")
        cursor.execute(get_code)
        for (aname, uid, code, year, s1, s2, s3, s4, s5) in cursor:
            self.table.setItem(row, col_code, QTableWidgetItem(str(code)))
            self.table.setItem(row, col_year, QTableWidgetItem(str(year)))
            self.table.setItem(row, col_uid, QTableWidgetItem(str(uid)))
            self.table.setItem(row, col_aname, QTableWidgetItem(str(aname)))
            self.table.setItem(row, col_s1, QTableWidgetItem(str(s1)))
            self.table.setItem(row, col_s2, QTableWidgetItem(str(s2)))
            self.table.setItem(row, col_s3, QTableWidgetItem(str(s3)))
            self.table.setItem(row, col_s4, QTableWidgetItem(str(s4)))
            self.table.setItem(row, col_s5, QTableWidgetItem(str(s5)))
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
