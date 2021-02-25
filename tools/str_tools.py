def str2int(s):
    """
    字符串转整形
    :param s: 待转换的字符串
    :return: 转换后的数值。如果转换失败，返回None
    """
    try:
        if s is None:
            return None
        s = s.strip()
        if s == "":
            return None
        return int(s)
    except Exception as e:
        print(e)
        return None
