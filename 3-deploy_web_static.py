#!/usr/bin/python3
"""fabric script to create tarball for deployment"""
from datetime import datetime
import os
from fabric.api import *

env.hosts = ["35.185.2.47", "3.94.190.44"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """deploy tarball content to server"""
    if not os.path.exists(archive_path):
        return False
    base = os.path.basename(archive_path)
    f_name = base.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(f_name))
    run("tar -xzf /tmp/{} \
        -C /data/web_static/releases/{}".format(base, f_name))
    run("rm /tmp/{}".format(base))
    run("rm -rf /data/web_static/current")
    run("ln -fs /data/web_static/releases/{}/ \
        /data/web_static/current".format(f_name))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/current/web_static")

    return True


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


def deploy():
    """runner to make package and deploy"""
    ball = do_pack()
    if path is None:
        return false
    return(do_deploy(ball))
