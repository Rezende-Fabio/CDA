from flask import Blueprint, render_template, request, abort, url_for, make_response
from ...controllers.ControleGerarRelatorio import ControleGerarRelatorio
from ...extensions.HtmlToPdf import PdfKit
from ...extensions.LogErro import LogErro
from flask_login import login_required
import traceback
import sys


relatorioBlue = Blueprint("relatorioBlue", __name__)

##############################################################
# Rotas relacionadas aos relatórios
##############################################################

#Rota para tela de gerar relatórios
@relatorioBlue.route('/relatorios', methods=["GET"])
@login_required
def relatorio():
    try:
        context = {"titulo": "Relatórios", "active": "relat"}
        return render_template("public/relatorio.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)


#Rota para gera relatorios do controle de chaves
@relatorioBlue.route('/relatorios/controle-caves', methods=["POST"])
@login_required
def relatorioControleChaves():
    try:
        controleGerarRelatorio = ControleGerarRelatorio()
        movimentos = controleGerarRelatorio.gerarRelatControleChave(request.form["deControlChave"], request.form["ateControlChave"])
        # html = render_template("public/relatorios/relatControleChave.html", context=context)
        context = {"de": request.form["deControlChave"], "ate": request.form["ateControlChave"], "movimentos": movimentos}
        # html = render_template("public/relatorios/relatControleChave.html", context=context)
        # css = [f"{url_for('static', filename='css/styleRelatorio.css')}", f"{url_for('static', filename='plugins/bootstrap/css/bootstrap.min.css')}"]
        # pdfKit = PdfKit()
        # pdf = pdfKit.fromString(html, css)
        # response = make_response(pdf)
        # response.headers["Content-Type"] = "application/pdf"
        # response.headers["Content-Disposition"] = "inline; filename=output.pdf"
        #return response
        return render_template("public/relatorios/relatControleChave.html", context=context)
    except:
        log = LogErro()
        tipoExcecao, valorExcecao, tb = sys.exc_info()
        tracebackInfo = traceback.extract_tb(tb)
        log.geraLogErro(tipoExcecao, valorExcecao, tracebackInfo, request.url)
        abort(500)