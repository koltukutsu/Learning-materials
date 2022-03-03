import cv2
from os import listdir
from os.path import isfile, join

image_folder_path = "/home/hasan/Desktop/calismalar_2021/object_detection/datasets/dagitilanlar/ali/id0/"
label_folder_path = "/home/hasan/Desktop/calismalar_2021/object_detection/datasets/dagitilanlar/ali/id0/"  # resimlerin bulundugu yolu veriyoruz burada.


filenames = sorted([f[:-4] for f in listdir(label_folder_path) if isfile(join(label_folder_path, f))])

print(filenames)
label_dict ={
            0: "kasisli_yol",
            1: "ileri_ve_sag_mecburi",
            2: "okul_gecidi_b14b",
            3: "ana_yol_tali_yol_t22b",
            4: "sola_tehlikeli_viraj",
            5: "yaya_gecidi_b14a",
            6: "u_donusu_yapilmaz",
            7: "hastane",
            8: "akaryakit_istasyonu",
            9: "ana_yol_tali_yol_t22a",
            10: "ana_yol_tali_yol_sag",
            11: "yaya_gecidi_t11",
            12: "sola_donulmez",
            13: "okul_gecidi_t12",
            14: "ileri_ve_sol_mecburi",
            15: "gizli_buzlanma",
            16: "ana_yol_tali_yol_t22a",
            17: "saga tehlikeli_viraj",
            18: "sagdan_gidiniz",
            19: "gabari",
            20: "tek_yonlu_yol",
            21: "saga_donulmez",
            22: "ana_yol_tali_yol_kavsagi_t22a",
            23: "yon_levhasi",
            24: "ana_yol_tali_yol_kavsagi_t22b",
            25: "park_etmek_yasaktir",
            26: "isikli_isaret_cihazi",
            27: "ada_etrafinda_donunuz",
            28: "ana_yol_tali_yol_kavsagi_t22d)",
            29: "ileri_cikmaz_yol",
            30: "girisi_olmayan_yol",
            31: "ana_yol_tali_yol_t22d",
            32: "sagdan_daralan_kaplama",
            33: "ana_yol_tali_yol_t22c",
            34: "yol_ver",
            35: "ana_yol",
            36: "yuk_tasitlarinin_ondeki_tasiti_gecmesi_yasaktir",
            37: "ondeki_tasiti_gecmek_yasaktir",
            38: "tehlike",
            39: "yolda_calisma",
            40: "dur",
            41: "ileri_mecburi_yon",
            42: "kaygan_yol",
            43: "saga_mecburi_yon",
            44: "tasit_trafigine_kapali_yol",
            45: "trafik_lambasi",
            46: "kamyonlar_icin_gecme_yasagi_sonu",
            47: "kamyon_giremez",
            48: "gecme_yasagi_sonu",
            49: "bisiklet_gecebilir",
            50: "cikmaz_yol",
            51: "iki_taraftan_daralan_kaplama",
            52: "sinirlama_sonu",
            53: "soldan_gidiniz",
            54: "tehlikeli_viraj_yon_levhasi",
            55: "vahsi_hayvanlar_gecebilir",
            56: "park_yeri",
            57: "durak",
            58: "azami_hiz_sinirlamasi_10",
            59: "azami_hiz_sinirlamasi_20",
            60: "azami_hiz_sinirlamasi_30",
            61: "azami_hiz_sinirlamasi_40",
            62: "azami_hiz_sinirlamasi_50",
            63: "azami_hiz_sinirlamasi_60",
            64: "azami_hiz_sinirlamasi_70",
            65: "azami_hiz_sinirlamasi_82",
            66: "hiz_sinirlamasi_sonu_20",
            67: "yesil_isik",
            68: "kirmizi_isik",
            69: "sari_isik",
            70: "ileriden_sola_mecburi_yon",
            71: "ileriden_saga_mecburi_yon",
            72: "sagdan_ana_yola_giris",
            73: "her_iki_yandan_gidiniz",
            74: "duraklamak_ve_park_etmek_yasaktir",
            75: "sola_mecburi_yon",
            76: "donus_adasi_ek_levhasi",
            77: "refuj_basi_ek_levhasi_sol",
            78: "refuj_basi_ek_levhasi_sag",
            79: "donel_kavsak",
            80: "yaya_ust_gecidi",
            81: "saga_ve_sola_mecburi_yon",
            82: "mecburi_bisiklet_yolu",
            83: "engelli_park_yeri",
            84: "elektronik_denetleme_sistemi",
            85: "azami_hiz_sinirlamasi_120",
            86: "mecburi_asgari_hiz_40",
            87: "onarim_yaklasim_levhasi",
            88: "kontrolsuz_kavsak",
            89: "mecburi_bisiklet_yolu_sonu",
            90: "u_donusu_levhasi",
            91: "sola_tehlikeli_devamli_virajlar",
            92: "butun_yasaklama_ve_kisitlamalarin_sonu",
            93: "hiz_sinirlamasi_sonu_80",
            94: "azami_hiz_sinirlamasi_80",
            95: "azami_hiz_sinirlamasi_100",
            96: "iki_yonlu_trafik_kirmizi",
            97: "sagdan_birlesen_tali_yol",
            98: "soldan_birlesen_tali_yol",
            99: "dusuk_banket",
            100: "okul_gecidi_b14b",
            101: "duraklamak_yasak",
            102: "rand_trafik_isigi",
            103: "rand_ana_tali_yol",
            104: "ran_yaya_gecidi",
            105: "eds",
            106: "kavisli_yol",
            107: "2_yonlu_yol",
            108: "rastgele_sol",
        }


for f in filenames:

    image_name = image_folder_path + f + '.jpg'
    txt_name = label_folder_path + f + '.txt'

    print(image_name, txt_name, f)

    img = cv2.imread(image_name)

    img_width = img.shape[1]
    img_height = img.shape[0]
    
    labels = []
    
    if isfile(txt_name):
        with open(txt_name, "r") as fr:
            try:
                labels = fr.readlines()
            except:
                print("can't read txt")
    else:
        print(f)
            
    for label in labels:
        lab = label[:-2]
        values = lab.split(' ')
        try:
	        klas = label_dict[int(values[0])]
	        
	        start_point =   (int((float(values[1]) - float(values[3]) / 2) * img_width),
	                        int((float(values[2]) - float(values[4]) / 2) * img_height))
	        end_point = (int((float(values[1]) + float(values[3]) / 2) * img_width),
	                    int((float(values[2]) + float(values[4]) / 2) * img_height))
	                    
	        color = (36,255,12)
	        img = cv2.rectangle(img, start_point, end_point, color, 3)
	        cv2.putText(img, klas, (start_point[0], start_point[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        except:
        	print(f, values[0])

    cv2.putText(img, f, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 3)
    img = cv2.resize(img, (1600,800), interpolation = cv2.INTER_AREA)                  # keyfinize gore piksel degerleri girebilirsiniz
    cv2.imshow('asd', img)
    cv2.waitKey()		
