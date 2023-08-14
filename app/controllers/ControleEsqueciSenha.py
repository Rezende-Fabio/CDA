from ..models.dao.EsqueciSenhaDao import EsqueciSenhaDao
from ..extensions.EnviaEmail import EnviaEmail
from ..models.entity.Usuario import Usuario
from datetime import datetime

"""
Classe Controller para funções do esqueci a senha
@author - Fabio
@version - 1.0
@since - 13/06/2023
"""

class ControleEsqueciSenha:

    def verificarUsuario(self, usuario: str, email: str) -> int:
        #########################################################################################
        # Essa Função recebe usuario e e-mail como parametro para verificar se o usuário existe
        # e para gerar o hash que vai ser enviado posteriormente por e-mail.
        
        # PARAMETROS:
        #   usuario = Usuário informado no form de esqueci a senha;
        #   email = E-mail informado no form de esqueci a senha.
        
        # RETORNOS:
        #   return 1 = Retorna 1 caso envie o e-mail corretamente;
        #   return 2 = Retorna 2 caso não envie o e-mail corretamente;
        #   return 3 = Retrona 3 caso usuário/e-mail incorreto.
        #########################################################################################

        user = Usuario()
        esqueciSenhaDao = EsqueciSenhaDao()
        user.usuario = usuario
        user.email = email
        respDao = esqueciSenhaDao.verificaUsuario(user)
        if respDao != 0:
            user.gerarHashSenhaNova()
            while True:
                if esqueciSenhaDao.verificaHash(user.hashSenhaNova):
                    break
                else:
                    user.gerarHashSenhaNova()
            
            esqueciSenhaDao.insereHash(user)

            enviaEmail = EnviaEmail()
            if enviaEmail.enviarEmail(user):
                return 1
            else:
                return 2
        else:
            return 3


    def verificarHash(self, hash: str) -> int:
        #########################################################################################
        # Essa Função recebe o hash passado pela URL e verifica se existe.
        
        # PARAMETROS:
        #   hash = Hash que foi passado pela URL do e-mail.
        
        # RETORNOS:
        #   return 1 = Retorna 1 caso o hash não exista;
        #   return 2 = Retorna 2 caso o hash exista;
        #   return 3 = Retorna 3 caso o hash exista mas o tempo já expirou.
        #########################################################################################

        dataAtual = datetime.now()
        esqueciSenhaDao = EsqueciSenhaDao()
        usuario = esqueciSenhaDao.verificaHashTempo(hash)
        if usuario:
            if str(dataAtual) > usuario.us_limiteNovasenha:
                return 3
            else:
                return 1
        else:
            return 2
        

    def trocaSenha(self, senha: str, hash: str) -> int:
        user = Usuario()
        user.gerarSenha(senha)
        user.hashSenhaNova= ""
        user.senhaNova = False

        esqueciSenhaDao = EsqueciSenhaDao()
        if esqueciSenhaDao.trocaSenha(hash, user):
            return 1
        else: 
            return 2