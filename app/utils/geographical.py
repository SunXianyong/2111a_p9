from geopy.distance import geodesic

print(geodesic((39.90628799261383, 116.39224548618898), (40.137986161120004, 116.20105861668382)).km)  # 计算两个坐标直线距离
https://restapi.amap.com/v3/geocode/geo?address=北京市朝阳区阜通东大街6号&output=XML&key=<用户的key>
https://restapi.amap.com/v5/direction/electrobike?key=0&origin=116.39224548618898,39.90628799261383&destination=116.20105861668382,40.137986161120004