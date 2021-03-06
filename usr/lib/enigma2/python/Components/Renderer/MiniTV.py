 <!-- chStreams -->
  <screen name="1channel.ch" position="center,center" size="1280,720" flags="wfNoBorder">
    <ePixmap position="0,0" size="1280,720" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/liquidblue/images/mpback.png" />
    <widget source="global.CurrentTime" render="Label" position="840,42" size="300,28" font="mediaportal; 26" halign="left" backgroundColor="#26181d20" transparent="1" foregroundColor="#00bbbbbb">
      <convert type="ClockToText">Format:%A, %d.%m.%Y</convert>
    </widget>
    <widget source="global.CurrentTime" render="Label" position="1140,42" size="100,28" font="mediaportal;26" halign="center" backgroundColor="#26181d20" transparent="1" foregroundColor="#00bbbbbb">
      <convert type="ClockToText">Default</convert>
    </widget>
    <widget source="session.VideoPicture" render="Pig" position="913,136" size="328,186" zPosition="3" backgroundColor="transparent" />
    <eLabel position="912,135" size="330,188" backgroundColor="#00ffffff" zPosition="0" name="Videoback" foregroundColor="#00ffffff" />
    <!-- select screen -->
    <widget name="leftContentTitle" position="913,356" size="328,100" backgroundColor="#26181d20" transparent="1" zPosition="1" font="mediaportal;24" valign="center" halign="center" foregroundColor="#00ffffff" />
    <widget name="streamlist" position="55,136" size="850,380" backgroundColor="#26181d20" scrollbarMode="showOnDemand" transparent="1" selectionPixmap="/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/liquidblue/images/sel.png" foregroundColor="#00bbbbbb" />
    <widget name="stationIcon" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/MediaPortal/skins/liquidblue/images/no_coverArt.png" position="917,439" size="320,240" transparent="1" alphatest="blend" />
    <widget name="handlung" position="55,525" size="850,160" backgroundColor="#26181d20" transparent="1" font="mediaportal;18" valign="top" foregroundColor="#00ffffff" />
  </screen>                                                 
				infobarinstance = InfoBar.instance
				if infobarinstance.session.pipshown: # check if PiP is already shown
					self.currentPiPService = infobarinstance.session.pip.getCurrentService() # need current service
					self.currentPiPServicePath = infobarinstance.session.pip.servicePath # and current service path for reactivating
					infobarinstance.showPiP() # it is, close it!
				if self.Size:
					self.instance.resize(self.Size)
				if self.Position:
					self.instance.move(self.Position)
				self.timer.start(500)
			else:
				self.instance.hide()

	def onHide(self):
		self.timer.stop()
		self.source.shown = False
		self.source.closePiPService()
		if self.instance:
			self.preWidgetRemove(self.instance)
		# check if PiP was runnung before
		if self.currentPiPService is not None and self.currentPiPServicePath is not None:
			# PiP was running, so enabled it 
			from Screens.InfoBar import InfoBar
			from Screens.PictureInPicture import PictureInPicture
			infobarinstance = InfoBar.instance
			infobarinstance.session.pip = infobarinstance.session.instantiateDialog(PictureInPicture)
			infobarinstance.session.pip.show()
			if infobarinstance.session.pip.playService(self.currentPiPService):
				infobarinstance.session.pipshown = True
				infobarinstance.session.pip.servicePath = self.currentPiPServicePath
			else:
				infobarinstance.session.pipshown = False
				del infobarinstance.session.pip
		self.currentPiPService = None
		self.currentPiPServicePath = None
