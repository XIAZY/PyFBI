#!/usr/bin/env python3
import os
import socket
import struct
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

from ui import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_add.clicked.connect(self.add_cia)
        self.pushButton_install.clicked.connect(self.install_cia)
        self.lineEdit_ip.returnPressed.connect(self.install_cia)

    def add_cia(self):
        file_name = QFileDialog.getOpenFileName(self, 'Select CIA', '~', '*.cia')[0]
        if file_name:
            self.listWidget.addItem(file_name)

    def install_cia(self):
        self.listWidget.setDisabled(True)
        self.spinBox_port.setDisabled(True)
        self.lineEdit_ip.setDisabled(True)
        self.pushButton_add.setDisabled(True)
        self.pushButton_install.setDisabled(True)
        file_list = []
        for i in range(self.listWidget.count()):
            file_list.append(self.listWidget.item(i).text())
        ip = self.lineEdit_ip.text()
        port = int(self.spinBox_port.text())
        try:
            if not file_list:
                raise UserWarning('No file selected')
            if not ip:
                raise UserWarning('No IP entered')
            self.work = WorkingThread(file_list, ip, port)
            self.work.status_report_signal.connect(self.status_receive_signal)
            self.work.progress_report_signal.connect(self.progress_receive_signal)
            self.work.stop_signal.connect(self.stop_signal)
            self.work.start()
        except ConnectionRefusedError as e:
            self.stop_signal('%s. Is FBI running?' % e)
        except ConnectionResetError as e:
            self.stop_signal('%s. Connection closed by FBI.' % e)
        except OSError as e:
            self.stop_signal('%s. No route to host.' % e)
        except UserWarning as e:
            self.stop_signal('%s' % e)

    def status_receive_signal(self, text):
        self.statusbar.showMessage(text)

    def progress_receive_signal(self, progress):
        self.progressBar.setValue(int(progress))

    def stop_signal(self, text):
        self.listWidget.setEnabled(True)
        self.spinBox_port.setEnabled(True)
        self.pushButton_add.setEnabled(True)
        self.pushButton_install.setEnabled(True)
        self.lineEdit_ip.setEnabled(True)
        self.statusbar.showMessage(text)


class WorkingThread(QThread):
    status_report_signal = pyqtSignal(str)
    progress_report_signal = pyqtSignal(float)
    stop_signal = pyqtSignal(str)

    def __init__(self, file_list, ip, port):
        super(WorkingThread, self).__init__()
        self.file_list = file_list
        self.ip = ip
        self.port = port

    def run(self):
        file_count = len(self.file_list)
        file_count_msg = struct.pack('>L', file_count)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.ip, self.port))
        sock.send(file_count_msg)
        for file_name in self.file_list:
            ack = sock.recv(1)
            if ack == b'\x01':
                file_size = os.path.getsize(file_name)
                file_size_msg = struct.pack('>Q', file_size)
                sock.send(file_size_msg)
                with open(file_name, 'rb') as f:
                    progress = 0
                    while True:
                        chunk = f.read(131072)
                        if not chunk:
                            break
                        # yield (file_name, sock.send(chunk) / file_size * 100)
                        progress += (sock.send(chunk) / file_size * 100)
                        self.progress_report_signal.emit(progress)
                        self.status_report_signal.emit('Sending %s' % file_name)
            else:
                self.stop_signal.emit('Operation cancelled by FBI')
        self.stop_signal.emit('All Done!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
