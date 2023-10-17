from ..models.dao.ConsultaLogControlChaveDao import ConsultaLogControlChaveDao
from ..models.dao.ConsultaParametrosDao import ConsultaParametrosDao
from ..models.dao.ManterUsuarioDao import ManterUsuarioDao
from ..extensions.FiltrosJson import filtroDataHora
from dateutil.relativedelta import relativedelta
from ..models.entity.Log import Log
from datetime import datetime
from typing import Optional
import json as js

class ControleConsultarLogControlChav:
    """
    Classe Controller para as funções de consulta de logs do controle de chaves
    @author - Fabio
    @version - 1.0
    @since - 14/09/2023
    """

    def consultaLogControlChave(self, acao: str, log: Optional[str]=None) -> list[dict]:
        """
        Consulta e retorna uma lista de logs de inserção de tercerios de acordo com a data na tabela de parâmetros('PAR_MANUT_CONTROL_CHAV').

        :return: Uma lista de dicionários contendo informações sobre os logs de inserção de tercerios.
            Cada dicionário possui tercerios "id", "dataHora", "acao", "resp" e "movChav".
        """

        dataDe = datetime.now()
        if log == None:
            #Consulta a data na tabela de parametros para fazer a pesquisa apartir desta data
            consultaParametro = ConsultaParametrosDao()
            mesesAtras = consultaParametro.consultaParametros("PAR_MANUT_CONTROL_CHAV")
            dataDe = dataDe - relativedelta(months=mesesAtras)
            dataDe = dataDe.strftime("%Y-%m-01")
        else:
            dataDe = dataDe.strftime("%Y-%m-%d")

        consultaControleChaveDao = ConsultaLogControlChaveDao()
        respDao = consultaControleChaveDao.consultaLogsControlChave(dataDe, acao)
        listaLogs = []

        for log in respDao:
            dictLog = {
                "id": log.id_logChave,
                "dataHora": filtroDataHora(log.lmch_dataHora),
                "acao": log.lmch_acao,
                "resp": log.nomeUser,
                "movChav": js.loads(log.lmch_dadosAntigos.decode("utf-8")) if acao in ["UPDATE", "DELETE"] else js.loads(log.lmch_dadosNovos.decode("utf-8"))
            }

            listaLogs.append(dictLog)

        return listaLogs      
        
        
    def consultaLogControlChaveDetelhado(self, id: int) -> Log:
        """
        Consulta e retorna detalhes de um registro de log do controle de chaves.

        :param id: O ID do registro de log de controle de chaves.
        
        :return: Um objeto Log contendo detalhes do registro de log de controle de chaves.
        """

        consultaControleChaveDao = ConsultaLogControlChaveDao()
        manterUsuarioDao = ManterUsuarioDao()
        respDao = consultaControleChaveDao.consultaLogsControlChaveDetalhado(id)
        
        usuario = manterUsuarioDao.consultarUsuarioDetalhado(respDao.lmch_idUsua)
        logControlChav = Log(id=respDao.id_logChave, dataHora=respDao.lmch_dataHora, acao=respDao.lmch_acao, observacao=respDao.lmch_observacao, usuario=usuario)
        logControlChav.converteDictDadosAntigos(respDao.lmch_dadosAntigos)
        logControlChav.converteDictDadosNovos(respDao.lmch_dadosNovos)

        return logControlChav
