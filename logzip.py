#!/usr/bin/python
# -*-coding=utf_8 -*-

import os
import tarfile
import datetime


def tarer(fname, files):
    t = tarfile.open(fname + ".tar.gz", "w:gz")
    for file in files:
        t.add(file)
    t.close()


def zip_dir(dirname, patterns, fname):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                for p in patterns:
                    if p in name:
                        filelist.append(os.path.join(root, name))

    tarer(fname, filelist)

    for file in filelist:
        os.remove(file)


def day_get(d, num):
    oneday = datetime.timedelta(days=num)
    day = d - oneday
    return day.strftime('%Y-%m-%d')


def logzip(num):
    d = datetime.datetime.now()
    days = []
    for i in range(num):
        days.append(day_get(d, i))
    zip_dir('./', days, '%s__%ddays' % (d.strftime('%Y-%m-%d'), num))

if __name__ == '__main__':
    logzip(10)
