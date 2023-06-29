import time
def focus_timer(minutes):
    seconds = minutes * 60
    print(f"专注倒计时开始，时长: {minutes} 分钟")
    time.sleep(seconds)
    print("专注时间结束！")

focus_time = int(input("请输入专注时长（分钟）："))
focus_timer(focus_time)
