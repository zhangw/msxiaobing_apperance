# -*- coding: utf-8 -*-
"""
run_rating_apperance.py

Created by <jimokanghanchao@gmail.com> on Nov 30,2015
"""

from post_msxiaobing import rating_apperance
import argparse

def main():
  parser = \
  argparse.ArgumentParser(description="根据输入的本机图片路径，借用微软小冰计算人[http://kan.msxiaobing.com/ImageGame/Portal?task=howold]测算颜值.")
  parser.add_argument("--path", type=str, help="输入本机的图片全路径，比如--path /Users/xxx/xxx.jpg")
  args = parser.parse_args()
  if args.path is not None:
    rating_apperance(args.path)
  else:
    parser.print_help()

if __name__ == '__main__':
  main()
