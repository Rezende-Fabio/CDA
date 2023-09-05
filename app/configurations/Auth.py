from flask_login import LoginManager


def init_app(app):
    login_manager = LoginManager()
    login_manager.login_view = 'autenticacaoBlue.login'
    login_manager.login_message = "Por favor, faça o login para acessar esta página."
    login_manager.init_app(app)
    
    from ..models.Tables import SysUser
    @login_manager.user_loader
    def load_user(id):
        return SysUser.query.filter(SysUser.id == id, SysUser.us_delete != True, SysUser.us_ativo != True).first()