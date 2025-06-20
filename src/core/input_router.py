import re

def route_input(user_input):
    """判断输入是URL还是人名"""
    url_pattern = r"https?://[^\s]+"
    if re.match(url_pattern, user_input):
        return "url", user_input
    else:
        return "name", user_input