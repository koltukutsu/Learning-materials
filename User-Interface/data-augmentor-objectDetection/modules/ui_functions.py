# ///////////////////////////////////////////////////////////////
# Thx to 
#       WANDERSON M.PIMENTA by MehmetSemihBabacan for his splendid design and vital effort
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            # file = file[file.index("\")] if file.count("\")
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # ///////////////////////////////////////////////////////////////
    # Special Ones, like Keras and SO on
    
    def generate(self):
        ## global variable kullanmak yerine 
        ## hizli acilmasi icin applicationin iceri kondular
        from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
        from random import randint
        import json
        import glob
        import os
        ###
        with open("data/arguments.json", "r") as arg_json:
            arg_dict = json.load(arg_json)

        self.img_from = self.keras_from.text()
        self.img_to = self.keras_to.text()
        self.img_type = self.keras_img_type.text()
        self.limit = self.keras_iterasyon.text()
        self.img_name = self.keras_cikan_isim.text()
        self.img_final_type = self.keras_final_type.text()

        for i in range(1,23):
            if eval(f"self.lbl_{i}.isChecked() == True"):
                print(eval(f"self.lbl_{i}.text()"), " >> ", eval(f"self.txt_{i}.text()"))
                arg_dict[eval(f"self.lbl_{i}.text()")] = eval(f"self.txt_{i}.text()")
        
        datagen = ImageDataGenerator(
                featurewise_center=bool(arg_dict.get("featurewise_center")),
                samplewise_center=bool(arg_dict.get("samplewise_center")),
                featurewise_std_normalization=bool(arg_dict.get("featurewise_std_normalization")),
                samplewise_std_normalization=bool(arg_dict.get("samplewise_std_normalization")),
                zca_whitening=arg_dict.get("zca_whitening"),
                zca_epsilon=bool(arg_dict.get("zca_epsilon")),
                rotation_range=int(arg_dict.get("rotation_range")),
                width_shift_range=float(arg_dict.get("width_shift_range")),
                height_shift_range=float(arg_dict.get("height_shift_range")),
                brightness_range=None if arg_dict.get("brightness_range") is None else eval(arg_dict.get("brightness_range")), ## iki tane degerleri, interval olara list
                shear_range=float(arg_dict.get("shear_range")),
                zoom_range=float(arg_dict.get("zoom_range")),
                channel_shift_range=float(arg_dict.get("channel_shift_range")),
                fill_mode=str(arg_dict.get("fill_mode")),
                cval=float(arg_dict.get("cval")),
                horizontal_flip=bool(arg_dict.get("horizontal_flip")),
                vertical_flip=bool(arg_dict.get("vertical_flip")),
                rescale=None if (arg_dict.get("rescale") is None or arg_dict.get("rescale") ==  0) else eval(arg_dict.get("rescale")),
                preprocessing_function=None if arg_dict.get("preprocessing_function") is None else arg_dict.get("preprocessing_function"),
                data_format=None if arg_dict.get("data_format") is None else str(arg_dict.get("data_format")),
                validation_split=float(arg_dict.get("validation_split")),
                dtype=None if arg_dict.get("dtype") is None else eval(arg_dict.get("dtype")),
                    )
        
        self.img_from = self.img_from if self.img_from[-1] == "/" else self.img_from + "/"
        self.img_to = self.img_to if self.img_to[-1] != "/" else self.img_to[:-1]
        direction_name = self.img_to.split("/")[-1]
        self.img_to = "/" + "/".join(self.img_to.split("/")[:-1])
        os.chdir(self.img_to)
        
        ### dosya varmi kontrol
        try:
            os.mkdir(direction_name)
        except FileExistsError:
            direction_name = direction_name + "_YENI_" + str(randint(0, 16))
            os.mkdir(direction_name)
        ###

        amount = len(glob.glob(self.img_from + "*." + self.img_type))

        for i, image in enumerate(glob.glob(self.img_from + "*." + self.img_type)):
            img = load_img(image)  
            img_input = img_to_array(img)  
            img_input = img_input.reshape((1,) + img_input.shape)  
            
            iteration = 0

            print(f"-{amount}- tane verilen 'Resimler'den gelen {i}. Paket")  # simdilik print ile veriyorum
            for batch in datagen.flow(img_input, batch_size=1,
                                save_to_dir=str(direction_name), save_prefix=str(self.img_name), save_format=self.img_final_type):
                iteration += 1
                if iteration > int(self.limit) - 1:
                    break  
                
        with open("0_given_args.json", "w") as given_args:
            os.chdir(direction_name)
            json.dump(arg_dict, given_args)
                
        QMessageBox.information(self, "Bitti", f"'{amount} tane resimden {int(self.limit) * amount}' tane resim üretildi\nVerilen argumanlar {self.img_to} klasorunun icine '0_given_args.json' olarak kaydedildi")
    def deneme(self):
        for item in range(1,23):
            print(f"{item}" + eval(f"self.txt_{item}.text()"))