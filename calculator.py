def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "错误：不能除以零"
    return a / b

def main():
    print("=== 简易计算器 ===")
    print("支持的操作: +, -, *, /")
    print("输入 q 退出")

    while True:
        expr = input("\n请输入表达式 (如 3 + 5): ")
        if expr.lower() == 'q':
            print("再见！")
            break

        try:
            parts = expr.split()
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print(f"不支持的操作: {op}")
                continue

            print(f"结果: {a} {op} {b} = {result}")
        except (ValueError, IndexError):
            print("输入格式错误，请使用: 数字 运算符 数字")

if __name__ == "__main__":
    main()
