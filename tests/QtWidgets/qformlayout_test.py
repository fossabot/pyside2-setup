#############################################################################
##
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the test suite of PySide2.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

import unittest
from PySide2.QtWidgets import QFormLayout, QWidget

from helper import UsesQApplication

class QFormLayoutTest(UsesQApplication):

    def testGetItemPosition(self):
        formlayout = QFormLayout()
        row, role = formlayout.getItemPosition(0)
        self.assert_(isinstance(row, int))
        self.assert_(isinstance(role, QFormLayout.ItemRole))
        self.assertEqual(row, -1)

        widget = QWidget()
        formlayout.addRow(widget)
        row, role = formlayout.getItemPosition(0)
        self.assert_(isinstance(row, int))
        self.assert_(isinstance(role, QFormLayout.ItemRole))
        self.assertEqual(row, 0)
        self.assertEqual(role, QFormLayout.SpanningRole)

    def testGetWidgetPosition(self):
        formlayout = QFormLayout()
        widget = QWidget()
        row, role = formlayout.getWidgetPosition(widget)
        self.assert_(isinstance(row, int))
        self.assert_(isinstance(role, QFormLayout.ItemRole))
        self.assertEqual(row, -1)

        formlayout.addRow(widget)
        row, role = formlayout.getWidgetPosition(widget)
        self.assert_(isinstance(row, int))
        self.assert_(isinstance(role, QFormLayout.ItemRole))
        self.assertEqual(row, 0)
        self.assertEqual(role, QFormLayout.SpanningRole)

    def testGetLayoutPosition(self):
        formlayout = QFormLayout()
        layout = QFormLayout()
        row, role = formlayout.getLayoutPosition(layout)
        self.assert_(isinstance(row, int))
        self.assert_(isinstance(role, QFormLayout.ItemRole))
        self.assertEqual(row, -1)

        formlayout.addRow(layout)
        row, role = formlayout.getLayoutPosition(layout)
        self.assert_(isinstance(row, int))
        self.assert_(isinstance(role, QFormLayout.ItemRole))
        self.assertEqual(row, 0)
        self.assertEqual(role, QFormLayout.SpanningRole)


if __name__ == "__main__":
   unittest.main()

