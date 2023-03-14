origin = "❏什么是数据管理 n 对数据进行分类、组织、编码、存储、检索和维护 n 是数据处理的中心问题 ❏数据管理技术的发展过程 n 人工管理阶段（&%世纪$%年代中之前） n 文件系统阶段（&%世纪$%年代末001%年代中） n 数据库系统阶段（&%世纪1%年代末00现在）"
fileName = "01-绪论.md"

with open(f"Shujuku-Xitong-Gailun/{fileName}", encoding="utf-8", mode="r") as file:
    origin = str(file.read())

startIndex = origin.index("ATABASE ❏") + len("ATABASE ")
info = origin[startIndex:]
output = info.replace("❏", "\n- ").replace(" n ", "\n    - ").replace("&%", "").replace("$%", "")

with open(f"Shujuku-Xitong-Gailun/{fileName}", encoding="utf-8", mode="w") as file:
    file.write(origin[0:startIndex - len("ATABASE ")] + "\n" + output)

print(output)
