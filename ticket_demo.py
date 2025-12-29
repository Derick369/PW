# -*- coding: utf-8 -*-
"""
抢票脚本原理演示 - 仅用于教学目的
这个简单的例子展示了抢票脚本的基本工作流程，但不包含实际抢票功能
"""

import time
import random
from datetime import datetime

# 模拟票务网站API地址（实际不存在）
TICKET_API_URL = "https://example-ticket-system.com/api/tickets"

# 用户信息（模拟）
USER_INFO = {
    "username": "demo_user",
    "password": "demo_pass",
    "phone": "13800138000"
}

# 目标票信息（模拟）
TARGET_TICKET = {
    "event_id": "concert_2025",
    "date": "2025-12-30",
    "ticket_type": "vip",
    "quantity": 2
}

class TicketDemo:
    def __init__(self):
        # 无需创建实际会话，仅模拟登录状态
        self.is_logged_in = False
    
    def login(self):
        """模拟登录功能"""
        print(f"[{datetime.now()}] 正在登录票务系统...")
        
        # 完全模拟登录过程
        try:
            # 模拟网络延迟
            time.sleep(1)
            self.is_logged_in = True
            print(f"[{datetime.now()}] 登录成功！")
            return True
        except Exception as e:
            print(f"[{datetime.now()}] 登录失败: {e}")
            return False
    
    def check_ticket_availability(self):
        """模拟检查票的可用性"""
        print(f"[{datetime.now()}] 正在检查 {TARGET_TICKET['ticket_type']} 票的可用性...")
        
        # 完全模拟检查过程
        try:
            # 模拟网络延迟
            time.sleep(0.5)
            
            # 模拟随机返回票务状态（仅演示）
            available = random.choice([True, False, False])  # 模拟大部分时间无票，偶尔有票
            
            if available:
                print(f"[{datetime.now()}] 发现票了！")
                return True
            else:
                print(f"[{datetime.now()}] 暂时没票，继续等待...")
                return False
        except Exception as e:
            print(f"[{datetime.now()}] 检查失败: {e}")
            return False
    
    def book_ticket(self):
        """模拟订票功能"""
        print(f"[{datetime.now()}] 正在尝试预订票...")
        
        # 完全模拟订票过程
        try:
            # 模拟网络延迟
            time.sleep(1)
            
            # 模拟订票结果
            success = random.choice([True, False])  # 模拟订票可能成功或失败
            
            if success:
                print(f"[{datetime.now()}] 订票成功！订单号: {random.randint(100000, 999999)}")
                return True
            else:
                print(f"[{datetime.now()}] 订票失败，可能被其他人抢走了")
                return False
        except Exception as e:
            print(f"[{datetime.now()}] 订票请求失败: {e}")
            return False
    
    def run(self):
        """运行抢票流程"""
        print("=== 抢票脚本演示开始 ===")
        print("注意：这只是原理演示，不是真正的抢票工具！")
        
        # 1. 登录
        if not self.login():
            return
        
        # 2. 循环检查票的可用性
        attempts = 0
        max_attempts = 10  # 设置最大尝试次数
        
        while attempts < max_attempts:
            attempts += 1
            
            # 检查是否有票
            if self.check_ticket_availability():
                # 3. 尝试订票
                if self.book_ticket():
                    print("\n=== 演示结束：模拟抢票成功！ ===")
                    return
            
            # 等待一段时间后再次尝试（避免请求过于频繁）
            wait_time = 2  # 等待2秒
            print(f"等待 {wait_time} 秒后再次尝试...\n")
            time.sleep(wait_time)
        
        print("\n=== 演示结束：达到最大尝试次数 ===")


if __name__ == "__main__":
    demo = TicketDemo()
    demo.run()