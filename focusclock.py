import time

# 设置专注时间（以分钟为单位）
focus_time = 25 

# 用当前时间加上专注时间来计算结束时间
end_time = time.time() + focus_time * 60 

# 计算分钟和秒钟
minutes = focus_time
seconds = 0

# 倒计时循环
while True:
    # 显示剩余时间
    print(f"Time left: {minutes:02d}:{seconds:02d}", end="\r")
    
    # 如果时间到了，打印一条消息并退出循环
    if time.time() > end_time:
        print("Time's up!")
        break
    
    # 等待1秒钟
    time.sleep(1)
    
    # 更新分钟和秒钟
    seconds -= 1
    if seconds < 0:
        seconds = 59
        minutes -= 1
