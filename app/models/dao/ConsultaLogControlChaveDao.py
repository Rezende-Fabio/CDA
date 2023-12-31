from ...configurations.Database import DB
from ..Tables import CDA001, SysUser

class ConsultaLogControlChaveDao:
    """
    Classe Dao para funções de consulta de logs do controle de chave
    @tables - SysUser, CDA001
    @author - Fabio
    @version - 1.0
    @since - 14/09/2023
    """

    def consultaLogsControlChave(self, data: str, acao: str) -> CDA001:
        logs = DB.session.query(CDA001.id_logChave, CDA001.lmch_acao, CDA001.lmch_dataHora, CDA001.lmch_dadosNovos, CDA001.lmch_dadosAntigos, SysUser.us_usuario.label("nomeUser"))\
            .join(SysUser, CDA001.lmch_idUsua == SysUser.id)\
                .filter(CDA001.lmch_acao==acao, CDA001.lmch_dataHora>=data)\
                    .order_by(CDA001.lmch_dataHora)

        return logs
    

    def consultaLogsControlChaveDetalhado(self, id: int) -> CDA001:
        log = DB.session.query(CDA001.id_logChave, CDA001.lmch_acao, CDA001.lmch_dataHora, CDA001.lmch_dadosNovos, CDA001.lmch_dadosAntigos, CDA001.lmch_observacao, CDA001.lmch_idUsua)\
            .filter(CDA001.id_logChave==id)\
                .first()
        
        return log
