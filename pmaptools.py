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
"""
import os

# Import the PyQt and QGIS libraries

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
from qgis.core import *

class PMAPTools:

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface

  def initGui(self):
    # Load pmapDock.ui
    path = os.path.dirname( os.path.abspath( __file__ ) )
    self.dock = uic.loadUi( os.path.join( path, "pmapDock.ui" ) )
    self.iface.addDockWidget( Qt.RightDockWidgetArea, self.dock )

    # Load HTML Guides and buttons in the Dock
    self.dock.webView.load( QUrl.fromLocalFile(os.path.join( path, "PMaPToolsDocs.html" )) )
    self.dock.showAboutButton.clicked.connect( self.showAbout )

    # Create KKP BPN Link
    self.action_kkp = QAction( QIcon( os.path.dirname(os.path.realpath(__file__)) + 
      "/kkp.ico" ), "KKP BPN Pusat", self.iface.mainWindow() )
    QObject.connect( self.action_kkp, SIGNAL("triggered()"), self.visitBPN )

    # Create InaSAFE Link
    self.action_inasafe = QAction( QIcon( os.path.dirname(os.path.realpath(__file__)) + 
      "/inasafe.ico" ), "InaSAFE BNPB", self.iface.mainWindow() )
    QObject.connect( self.action_inasafe, SIGNAL("triggered()"), self.visitInasafe )

    # Create BKPM Link
    self.action_bkpm = QAction( QIcon( os.path.dirname(os.path.realpath(__file__)) + 
      "/bkpm.ico" ), "BKPM SPIPISE", self.iface.mainWindow() )
    QObject.connect( self.action_bkpm, SIGNAL("triggered()"), self.visitBkpm )

    # Create Toggle Dock Button
    self.toggle_dock = QAction( QIcon( os.path.dirname(os.path.realpath(__file__)) + 
      "/map_marker.png" ), "Dock PMaP Tools", self.iface.mainWindow() )
    self.toggle_dock.setCheckable(True)
    self.toggle_dock.setChecked(True)
    QObject.connect( self.toggle_dock, SIGNAL("triggered()"), self.toggleDock )

    # Create About Dialog
    self.show_about = QAction( QIcon( os.path.dirname(os.path.realpath(__file__)) + 
      "/icon_default.png" ), "Tentang PMaP", self.iface.mainWindow() )
    QObject.connect( self.show_about, SIGNAL("triggered()"), self.showAbout )

    # Remove QGIS Help menu
    helpMenu = self.iface.helpMenu()
    helpMenu.menuAction().setVisible( False )

    # Add a custom menu
    self.menu = QMenu( "&PMaP Tools", self.iface.mainWindow().menuBar() )
    self.iface.mainWindow().menuBar().addMenu( self.menu )
    # Add sub-menus
    self.menu.addAction( self.action_kkp )
    self.menu.addAction( self.action_inasafe )
    self.menu.addAction( self.action_bkpm )
    self.menu.addSeparator()
    self.menu.addAction( self.show_about )
    
    # Add a custom toolbar
    self.toolbar = self.iface.addToolBar( "PMAP Tools" )
    self.toolbar.addAction( self.toggle_dock )
    self.toolbar.addAction( self.show_about )

  def unload(self):
    # Remove the plugin menu item and icon
    self.menu.deleteLater()
    self.toolbar.deleteLater()
    self.dock.deleteLater()

  # visit link methods
  def visitBPN(self):
    QDesktopServices.openUrl( QUrl("http://kkp.bpn.go.id/") )

  def visitInasafe(self):
    QDesktopServices.openUrl( QUrl("http://inasafe.org/") )

  def visitBkpm(self):
    QDesktopServices.openUrl( QUrl("https://online-spipise.bkpm.go.id/") )

  def showAbout(self):
    QMessageBox.information( self.iface.mainWindow(), 
      "Tentang PMaP", 
      "Participatory Mapping and Planning (PMaP) atau Pemetaan dan Perencanaan Partisipatif merupakan bagian dari Proyek Kemakmuran Hijau yang bertujuan untuk merepresentasikan informasi spasial wilayah lokal yang mengkombinasikan teknologi kartografi modern dengan metode-metode partisipatif.", 
      QMessageBox.Ok )

  # Run method that performs all the real work
  def toggleDock(self):
    """Show or hide the dock widget."""
    if self.dock.isVisible():
      self.dock.setVisible(False)
    else:
      self.dock.setVisible(True)
      self.dock.raise_()
