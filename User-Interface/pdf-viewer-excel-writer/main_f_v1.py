import sys
from PyQt5 import QtCore, QtGui,QtWidgets, QtWebEngineWidgets, uic
import pandas as pd
from string import digits
from main import Ui_Form

PDF = ""

        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # MainWindow.__init__(self)
        super(MainWindow, self).__init__()
        # uic.loadUi("main.ui", self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ROOT = "file:\\\\\\"
        self.KEY_WORDS = ['belgeyi_kontrol_et', 'PDF Hatasi', 'hata_kontrol_et', 'Bakilacak']
        self.index = 0
        
        # self.pdf_goster.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        
        # self.pdf_goster.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.ui.pdf_goster.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.ui.pdf_goster.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        
        
        self.ui.yukle.clicked.connect(self.baslat_clicked)
        
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("D"), self)
        self.shortcut.activated.connect(self.next_pdf)
        
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("A"), self)
        self.shortcut.activated.connect(self.prev_pdf)
        
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("B"), self)
        self.shortcut.activated.connect(self.save_and_exit)
        
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        # self.ui = Ui_Form()
        # self.ui.setupUi(self)
    @QtCore.pyqtSlot()
    def baslat_clicked(self):
        self.root_for_excel = self.ui.dir_path.toPlainText()
        
        if "xlsx" in self.root_for_excel:
            print("oluyor")
            df = pd.read_excel(self.root_for_excel)
            print("olmuyor")
            self.id_col = df.columns[0]
            self.value_col = df.columns[1]

            self.df_hatali = df[df[self.value_col].isin(self.KEY_WORDS)]
            self.content_display()
            # print(self.df_hatali)
        else:
            print("not an .xlsx extension file")
        
    @QtCore.pyqtSlot()
    def next_pdf(self):
        self.index += 1
        print(self.index)
        # self.content_display()
        
    @QtCore.pyqtSlot()
    def prev_pdf(self):
        if self.index > 0:
            self.index -= 1
            print(self.index)
            # self.content_display()
            # self.content_change()
    
    
    @QtCore.pyqtSlot()        
    def content_display(self):
        self._id = self.df_hatali[self.id_col][self.index]
        self._value = self.df_hatali[self.value_col][self.index]
        
        print(self._id)
        self.ui.idler.setPlainText(str(self._id))
        self.ui.degerler.setPlainText(self._value)

        eklenecek = self.root_for_excel.split("\\")[:-1]
        eklenecek = "\\".join(eklenecek) + "\\" # suan elimde normal path var, sorun yok
        
        self.pdf_path = self.ROOT + eklenecek + str(self._id) + ".pdf"
        print(self.pdf_path)
        self.ui.pdf_goster.setUrl(QtCore.QUrl(PDF))
        # window.setGeometry(600, 50, 800, 600)
        # Window.show()
        print(self.pdf_path)
        
    @QtCore.pyqtSlot()
    def content_change(self, from_where):
        # if self.index >= 0:
        # self.df_hatali[self.id_col][self.index - 1] = self._id 
        if from_where == "next":
            self.df_hatali[self.value_col][self.index - 1] = self._value
        elif from_where == "prev":
            self.df_hatali[self.value_col][self.index - 1] = self._value

    @QtCore.pyqtSlot()    
    def save_and_exit(self):
        self.df.to_excel()
        

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())