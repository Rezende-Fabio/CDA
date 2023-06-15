import bcrypt

#Classe Usuario do sistema
class Usuario:
    id: int
    nome: str
    email: str
    grupo: str
    usuario: str
    senha: str
    complex: str
    ativo: bool
    delete: bool
    senhaCompara: str

    def set_id(self, id: int) -> None:
        self.id = id

    def set_nome(self, nome: str) -> None:
        self.nome = nome

    def set_email(self, email: str) -> None:
        self.email = email
    
    def set_grupo(self, grupo: str) -> None:
        self.grupo = grupo
        
    def set_usuario(self, usuario: str) -> None:
        self.usuario = usuario

    def set_senha(self, senha: str) -> None:
        self.senha = senha
    
    def set_complex(self, complex: str) -> None:
        self.complex = complex

    def set_ativo(self, ativo: bool) -> None:
        self.ativo = ativo
    
    def set_delete(self, delete: bool) -> None:
        self.delete = delete

    def set_senhaCompara(self, senhaCompara: str) -> None:
        self.senhaCompara = senhaCompara

    def get_id(self) -> int:
        return self.id

    def get_nome(self) -> str:
        return self.nome

    def get_email(self) -> str:
        return self.email
    
    def get_grupo(self) -> str:
        return self.grupo
        
    def get_usuario(self) -> str:
        return self.usuario

    def get_senha(self) -> str:
        return self.senha
    
    def get_complex(self) -> str:
        return self.complex

    def get_ativo(self) -> bool:
        return self.ativo
    
    def get_delete(self) -> bool:
        return self.delete
    
    def get_senhaCompara(self) -> str:
        return self.senhaCompara
    
    def gerarSenha(self, senha: str) -> None:
        salt = bcrypt.gensalt(8)
        hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
        self.senha = hash.decode("utf-8")
        self.complex = salt.decode("utf-8")

    def verificarSenha(self) -> bool:
        hash = bcrypt.hashpw(self.senha.encode('utf-8'), bytes(self.complex, 'utf-8'))
        if hash == self.senhaCompara:
            return True
        else:
            return False