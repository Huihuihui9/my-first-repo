import os
import sys


def batch_rename(directory, prefix="", suffix="", replace_old="", replace_new=""):
    """批量重命名指定目录下的文件"""
    if not os.path.isdir(directory):
        print(f"错误：目录不存在 - {directory}")
        return

    files = os.listdir(directory)
    count = 0

    for filename in files:
        old_path = os.path.join(directory, filename)
        if os.path.isdir(old_path):
            continue

        name, ext = os.path.splitext(filename)
        new_name = name

        if replace_old:
            new_name = new_name.replace(replace_old, replace_new)

        new_name = f"{prefix}{new_name}{suffix}{ext}"

        if new_name != filename:
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"重命名: {filename} -> {new_name}")
            count += 1

    print(f"\n完成！共重命名 {count} 个文件")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python batch_rename.py <目录> [选项]")
        print("选项:")
        print("  --prefix <前缀>     添加前缀")
        print("  --suffix <后缀>     添加后缀")
        print("  --replace <旧> <新> 替换文件名中的文字")
        print("\n示例:")
        print("  python batch_rename.py ./photos --prefix vacation_")
        print("  python batch_rename.py ./docs --replace draft final")
        sys.exit(1)

    directory = sys.argv[1]
    prefix = ""
    suffix = ""
    replace_old = ""
    replace_new = ""

    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == "--prefix" and i + 1 < len(args):
            prefix = args[i + 1]
            i += 2
        elif args[i] == "--suffix" and i + 1 < len(args):
            suffix = args[i + 1]
            i += 2
        elif args[i] == "--replace" and i + 2 < len(args):
            replace_old = args[i + 1]
            replace_new = args[i + 2]
            i += 3
        else:
            i += 1

    batch_rename(directory, prefix, suffix, replace_old, replace_new)
