from ..models.dao.ConsultaParametrosDao import ConsultaParametrosDao

class ControleConsultaParametros:
    """
    Classe Controller para as funções de consulta de parametros de sistemas
    @author - Fabio
    @version - 1.0
    @since - 11/09/2023
    """

    def consultaParametros(self, codigo: str) -> int:
        """
        Consulta e retorna um dicionário com todos os meses de cada consulta de log de usuários.

        :return: Um dicionário contendo informações sobre os cada mês para pesquisa.
                Dicionário possui chaves "insert", "update", "active" e "delelte".
        """

        consultaParametrosDao = ConsultaParametrosDao()
        parametrosMeses = consultaParametrosDao.consultaParametros(codigo)

        return parametrosMeses
    

    def consultaTodosParametros(self) -> list[dict]:
        """
        Consulta e retorna um dicionário com todos os parâmetros do sistema.

        :return: Um dicionário contendo informações sobre os cada parâmetro.
                Dicionário possui chaves "codigo", "valor" e "desc".
        """
        
        consultaParametrosDao = ConsultaParametrosDao()
        parametros = consultaParametrosDao.consultaTodosParametros()

        listaParametros = []
        for parm in parametros:
            dicParm = {
                "codigo": parm.par_codigo,
                "valor": parm.par_valor,
                "desc": parm.par_desc
            }

            listaParametros.append(dicParm)

        return listaParametros


    def aletarParametros(self, listaParams: list[dict]) -> bool:
        """
        Altera os parâmetros das tabelas de logs do menter usuários.

        :param listaParams: Uma lista contendo os novos valores para efetuar as cnosultas.

        :return: True caso a alteração sejá bem-sucedida, False caso não.
        """

        consultaParametrosDao = ConsultaParametrosDao()
        for parametros in listaParams:
            consultaParametrosDao.aleterarParametros(parametros["codigo"], parametros["valor"])

        return True