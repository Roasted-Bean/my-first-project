def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("오류: 0으로 나눌 수 없습니다.")
        return None
    return a / b

def power(a, b):
    return a ** b

def main():
    print("=== 계산기 ===")
    print("연산자: +  -  *  /  **  (종료: q)")

    while True:
        print()
        user_input = input("계산식 입력 (예: 3 + 5): ").strip()

        if user_input.lower() == 'q':
            print("종료합니다.")
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("형식 오류. 예: 3 + 5")
            continue

        try:
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])
        except ValueError:
            print("숫자를 올바르게 입력하세요.")
            continue

        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = subtract(a, b)
        elif operator == '*':
            result = multiply(a, b)
        elif operator == '/':
            result = divide(a, b)
        elif operator == '**':
            result = power(a, b)
        else:
            print(f"알 수 없는 연산자: {operator}")
            continue

        if result is not None:
            # 정수로 떨어지면 정수로 표시
            if result == int(result):
                print(f"결과: {int(result)}")
            else:
                print(f"결과: {result}")

if __name__ == "__main__":
    main()
