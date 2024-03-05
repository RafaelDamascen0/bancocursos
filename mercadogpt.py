import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout,
    QLineEdit, QTableWidget, QTableWidgetItem, QPushButton
)
from PyQt5.QtGui import QPixmap


class CaixaMercado(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 25, 1590, 840)
        self.setWindowTitle("Caixa Mercadão")

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        header = self.create_header()
        products_layout = self.create_products_layout()
        table_layout = self.create_table_layout()

        layout.addLayout(header)
        layout.addLayout(products_layout)
        layout.addLayout(table_layout)

        self.setLayout(layout)

    def create_header(self):
        header_layout = QVBoxLayout()

        header_label = QLabel("CAIXA ABERTO")
        header_label.setStyleSheet("QLabel{color:#0E166E;background-color:white;font-size:40pt}")
        header_label.setFixedHeight(80)

        header_layout.addWidget(header_label)

        return header_layout

    def create_products_layout(self):
        products_layout = QHBoxLayout()

        left_info_layout = QVBoxLayout()
        left_info_layout.setContentsMargins(0, 0, 10, 0)

        right_info_layout = QVBoxLayout()
        right_info_layout.setContentsMargins(10, 0, 0, 0)

        left_info_layout.addWidget(self.create_info_widget("#1D6BE0"))
        right_info_layout.addWidget(self.create_info_widget("#424242"))

        products_layout.addLayout(left_info_layout)
        products_layout.addLayout(right_info_layout)

        return products_layout

    def create_info_widget(self, background_color):
        info_widget = QLabel()
        info_widget.setStyleSheet(f"QLabel{{background-color:{background_color}}}")
        info_widget.setFixedWidth(400)

        item_layout = QHBoxLayout()

        logo_label = QLabel()
        logo_label.setPixmap(QPixmap("logo_caixa.jpg"))
        logo_label.setScaledContents(True)

        item_layout.addWidget(logo_label)
        info_widget.setLayout(item_layout)

        return info_widget

    def create_table_layout(self):
        table_layout = QHBoxLayout()

        self.tabela = QTableWidget(self)
        self.tabela.setColumnCount(6)
        self.tabela.setRowCount(10)

        columns = ["Código", "Nome do Produto", "Descrição", "Quantidade", "Preço Unitário", "Subtotal"]
        self.tabela.setHorizontalHeaderLabels(columns)

        table_layout.addWidget(self.tabela)

        return table_layout


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = CaixaMercado()
    janela.show()
    sys.exit(app.exec_())