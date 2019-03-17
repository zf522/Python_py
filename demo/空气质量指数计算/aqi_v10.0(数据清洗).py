import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False


def main():
    # 打开csv文件
    aqi_data = pd.read_csv("China_city_aqi.csv")
    # aqi_data =pd.skipna("China_city_aqi.csv")
    # 打印数据
    print(aqi_data.head(4))
    print("=" * 50)
    print(aqi_data.tail(3))
    print("=" * 50)
    # 清洗数据:条件：AQI>0
    clean_data = aqi_data[aqi_data["AQI"] > 0]
    # 选择打印
    print(aqi_data[['city', 'AQI']][:3])
    print("最大值：", clean_data["AQI"].max())
    print("最小值：", clean_data["AQI"].min())
    print("均值：", clean_data["AQI"].mean())

    top_cities = clean_data.sort_values(by=["AQI"]).head(30)
    top_cities.plot(kind='line', x='city', y='AQI', title="空气质量最好的30个城市", figsize=(10, 7))

    plt.savefig("top_aqi.png")
    plt.show()


if __name__ == '__main__':
    main()
