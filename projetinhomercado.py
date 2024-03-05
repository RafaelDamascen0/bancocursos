import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QStyle, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
 
 
class CaixaMercado(QWidget):
 
 
    def __init__(self):    
        super().__init__()
 
 
        self.setGeometry(0,25,1590,840)
        # configuração da tela ao abrir o programa
        self.setWindowTitle("Caixa Mercadão")
        # Nome da janela
 
        principal = QVBoxLayout()
        # Tela principal
 
        faixaSup = QLabel()
        faixaSup.setStyleSheet("QLabel{background-color:#00c853}")
        faixaSup.setFixedHeight(100)
        # É a faixa que fica na parte acima da janela
 
        faixaInf = QLabel()
        faixaInf.setStyleSheet("QLabel{background-color:#00c853}")
        faixaInf.setFixedHeight(800)
        # É o resto da janela que fica abaixo da faixa superior
 
        divCabecalho = QVBoxLayout()
        # Layout para dividir as labels cabecalho e caixa
 
        cabecalho = QLabel("CAIXA ABERTO")
        cabecalho.setStyleSheet("QLabel{color:#388e3c;background-color:white;font-size:40pt}")
        cabecalho.setFixedHeight(80)
        # É um rótulo que indicará um cabecalho com o texto de "Caixa Aberto"
 
        caixa = QLabel()
        # Está Label está servindo para adicionar um novo layout abaixo do cabelhaço
 
        divCaixas = QHBoxLayout()
        # Este layout serve para colocar na tela os itens vindo das labels
        # info e visualizacao
 
        labelCaixa = QLabel()
        # label para armazenar tudo que vir abaixo do cabecalho
 
        infoGeralEsq = QVBoxLayout()
        # Layout que mostra todas as informações da coluna da esquerda da tela
 
        info = QLabel()
        info.setFixedHeight(400)
        # Está label é para guardar as informações vinda do Layout informações
 
        informacoes = QHBoxLayout()
        # Layout para dividir a tela em esquerda e direita
 
        informacoesProdutoEsq = QLabel()
        informacoesProdutoEsq.setStyleSheet("QLabel{background-color:#424242}")
        informacoesProdutoEsq.setFixedWidth(400)
        # A label a seguir é para adicionar um layout que divida os campos a esquerda
        # da tela
 
        informacoesProdutoDir = QLabel()
        informacoesProdutoDir.setStyleSheet("QLabel{background-color:#424242}")
        informacoesProdutoDir.setFixedWidth(450)
        # A label a seguir é para adicionar um layout que divida os campos a direita
        # da tela
 
        ItemEsq = QHBoxLayout()
        ItemDir = QHBoxLayout()
        # Estes layouts é para dividir os itens a seguir a esquerda e direita
 
        labelLogo = QLabel()
        labelLogo.setPixmap(QPixmap("minimercado.jpg"))
        labelLogo.setScaledContents(True)
        # Este é a logo do mercado
        ItemEsq.addWidget(labelLogo)
        # Adicionando a Logo aos itens a esquerda
        informacoesProdutoEsq.setLayout(ItemEsq)
        # Adicionando ele a tela
 
        ProdutoPreco = QLabel()
        # Label criada para armazenar os itens do Layout divItens
 
        divItens = QVBoxLayout()
        # Layout criado para deixar os itens um embaixo do outro
       
        codigoProduto = QLabel("Código do Produto")
        codigoProduto.setStyleSheet("QLabel{color:white;background-color:#388e3c;font-size:15pt}")
        self.codigoProdutoEdit = QLineEdit()
        self.codigoProdutoEdit.setStyleSheet("QLineEdit{padding:15px;font-size:15pt; width:350}")
        # Este será o campo que aparecerá o código do cliente
 
        quantidadeProduto = QLabel("Quantidade")
        quantidadeProduto.setStyleSheet("QLabel{color:white;background-color:#388e3c;font-size:15pt}")
        self.quantidadeProdutoEdit = QLineEdit()
        self.quantidadeProdutoEdit.setStyleSheet("QLineEdit{padding:15px;font-size:15pt; width:350}")
        # Este campo é para a quantidade de itens do produto que irá comprar
 
        precoUnitarioProduto = QLabel("Preço Unidade")
        precoUnitarioProduto.setStyleSheet("QLabel{color:white;background-color:#388e3c;font-size:15}")
        self.precoUnitarioEdit = QLineEdit()
        self.precoUnitarioEdit.setStyleSheet("QLineEdit{padding:15px;font-size:15; width:350}")
        # Este é o preço da unidade do produto
 
        subtotalProduto = QLabel("Preço Subtotal")
        subtotalProduto.setStyleSheet("QLabel{color:white;background-color:#388e3c;font-size:15pt}")
        self.subtotalProdutoEdit = QLineEdit()
        self.subtotalProdutoEdit.setStyleSheet("QLineEdit{padding:15px;font-size:15; width:350}")
        # Este será o calculo total do quanto irá pagar pela quantidade do produto
 
        divItens.addWidget(codigoProduto)
        divItens.addWidget(self.codigoProdutoEdit)
 
        divItens.addWidget(quantidadeProduto)
        divItens.addWidget(self.quantidadeProdutoEdit)
 
        divItens.addWidget(precoUnitarioProduto)
        divItens.addWidget(self.precoUnitarioEdit)
 
        divItens.addWidget(subtotalProduto)
        divItens.addWidget(self.subtotalProdutoEdit)
        # Adicionando os itens na direita, os rótulos e as linhas de edição
        ProdutoPreco.setLayout(divItens)
        ItemDir.addWidget(ProdutoPreco)
        informacoesProdutoDir.setLayout(ItemDir)
        # Adicionando os itens a tela
 
        labelProduto = QLabel()
 
        infoProduto = QHBoxLayout()
 
        nomeProduto = QLabel("Nome do Produto")
        nomeProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        nomeProdutoEdit = QLineEdit()
        nomeProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15; width:200}")

        
 
        descricaoProduto = QLabel("Descrição do Produto")
        descricaoProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        descricaoProdutoEdit = QLineEdit()
        descricaoProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15; width:200}")
 
        infoProduto.addWidget(nomeProduto)
        infoProduto.addWidget(descricaoProduto)
        labelProduto.setLayout(infoProduto)
 
        visualizacao = QLabel()
        # Serve para guardar o layout listagem
 
        listagem = QHBoxLayout()
        # É um layout para poder visualizar a tabela
 
        self.tabela = QTableWidget(self)
        self.tabela.setColumnCount(5)
        self.tabela.setRowCount(10)
        # Estamos definindo quantas linhas e colunas terão na tabela
 
        colunas = ["Código","Nome do Produto","Descrição","Quantidade","Preço Unitário","Subtotal"]
        self.tabela.setHorizontalHeaderLabels(colunas)
        # Aqui está sendo definido os nomes das colunas
 
        informacoes.addWidget(informacoesProdutoEsq)
        informacoes.addWidget(informacoesProdutoDir)
        info.setLayout(informacoes)
 
        listagem.addWidget(self.tabela)
        visualizacao.setLayout(listagem)
 
        infoGeralEsq.addWidget(info)
        infoGeralEsq.addWidget(labelProduto)
        labelCaixa.setLayout(infoGeralEsq)
 
        divCaixas.addWidget(labelCaixa)
        divCaixas.addWidget(visualizacao)
        caixa.setLayout(divCaixas)
       
        divCabecalho.addWidget(cabecalho)
        divCabecalho.addWidget(caixa)
        faixaInf.setLayout(divCabecalho)
 
        principal.addWidget(faixaSup)
        principal.addWidget(faixaInf)
        # Esta adicionando as variáveis faixaSup e faixaInf no layout principal
 
        self.setLayout(principal)
        # Código para poder visualizar na tela o conteudo

        self.keyPressEvent = self.keyPressEvent
 
    def keyPressEvent(self, e):

        if(e.key() == Qt.Key_F2):
            print('Você teclou f2')
            self.tabelas.setItem(self.linha,0,QTableWidgetItem(str(self.codigoProdutoEdit.text())))
            self.tabelas.setItem(self.linha,1,QTableWidgetItem(str(self.nomeProdutoEdit.text())))
            self.tabelas.setItem(self.linha,2,QTableWidgetItem(str(self.descricaoProdutoEdit.text())))
            self.tabelas.setItem(self.linha,2,QTableWidgetItem(str(self.quantidadeProdutoEdit.text())))
            self.tabelas.setItem(self.linha,3,QTableWidgetItem(str(self.precoUnitarioProdutoEdit.text())))
            self.tabela.setItem(self.linha,4,QTableWidgetItem(str(self.subtotalProdutoEdit.text())))
            self.linha+=1
            self.total+=float(self.SubTotalProdutoEdit.text())
            self.TotalPagarEdit.setText(str(self.total))
 
 
 
app = QApplication(sys.argv)
janela = CaixaMercado()
janela.show()
app.exec_()