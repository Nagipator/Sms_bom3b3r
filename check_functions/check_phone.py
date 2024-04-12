async def check_phone(phone: str):
    if phone[:3:] != "+79":
        return {"error": "The phone should start with +79"}
    elif not phone[1::].isdigit():
        return {"error": "The phone must consist of numbers"}
    elif len(phone[1::]) != 11:
        return {"error": "The phone must consist of 11 digits"}

