# __init__.py
import shutil, errno
import os

def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

src_fn = os.path.dirname(os.path.abspath(__file__)) + "/check_ldap_sync.sh"
dst_fn = "/usr/local/zenoss/zenoss/libexec/check_ldap_sync.sh"
copyanything(src_fn, dst_fn)
