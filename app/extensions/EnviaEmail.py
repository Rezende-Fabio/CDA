from ..models.entity.Usuario import Usuario
from email.message import EmailMessage
import smtplib
import netifaces


class EnviaEmail:
    """
    Classe para funções relacionadas ao enviar E-mail
    @author - Fabio
    @version - 1.0
    @since - 14/06/2023
    """

    def enviarEmail(self, usuario: Usuario):#Função para enviar E-mail
        try:
            endercoEmail = '' #E-mail que vai conectar no servidor
            senhaEmail = '' #Senha do e-mail
            
            msg = EmailMessage()
            msg['Subject'] = "Alteração de senha no CDA" #Assunto do E-mail
            msg["From"] = "" #Correspondente que vai aparcer no e-mail
            msg["To"] = usuario.email #Pra quem vai enviar
            msg.set_type("text/html")
            msg.set_content("Alteração de senha no CDA") 
            #Mensagem
            htmlMsg = f"""
            <h3>Solicitação de alteração de senha do usuário {usuario.usuario} foi aceita. Utilize a link abaixo para alterção da mesma.</h3>
            <br>
            
            <p><strong>Link:</strong> <a href='http://{self.ipServidor()}:6560/esqueci-senha/{usuario.hashSenhaNova}'>http://{self.ipServidor()}:6560/esqueci-senha/{usuario.hashSenhaNova}</a></p>
            <p style="color: #FF0000;"><strong>Esse link expira em 2 minutos.</strong></p>
            <br><br>
            
            E-mail enviado automaticamente. Não responder.<br>
            Obrigado!
            """
        
            msg.add_alternative(htmlMsg, subtype="html")
            
            with smtplib.SMTP_SSL('', ) as smtp: #Abre o servidor executa as funções abaixo e fecha a conexão
                smtp.login(endercoEmail, senhaEmail) #Faz login no Servidor
                smtp.send_message(msg) #Envia o E-mail
            
            return True
        
        except:
            return False    
    
        
    def ipServidor(self):
        interfaces = netifaces.interfaces()
        for interface in interfaces:
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                ipv4_addresses = addresses[netifaces.AF_INET]
                for address in ipv4_addresses:
                    if 'addr' in address:
                        ip_address = address['addr']
                        if ip_address.startswith('') or ip_address.startswith(''):
                            return ip_address