from PyQt4.QtGui import *
from PyQt4.QtCore import *
class tabloOrnegi(QDialog):
    def __init__(self,ebeveyn=None):
        super(tabloOrnegi,self).__init__(ebeveyn)
        grid=QGridLayout()
        self.tablo=QTableWidget()
        self.tablo.resize(400,250)
        self.tablo.setRowCount(4)
        self.tablo.setColumnCount(3)
        grid.addWidget(self.tablo)
        self.tablo.setItem(0,0,QTableWidgetItem('Adı'))
        self.tablo.setItem(0,1,QTableWidgetItem('Soyadı'))
        self.tablo.setItem(0,2,QTableWidgetItem('Bolum'))
        self.tablo.setItem(1,0,QTableWidgetItem('Can'))
        self.tablo.setItem(1,1,QTableWidgetItem('Aydın'))
        self.tablo.setItem(1,2,QTableWidgetItem('YBS'))
        self.tablo.setItem(2,0,QTableWidgetItem('Semih'))
        self.tablo.setItem(2,1,QTableWidgetItem('Yarar'))
        self.tablo.setItem(2,2,QTableWidgetItem('YBS'))
        self.tablo.setItem(3,0,QTableWidgetItem('Büşra'))
        self.tablo.setItem(3,1,QTableWidgetItem('Demirgüreşci'))
        self.tablo.setItem(3,2,QTableWidgetItem('İktisat'))
        self.tablo.show()
        return pencere.exec_()

uyg=QApplication([])
pencere=tabloOrnegi()
pencere.show()
uyg.exec_
