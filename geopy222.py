
# from geopy import distance
# list1=[32.40665,120.5369]
# list2=[32.40745,120.54085]
# # newport_ri = (32.40665,120.5369)
# # cleveland_oh = (32.40745,120.54085)
# print(distance.distance(list1, list2).m)


from geopy.geocoders import BaiduV3
geololocator=BaiduV3(api_key='7CC5wQYzlSVN2YolOcGClF5dZF5WEUsZ')
location=geololocator.geocode('南通鑫乾国际广场')
print(location.latitude,location.longitude)
