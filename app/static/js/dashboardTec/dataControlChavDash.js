var dadosLogsControleChave = []

$.ajax({
    url: '/lista-logs-controle-chaves',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
        acao: "RETIRADA",
        log: true
    }),
    success: function(resp){
        for(x in resp.data){
            if (resp.login == "ADM"){
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/log/log-controle-chave/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }else{
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/tec/log/log-controle-chave/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }
           dataresp = {
            acao: resp.data[x].acao,
            data: resp.data[x].dataHora,
            resp: resp.data[x].resp,
            codigo: resp.data[x].movChav.chave.codigo,
            chave: resp.data[x].movChav.chave.nome.substring(0, 15),
            visualizar: visu
           }
           dadosLogsControleChave.push(dataresp)
        }
    }
});

$.ajax({
    url: '/lista-logs-controle-chaves',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
       acao: "DEVOLUCAO",
       log: true
    }),
    success: function(resp){
        for(x in resp.data){
            if (resp.login == "ADM"){
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/log/log-controle-chave/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }else{
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/tec/log/log-controle-chave/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }
           dataresp = {
            acao: resp.data[x].acao,
            data: resp.data[x].dataHora,
            resp: resp.data[x].resp,
            codigo: resp.data[x].movChav.chave.codigo,
            chave: resp.data[x].movChav.chave.nome.substring(0, 15),
            visualizar: visu
           }
           dadosLogsControleChave.push(dataresp)
        }
    }
});
