from __future__ import with_statement

from fabric.api import env, warn, settings, get, put
from fabric.colors import *

from install.utils import _r, _s, _p, _l, _L, _fe, _cd, _w
import install.utils as utils
from StringIO import StringIO


SUPPORTED_OSES = ("deb")
conf = env.conf

def osSupported():
  return env.TARGET_OS in SUPPORTED_OSES

if env.TARGET_OS in SUPPORTED_OSES:
  # import the corresponding modules
  from ..modules.basic import basic as basic 
  from ..modules.database import mysql as database 
  from ..modules.django import gunicorn as djangoserver
  from ..modules.static import nginx as staticserver
  from ..modules.worker import celery as worker


def about():
  return "production setup, uses production level servers, minifies code ect..."


def neededVars():
  return (
    ("REMOTE_IP", "machine to install", "10.0.0.10"),
    ("INSTALL_DIR", "where to install the server (absolute path)", "/srv/lmt"),
    ("VIRTENV_DIR", "where to install virtualenv (relative)", "/py_env"),
    ("SYS_USER", "the username the whole stuff will be running on (will be created)", "lmt"),
    ("SYS_PSW", "the password for SYS_USER (if user exists the pw IWLL BE CHANGED)", 'pw' ),#utils.psw_gen()),
    ("SYS_GROUP", "the group of the sys_user", "www-lmt")
  )


def beforeInstallCmds():
  
  # add users and groups
  with settings(warn_only=True):
    _s("groupadd -f %(SYS_GROUP)s" % conf)
    res = _s('adduser --ingroup %(SYS_GROUP)s --disabled-password --gecos "" %(SYS_USER)s' % conf)
    if res.return_code==4:
      warn(yellow("user already exists"))
    _s('echo "%(SYS_USER)s:%(SYS_PSW)s" | chpasswd' % conf)
    #exchange ssh jeys to automate login
    env.password = conf['SYS_PSW']
    _L("ssh-copy-id -i ~/.ssh/id_dsa.pub %(SYS_USER)s@%(REMOTE_IP)s")


def betweenInstallCmds():
  _s("mkdir -p %(INSTALL_DIR)s" % conf)
  _s("chown -R %(SYS_USER)s:%(SYS_GROUP)s %(INSTALL_DIR)s" % conf)
  _s("chmod u+rwx %(INSTALL_DIR)s" % conf)
  
  with _cd(conf['INSTALL_DIR']):
    _w("virtualenv --distribute --system-site-packages .%(VIRTENV_DIR)s" % conf)
  
  
def postInstallCmds():
  
  _w("mkdir -p " + conf['REPRO_DIR'])
  with _cd(conf['REPRO_DIR']):
    _r("git clone -b master https://github.com/RafiKueng/LensTools.git .")

    
#################################################################################  



def setup():
  
  # BACKEND
  
  with _cd(conf['REPRO_DIR']):
    _s("cp backend %(INSTALL_DIR)s/backend" % conf)
    





#################################################################################  

def _create_machine_config():
  inp = StringIO.StringIO()
  get(conf['INSTALL_DIR']+'/backend/settings/machine.template.py', inp)
  txt = inp.read()
  txt = txt % conf
  outp = StringIO.StringIO()
  outp.write(txt)
  put(outp, conf['INSTALL_DIR']+'/backend/settings/machine.py')
  
  
  
  
  
  
  
  
  
  
  
  
  
  