# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'channel_stats.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChannelStats(object):
    def setupUi(self, ChannelStats):
        ChannelStats.setObjectName("ChannelStats")
        ChannelStats.resize(363, 566)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        ChannelStats.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChannelStats)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cursor_group = QtWidgets.QGroupBox(ChannelStats)
        self.cursor_group.setFlat(False)
        self.cursor_group.setCheckable(False)
        self.cursor_group.setObjectName("cursor_group")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.cursor_group)
        self.gridLayout_4.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cursor_t = QtWidgets.QLabel(self.cursor_group)
        self.cursor_t.setText("")
        self.cursor_t.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cursor_t.setObjectName("cursor_t")
        self.gridLayout_4.addWidget(self.cursor_t, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.cursor_group)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)
        self.cursor_value = QtWidgets.QLabel(self.cursor_group)
        self.cursor_value.setText("")
        self.cursor_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cursor_value.setObjectName("cursor_value")
        self.gridLayout_4.addWidget(self.cursor_value, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.cursor_group)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.cursor_group)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 2, 1, 1)
        self.unit1 = QtWidgets.QLabel(self.cursor_group)
        self.unit1.setText("")
        self.unit1.setObjectName("unit1")
        self.gridLayout_4.addWidget(self.unit1, 1, 2, 1, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout.addWidget(self.cursor_group, 2, 0, 1, 2)
        self.range_group = QtWidgets.QGroupBox(ChannelStats)
        self.range_group.setObjectName("range_group")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.range_group)
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.selected_delta = QtWidgets.QLabel(self.range_group)
        self.selected_delta.setText("")
        self.selected_delta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.selected_delta.setObjectName("selected_delta")
        self.gridLayout_5.addWidget(self.selected_delta, 5, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.range_group)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)
        self.selected_stop = QtWidgets.QLabel(self.range_group)
        self.selected_stop.setText("")
        self.selected_stop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.selected_stop.setObjectName("selected_stop")
        self.gridLayout_5.addWidget(self.selected_stop, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.range_group)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.range_group)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 5, 0, 1, 1)
        self.selected_max = QtWidgets.QLabel(self.range_group)
        self.selected_max.setText("")
        self.selected_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.selected_max.setObjectName("selected_max")
        self.gridLayout_5.addWidget(self.selected_max, 4, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.range_group)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 2, 0, 1, 1)
        self.selected_delta_t = QtWidgets.QLabel(self.range_group)
        self.selected_delta_t.setText("")
        self.selected_delta_t.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.selected_delta_t.setObjectName("selected_delta_t")
        self.gridLayout_5.addWidget(self.selected_delta_t, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.range_group)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.range_group)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)
        self.selected_min = QtWidgets.QLabel(self.range_group)
        self.selected_min.setText("")
        self.selected_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.selected_min.setObjectName("selected_min")
        self.gridLayout_5.addWidget(self.selected_min, 3, 1, 1, 1)
        self.selected_start = QtWidgets.QLabel(self.range_group)
        self.selected_start.setText("")
        self.selected_start.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.selected_start.setObjectName("selected_start")
        self.gridLayout_5.addWidget(self.selected_start, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.range_group)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 0, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.range_group)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 1, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.range_group)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 2, 2, 1, 1)
        self.unit2 = QtWidgets.QLabel(self.range_group)
        self.unit2.setText("")
        self.unit2.setObjectName("unit2")
        self.gridLayout_5.addWidget(self.unit2, 3, 2, 1, 1)
        self.unit3 = QtWidgets.QLabel(self.range_group)
        self.unit3.setText("")
        self.unit3.setObjectName("unit3")
        self.gridLayout_5.addWidget(self.unit3, 4, 2, 1, 1)
        self.unit4 = QtWidgets.QLabel(self.range_group)
        self.unit4.setText("")
        self.unit4.setObjectName("unit4")
        self.gridLayout_5.addWidget(self.unit4, 5, 2, 1, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout.addWidget(self.range_group, 3, 0, 1, 2)
        self.visible_group = QtWidgets.QGroupBox(ChannelStats)
        self.visible_group.setObjectName("visible_group")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.visible_group)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_19 = QtWidgets.QLabel(self.visible_group)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.visible_group)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)
        self.visible_delta = QtWidgets.QLabel(self.visible_group)
        self.visible_delta.setText("")
        self.visible_delta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visible_delta.setObjectName("visible_delta")
        self.gridLayout_3.addWidget(self.visible_delta, 5, 1, 1, 1)
        self.visible_delta_t = QtWidgets.QLabel(self.visible_group)
        self.visible_delta_t.setText("")
        self.visible_delta_t.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visible_delta_t.setObjectName("visible_delta_t")
        self.gridLayout_3.addWidget(self.visible_delta_t, 2, 1, 1, 1)
        self.visible_min = QtWidgets.QLabel(self.visible_group)
        self.visible_min.setText("")
        self.visible_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visible_min.setObjectName("visible_min")
        self.gridLayout_3.addWidget(self.visible_min, 3, 1, 1, 1)
        self.visible_start = QtWidgets.QLabel(self.visible_group)
        self.visible_start.setText("")
        self.visible_start.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visible_start.setObjectName("visible_start")
        self.gridLayout_3.addWidget(self.visible_start, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.visible_group)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)
        self.visible_max = QtWidgets.QLabel(self.visible_group)
        self.visible_max.setText("")
        self.visible_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visible_max.setObjectName("visible_max")
        self.gridLayout_3.addWidget(self.visible_max, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.visible_group)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.visible_group)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.visible_stop = QtWidgets.QLabel(self.visible_group)
        self.visible_stop.setText("")
        self.visible_stop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.visible_stop.setObjectName("visible_stop")
        self.gridLayout_3.addWidget(self.visible_stop, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.visible_group)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.visible_group)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 0, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.visible_group)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 1, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.visible_group)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 2, 2, 1, 1)
        self.unit5 = QtWidgets.QLabel(self.visible_group)
        self.unit5.setText("")
        self.unit5.setObjectName("unit5")
        self.gridLayout_3.addWidget(self.unit5, 3, 2, 1, 1)
        self.unit6 = QtWidgets.QLabel(self.visible_group)
        self.unit6.setText("")
        self.unit6.setObjectName("unit6")
        self.gridLayout_3.addWidget(self.unit6, 4, 2, 1, 1)
        self.unit7 = QtWidgets.QLabel(self.visible_group)
        self.unit7.setText("")
        self.unit7.setObjectName("unit7")
        self.gridLayout_3.addWidget(self.unit7, 5, 2, 1, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout.addWidget(self.visible_group, 4, 0, 1, 2)
        self.overall_group = QtWidgets.QGroupBox(ChannelStats)
        self.overall_group.setObjectName("overall_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.overall_group)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.overall_group)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.overall_group)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.overall_start = QtWidgets.QLabel(self.overall_group)
        self.overall_start.setText("")
        self.overall_start.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.overall_start.setObjectName("overall_start")
        self.gridLayout_2.addWidget(self.overall_start, 0, 1, 1, 1)
        self.overall_stop = QtWidgets.QLabel(self.overall_group)
        self.overall_stop.setText("")
        self.overall_stop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.overall_stop.setObjectName("overall_stop")
        self.gridLayout_2.addWidget(self.overall_stop, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.overall_group)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.overall_min = QtWidgets.QLabel(self.overall_group)
        self.overall_min.setText("")
        self.overall_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.overall_min.setObjectName("overall_min")
        self.gridLayout_2.addWidget(self.overall_min, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.overall_group)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.overall_max = QtWidgets.QLabel(self.overall_group)
        self.overall_max.setText("")
        self.overall_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.overall_max.setObjectName("overall_max")
        self.gridLayout_2.addWidget(self.overall_max, 3, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.overall_group)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 0, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.overall_group)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 1, 2, 1, 1)
        self.unit8 = QtWidgets.QLabel(self.overall_group)
        self.unit8.setText("")
        self.unit8.setObjectName("unit8")
        self.gridLayout_2.addWidget(self.unit8, 2, 2, 1, 1)
        self.unit9 = QtWidgets.QLabel(self.overall_group)
        self.unit9.setText("")
        self.unit9.setObjectName("unit9")
        self.gridLayout_2.addWidget(self.unit9, 3, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout.addWidget(self.overall_group, 5, 0, 1, 2)
        self.name = QtWidgets.QLabel(ChannelStats)
        self.name.setTextFormat(QtCore.Qt.RichText)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(ChannelStats)
        QtCore.QMetaObject.connectSlotsByName(ChannelStats)

    def retranslateUi(self, ChannelStats):
        _translate = QtCore.QCoreApplication.translate
        ChannelStats.setWindowTitle(_translate("ChannelStats", "Form"))
        self.cursor_group.setTitle(_translate("ChannelStats", "Cursor"))
        self.label_12.setText(_translate("ChannelStats", "Timestamp      "))
        self.label_11.setText(_translate("ChannelStats", "Value"))
        self.label_2.setText(_translate("ChannelStats", " s"))
        self.range_group.setTitle(_translate("ChannelStats", "Selected range"))
        self.label_15.setText(_translate("ChannelStats", "Last timestamp"))
        self.label_17.setText(_translate("ChannelStats", "Max"))
        self.label_18.setText(_translate("ChannelStats", "Δ"))
        self.label_21.setText(_translate("ChannelStats", "Δt"))
        self.label_14.setText(_translate("ChannelStats", "Min"))
        self.label_13.setText(_translate("ChannelStats", "First timestamp"))
        self.label_20.setText(_translate("ChannelStats", " s"))
        self.label_22.setText(_translate("ChannelStats", " s"))
        self.label_23.setText(_translate("ChannelStats", " s"))
        self.visible_group.setTitle(_translate("ChannelStats", "Visible range"))
        self.label_19.setText(_translate("ChannelStats", "Δ"))
        self.label_16.setText(_translate("ChannelStats", "Δt"))
        self.label_10.setText(_translate("ChannelStats", "Max"))
        self.label_7.setText(_translate("ChannelStats", "First timestamp"))
        self.label_8.setText(_translate("ChannelStats", "Last timestamp"))
        self.label_9.setText(_translate("ChannelStats", "Min"))
        self.label_24.setText(_translate("ChannelStats", " s"))
        self.label_25.setText(_translate("ChannelStats", " s"))
        self.label_26.setText(_translate("ChannelStats", " s"))
        self.overall_group.setTitle(_translate("ChannelStats", "Overall"))
        self.label_6.setText(_translate("ChannelStats", "Max"))
        self.label_3.setText(_translate("ChannelStats", "First timestamp"))
        self.label_5.setText(_translate("ChannelStats", "Min"))
        self.label_4.setText(_translate("ChannelStats", "Last timestamp"))
        self.label_27.setText(_translate("ChannelStats", " s"))
        self.label_28.setText(_translate("ChannelStats", " s"))
        self.name.setText(_translate("ChannelStats", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#550000;\">Channel name</span></p></body></html>"))
