from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QFont

iconPlayRed = QIcon()
iconPlayRed.addFile(u":/Icons/images/icons/icons8-play_red.png",
                    QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconPlayGray = QIcon()
iconPlayGray.addFile(u":/Icons/images/icons/icons8-play_gray.png",
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconPauseRed = QIcon()
iconPauseRed.addFile(u":/Icons/images/icons/icons8-pause_red.png",
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconRecordGray = QIcon()
iconRecordGray.addFile(u":/Icons/images/icons/icons8-record_gray.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconRecordRed = QIcon()
iconRecordRed.addFile(u":/Icons/images/icons/icons8-record_red.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconRecordDotGray = QIcon()
iconRecordDotGray.addFile(u":/Icons/images/icons/icons8-record-dot_gray.png",
                          QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconRecordDotRed = QIcon()
iconRecordDotRed.addFile(u":/Icons/images/icons/icons8-record-dot_red.png",
                         QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconForwardGray = QIcon()
iconForwardGray.addFile(u":/Icons/images/icons/icons8-forward_gray.png",
                        QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconForwardRed = QIcon()
iconForwardRed.addFile(u":/Icons/images/icons/icons8-forward_red.png",
                       QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconBackwardGray = QIcon()
iconBackwardGray.addFile(u":/Icons/images/icons/icons8-replay_gray.png",
                         QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconBackwardRed = QIcon()
iconBackwardRed.addFile(u":/Icons/images/icons/icons8-replay_red.png",
                        QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconSoundGray = QIcon()
iconSoundGray.addFile(u":/Icons/images/icons/icons8-audiomaster_gray.png",
                      QSize(), QIcon.Mode.Normal, QIcon.State.Off)

iconSoundRed = QIcon()
iconSoundRed.addFile(u":/Icons/images/icons/icons8-audiomaster_red.png",
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)


font5 = QFont()
font5.setFamilies([u"Poppins"])
font5.setBold(False)

colors = ["#575757", "#868686", "#0D0404", "#757575"]
