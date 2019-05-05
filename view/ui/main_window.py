# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.pyqt5/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/list.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.vlw_left_coll = QtWidgets.QWidget(self.central_widget)
        self.vlw_left_coll.setMinimumSize(QtCore.QSize(310, 0))
        self.vlw_left_coll.setMaximumSize(QtCore.QSize(310, 16777215))
        self.vlw_left_coll.setObjectName("vlw_left_coll")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.vlw_left_coll)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.organization_data = QtWidgets.QGroupBox(self.vlw_left_coll)
        self.organization_data.setAutoFillBackground(True)
        self.organization_data.setObjectName("organization_data")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.organization_data)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fl_organization_labels = QtWidgets.QFormLayout()
        self.fl_organization_labels.setObjectName("fl_organization_labels")
        self.name_label = QtWidgets.QLabel(self.organization_data)
        self.name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.name_label.setObjectName("name_label")
        self.fl_organization_labels.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.org_name = QtWidgets.QLabel(self.organization_data)
        self.org_name.setWordWrap(True)
        self.org_name.setObjectName("org_name")
        self.fl_organization_labels.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.org_name)
        self.inn_label = QtWidgets.QLabel(self.organization_data)
        self.inn_label.setObjectName("inn_label")
        self.fl_organization_labels.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.inn_label)
        self.inn = QtWidgets.QLabel(self.organization_data)
        self.inn.setObjectName("inn")
        self.fl_organization_labels.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inn)
        self.ogrn_label = QtWidgets.QLabel(self.organization_data)
        self.ogrn_label.setObjectName("ogrn_label")
        self.fl_organization_labels.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ogrn_label)
        self.ogrn = QtWidgets.QLabel(self.organization_data)
        self.ogrn.setObjectName("ogrn")
        self.fl_organization_labels.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ogrn)
        self.org_address_label = QtWidgets.QLabel(self.organization_data)
        self.org_address_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.org_address_label.setObjectName("org_address_label")
        self.fl_organization_labels.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.org_address_label)
        self.org_address = QtWidgets.QLabel(self.organization_data)
        self.org_address.setWordWrap(True)
        self.org_address.setObjectName("org_address")
        self.fl_organization_labels.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.org_address)
        self.head_full_name_label = QtWidgets.QLabel(self.organization_data)
        self.head_full_name_label.setObjectName("head_full_name_label")
        self.fl_organization_labels.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.head_full_name_label)
        self.head_full_name = QtWidgets.QLabel(self.organization_data)
        self.head_full_name.setObjectName("head_full_name")
        self.fl_organization_labels.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.head_full_name)
        self.representative_full_name_label = QtWidgets.QLabel(self.organization_data)
        self.representative_full_name_label.setObjectName("representative_full_name_label")
        self.fl_organization_labels.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.representative_full_name_label)
        self.representative_full_name = QtWidgets.QLabel(self.organization_data)
        self.representative_full_name.setObjectName("representative_full_name")
        self.fl_organization_labels.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.representative_full_name)
        self.representative_position_label = QtWidgets.QLabel(self.organization_data)
        self.representative_position_label.setObjectName("representative_position_label")
        self.fl_organization_labels.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.representative_position_label)
        self.representative_position = QtWidgets.QLabel(self.organization_data)
        self.representative_position.setObjectName("representative_position")
        self.fl_organization_labels.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.representative_position)
        self.verticalLayout_2.addLayout(self.fl_organization_labels)
        self.organization_edit_btn = QtWidgets.QPushButton(self.organization_data)
        self.organization_edit_btn.setObjectName("organization_edit_btn")
        self.verticalLayout_2.addWidget(self.organization_edit_btn)
        self.verticalLayout_4.addWidget(self.organization_data)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.is_nov_obl = QtWidgets.QCheckBox(self.vlw_left_coll)
        self.is_nov_obl.setChecked(True)
        self.is_nov_obl.setObjectName("is_nov_obl")
        self.verticalLayout_4.addWidget(self.is_nov_obl)
        self.hide_group_box = QtWidgets.QGroupBox(self.vlw_left_coll)
        self.hide_group_box.setAutoFillBackground(True)
        self.hide_group_box.setObjectName("hide_group_box")
        self.gridLayout = QtWidgets.QGridLayout(self.hide_group_box)
        self.gridLayout.setObjectName("gridLayout")
        self.hide_col_family_name = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_family_name.setChecked(True)
        self.hide_col_family_name.setObjectName("hide_col_family_name")
        self.gridLayout.addWidget(self.hide_col_family_name, 0, 0, 1, 1)
        self.hide_col_sex = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_sex.setChecked(True)
        self.hide_col_sex.setObjectName("hide_col_sex")
        self.gridLayout.addWidget(self.hide_col_sex, 3, 0, 1, 1)
        self.hide_col_hazard_types = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_hazard_types.setChecked(True)
        self.hide_col_hazard_types.setObjectName("hide_col_hazard_types")
        self.gridLayout.addWidget(self.hide_col_hazard_types, 2, 1, 1, 1)
        self.hide_col_patronymic = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_patronymic.setChecked(True)
        self.hide_col_patronymic.setObjectName("hide_col_patronymic")
        self.gridLayout.addWidget(self.hide_col_patronymic, 2, 0, 1, 1)
        self.hide_col_birth_date = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_birth_date.setChecked(True)
        self.hide_col_birth_date.setObjectName("hide_col_birth_date")
        self.gridLayout.addWidget(self.hide_col_birth_date, 4, 0, 1, 1)
        self.hide_col_specialty = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_specialty.setChecked(True)
        self.hide_col_specialty.setObjectName("hide_col_specialty")
        self.gridLayout.addWidget(self.hide_col_specialty, 1, 1, 1, 1)
        self.hide_col_first_name = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_first_name.setChecked(True)
        self.hide_col_first_name.setObjectName("hide_col_first_name")
        self.gridLayout.addWidget(self.hide_col_first_name, 1, 0, 1, 1)
        self.hide_col_experience = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_experience.setChecked(True)
        self.hide_col_experience.setObjectName("hide_col_experience")
        self.gridLayout.addWidget(self.hide_col_experience, 0, 1, 1, 1)
        self.hide_col_hazard_factors = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_hazard_factors.setChecked(True)
        self.hide_col_hazard_factors.setObjectName("hide_col_hazard_factors")
        self.gridLayout.addWidget(self.hide_col_hazard_factors, 3, 1, 1, 1)
        self.hide_col_address_free_form = QtWidgets.QCheckBox(self.hide_group_box)
        self.hide_col_address_free_form.setChecked(True)
        self.hide_col_address_free_form.setObjectName("hide_col_address_free_form")
        self.gridLayout.addWidget(self.hide_col_address_free_form, 5, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.hide_group_box)
        self.horizontalLayout_7.addWidget(self.vlw_left_coll)
        self.separator = QtWidgets.QFrame(self.central_widget)
        self.separator.setFrameShape(QtWidgets.QFrame.VLine)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator.setObjectName("separator")
        self.horizontalLayout_7.addWidget(self.separator)
        self.vl_employees_list = QtWidgets.QVBoxLayout()
        self.vl_employees_list.setObjectName("vl_employees_list")
        self.employees_table = QtWidgets.QTableView(self.central_widget)
        self.employees_table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.employees_table.setAlternatingRowColors(True)
        self.employees_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.employees_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.employees_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.employees_table.setSortingEnabled(True)
        self.employees_table.setObjectName("employees_table")
        self.employees_table.horizontalHeader().setHighlightSections(False)
        self.employees_table.horizontalHeader().setSortIndicatorShown(True)
        self.employees_table.verticalHeader().setVisible(False)
        self.employees_table.verticalHeader().setDefaultSectionSize(50)
        self.vl_employees_list.addWidget(self.employees_table)
        self.hl_employees_list_btns = QtWidgets.QHBoxLayout()
        self.hl_employees_list_btns.setObjectName("hl_employees_list_btns")
        self.add_employee_btn = QtWidgets.QPushButton(self.central_widget)
        self.add_employee_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.add_employee_btn.setObjectName("add_employee_btn")
        self.hl_employees_list_btns.addWidget(self.add_employee_btn)
        self.remove_employee_btn = QtWidgets.QPushButton(self.central_widget)
        self.remove_employee_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.remove_employee_btn.setObjectName("remove_employee_btn")
        self.hl_employees_list_btns.addWidget(self.remove_employee_btn)
        self.vl_employees_list.addLayout(self.hl_employees_list_btns)
        self.horizontalLayout_7.addLayout(self.vl_employees_list)
        self.horizontalLayout_7.setStretch(2, 1)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu_new_file = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/star.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_new_file.setIcon(icon1)
        self.menu_new_file.setObjectName("menu_new_file")
        self.menu_open = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_open.setIcon(icon2)
        self.menu_open.setObjectName("menu_open")
        self.menu_save = QtWidgets.QAction(MainWindow)
        self.menu_save.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/diskette.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_save.setIcon(icon3)
        self.menu_save.setObjectName("menu_save")
        self.menu_save_as = QtWidgets.QAction(MainWindow)
        self.menu_save_as.setEnabled(False)
        self.menu_save_as.setIcon(icon3)
        self.menu_save_as.setObjectName("menu_save_as")
        self.menu_export_word = QtWidgets.QAction(MainWindow)
        self.menu_export_word.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/word.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_export_word.setIcon(icon4)
        self.menu_export_word.setObjectName("menu_export_word")
        self.menu_about = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/question.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_about.setIcon(icon5)
        self.menu_about.setObjectName("menu_about")
        self.menu_tes = QtWidgets.QAction(MainWindow)
        self.menu_tes.setObjectName("menu_tes")
        self.menu_auto_save = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/files_list.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_auto_save.setIcon(icon6)
        self.menu_auto_save.setObjectName("menu_auto_save")
        self.menu_import_excel = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/excel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_import_excel.setIcon(icon7)
        self.menu_import_excel.setObjectName("menu_import_excel")
        self.menu_file.addAction(self.menu_new_file)
        self.menu_file.addAction(self.menu_open)
        self.menu_file.addAction(self.menu_import_excel)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_save)
        self.menu_file.addAction(self.menu_save_as)
        self.menu_file.addAction(self.menu_auto_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_export_word)
        self.menu_help.addAction(self.menu_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.employees_table, self.add_employee_btn)
        MainWindow.setTabOrder(self.add_employee_btn, self.remove_employee_btn)
        MainWindow.setTabOrder(self.remove_employee_btn, self.organization_edit_btn)
        MainWindow.setTabOrder(self.organization_edit_btn, self.hide_col_family_name)
        MainWindow.setTabOrder(self.hide_col_family_name, self.hide_col_first_name)
        MainWindow.setTabOrder(self.hide_col_first_name, self.hide_col_patronymic)
        MainWindow.setTabOrder(self.hide_col_patronymic, self.hide_col_sex)
        MainWindow.setTabOrder(self.hide_col_sex, self.hide_col_birth_date)
        MainWindow.setTabOrder(self.hide_col_birth_date, self.hide_col_address_free_form)
        MainWindow.setTabOrder(self.hide_col_address_free_form, self.hide_col_experience)
        MainWindow.setTabOrder(self.hide_col_experience, self.hide_col_specialty)
        MainWindow.setTabOrder(self.hide_col_specialty, self.hide_col_hazard_types)
        MainWindow.setTabOrder(self.hide_col_hazard_types, self.hide_col_hazard_factors)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список сотрудников"))
        self.organization_data.setTitle(_translate("MainWindow", "Данные об организации"))
        self.name_label.setText(_translate("MainWindow", "Наименование:"))
        self.org_name.setText(_translate("MainWindow", "<НЕ ЗАПОЛНЕНО>"))
        self.inn_label.setText(_translate("MainWindow", "ИНН:"))
        self.inn.setText(_translate("MainWindow", "<НЕ ЗАПОЛНЕНО>"))
        self.ogrn_label.setText(_translate("MainWindow", "ОГРН:"))
        self.ogrn.setText(_translate("MainWindow", "<НЕ ЗАПОЛНЕНО>"))
        self.org_address_label.setText(_translate("MainWindow", "Адрес:"))
        self.org_address.setText(_translate("MainWindow", "<НЕ ЗАПОЛНЕНО>"))
        self.head_full_name_label.setText(_translate("MainWindow", "Руководитель:"))
        self.head_full_name.setText(_translate("MainWindow", "<НЕ ЗАПОЛНЕНО>"))
        self.representative_full_name_label.setText(_translate("MainWindow", "Представитель:"))
        self.representative_full_name.setText(_translate("MainWindow", "<НЕ ЗАПОЛНЕНО>"))
        self.representative_position_label.setText(_translate("MainWindow", "Должность:"))
        self.representative_position.setText(_translate("MainWindow", "<НЕ ЗАПОЛНЕНО>"))
        self.organization_edit_btn.setText(_translate("MainWindow", "Изменить"))
        self.is_nov_obl.setText(_translate("MainWindow", "Искать адреса только в Новгородской области?"))
        self.hide_group_box.setTitle(_translate("MainWindow", "Отображать сведения"))
        self.hide_col_family_name.setText(_translate("MainWindow", "Фамилия"))
        self.hide_col_sex.setText(_translate("MainWindow", "Пол"))
        self.hide_col_hazard_types.setText(_translate("MainWindow", "Типы вредностей"))
        self.hide_col_patronymic.setText(_translate("MainWindow", "Отчество"))
        self.hide_col_birth_date.setText(_translate("MainWindow", "Дата рождения"))
        self.hide_col_specialty.setText(_translate("MainWindow", "Должность"))
        self.hide_col_first_name.setText(_translate("MainWindow", "Имя"))
        self.hide_col_experience.setText(_translate("MainWindow", "Стаж"))
        self.hide_col_hazard_factors.setText(_translate("MainWindow", "Факторы вредностей"))
        self.hide_col_address_free_form.setText(_translate("MainWindow", "Адрес"))
        self.add_employee_btn.setText(_translate("MainWindow", "Добавить сотрудника  (F1)"))
        self.remove_employee_btn.setText(_translate("MainWindow", "Удалить сотрудника (Delete)"))
        self.menu_file.setTitle(_translate("MainWindow", "Файл"))
        self.menu_help.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "Открыть"))
        self.menu_new_file.setText(_translate("MainWindow", "Создать"))
        self.menu_open.setText(_translate("MainWindow", "Открыть"))
        self.menu_save.setText(_translate("MainWindow", "Сохранить"))
        self.menu_save_as.setText(_translate("MainWindow", "Сохранить как..."))
        self.menu_export_word.setText(_translate("MainWindow", "Экспорт в Word 2007"))
        self.menu_about.setText(_translate("MainWindow", "О программе..."))
        self.menu_about.setIconText(_translate("MainWindow", "О программе..."))
        self.menu_about.setToolTip(_translate("MainWindow", "Сведения о программе."))
        self.menu_tes.setText(_translate("MainWindow", "Файл1"))
        self.menu_auto_save.setText(_translate("MainWindow", "Список автосохранений"))
        self.menu_import_excel.setText(_translate("MainWindow", "Импорт из Excel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
