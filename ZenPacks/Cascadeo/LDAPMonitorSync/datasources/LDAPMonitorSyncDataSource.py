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
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from AccessControl import ClassSecurityInfo, Permissions
from Products.ZenUtils.ZenTales import talesCompile, getEngine

import os


class LDAPMonitorSyncDataSource(ZenPackPersistence,
                                BasicDataSource.BasicDataSource):
    
    ZEN_COMMAND = 'COMMAND'
    
    sourcetypes = (ZEN_COMMAND,)
    sourcetype = ZEN_COMMAND

    ZENPACKID = 'ZenPacks.Cascadeo.LDAPMonitorSync'

    parser = 'Auto'

    eventClass = '/Cmd'

    _properties = BasicDataSource.BasicDataSource._properties
        
    def __init__(self, id, title=None, buildRelations=True):
        BasicDataSource.BasicDataSource.__init__(self, id, title,
                buildRelations)

    def useZenCommand(self):
        return True


    def getCommand(self, context):
        cmd = 'check_ldap_sync.sh ldap-master-1.cascadeo.com ${dev/id}'
        cmd = BasicDataSource.BasicDataSource.getCommand(self, context, cmd)
        return cmd


    def checkCommandPrefix(self, context, cmd):
        if self.usessh:
            return os.path.join(context.zCommandPath, cmd)
        zp = self.getZenPack(context)
        return zp.path('lib', cmd)


InitializeClass(LDAPMonitorSyncDataSource)
