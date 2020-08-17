#!/usr/bin/python3
"""fabric script to create tarball for deployment"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """pack script to make tarball"""
    local("mkdir -p versions")
    file = 'versions/web_static_{}.tgz'\
           .format(datetime.strftime(datetime.now(), "%Y%m%d%I%M%S"))
    ball = 'tar -cvzf {} web_static'.format(file)
    run = local(ball)
    if run.failed:
        return None
    return file
