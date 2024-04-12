import asyncio
from datetime import datetime, timedelta


async def check_time(now_time: str, old_time: str, user_role: str):   #Год месяц день часы минуты секунды
    now = datetime.strptime(now_time, "%Y-%m-%d %H:%M:%S")
    old = datetime.strptime(old_time, "%Y-%m-%d %H:%M:%S")
    del_time_for_premium = timedelta(minutes=5)
    del_time_for_main = timedelta(minutes=10)
    if user_role == "premium_user":
        old += del_time_for_premium
        if now - old >= timedelta(minutes=0):
            return True, "OK"
        else:
            return False, old - now
    else:
        old += del_time_for_main
        if now - old >= timedelta(minutes=0):
            return True, "OK"
        else:
            return False, old - now


if __name__ == "__main__":
    s = asyncio.run(check_time("2024-04-11 11:44:43", "2024-04-11 11:39:43", "main_user"))
    print(s)
    if s[0]:
        print(s[1])
    else:
        print(s[1])
