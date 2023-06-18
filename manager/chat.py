from random import choice

SORRY_MESSAGES = [
    "죄송합니다. 그 질문에 대한 답을 모르겠습니다.",
    "저는 아직 개발 중이라 모든 질문에 답할 수 없습니다.",
    "그 질문은 저에게 너무 어렵습니다.",
    "뭐라고 말해야 할지 잘 모르겠습니다.",
    "대답할 수 없는 유형의 질문입니다.",
    "죄송합니다. 그것에 대한 대답은 아직 제공할 수 없습니다.",
    "아직은 답변이 불가한 유형입니다. 더 나은 서비스로 찾아뵙겠습니다."
]


def hello(text: str) -> str:
    return "Hello Taxim!"


def response(in_text: str):
    if "대포차" in in_text and "의심" in in_text:
        out_text = "현재 가장 대포차로 의심가는 차량은 29수4635 차량 입니다. 차량의 소유주의 정보에 따른 에상 경로와 가장 다르게 이동하고 있습니다."
        focus = "V5"
    elif "도난" in in_text and "의심" in in_text:
        out_text = "현재 도난 의심 차량은 없습니다."
        focus = None
    else:
        out_text = choice(SORRY_MESSAGES)
        focus = None
    return {
        "text": out_text,
        "focus": focus
    }