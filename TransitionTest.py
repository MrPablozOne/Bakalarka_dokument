#
#    Copyright (C) 2014 Pavel Siemko
#
#    This file is part of Kaira.
#
#    Kaira is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License, or
#    (at your option) any later version.
#
#    Kaira is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Kaira.  If not, see <http://www.gnu.org/licenses/>.
#

#Pokus o unittest libovolneho prechodu


#import neteditor
#from neteditor import NetList


class TransitionTest:


    def __init__(self, neteditor):
        self.neteditor = neteditor
        self.netlist = None
        self.netlist = self.neteditor.get_net()

        #self.netlist._add_net()

    #def doNet(self):

    def doTest(self):
        print("ahoj2")


def doTest():
    print("ahoj2")

