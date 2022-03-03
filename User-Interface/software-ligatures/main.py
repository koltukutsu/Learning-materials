from PyQt5.QtGui import QFileOpenEvent
from ui_main import Ui_Form

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        lyout = self.ui

        lyout.sec_k.clicked.connect(self.open)
        lyout.calistir.clicked.connect(self.generate)

    def open(self) -> list or str:
        path = QFileDialog.getOpenFileName(
            self, "Bir dosya aç", "", "Tüm Dosyalar (*.*)"
        )
        if path != ("", ""):
            self.ui.kaynak.setText(path[0])
            name = path[0].split("/")[-1]
            name = name.rstrip(".txt") + "_SONUC" + ".txt"
            self.ui.sonuc.setText(name)

    def generate(self):
        import pandas as pd

        FROM = self.ui.kaynak.text()
        AD = self.ui.sonuc.text()
        TO = "/".join(FROM.split("/")[:-1]) + "/" + AD

        df = pd.read_csv(FROM, names=["string"], header=None, encoding="UTF-16")

        df["parcali"] = df.string.apply(lambda x: "{}".format(list(x)))
        df["giris"] = df["string"].apply(lambda x: '"' + x + '"')

        new_df = df[df["giris"].str.contains("_")].reset_index()
        chief_df = df[~df["giris"].str.contains("_")].reset_index()
        df["giris"] = df["giris"].str.replace('"', "")

        list_ = chief_df["string"]
        list_ = list_.str.replace('"', "")
        none = ""
        bakalim = []
        value = ""
        limit_ = len(list_)
        for i in range(len(list_)):
            # the whole list is first loop
            # the letters of the items is the second loop
            # in the second loop there must be a while loop
            none = ""
            value = list_[i]
            kust1 = list(value)
            print("~~~11111")
            print(value)
            for a in range(len(kust1)):
                if kust1[a] == kust1[0]:
                    none += '"' + kust1[a] + 'ـ" '

                elif kust1[a] == kust1[-1]:

                    none += '"ـ' + kust1[a] + '"'

                elif kust1[a] == kust1[1]:
                    none += '"ـ' + kust1[a] + 'ـ" '

                else:
                    none += '"ـ' + kust1[a] + 'ـ" '
                kust1[a] = a

            while none[-1] in 'ــ "':
                none = none[:-1]
                print(none)
                print(none[-1] in 'ــ "')
            none += '"'
            print("~~~2222")

            bakalim.append(none)
        chief_df["parcali_asil"] = bakalim
        chief_df["parcali_asil"] = chief_df["parcali_asil"].replace("'", "")
        chief_df["parcali_asil"] = chief_df["parcali_asil"].replace("ـقـ", "ـفـ")
        chief_df["parcali_asil"] = chief_df["parcali_asil"].replace("ـق", "ـف")
        chief_df["parcali_asil"] = chief_df["parcali_asil"].replace("قـ", "فـ")
        # 2
        chief_df["parcali"] = chief_df["parcali"].str.replace('"', "")
        chief_df["parcali"] = chief_df["parcali"].str.replace(" ", "")
        chief_df["parcali"] = chief_df["parcali"].str.replace("[", "")
        chief_df["parcali"] = chief_df["parcali"].str.replace("]", "")
        chief_df["parcali"] = chief_df["parcali"].str.replace(",", " ")
        chief_df["parcali"] = chief_df["parcali"].str.replace("'", '"')

        new_ar = df["giris"]
        print(TO)
        _file = open(TO, "w", encoding="UTF-16")
        for element in range(len(new_ar)):
            to_write = (
                f"sub "
                + chief_df.giris[element]
                + '" ->'
                + chief_df.parcali_asil[element]
                + ";\n"
            )
            _file.write(to_write)
            print(to_write)

        _file.close()
        QMessageBox.about(
            self,
            "Tamamlandı",
            f"Dosyanın bulunduğu yere {AD} adinda sonuç dosyası oluşturuldu",
        )


if __name__ == "__main__":
    app = QApplication(["Çevirici"])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
