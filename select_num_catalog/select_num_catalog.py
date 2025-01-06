# 文件路径
input_file = "昆明区域地震目录2022-2024.txt"
output_file_3 = "YN_catalog_3.txt"
output_file_single = "YN_catalog_single.txt"

# 打开文件
with open(input_file, "r", encoding="gbk", errors="ignore") as infile, \
     open(output_file_3, "w", encoding="utf-8") as outfile_3, \
     open(output_file_single, "w", encoding="utf-8") as outfile_single:
    
    for line in infile:
        if line.strip():  # 忽略空行
            # 去除多余空白并按制表符分割
            fields = line.strip().split("\t")
            if len(fields) >= 8:  # 确保至少有 8 个字段
                column_8 = fields[7]  # 第 8 列
                if "(" in column_8 and ")" in column_8:  # 判断是否包含括号
                    outfile_single.write(line)
                else:
                    outfile_3.write(line)
            else:
                print(f"字段不足，行内容：{line.strip()}")

print("处理完成！结果已保存为 'YN_catalog_3.txt' 和 'YN_catalog_single.txt'。")

