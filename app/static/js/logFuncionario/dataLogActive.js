var dadosLogFuncActive = []

$.ajax({
    url: '/lista-logs-funcionarios',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
       tipo: "ACTIVE"
    }),
    success: function(resp){
        for(x in resp){
           dataresp = {
            acao: resp[x].acao,
            data: resp[x].dataHora,
            resp: resp[x].resp,
            func: resp[x].func.nome,
            visualizar: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/controle-chave/incluir-devolucao/${resp[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`)
           }
           dadosLogFuncActive.push(dataresp)
        }
    }
});


var colunasLogFuncActive = [
    {
        id: 'acao',
        name: 'Ação'
    },
    {
        id: 'data',
        name: 'Data'
    },
    {
        id: 'resp',
        name: "Responsável"
    },
    {
        id: 'func',
        name: "Funcionários"
    },
    {
        id: 'visualizar',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Visualizar</span>")
    }
]