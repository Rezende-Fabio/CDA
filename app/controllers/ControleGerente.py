from ..models.dao.ConsultaParametrosDao import ConsultaParametrosDao
from ..models.dao.ManterFuncionarioDao import ManterFuncionarioDao
from ..models.dao.ControleGerenteDao import ControleGerenteDao
from ..models.entity.MovimentoGerente import MovimentoGerente
from ..extensions.FiltrosJson import filtroData, filtroNome
from ..models.dao.ConsultaIdsDao import ConsultaIdsDao
from dateutil.relativedelta import relativedelta
from ..models.dao.GeraLogDao import GeraLogDao
from ..models.entity.Usuario import Usuario
from ..models.entity.Log import Log
from datetime import datetime
from flask import session

class ControleDeGerente:
    """
    Classe Controller para as funções recionadas ao controle de gerentes
    @author - Fabio
    @version - 1.0
    @since - 11/08/2023
    """

    def inserirEntrada(self, dataEnt: str, horaEnt: str, gerente: str) -> bool:
        """
        Insere um registro de entrada para um gerente.

        :param dataEnt: A data da entrada no formato "YYYY-MM-DD".
        :param horaEnt: A hora da entrada no formato "HH:MM".
        :param gerente: O crachá do gerente que está entrando.
        """

        controleGerenteDao = ControleGerenteDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        self.usuarioLogado = Usuario()

        self.movimentoGerNovo = MovimentoGerente(dataEnt=dataEnt.replace("-", ""), horaEnt=horaEnt, delete=False,
                                                 gerente=manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(list(gerente.split())[0]))

        if controleGerenteDao.inserirEntrada(self.movimentoGerNovo):
            consultaIds = ConsultaIdsDao()
            #Verifica se o usuário que está logo é do grupo de ADMIN
            if session["grupo"] == "ADM":
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
            else:
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

            self.movimentoGerNovo.id = consultaIds.consultaIdFinalMovGer()
            self.geraLogControleGerente("ENTRADA", "")

        return True
    

    def inserirSaida(self, id: int, dataSai: str, horaSai: str, cracha: str) -> bool:
        """
        Insere um registro de saída para um gerente.

        :param id: O ID do movimento de entrada do gerente.
        :param dataSai: A data da saída no formato "YYYY-MM-DD".
        :param horaSai: A hora da saída no formato "HH:MM".
        :param cracha: O crachá do gerente que está saindo.
        """

        controleGerenteDao = ControleGerenteDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        self.usuarioLogado = Usuario()

        self.movimentoGerNovo = controleGerenteDao.consultaMovimentoDetalhado(id)
        self.movimentoGerNovo.dataSai = dataSai.replace("-", "")
        self.movimentoGerNovo.horaSai = horaSai
        self.movimentoGerNovo.gerente = manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(cracha)

        if controleGerenteDao.inserirSaida(self.movimentoGerNovo):
            consultaIds = ConsultaIdsDao()
            #Verifica se o usuário que está logo é do grupo de ADMIN
            if session["grupo"] == "ADM":
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
            else:
                self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

            self.geraLogControleGerente("SAIDA", "")

        return True
    

    def editarMovimentoGerente(self, id: int, crachaGerente: str, dataEnt: str, horaEnt: str, dataSai: str, horaSai: str, observacao: str) -> bool:
        """
        Altera um movimento de gerente específico

        :param id: O ID do registro de movimento de chave a ser alterado.
        :param dataEnt: Data da devolução da chave no formato 'YYYY-MM-DD'.
        :param horaEnt: Hora da devolução da chave no formato 'HH:MM'.
        :param dataSai: Data da devolução da chave no formato 'YYYY-MM-DD'.
        :param horaSai: Hora da devolução da chave no formato 'HH:MM'.
        :param crachaGerente: Crachá do responsável pela devolução da chave.
        :param observacao: A observação relacionada à edição do movimento de gerente (obrigatorio para usuários do grupo VIG).

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        controleGerenteDao = ControleGerenteDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        consultaIds = ConsultaIdsDao()
        self.usuarioLogado = Usuario()

        gerente = manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(crachaGerente)
        self.movimentoGerAntigo = controleGerenteDao.consultaMovimentoDetalhado(id)
        self.movimentoGerAntigo.gerente = gerente

        self.movimentoGerNovo = MovimentoGerente(id=id, dataEnt=dataEnt.replace("-", ""), horaEnt=horaEnt, dataSai=dataSai.replace("-", ""), horaSai=horaSai, gerente=gerente)

        controleGerenteDao.editarMovimentoGerente(self.movimentoGerNovo)

        #Verifica se o usuário que está logo é do grupo de ADMIN
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        self.geraLogControleGerente("UPDATE", observacao)

        return True


    def excluirMovimentoGerente(self, id: int, crachaGer: str, observacao: str) -> bool:
        """
        Exclui um movimento de gerente especifíco.

        :param id: O ID do registro de movimento de gerente a ser alterado.
        :param crachaGer: O crachá do gerente.
        :param observacao: A observação relacionada à exclusão do movimento de gerente (obrigatorio para usuários do grupo VIG).

        :return: True se a edição for bem-sucedida, False caso contrário.
        """

        controleGerenteDao = ControleGerenteDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        self.usuarioLogado = Usuario()
        consultaIds = ConsultaIdsDao()

        gerente = manterFuncionarioDao.consultarFuncionarioDetalhadoCracha(crachaGer)
        self.movimentoGerAntigo = controleGerenteDao.consultaMovimentoDetalhado(id)
        self.movimentoGerAntigo.gerente = gerente

        controleGerenteDao.excluirMovimentoGerente(self.movimentoGerAntigo)

        #Verifica se o usuário que está logo é do grupo de ADMIN
        if session["grupo"] == "ADM":
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuario"])
        else:
            self.usuarioLogado.id = consultaIds.consultaIdUserLogado(session["usuarioVIG"])

        self.geraLogControleGerente("DELETE", observacao)

        return True
    

    def consultaGerentesEntrada(self) -> list[dict]:
        """
        Consulta os registros de entrada de gerentes.

        :return: Uma lista de dicionários contendo os detalhes dos movimentos de entrada dos gerentes.
            Cada dicionário possui chaves "id", "nome" e "entrada".
        """

        controleGerenteDao = ControleGerenteDao()
        respDao = controleGerenteDao.consultaGerentesEntrada()
        movimentosGerente = []
        for gerente in respDao:
            dictMov = {
                "id": gerente.id_movGere,
                "nome": filtroNome(gerente.nomeGer),
                "entrada": f"{filtroData(gerente.mge_dataEntra)} {gerente.mge_horaEntra}"
            }
            movimentosGerente.append(dictMov)
        
        return movimentosGerente
    

    def listaGerentesManut(self) -> list[dict]:
        """
        Lista os registros de movimentos de entrada e saída de gerentes para manutenção de acordo com a data na tabela de parâmetros('PAR_MANUT_CONTROL_GER').

        :return: Uma lista de dicionários contendo os detalhes dos movimentos de entrada e saída de gerentes.
            Cada dicionário possui chaves "id", "nome", "entrada" e "saida".
        """

        #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
        consultaParametro = ConsultaParametrosDao()
        mesesAtras = consultaParametro.consultaParametros("PAR_MANUT_CONTROL_GER")
        dataDe = datetime.now()
        dataDe = dataDe - relativedelta(months=mesesAtras)
        dataDe = dataDe.strftime("%Y%m01")

        controleGerenteDao = ControleGerenteDao()
        respDao = controleGerenteDao.consultaGerentesManut(dataDe)
        movimentosGerente = []
        for gerente in respDao:
            dictMov = {
                "id": gerente.id_movGere,
                "nome": filtroNome(gerente.nomeGer),
                "entrada": f"{filtroData(gerente.mge_dataEntra)} {gerente.mge_horaEntra}",
                "saida": f"{filtroData(gerente.mge_dataSaid)} {gerente.mge_horaSaid}"
            }
            movimentosGerente.append(dictMov)
        
        return movimentosGerente


    def consultaMovimentoDetalhado(self, id: int) -> MovimentoGerente:
        """
        Consulta os detalhes de um movimento de gerente específico.

        :param id: O ID do movimento de gerente a ser consultado.

        :return: Um objeto MovimentoGerente preenchido com os detalhes do movimento.
        """

        controleGerenteDao = ControleGerenteDao()
        manterFuncionarioDao = ManterFuncionarioDao()
        #Pesquisa qual id do gerente desse movimento
        idGerMov = controleGerenteDao.consultaIdGerMov(id)
        movimento = controleGerenteDao.consultaMovimentoDetalhado(id)
        movimento.gerente = manterFuncionarioDao.consultarFuncionarioDetalhado(idGerMov)

        return movimento


    def geraLogControleGerente(self, acao: str, observacao: str) -> None:
        """
        Gera um registro de log para ações relacionadas ao controle de gerentes.

        :param acao: Ação realizada (ENTRADA, SAIDA, UPDATE, DELETE).
        :param observacao: Observações adicionais sobre a ação (obrigatorio para usuários do grupo VIG).

        :return: Nenhum valor é retornado.
        """

        log = Log(acao=acao, dataHora=datetime.now(), observacao=observacao, usuario=self.usuarioLogado)

        if acao == "ENTRADA" or acao == "SAIDA":
            log.dadosAntigos = {"vazio": 0}
            log.dadosNovos = self.movimentoGerNovo.toJson()
        elif acao == "UPDATE":
            log.dadosAntigos = self.movimentoGerAntigo.toJson()
            log.dadosNovos = self.movimentoGerNovo.toJson()
        else:
            log.dadosAntigos = self.movimentoGerAntigo.toJson()
            log.dadosNovos = {"vazio": 0}

        logDao = GeraLogDao()
        logDao.inserirLogControleGerente(log)