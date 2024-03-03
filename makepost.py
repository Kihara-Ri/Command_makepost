#!/usr/bin/env python3
'''
This is a python script which I'm going to create a markdown file that appends 'Post Front-matter'
so that I won't spend more time on this.
'''
import argparse
import os
from datetime import datetime

def create_post(title, file_path):
    # 确保路径存在
    os.makedirs(file_path, exist_ok=True)
    
    # 格式化文件名和日期
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 创建post路径
    post_path = os.path.join(file_path, f"{title}.md")
    
    # 填充内容
    content = f"""--- 
title: {title}
date: '{date_now}'
updated: 
categories: 
description: 
keywords: 
top_img: 
cover: 
copyright: true
mathjax: 
swiper_index: 
tags: 
  - 
  - 
abbrlink: {title}
main_color: "#e4bf66"
---
"""
    
    # 写入文件
    with open(post_path, 'w') as file:
        file.write(content)
    print(f"Post created at {file_path}")
    return post_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new blog post.')
    parser.add_argument('title', type=str, help='Title of the post')
    parser.add_argument('--path', type=str, default='/Users/kiharari/kiharablog/blogsite/source/_posts', help='Path where the post are going to be created')
    
    args = parser.parse_args()
    post_path = create_post(args.title, args.path)
    print(f"Post {args.title}.md successfully in path {post_path}")
