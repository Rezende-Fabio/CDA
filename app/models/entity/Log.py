from ..entity.Usuario import Usuario
from datetime import datetime
import json

"""
Classe Log
@author - Fabio
@version - 2.0
@since - 23/05/2023
"""

class Log:
    id: int
    acao: str
    dataHora: datetime
    observacao: str
    usuario: Usuario
    dadosAntigos: dict
    dadosNovos: dict

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def acao(self) -> str:
        return self._acao
    
    @acao.setter
    def acao(self, acao: str) -> None:
        self._acao = acao

    @property
    def dataHora(self) -> datetime:
        return self._dataHora
    
    @dataHora.setter
    def dataHora(self, dataHora: datetime) -> None:
        self._dataHora = dataHora

    @property
    def observacao(self) -> str:
        return self._observacao
    
    @observacao.setter
    def observacao(self, observacao: str) -> None:
        self._observacao = observacao
    
    @property
    def usuario(self) -> Usuario:
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario: Usuario) -> None:
        self._usuario = usuario
    
    @property
    def dadosAntigos(self) -> dict:
        return self._dadosAntigos
    
    @dadosAntigos.setter
    def dadosAntigos(self, dadosAntigos: dict) -> None:
        self._dadosAntigos = dadosAntigos
    
    @property
    def dadosNovos(self) -> dict:
        return self._dadosNovos
    
    @dadosNovos.setter
    def dadosNovos(self, dadosNovos: dict) -> None:
        self._dadosNovos = dadosNovos
    
    def converteDadosAntigos(self) -> bytes:
        jsondata = json.dumps(self._dadosAntigos)

        return bytes(jsondata, encoding='utf-8')
    
    def converteDadosNovos(self) -> bytes:
        jsondata = json.dumps(self._dadosNovos)

        return bytes(jsondata, encoding='utf-8')