from .Funcionario import Funcionario
from .Terceiro import Terceiro

"""
Classe Movimento de Terceiro
@author - Fabio
@version - 1.0
@since - 01/08/2023
"""

class MovimentoTerceiro:
    id: int
    terceiro: Terceiro
    dataEnt: str
    horaEnt: str
    placa: str
    veiculo: str
    motivo: str
    empresa: str
    dataSai: str
    horaSai: str
    pessoaVisit: Funcionario
    delete: bool
    acomps: list[Terceiro]


    def __init__(self) -> None:
        self._id = None
        self._terceiro = None
        self._dataEnt = None
        self._horaEnt = None
        self._placa = None
        self._veiculo = None
        self._motivo = None
        self._empresa = None
        self._dataSai = None
        self._horaSai = None
        self._pessoaVisit = None
        self._delete = None
        self._acomps = None

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def terceiro(self) -> Terceiro:
        return self._terceiro
    
    @terceiro.setter
    def terceiro(self, terceiro: Terceiro) -> None:
        self._terceiro = terceiro

    @property
    def dataEnt(self) -> str:
        return self._dataEnt
    
    @dataEnt.setter
    def dataEnt(self, dataEnt: str) -> None:
        self._dataEnt = dataEnt

    @property
    def horaEnt(self) -> str:
        return self._horaEnt
    
    @horaEnt.setter
    def horaEnt(self, horaEnt: str) -> None:
        self._horaEnt = horaEnt
    
    @property
    def placa(self) -> str:
        return self._placa
    
    @placa.setter
    def placa(self, placa: str) -> None:
        self._placa = placa
    
    @property
    def veiculo(self) -> str:
        return self._veiculo
    
    @veiculo.setter
    def veiculo(self, veiculo: str) -> None:
        self._veiculo = veiculo
    
    @property
    def motivo(self) -> str:
        return self._motivo
    
    @motivo.setter
    def motivo(self, motivo: str) -> None:
        self._motivo = motivo

    @property
    def empresa(self) -> str:
        return self._empresa
    
    @empresa.setter
    def empresa(self, empresa: str) -> None:
        self._empresa = empresa

    @property
    def dataSai(self) -> str:
        return self._dataSai
    
    @dataSai.setter
    def dataSai(self, dataSai: str) -> None:
        self._dataSai = dataSai
    
    @property
    def horaSai(self) -> str:
        return self._horaSai
    
    @horaSai.setter
    def horaSai(self, horaSai: str) -> None:
        self._horaSai = horaSai
    
    @property
    def pessoaVisit(self) -> Funcionario:
        return self._pessoaVisit
    
    @pessoaVisit.setter
    def pessoaVisit(self, pessoaVisit: Funcionario) -> None:
        self._pessoaVisit = pessoaVisit

    @property
    def delete(self) -> bool:
        return self._delete
    
    @delete.setter
    def delete(self, delete: bool) -> None:
        self._delete = delete

    @property
    def acomps(self) -> list[Terceiro]:
        return self._acomps
    
    @acomps.setter
    def acomps(self, acomps: list[Terceiro]) -> None:
        self._acomps = acomps


    def calcularTempo(self) -> str:
        pass
    
        
    def toJson(self) -> dict:
        json = {
            "id": self._id,
            "dataEnt": self._dataEnt,
            "horaEnt": self._horaEnt,
            "tercerio": self.terceiro.toJson(),
            "placa": self._placa,
            "veiculo": self._veiculo,
            "motivo": self._motivo,
            "empresa": self._empresa,
            "dataSai": self._dataSai,
            "horaSai": self._horaSai,
            "pessoaVisit": self.pessoaVisit.toJson(),
            "acomps": [] if len(self._acomps) < 0 else [acomp.toJson() for acomp in self._acomps],
            "delete": self._delete
        }

        return json