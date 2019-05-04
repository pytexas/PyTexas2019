#!/usr/bin/env python3

import os
import requests

BASE = 'https://www.pytexas.org'
FILES = [
  "/conference/data/2019.json",
  "/static-2019/vuetify.min.4ee7ed0d3bfa.css",
  "/static-2019/global.6c2e85abb395.css",
  "/static-2019/pytexas.5c0e03dfb39f.css",
  "/static-2019/pytexas.8c010be8a206.js",
  "/static-2019/img/atx.3ab5136e351b.svg",
  "/static-2019/img/banner80.39225f4a7c1f.png",
  "/static-2019/img/icon.d99d2b99008d.svg",
  "/static-2019/img/icons/about.764234acc6c0.svg",
  "/static-2019/img/icons/blog.13fb6a09bcb5.svg",
  "/static-2019/img/icons/chat.9843a75b860d.svg",
  "/static-2019/img/icons/talks.9843a75b860d.svg",
  "/static-2019/img/icons/community.fefb33f67adc.svg",
  "/static-2019/img/icons/sponsors.3cf80e0dcd9a.svg",
  "/static-2019/img/icons/venue.4370b746c0cd.svg",
  "/static-2019/img/icons/external.f9289b910493.svg",
  "/static-2019/img/icons/external-white.d945d98d7fb0.svg",
  "/static-2019/img/icons/background.e5e4f4cb920f.png",
  "/static-2019/img/social/about.me.f65a5145d048.png",
  "/static-2019/img/social/facebook.287207afff4d.png",
  "/static-2019/img/social/github.c3ec7b84d61f.png",
  "/static-2019/img/social/google.fa243b13d494.png",
  "/static-2019/img/social/linkedin.7ebd98e43085.png",
  "/static-2019/img/social/twitter.d66f6b578aef.png",
  "/static-2019/img/social/website.e664e4203b87.png",
  "/static-2019/md/venue.e2ee2d8c8004.md",
  "/static-2019/md/sponsors/prospectus.0f8b25c8386c.md",
  "/static-2019/md/community/employers.9257ae065143.md",
  "/static-2019/md/community/chat.d74320211d3b.md",
  "/static-2019/md/community/mailing-list.a577ad78bb26.md",
  "/static-2019/md/community/meetups.41334131fef2.md",
  "/static-2019/md/about/volunteering.4aba0e4c0811.md",
  "/static-2019/md/about/conference.0409dd947791.md",
  "/static-2019/md/about/grants.78277bbd1bb7.md",
  "/static-2019/md/about/registration.3389bb22c19e.md",
  "/static-2019/md/about/privacy.e1c9ca5ba45c.md",
  "/static-2019/md/about/code-of-conduct.00a66b7f860f.md",
  "/static-2019/md/about/diversity-statement.5d7d105cccca.md",
  "/static-2019/md/about/faq.5a0479f48718.md",
  "/static-2019/md/talks/speaking.fd11936b58ec.md",
]


for file in FILES:
  url = BASE + file
  path = file[1:]

  print(url)
  response = requests.get(url)

  d = os.path.dirname(path)
  if not os.path.exists(d):
    os.makedirs(d)

  with open(path, 'wb') as fh:
    fh.write(response.content)
