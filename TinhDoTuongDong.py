import math
import jsonpickle as json
import TrichRutDacTrung

class Feature:
    def __init__(self, link=None, feature=None):
        self.link = link
        self.feature = feature
        
def sapxep(arr):
    # Tạo một từ điển để đếm số lần xuất hiện của mỗi phần tử
    count_dict = {}
    for item in arr:
        count_dict[item] = count_dict.get(item, 0) + 1
    
    # Sắp xếp từ điển theo số lần xuất hiện giảm dần
    sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Tạo một danh sách mới từ các phần tử đã sắp xếp
    sorted_unique_items = [item for item, count in sorted_items]
    
    return sorted_unique_items

def SimilarityCalculation(features, base_features):
    # Tính toán khoảng cách Euclid giữa các đặc trưng của base_features và features
    links = []

    for base_feature in base_features:
        min_distance = float('inf')
        most_similar_link = None

        for feature in features:
            distance = euclideanDistance(base_feature.feature, feature.feature)
            if distance < min_distance:
                min_distance = distance
                most_similar_link = feature.link
        links.append(most_similar_link)

    sorted_links = sapxep(links)
    top_links = sorted_links[:3]
    
    return top_links

# Hàm tính toán khoảng cách Euclid
def euclideanDistance(feature1, feature2):
    d = 0.0
    for i in range(len(feature1)):
        d += (feature1[i] - feature2[i])**2
    d = math.sqrt(d)
    return d

# # Mở file JSON và đọc nội dung của file
# with open('metadata/data.json', 'r') as file:
#     json_data = file.read()

# # Chuyển đổi nội dung file JSON thành đối tượng Python
# feature_list = json.loads(json_data)

# # Trích rút đặc trưng cho file âm thanh cụ thể
# audio_features = TrichRutDacTrung.features("data/người (96)-[AudioTrimmer.com].wav")
# # Giả sử audio_features là danh sách các đặc trưng của âm thanh
# audio_features = [Feature(feature=f) for f in audio_features]

# # Tính toán độ tương đồng và in ra link của 3 Feature có độ tương đồng cao nhất
# similar_links = SimilarityCalculation(feature_list, audio_features)
# print("Links of the 3 most similar features:")
# for link in similar_links:
#     print(link)
