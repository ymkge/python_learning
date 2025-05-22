def count_upper_and_digits(text):
    """
    文字列中の大文字と数字の数を数えます。

    Args:
        text (str): 処理する文字列。

    Returns:
        dict: 'upper_count' と 'digit_count' をキーとする辞書。
    """
    upper_count = 0
    digit_count = 0
    for char in text:
        if 'A' <= char <= 'Z':  # 大文字を判定
            upper_count += 1
        elif '0' <= char <= '9':  # 数字を判定
            digit_count += 1
    return {"upper_count": upper_count, "digit_count": digit_count}

# ユーザーに文字列の入力を促す
user_input_text = input("分析したい文字列を入力してください: ")

# 関数を呼び出して結果を表示
counts = count_upper_and_digits(user_input_text)
print(f"大文字の数: {counts['upper_count']}個")
print(f"数字の数: {counts['digit_count']}個")