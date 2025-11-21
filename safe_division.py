def safe_division(a, b):
    """
    安全除法函式：防止除以零的錯誤
    
    參數：
        a: 被除數
        b: 除數
    
    回傳：
        當 b 不為零時回傳 a / b 的結果
        當 b 為零時回傳 None，防止例外發生
    """
    # 檢查除數是否為零
    if b != 0:
        return a / b
    else:
        return None
