from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.VerificaMovimentoDao import VerificaMovimentoDao
from ..models.dao.ControleTerceiroDao import ControleTerceiroDao
from ..models.dao.ControleGerenteDao import ControleGerenteDao
from ..models.dao.ControleChaveDao import ControleChaveDao
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from ..models.entity.Funcionario import Funcionario
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from datetime import datetime
from flask import session


class ControleManterFuncionario:
    """
    Classe Controller para funções relacionadas ao CRUD de funcionário
    @author - Fabio
    @version - 1.0
    @since - 23/06/2023
    """

    def consultarFuncionarios(self) -> list[dict]:
        """
        Consulta e retorna uma lista de dicionários contendo informações resumidas de todos os funcionários.

        :return: Uma lista de dicionários, cada um contendo informações resumidas de um funcionário.
            Cada dicionário possui chaves "id", "cracha", "nome", "maquina" e "gerente".
        """

        manterFuncionarioDao = ManterFuncionarioDao()
        respDao = manterFuncionarioDao.consultarFuncionarios()
        listaFuncionarios = []
        for funcionario in respDao:
            dicFunc ={
                "id": funcionario.id_funcionario,
                "cracha": funcionario.fu_cracha,
                "nome": funcionario.fu_nome,
                "maquina": funcionario.fu_maquina,
                "gerente": "SIM" if funcionario.fu_gerente else "NÃO"
            }

            listaFuncionarios.append(dicFunc)
        
        return listaFuncionarios


    def consultaFuncionarioDetalhado(self, id: int) -> Funcionario:
        """
        Consulta detalhes de um funcionário com base no ID.

        :param id: O ID do funcionário a ser consultado.

        :return: Um objeto da classe Funcionario contendo os detalhes do funcionário.
        """

        manterFuncionarioDao = ManterFuncionarioDao()
        funcionario = manterFuncionarioDao.consultarFuncionarioDetalhado(id)

        return funcionario
    

    def incluirFuncionario(self, nome: str, cracha: str, maquina: str, gerente: bool) -> bool:
        """
        Inclui um novo funcionário no sistema.

        :param nome: O nome do novo funcionário.
        :param cracha: O número do crachá do novo funcionário.
        :param maquina: A máquina associada ao novo funcionário.
        :param gerente: Indica se o novo funcionário é um gerente ou não (True ou False).

        :return: True se a inclusão for bem-sucedida, False caso contrário.
        """

        
        self.usuarioLogado = Usuario()
        self.funcionarioNovo = Funcionario(cracha=cracha, nome=nome, maquina=maquina, gerente=gerente, ativo=False, delete=False)

        self.usuarioLogado = Usuario()

        manterFuncionarioDao = ManterFuncionarioDao()
        consultaIdUser = ConsultaIdsDao()
        if manterFuncionarioDao.inserirFuncionario(self.funcionarioNovo):
            consultaIdUser = ConsultaIdsDao()
            self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
            self.funcionarioNovo.id = consultaIdUser.consultaIdFinalFunc()
            self.geraLogFuncionario("INSERT")
        
        return True
        
    

    def editarFuncionario(self, id: int, nome: str, cracha: str, maquina: str, gerente: bool) -> bool:
        """
        Edita as informações de um funcionário existente no sistema com base no ID fornecido.

        :param id: O ID do funcionário a ser editado.
        :param nome: O novo nome do funcionário.
        :param cracha: O novo número do crachá do funcionário.
        :param maquina: A nova máquina associada ao funcionário.
        :param gerente: Indica se o funcionário é um gerente ou não (True ou False).

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        self.usuarioLogado = Usuario()
        self.funcionarioAntigo = Funcionario()
        manterFuncionarioDao = ManterFuncionarioDao()
        consultaIdUser = ConsultaIdsDao()

        self.funcionarioAntigo = manterFuncionarioDao.consultarFuncionarioDetalhado(id)

        self.funcionarioNovo = Funcionario(id=id, cracha=cracha, nome=nome, maquina=maquina, gerente=gerente, ativo=False, delete=False)

        if manterFuncionarioDao.editarFuncionario(self.funcionarioNovo):
            self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])
            self.geraLogFuncionario("UPDATE")
        
        return True


    def excluirFuncionario(self, id: int) -> int:
        """
        Exclui ou Inativa um funcionário do sistema com base no ID fornecido.

        :param id: O ID do funcionário a ser excluído.

        :return: Um código indicando o resultado da operação:
            - 1 Funcionário excluído com sucesso.
            - 2 Funcionário inativado com sucesso (quando funcionário tem movimentação no sistema).
            - 3 se existem movimentos em aberto associados ao gerente.
        """

        #Verifica se o funcionário está em algum movimento de gerente aberto
        controleGerenteDao = ControleGerenteDao()
        #Consulta os ids dos movimentos
        idsMov = controleGerenteDao.verificaMovIdGerente(id)
        for idMov in idsMov:
            #Verifica se existe algum movimento em abeto
            if controleGerenteDao.consultaMovAbertoGerente(idMov[0]):
                return 3
        
        #Verifica se o funcionário está em algum movimento de terceiro aberto
        controleterceiroDao = ControleTerceiroDao()
        #Consulta os ids dos movimentos
        idsMov = controleterceiroDao.verificaMovIdFuncionario(id)
        for idMov in idsMov:
            #Verifica se existe algum movimento em abeto
            if controleterceiroDao.consultaMovAbertoTerc(idMov[0]):
                return 3

        #Verifica se o funcionário está em algum movimento de chave aberto
        controleChaveDao = ControleChaveDao()
        #Consulta os ids dos movimentos
        idsMov = controleChaveDao.verificaMovIdFuncionario(id)
        for idMov in idsMov:
            #Verifica se existe algum movimento em abeto
            if controleChaveDao.consultaMovAbertoChave(idMov[0]):
                return 3
            
        manterFuncionarioDao = ManterFuncionarioDao()
        verificaMovimento = VerificaMovimentoDao()
        consultaIdUser = ConsultaIdsDao()
        self.usuarioLogado = Usuario()
        self.funcionarioAntigo = Funcionario()

        self.funcionarioAntigo = manterFuncionarioDao.consultarFuncionarioDetalhado(id)

        self.usuarioLogado.id = consultaIdUser.consultaIdUserLogado(session["usuario"])

        if verificaMovimento.verificaMovimentoFuncionario(id):
            if manterFuncionarioDao.inativarFuncionario(id):
                self.geraLogFuncionario("ACTIVE")
                return 2
        else:
            if manterFuncionarioDao.excluirFuncionario(id):
                self.geraLogFuncionario("DELETE")
                return 1  


    def geraLogFuncionario(self, acao: str):
        """
        Gera um registro de log para ações relacionadas ao manter funcionario.

        :param acao: Ação realizada (INSERT, UPDATE, DELETE).

        :return: Nenhum valor é retornado.
        """

        log = Log(acao=acao, dataHora=datetime.now(), observacao="", usuario=self.usuarioLogado)

        if acao == "INSERT":
            log.dadosAntigos = {"vazio": 0}
            log.dadosNovos = self.funcionarioNovo.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.funcionarioAntigo.toJson()
            log.dadosNovos = self.funcionarioNovo.toJson()
        else:
            log.dadosAntigos = self.funcionarioAntigo.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogFuncionario(log)
