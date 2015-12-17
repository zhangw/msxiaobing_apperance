#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
run_rating_apperance.py

Created by <jimokanghanchao@gmail.com> on Nov 30,2015
"""

from post_msxiaobing import rating_apperance
import argparse

def main():
  parser = \
  argparse.ArgumentParser(description="根据输入的本机图片路径/图片的URL，借用微软小冰计算人[http://kan.msxiaobing.com/ImageGame/Portal?task=yanzhi]测算颜值.")
  #--path and --url should be in a mutually exclusive group
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument("--path", type=str, help="输入本机的图片全路径，比如--path /Users/xxx/xxx.jpg")
  group.add_argument("--url", type=str, help="输入图片的URL，比如--url http://ww2.sinaimg.cn/mw1024/7d01636bjw1ew43tsta3kj20ak0bjaag.jpg")
  args = parser.parse_args()
  if args.path is not None:
    rating_apperance(args.path)
  elif args.url is not None:
    rating_apperance(args.url, local=False)
  else:
    parser.print_help()

if __name__ == '__main__':
  main()
