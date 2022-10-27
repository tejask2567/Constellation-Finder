from DeepImageSearch import Index, LoadData, SearchImage

image_list = LoadData().from_folder(['Data'])
# Index(image_list).Start()
results = SearchImage().get_similar_images(
    image_path="Data/Pisces_third_60.jpg", number_of_images=5)
res = list(results.values())[0]
print(res)
