import csv
import os


def create_sample_csv(filename="sample_data.csv"):
    """创建示例CSV文件"""
    data = [
        ["姓名", "年龄", "城市", "薪资"],
        ["张三", "28", "北京", "15000"],
        ["李四", "35", "上海", "22000"],
        ["王五", "24", "深圳", "12000"],
        ["赵六", "31", "杭州", "18000"],
        ["钱七", "27", "北京", "16000"],
        ["孙八", "29", "上海", "20000"],
        ["周九", "26", "深圳", "13000"],
        ["吴十", "33", "杭州", "21000"],
    ]

    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"已创建示例文件: {filename}")
    return filename


def read_csv(filename):
    """读取CSV文件"""
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return list(reader)


def filter_by_city(data, city):
    """按城市筛选"""
    return [row for row in data if row["城市"] == city]


def average_salary(data):
    """计算平均薪资"""
    salaries = [int(row["薪资"]) for row in data]
    return sum(salaries) / len(salaries)


def top_earners(data, n=3):
    """薪资最高的前N人"""
    sorted_data = sorted(data, key=lambda x: int(x["薪资"]), reverse=True)
    return sorted_data[:n]


if __name__ == "__main__":
    filename = create_sample_csv()

    print("\n--- 读取全部数据 ---")
    data = read_csv(filename)
    for row in data:
        print(f"{row['姓名']} | {row['年龄']}岁 | {row['城市']} | {row['薪资']}元")

    print("\n--- 筛选北京员工 ---")
    beijing = filter_by_city(data, "北京")
    for row in beijing:
        print(f"{row['姓名']} - {row['薪资']}元")

    print(f"\n--- 平均薪资: {average_salary(data):.0f} 元 ---")

    print("\n--- 薪资TOP 3 ---")
    for i, row in enumerate(top_earners(data), 1):
        print(f"{i}. {row['姓名']} - {row['薪资']}元 ({row['城市']})")
