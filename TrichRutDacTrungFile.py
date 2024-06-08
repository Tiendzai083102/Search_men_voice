import TrichRutDacTrung as ft
import os
from TinhDoTuongDong import Feature
import jsonpickle as json

# Đường dẫn đến thư mục chứa các file
folder_path = 'data'

# Lấy tất cả các file trong thư mục
files = os.listdir(folder_path)

listFeatures = []
demf = 0

for file in files:
    features = ft.features(os.path.join(folder_path, file))
    for feature in features:
        feature_obj = Feature(link=os.path.join(folder_path, file),feature=feature)
        listFeatures.append(feature_obj)

def save(data):
    data_json = json.dumps(data, indent=4)
    with open("metadata/data.json", "w") as file:
        file.write(data_json)

save(listFeatures)

