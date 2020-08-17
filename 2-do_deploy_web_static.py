#!/usr/bin/python3
"""fabric script to create tarball for deployment"""
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
