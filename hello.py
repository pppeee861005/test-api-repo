#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """
    主函數：打印歡迎信息
    """
    print("歡迎使用GitHub API測試倉庫！")
    print("這個Python文件是通過GitHub API上傳的。")
    
    # 顯示一些基本信息
    info = {
        "倉庫名稱": "test-api-repo",
        "創建方式": "GitHub API",
        "用途": "測試GitHub API功能"
    }
    
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
