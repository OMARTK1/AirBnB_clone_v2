#!/usr/bin/python3
# Fabfile to delete out-of-date archives
import os
from fabric.api import env, lcd, local, run, cd

env.hosts = ["104.196.168.90", "35.196.46.172"]

def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep. If set to 0 or 1, keeps only the most recent archive. 
                      If set to 2, keeps the two most recent archives, and so on.

    Returns:
        None
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
