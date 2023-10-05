#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Compress the contents of the web_static folder into a .tgz archive.
    """

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + timestamp + ".tgz"
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} web_static".format(archive_name))
    if result.return_code == 0:
        return "versions/{}".format(archive_name)
    else:
        return None
