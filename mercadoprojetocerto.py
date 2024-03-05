import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap


class CaixaPDV(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(5,30,1580,800)
        self.setWindowTitle("Caixa PDV")

        #retirar as margens da janela

        self.setContentsMargins(0,0,0,0)

        # Criando o primeiro layout horizontal chamado principal

        layout_principal = QVBoxLayout()

        #retirar as margens internas

        layout_principal.setContentsMargins(0,0,0,0)

        # Criando a label superior com a imagem do logo do caixa

        label_logo_img = QLabel("YZIDRO - PDV")
        
        # setar a altura da laybel com imagens

        label_logo_img.setFixedHeight(100)
        label_logo_img.setStyleSheet("QLabel{background-color:#1a237e; color:#ffffff;font-size:20pt; padding:10px}")

        #Criando a label inferiro que está no layout horizontal principal

        label_inf_lay_pri = QLabel()
        label_inf_lay_pri.setFixedHeight(700)
        label_inf_lay_pri.setStyleSheet("QLabel{background-color:#0d47a1}")

        #novo layout vertical para a label da parte inferior da tela

        layout_lab_inf = QVBoxLayout()

        #label do texto caixa aberto

        label_caixa_aberto = QLabel("CAIXA ABERTO")

        label_caixa_aberto.setFixedHeight(50)
        label_caixa_aberto.setStyleSheet("QLabel{background-color:#ffffff; color: blue; font-size:20pt; text-align:center;padding:10px; border-radius:10px}")
        layout_lab_inf.addWidget(label_caixa_aberto)


        #Nova label para a parte inferior para os detalhes dos itens

        label_detalhes_inf = QLabel()
        label_detalhes_inf.setFixedHeight(600)
        label_detalhes_inf.setStyleSheet("QLabel{background-color:lightblue}")

        layout_lab_inf.addWidget(label_detalhes_inf)

        # Criar um novo layout horizontal para a alocação de imagens e detealhes

        layout_hor_inf = QHBoxLayout()


        label_det_esq = QLabel()
        label_det_esq.setFixedWidth(760)

        # 'label_det_esq.setStyleSheet("QLabel{background-color:white}")

        label_det_dir = QLabel()
        label_det_dir.setFixedWidth(760)
        label_det_dir.setStyleSheet("QLabel{background-color:lightred}")

        # adicionar as labels ao layout horizontal

        layout_hor_inf.addWidget(label_det_esq)
        layout_hor_inf.addWidget(label_det_dir)
        label_detalhes_inf.setLayout(layout_hor_inf)

        #Criando o layout horizontal para exibir os dados em formato de coluna

        layout_hor_esq_inf = QHBoxLayout()
        #Criação de duas labels que ficarão ao lado esquerdo

        label_det_esq_1 = QLabel()
        label_det_esq_1.setStyleSheet("QLabel{background-color:white; border-radius:10px}")

        #Criando uma nova label para a imagem do carrinho

        label_det_esq_1.setPixmap(QPixmap("carrinho.png"))
        label_det_esq_1.setFixedWidth(300)
        label_det_esq_1.setScaledContents(True)            
        label_det_esq_1.setContentsMargins(10,10,10,10)

        
        label_det_esq_2 = QLabel()
        label_det_esq_2.setStyleSheet("QLabel{background-color:yellow;}")

        #Adiciona um novo layout para os elementos verticais

        layout_ver_esq_2 = QVBoxLayout()

        #labels e lineEdits

        label_codigo_barras = QLabel("CÓDIGO DE BARRAS")
        edit_codigo_barras = QLineEdit()

        label_valor_unitario = QLabel("VALOR UNITÁRIO")
        edit_valor_unitario = QLineEdit()   

        label_total_iten = QLabel("TOTAL DO ITEM")
        edit_total_item = QLineEdit()

        layout_ver_esq_2.addWidget(label_codigo_barras)
        layout_ver_esq_2.addWidget(edit_codigo_barras)

        layout_ver_esq_2.addWidget(label_valor_unitario)
        layout_ver_esq_2.addWidget(edit_valor_unitario) 

        layout_ver_esq_2.addWidget(label_total_iten)
        layout_ver_esq_2.addWidget(edit_total_item)

        #adicionar o layout na label_det_esq_2

        label_det_esq_2.setLayout(layout_ver_esq_2)

        #adicionando as labels no layout_hor_esq_inf

        layout_hor_esq_inf.addWidget(label_det_esq_1)
        layout_hor_esq_inf.addWidget(label_det_esq_2)

        label_det_esq.setLayout(layout_hor_esq_inf)

        # adicionando um novo layout a label na parte inferior

        label_inf_lay_pri.setLayout(layout_lab_inf)

        #adicionando as laybels no layout

        layout_principal.addWidget(label_logo_img)
        layout_principal.addWidget(label_inf_lay_pri)

        #adicionando o layout principal a tela principal

        self.setLayout(layout_principal)

if __name__=="__main__":

    app = QApplication(sys.argv)
    tela = CaixaPDV()
    tela.show()
    app.exec_()

