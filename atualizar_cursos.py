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
 
class AtualizarCursos(QWidget):
    def __init__(self):
        super().__init__()
 
        layout = QVBoxLayout()
 
        self.setGeometry(500,300,450,350)
        self.setWindowTitle("Cursos cadastrados")
       
       
        labelId = QLabel("Id curso: ")
        self.editId = QLineEdit()
 
 
        labelNome = QLabel("Nome do curso: ")
        self.editNome = QLineEdit()
 
        labelCh = QLabel("Carga Horária: ")
        self.editCh = QLineEdit()
 
 
        psbCadastro = QPushButton("Atualizar")
       
       
        layout.addWidget(labelId)
        layout.addWidget(self.editId)
 
 
        layout.addWidget(labelNome)
        layout.addWidget(self.editNome)
 
        layout.addWidget(labelCh)
        layout.addWidget(self.editCh)
 
       
        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.upCli)
 
 
        tbcurso = QTableWidget(self)
        tbcurso.setColumnCount(3)
        tbcurso.setRowCount(10)
 
        headerLine=["Id","Nome","Carga Horaria"]
 
        tbcurso.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from cursos_senac")
 
        lintb = 0
        for linha in cursor:
            tbcurso.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbcurso.setItem(lintb,1,QTableWidgetItem(linha[1]))
            tbcurso.setItem(lintb,2,QTableWidgetItem(linha[2]))
            lintb+=1
 
       
        layout.addWidget(tbcurso)
        self.setLayout(layout)
 
    def upCli(self):
        if (self.editId.text()==""):
            print("Não é possível atualizar sem o Id do curso")
       
        elif(self.editNome.text()=="" and self.editCh.text()==""):
            print("Não é possível atualizar se não houver dados")
 
        elif(self.editNome.text()!="" and self.editCh.text()==""):
            cursor.execute("update cursos_senac set cursos=%s where cursosid=%s",
                           (self.editNome.text(), self.editId.text()))
           
        elif(self.editNome.text()=="" and self.editCh.text()!=""):
            cursor.execute("update cursos_senac set carga_horaria=%s where cursosid=%s",
                           (self.editCh.text(), self.editId.text()))
           
        else:
            cursor.execute("update cursos_senac set cursos=%s, carga_horaria=%s where cursosid=%s",
                           (self.editNome.text(), self.editCh.text(), self.editId.text()))
           
        cx.commit()
        print("As Atualizações foram realizadas")
           
           
 
if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarCursos()
    tela.show()
    sys.exit(app.exec_())