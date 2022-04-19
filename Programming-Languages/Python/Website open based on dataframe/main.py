import json
from glob import glob
import os
import webbrowser
import pandas as pd
import time


def load_to_dict(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)


def open_online(filem: str, sleep_time: int or float, left_place=None):
    order_dict: dict
    order_dict = {"dosya adi": filem, "kalinan yer": 0}
    length: int
    # if os.path.exists("okunan_dosya.json"):
    #     os.remove("okunan_dosya.json")
    print(filem)
    df = pd.read_excel(filem)

    if left_place:
        df_link = df.iloc[left_place:, -1]
    else:
        df_link = df.iloc[:, -1]
    del df

    length = len(df_link)
    for order, link in enumerate(df_link):
        try:
            webbrowser.open_new_tab(link)
        finally:
            prompt(filem, left_file_num_global, order + 1, length)
            order_dict["kalinan yer"] = (
                order + 1
            )  # left place must be one more from the current order
            with open("okunan_dosya.json", "w") as current_json:
                json.dump(order_dict, current_json)
            time.sleep(sleep_time)
    os.remove("okunan_dosya.json")


def prompt(
    current_file: str, left_files_num: int, current_link_number: int, left_links: int
):
    print(
        f"""
          Dosya Adi: {current_file}
          -{left_files_num}- aded dosya kaldi
          -{current_link_number} / {left_links}- link sayilari
          Ctrl + C -> programdan cikmak ve otomatik kaydetmek icin
          """
    )


if __name__ == "__main__":
    config: dict
    FILES: list
    file_in_process: dict
    file_name: str
    DONE_FILES: list
    _delay = 5
    # take the config
    if os.path.exists("ayarlar.json"):
        config = load_to_dict("ayarlar.json")
    else:
        with open("ayarlar.json", "w") as config_json:
            config = {"gecikme": _delay}
            json.dump(config, config_json)
    # detect the done files
    if os.path.exists("bitmis_dosyalar.json"):
        DONE_FILES = load_to_dict("bitmis_dosyalar.json")["biten dosya isimler"]
        FILES = set(glob("Video Linkleri/*.xls*")) - set(DONE_FILES)
    else:
        DONE_FILES = set()
        FILES = set(glob("Video Linkleri/*.xls*"))

    print("biten dosyalar: ")
    print(*DONE_FILES, sep=" \n")
    print()
    print("bakilacak dosyalar: ")
    print(*FILES, sep=" \n ")

    print("Dosyalar Yukleniyor...")
    time.sleep(0.3)
    if os.path.exists("okunan_dosya.json"):
        print("Son kalinilan dosya bulundu...")
        file_in_process = load_to_dict("okunan_dosya.json")
        left_place = file_in_process["kalinan yer"]
        file_name = file_in_process["dosya adi"]

        print("Ismi:", file_name)
        print("Kalinan Yer: ", left_place)

        set_file = []
        set_file.append(file_name)
        set_file = set(set_file)
        FILES = FILES - set_file
    else:
        file_name = ""

    # I have all the files
    done_files_dict = {"biten dosya isimleri": list(DONE_FILES)}
    delay = config["gecikme"]
    if file_name:
        left_file_num_global = len(DONE_FILES)
        open_online(file_name, delay, left_place)
        done_files_dict["biten dosya isimleri"].append(file_name)
        with open("bitmis_dosyalar.json", "w") as done_json:
            json.dump(done_files_dict, done_json)

    if FILES:
        for i, excel_file_name in enumerate(FILES):
            left_file_num_global = len(FILES) - i
            open_online(excel_file_name, delay)
            done_files_dict["biten dosya isimleri"].append(excel_file_name)
            with open("bitmis_dosyalar.json", "w") as done_json:
                json.dump(done_files_dict, done_json)

    print("\nIslemler Bitti...")
