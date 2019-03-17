import pandas as pd


def main():
    # 打开csv文件
    aqi_data = pd.read_csv("China_city_aqi.csv")
    # aqi_data =pd.skipna("China_city_aqi.csv")
    # 打印数据
    print(aqi_data.head(4))
    print("=" * 50)
    print(aqi_data.tail(3))
    print("=" * 50)
    # 选择打印
    print(aqi_data[['city', 'AQI']][:3])
    print("最大值：", aqi_data["AQI"].max())
    print("最小值：", aqi_data["AQI"].min())
    print("均值：", aqi_data["AQI"].mean())
    print("*" * 100)
    print("基本信息：")
    print(aqi_data.info())
    print("=" * 100)
    print("=" * 100)
    # 升序排序取前十个

    top_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print("空气质量最好的前十城市：", top_cities)

    # 降序排序取前十个
    bottom_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print("空气质量最差的前十城市：", bottom_cities)

    top_cities.to_csv("top_cities.csv", index=False, encoding="utf-8")
    bottom_cities.to_csv("bottom_cities", index=False)


if __name__ == '__main__':
    main()
