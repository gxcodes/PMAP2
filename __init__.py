"""
/***************************************************************************
                                   PMAP Tools
                  Plugin to show PMAP Desktop IMS Tools Menu
                              -------------------
        begin                : 2016-06-20
        copyright            : (C) 2016 by Angga G. Pratama
        email                : a.pratama@forestcarbon.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "PMAP Tools"
def description():
    return "Plugin to show PMAP Desktop IMS Tools Menu"
def version():
    return "Version 1.0"
def icon():
    return "icon_default.png"
def qgisMinimumVersion():
    return "2.0"
def classFactory(iface):
    # load PMAPTools class from file pmaptools.py
    from pmaptools import PMAPTools
    return PMAPTools(iface)
