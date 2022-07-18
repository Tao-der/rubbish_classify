from detect_ui import Ui_mainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
from tensorflow.keras.preprocessing import image
import threading
import os
from PIL import Image
from PyQt5.QtWidgets import *
import queue
import time
import datetime
from PIL import Image
import numpy as np
import cv2
import glob
from createdb import ObjectDB

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
import numpy as np
from tensorflow.keras.preprocessing import image
from train.resnet50 import ResNet50
from data_process.data_config import get_train_parent
import threading


import os
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

class MyThread(threading.Thread):

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None



class Detection_window(QtWidgets.QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(Detection_window, self).__init__()
        self.setupUi(self)
        self.slot_init()
        self.capture = None
        self.objectDB = ObjectDB()
        self.objectDB.createDb()
        self.objectDB.createTable()
        self.preview_video = ""#the path of the preview video

        self.cmera_confirmed = False
        self.show_preview = True
        self.capture = None

        self.needDetect = True
        self.category = ""  
        self.showData()
        self.showPreview()

        self.realdic = ['chuyu_qingcai', 'chuyu_suiguo', 'huishou_kuangquansui', 'huishou_yilaguan', 'qita_suibei', 'qita_yantou', 'youhai_battery']
        self.pinyin2hanzi = {"chuyu":"厨余垃圾","huishou":"可回收垃圾","qita":"其他垃圾","youhai":"有害垃圾"}
        self.SIZE = (224, 224)
        self.model = ResNet50(classes=7)
        self.model.load_weights("./weights/resnet50_best.h5", by_name=True)


    def slot_init(self):
        self.pushButton_start.clicked.connect(self.pushButton_start_callback)
        self.pushButton_stop.clicked.connect(self.pushButton_stop_callback)
     

    ls /dev/


    def pushButton_start_callback(self):
        self.cmera_confirmed = False
        self.show_preview = False
        self.label_video.setText("正在初始化运行环境，请稍等...")
        my_thread = threading.Thread(target=self.getCameraData) #,args=(label,rtmp,))
        my_thread.start()

    def pushButton_stop_callback(self):
        weight=str(0)
        nums = str(0)
        status = str("") ## those three items must input by outside !!!!!!
        self.objectDB.insertInto(self.category, weight, nums, status)
        self.showData()
        self.cmera_confirmed = True
        self.show_preview = True
        self.showPreview()

    def showPreview(self):
        previewthread = threading.Thread(target=self.realShowPreview)  # ,args=(label,rtmp,))
        previewthread.start()

    def realShowPreview(self):
        if self.preview_video== "":
            return
        self.capture = cv2.VideoCapture(self.preview_video)
        if not self.capture.isOpened():
            raise IOError("Couldn't open camera or video")
        while self.show_preview:
            if weight > 1

            ret, img = self.capture.read()
            if ret != True:
                time.sleep(2)
                break
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(np.uint8(img))
            self.result = np.array(img)
            self.result = cv2.cvtColor(self.result, cv2.COLOR_RGB2BGRA)
            scale = 551.0 / max(self.result.shape[1], self.result.shape[0])
            self.result = cv2.resize(self.result,
                                     (int(self.result.shape[1] * scale), int(self.result.shape[0] * scale)),
                                     interpolation=cv2.INTER_AREA)
            self.QtImg = QtGui.QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                      QtGui.QImage.Format_RGB32)
            self.label_preview.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
        self.capture.release()


    def showData(self):
        #`id`, `category`,`weight`,`nums`,`status`
        result = self.objectDB.selectAll(None)
        if len(result) >10:
            result = result[-10:]
        i = 1
        if result is not None:
            self.tableWidget.setRowCount(len(result)+1)
            self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            for row in result:
                newItem = QTableWidgetItem(str(row[0]))
                self.tableWidget.setItem(i, 0, newItem)
                newItem = QTableWidgetItem(row[1])
                self.tableWidget.setItem(i, 1, newItem)
                newItem = QTableWidgetItem( row[2])
                self.tableWidget.setItem(i, 2, newItem)
                newItem = QTableWidgetItem(row[3])
                self.tableWidget.setItem(i, 3, newItem)
                newItem = QTableWidgetItem(row[4])
                self.tableWidget.setItem(i, 4, newItem)
                i+=1

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Detection_window()
    window.show()
    sys.exit(app.exec_())