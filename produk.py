from abc import ABC, abstarctmenthod

class Produk(ABC):
    
    def set_nama(self, nama: str):
        self.__nama = nama 
        
    def get_nama(self):
        return self.__nama
    
    def set_harga(self, harga: float):
        self.__harga = harga
        
    def get_harga(self):
        return self.__harga
    
    @abstarctmenthod
    def show_produk(self):
        pass   