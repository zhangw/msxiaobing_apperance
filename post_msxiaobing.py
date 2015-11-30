# -*- coding: utf-8 -*-
"""
post_msxiaobing.py

Created by <jimokanghanchao@gmail.com> on Nov 30,2015
"""
import time
import uuid
import urllib
import urllib2
import base64
import json

def main():
  path = "/Users/vincent/Others/pics_face/testpic/IMG_4032.PNG"
  print "使用测试图片%s" % path
  calculate_apperance(path)

def rating_apperance(path):
  print "正在上传图片计算颜值..."
  image_uploaded = upload_image(path)
  rst = analyze_image(image_uploaded,"yanzhi")['content']['text']
  print rst
  import re
  mark = re.findall(r"\d+\.?\d?",rst)
  if len(mark) >= 1:
    mark = float(mark[0]) * 10
    print "机器人小冰计算的颜值:%s" % mark


def upload_image(path):
  url = "http://kan.msxiaobing.com/Api/Image/UploadBase64"
  with open(path,"rb") as image_file:
    image_encoded = base64.b64encode(image_file.read())
    request = urllib2.Request(url)
    request.add_header("Content-type", "application/x-www-form-urlencoded; charset=UTF-8")
    request.add_data(image_encoded)
    res = urllib2.urlopen(request)
    if res.getcode() == 200:
      return json.loads(res.readlines()[0])

def analyze_image(imageinfo,type="yanzhi"):
  """
  type = ("howold","yanzhi"),howold:分析年龄，yanzhi:计算颜值。
  """
  if imageinfo is not None:
    image_url = imageinfo['Host'] + imageinfo['Url']
    url = "http://kan.msxiaobing.com/Api/ImageAnalyze/Process?service=%s&tid=%s" % (type,uuid.uuid4().hex)
    tv = time.time()
    tsmp = int(tv)
    msgid = int(tv*1000000)
    sid = "mtuId" + str(tsmp)
    """
    msgId:1448883026554
    timestamp:1448883026
    senderId:mtuId1448882946306
    content[imageUrl]:http://mediaplatform.trafficmanager.cn/image/fetchimage?key=KjPfyoxNK0-wLXTKA0seSdUvLskvStU3MjA01Tc01Dc20De1dHV0M3B0cjIxdTZycTYHAA%3D%3D
    """
    raw_params = {'msgId':msgid,'timestamp':tsmp,'senderId':sid, 'content[imageUrl]':image_url}
    params = urllib.urlencode(raw_params)
    request = urllib2.Request(url,params)
    res = urllib2.urlopen(request)
    if res.getcode() == 200:
      return json.loads(res.readlines()[0])

if __name__ == '__main__':
  main()
