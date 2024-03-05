import sys 
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QVBoxLayout, QPushButton
from pymongo import MongoClient

cliente = MongoClient("mongodb://root:senac123@127.0.0.1:37452")

db = cliente.Loja_db


class exibirUsuarios(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,500,300)
        self.setWindowTitle("usuarios cadastrados")

        tbusuarios = QTableWidget(self)
        tbusuarios.setColumnCount(3)
        tbusuarios.setRowCount(10)


        headerLine=["id","Nome Usuario","Senha","Nivel de Acesso"]

        tbusuarios.setHorizontalHeaderLabels(headerLine)

        lintb = 0

        for us in db["usuario"].find():

            tbusuarios.setItem(lintb,0,QTableWidgetItem(str(us["_id"])))
            tbusuarios.setItem(lintb,1,QTableWidgetItem(us["nomeusuario"]))
            tbusuarios.setItem(lintb,2,QTableWidgetItem(us["senha"]))
            tbusuarios.setItem(lintb,2,QTableWidgetItem(us["nivel"]))
            lintb +=1
 
        layout= QVBoxLayout()
        layout.addWidget(tbusuarios)
        self.setLayout(layout)       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = exibirUsuarios()
    tela.show()
    sys.exit(app.exec_())