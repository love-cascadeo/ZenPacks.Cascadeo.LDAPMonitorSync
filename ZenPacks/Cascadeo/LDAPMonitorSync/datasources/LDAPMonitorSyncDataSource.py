###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2008, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

__doc__='''LDAPMonitorSyncDataSource.py

Defines datasource for LDAPMonitorSync
'''

from Globals import InitializeClass

import Products.ZenModel.BasicDataSource as BasicDataSource

import os
import stat
import shutil

class LDAPMonitorSyncDataSource(BasicDataSource.BasicDataSource):

	def __init__(self, id, title=None, buildRelations=True):
		BasicDataSource.BasicDataSource.__init__(self, id, title, buildRelations)
		script_path = os.path.join(os.path.dirname( __file__ ), '..', 'lib', 'check_ldap_sync.sh')
		new_file = '/usr/local/zenoss/zenoss/libexec/check_ldap_sync.sh'
		shutil.copyfile(script_path, new_file)
		st = os.stat(new_file)
		os.chmod(new_file, st.st_mode | stat.S_IEXEC)

InitializeClass(LDAPMonitorSyncDataSource)
