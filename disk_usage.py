#!/usr/bin/env python

# Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# Refactored this code for building InfraHealth Bot - yogyadav137

"""
List all mounted disk partitions a-la "df -h" command.
$ python scripts/disk_usage.py
Device               Total     Used     Free  Use %      Type  Mount
/dev/sdb3            18.9G    14.7G     3.3G    77%      ext4  /
/dev/sda6           345.9G    83.8G   244.5G    24%      ext4  /home
/dev/sda1           296.0M    43.1M   252.9M    14%      vfat  /boot/efi
/dev/sda2           600.0M   312.4M   287.6M    52%   fuseblk  /media/Recovery
"""

import sys
import os
import psutil

sparkpart = 0
sparktot = 0
sparkused = 0
sparkfree = 0
sparkpct = 0
sparktype = 0
sparkmtpt = 0

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

def get_disk_usage_values(*args):
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue    
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))
        header01 = (templ % ("Device", "Total", "Used", "Free", "Use ", "Type","Mount"))
        sparkpart = part.device
        sparktot = bytes2human(usage.total)
        sparkused = bytes2human(usage.used)
        sparkfree = bytes2human(usage.free)
        sparkpct = int(usage.percent)
        sparktype = part.fstype
        sparkmtpt = part.mountpoint
        return (header01 + '\n' +
            sparkpart + "      " + sparktot + "   " +  sparkused + " " +  sparkfree + "     " +  str(sparkpct) + "        " +  sparktype + "     " +  sparkmtpt)

def main():
        get_disk_usage_values()

if __name__ == "__main__":
    import sys
    main()
