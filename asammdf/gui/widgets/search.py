# -*- coding: utf-8 -*-
from pathlib import Path

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import uic

from ..ui import resource_qt5 as resource_rc

HERE = Path(__file__).resolve().parent


class SearchWidget(QtWidgets.QWidget):

    selectionChanged = QtCore.pyqtSignal()

    def __init__(self, channels_db, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(HERE.joinpath("..", "ui", "search_widget.ui"), self)
        self.channels_db = channels_db

        self.matches = 0
        self.current_index = 1
        self.entries = []

        completer = QtWidgets.QCompleter(sorted(self.channels_db, key=lambda x: x.lower()), self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer.setModelSorting(QtWidgets.QCompleter.CaseInsensitivelySortedModel)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        self.search.setCompleter(completer)

        self.search.textChanged.connect(self.display_results)

        self.up_btn.clicked.connect(self.up)
        self.down_btn.clicked.connect(self.down)

    def down(self, event):
        if self.matches:
            self.current_index += 1
            if self.current_index >= self.matches:
                self.current_index = 0
            self.label.setText(f"{self.current_index + 1} of {self.matches}")
            self.selectionChanged.emit()

    def up(self, event):
        if self.matches:
            self.current_index -= 1
            if self.current_index < 0:
                self.current_index = self.matches - 1
            self.label.setText(f"{self.current_index + 1} of {self.matches}")
            self.selectionChanged.emit()

    def set_search_option(self, option):
        if option == "Match start":
            self.search.completer().setFilterMode(QtCore.Qt.MatchStartsWith)
        elif option == "Match contains":
            self.search.completer().setFilterMode(QtCore.Qt.MatchContains)

    def display_results(self, text):
        channel_name = text.strip()
        if channel_name in self.channels_db:
            self.entries = self.channels_db[channel_name]
            self.matches = len(self.entries)
            self.label.setText(f"1 of {self.matches}")
            self.current_index = 0
            self.selectionChanged.emit()

        else:
            self.label.setText("No match")
            self.matches = 0
            self.current_index = 0
            self.entries = []
