import datetime
# from dateutil.parser import parse
# from github import Github
from io import BytesIO
from itertools import groupby
import json
import os
import pipes
import re
import sys
import time

from fabric.api import env, task, local, sudo, run, prompt, settings
from fabric.api import get, put, require
from fabric.colors import red, green, blue, yellow
from fabric.context_managers import cd, prefix, show, hide, shell_env, quiet, lcd
from fabric.contrib.files import exists, sed, upload_template
from fabric.utils import puts

from fabfiles.github import test_utility_function


# FAB SETTTINGS
################################################################################
env.user = os.environ.get('USER')  # assume ur local username == remote username
env.roledefs = {}  # combined roles from inventory and integrationservers



# PREREQUISITES
################################################################################
# 1. SusOps engineer be part of the GCP project kolibri-demo-servers
# 2. The username $USER must be one of the default accounts created on instances
# see https://console.cloud.google.com/compute/metadata?project=kolibri-demo-servers


# PROVISIONING
################################################################################
from fabfiles.gcp import inventory
from fabfiles.gcp import create, delete
from fabfiles.gcp import list_instances, checkdns, checkdiskspace
from fabfiles.gcp import info, shell

env.roledefs.update(inventory)  # QA demoservers inventory (GCP VMs)


# DEMOSERVERS
################################################################################
from fabfiles.demoservers import demoserver, restart_kolibri, update_kolibri
from fabfiles.demoservers import import_channel, import_channels
from fabfiles.demoservers import stop_kolibri, restart_kolibri
from fabfiles.demoservers import delete_kolibri



# PROXY SERVICE
################################################################################
from fabfiles.proxyservice import checkproxies, update_proxy_servers
from fabfiles.proxyservice import install_squid_proxy, update_squid_proxy
from fabfiles.proxyservice import uninstall_squid_proxy





@task
def test_task():
    puts(blue('print blue...'))
    puts(red('print red'))
    puts(green('print green'))
    print('calling module:', test_utility_function())
    print('DONE')





