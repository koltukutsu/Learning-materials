import sys
from PyQt5 import QtCore, QtGui,QtWidgets, QtWebEngineWidgets, uic
import pandas as pd
from string import digits
from main import Ui_Form


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ROOT = "file:///"
        #TODO: Kullanicinin KEY_WORD'ler girmesine izin verebilirim
        self.KEY_WORDS = ['belgeyi_kontrol_et', 'PDF Kontrol Edilecek', 'PDF Hatasi', 'hata_kontrol_et', 'Bakilacak']
        self.index = 0
        self.root_for_excel = ""
        
        self.ui.pdf_goster.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.ui.pdf_goster.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        
        
        self.ui.yukle.clicked.connect(self.baslat_clicked)
        self.ui.sec.clicked.connect(self.file_choose)
        
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Return"), self)
        self.shortcut.activated.connect(self.baslat_clicked)
        
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("D"), self)
        self.shortcut.activated.connect(self.next_pdf)
        
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("A"), self)
        self.shortcut.activated.connect(self.prev_pdf)
        
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("B"), self)
        self.shortcut.activated.connect(self.save_and_exit)

    @QtCore.pyqtSlot()
    def baslat_clicked(self):
        self.index = 0
        self.root_for_excel = self.ui.dir_path.toPlainText().replace(" ", "")
        self.root_for_excel = self.ui.dir_path.toPlainText().replace("\n", "")
        if "xlsx" in self.root_for_excel:
            # print("oluyor")
            df = pd.read_excel(self.root_for_excel)
            # print("olmuyor")
            
            self.id_col = df.columns[0]
            self.value_col = df.columns[1]
            
            if self.ui.tercih.isChecked():
                print("kontrol edildi")
                self.df_hatali = df.copy()
                self.df_hatali = self.df_hatali.reset_index()
            else:
                self.df_hatali = df[df[self.value_col].isin(self.KEY_WORDS)]
                # self.hatali_id_arr = [i for i in self.df_hatali[self.id_col]]
                # self.hatali_value_arr = [i for i in self.df_hatali[self.value_col][:]]
                # print(type(self.hatali_id_arr))
                
                self.df_temiz = df[~df[self.value_col].isin(self.KEY_WORDS)]
                # self.temiz_id_arr = [i for i in self.df_temiz[self.id_col][:]]
                # self.temiz_value_arr = [i for i in self.df_temiz[self.value_col][:]]
            
                self.df_hatali = self.df_hatali.reset_index()
                self.df_temiz = self.df_temiz.reset_index()

            print(self.df_hatali)
            self.total_legth = len(self.df_hatali)
            self.load_datas()
            self.content_display()
            # print(self.df_hatali)
        else:
            print("xlsx uzantili bir dosya degil")
    
    @QtCore.pyqtSlot()
    def file_choose(self):
        self.file , self.check = QtWidgets.QFileDialog.getOpenFileName(None, "QtWidgets.QFileDialog.getOpenFileName()",
                                               "", "Excel Dosyasi (*.xlsx);;")
        if self.check:
            self.file = self.file.replace("/", "\\")
            self.ui.dir_path.setPlainText(str(self.file))
        
    @QtCore.pyqtSlot()
    def next_pdf(self):
        
        # print(self.df_hatali)
        if self.index <= len(self.df_hatali) - 1:
            self.content_change()
            if self.index != len(self.df_hatali) - 1:
                self.index += 1
            print(self.index)
            self.load_datas()
            self.content_display()
        
    @QtCore.pyqtSlot()
    def prev_pdf(self):
        if self.index > 0:
            self.content_change()
            self.index -= 1
            print(self.index)
            self.load_datas()
            self.content_display()
    
    @QtCore.pyqtSlot()        
    def load_datas(self):
        print("yuklenirken gelen index: ", self.index)
        self._id = self.df_hatali[self.id_col][self.index]
        # self._id = self.hatali_id_arr[self.index]
        
        self._value = self.df_hatali[self.value_col][self.index]
        # self._value = self.hatali_value_arr[self.index]
        
    @QtCore.pyqtSlot()        
    def content_display(self):        
        print("content display", self._id)
        print("content display", self._value)
        self.ui.kalan_goster.setText(f"{self.index + 1}/{self.total_legth}")
        self.ui.idler.setPlainText(str(self._id))
        self.ui.degerler.setPlainText(self._value)

        eklenecek = self.root_for_excel.split("\\")[:-1] # dir_path den alinan yol \ seklindedir, benim de \'lari / ile degistirmem lazim
        eklenecek = "/".join(eklenecek) + "/" # suan elimde normal path var, sorun yok
        self.pdf_path = self.ROOT + eklenecek + str(self._id) + ".pdf"
        print(self.pdf_path)
        try:
            self.ui.pdf_goster.setUrl(QtCore.QUrl(f"{self.pdf_path}"))
        except:
            print("error")
        
    @QtCore.pyqtSlot()
    def content_change(self):
        # self.hatali_value_arr[self.index] = self.ui.degerler.toPlainText()
        self.df_hatali[self.value_col][self.index] = self.ui.degerler.toPlainText().replace(" ", "").replace("\n", "")

    @QtCore.pyqtSlot()    
    def save_and_exit(self):
        self.df_exit = pd.DataFrame({self.id_col:[], self.value_col:[]})
        
        if self.ui.tercih.isChecked():
            self.df_exit = self.df_exit.append(self.df_hatali, ignore_index=True)    
        else:
            self.df_exit = self.df_exit.append(self.df_hatali, ignore_index=True)
            self.df_exit = self.df_exit.append(self.df_temiz, ignore_index=True)
            
        print("to exit")
        self.saving_path = self.root_for_excel.rstrip(".xlsx") + "YENI.xlsx"
        self.df_exit[[self.id_col, self.value_col]].to_excel(self.saving_path, index=False)
        QtWidgets.QMessageBox.about(self, "Kaydedildi", f"Kaydedilen Dosya Yolu: {self.saving_path}")
        print("Finito")
        

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())