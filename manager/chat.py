
def hello(text: str) -> str:
    return "Hello Taxim!"


def response(in_text: str):
    if "대포차" in in_text and "의심" in in_text:
        out_text = "현재 가장 대포차로 의심가는 차량은 29수4635 차량 입니다. 차량의 소유주의 정보에 따른 에상 경로와 가장 다르게 이동하고 있습니다."
        focus = "V5"
    elif "도난" in in_text and "의심" in in_text:
        out_text = "현재 도난 의심 차량은 없습니다."
        focus = ""
    else:
        out_text = ""
        focus = ""
    return {
        "text": out_text,
        "focus": focus
    }