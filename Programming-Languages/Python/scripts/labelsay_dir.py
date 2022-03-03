import glob

txts_path_default = "/home/semih/Documents/ailedeki kisiler_ilk"
label_path_default = "classes.txt"

with open(label_path_default, 'r') as labels:
    labels = [(no, name) for no, name in enumerate(labels.read().split('\n'))]
    label_ids = {str(i): 0 for i in range(len(labels.keys()))}
    
for txt_path in glob.glob(txts_path_default + "*.txt"):
    with open(txt_path, "r") as text:
        text_inside = text.read().split('\n')
        ids = [id.split()[0] for id in text_inside if id]

        for id in ids: 
            label_ids[id] += 1
            # if id == '0':
            #     labels['girilmez'] +=1
            # elif id == '1':
            #     labels['tasit_trafigine_kapali'] +=1
            # elif id == '2':
            #     labels['duz_veya_sola'] +=1
            # elif id == '3':
            #     labels['duz_veya_saga'] +=1
            # elif id == '4':
            #     labels['yalnizca_sola'] +=1
            # elif id == '5':
            #     labels['20_hiz_limiti_sonu'] +=1
            # elif id == '6':
            #     labels['30_limit'] +=1
            # elif id == '7':
            #     labels['20_limit'] +=1
            # elif id == '8':
            #     labels['yalnizca_saga'] +=1
            # elif id == '9':
            #     labels['saga_donulmez'] +=1
            # elif id == '10':
            #     labels['sola_donulmez'] +=1
            # elif id =='11':
            #     labels['dur'] +=1
            # elif id == '12':
            #     labels['park_yapilmaz'] +=1
            # elif id == '13':
            #     labels['park'] +=1
            # elif id == '14':
            #     labels['durak'] +=1  
            # elif id == '15':
            #     labels['kirmizi_isik'] +=1
            # elif id == '16':
            #     labels['sari_isik'] +=1
            # elif id == '17':
            #     labels['yesil_isik'] +=1
for no, name in labels:
    label_ids[name] = label_ids[no].pop()
print(label_ids)
# total = sum(labels.values())
# situation = f"""~~~~~~~~~~~~~~~~~~~~~~~~
# girilmez: {labels["girilmez"]}
# tasit_trafigine_kapali: {labels["tasit_trafigine_kapali"]}
# duz_veya_sola: {labels["duz_veya_sola"]}
# duz_veya_saga: {labels["duz_veya_saga"]}
# yalnizca_sola: {labels["yalnizca_sola"]}
# 20_hiz_limiti_sonu: {labels["20_hiz_limiti_sonu"]}
# 30_limit: {labels["30_limit"]}
# 20_limit: {labels["20_limit"]}
# yalnizca_saga: {labels["yalnizca_saga"]}
# saga_donulmez: {labels["saga_donulmez"]}
# sola_donulmez: {labels["sola_donulmez"]}
# dur: {labels["dur"]}
# park_yapilmaz: {labels["park_yapilmaz"]}
# park: {labels["park"]}
# durak: {labels["durak"]}
# kirmizi_isik: {labels["kirmizi_isik"]}
# sari_isik: {labels["sari_isik"]}
# yesil_isik: {labels["yesil_isik"]}

# TOPLAM:{total}
# ~~~~~~~~~~~~~~~~~~~~~~~~
# """

# with open("/home/semih/Desktop/sonuclar.txt", 'w') as situation_file:
#     situation_file.write(situation)

# print(situation)
