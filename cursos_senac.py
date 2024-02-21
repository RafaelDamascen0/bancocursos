import sys 

from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget, QTableWidgetItem,QLabel,QLineEdit, QVBoxLayout, QPushButton
import mysql.connector  

cx = mysql.connector.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="123@senac",
    database="tbcursos"
)

cursor = cx.cursor()

class cursosSenac(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(30,400,600,300)
        self.setWindowTitle("Cursos do senac")

        labelNome = QLabel("Nome do curso: ")
        self.editNome = QLineEdit()

        labelCh = QLabel("Carga Horária: ")
        self.editCh = QLineEdit()

        psbCadastro = QPushButton("Cadastrar")
        self.labelMsg =QLabel("|")

        layout = QVBoxLayout()
        layout.addWidget(labelNome)
        layout.addWidget(self.editNome)
        
        layout.addWidget(labelCh)
        layout.addWidget(self.editCh)

        layout.addWidget(psbCadastro)

        psbCadastro.clicked.connect(self.cadCurs)

        self.setLayout(layout)

    def cadCurs(self):
        cursor.execute("insert into cursos_senac(cursos,carga_horaria)values(%s,%s)",
                    (self.editNome.text(),self.editCh.text()))
        cx.commit()

        self.labelMsg.setText("Cliente cadastrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = cursosSenac()
    tela.show()
    sys.exit(app.exec_())


