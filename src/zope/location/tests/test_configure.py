##############################################################################
#
# Copyright (c) 2003-2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Test ZCML loading
"""
import unittest

class Test_ZCML_loads(unittest.TestCase):

    def test_it(self):
        try:
            from zope.configuration.xmlconfig import _clearContext
            from zope.configuration.xmlconfig import _getContext
            from zope.configuration.xmlconfig import XMLConfig
        except ImportError:
            pass
        else:
            import zope.location
            _clearContext()
            context = _getContext()
            XMLConfig('configure.zcml', zope.location)
            adapters = ([x for x in context.actions
                            if x['discriminator'] is not None])
            self.assertEqual(len(adapters), 4)
        

def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(Test_ZCML_loads),
    ))