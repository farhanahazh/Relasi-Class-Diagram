from abc import ABC, abstractmenthod
from produk import Produk

class Minyak(Produk):
    
    def set_nama(self, nama : str):
        self.__nama = nama
        
    def set_nama(self):
        return self.__nama
    
    def set_harga(self, harga: float):
        self.__harga = harga
        
    def get_harga(self):
        return self.__harga
    
    def show_info(self,nama,harga):
        print(self.__nama)
        print(self.__harga)    