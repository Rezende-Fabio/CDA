var dadosLogsControleGer = []

$.ajax({
    url: '/lista-logs-controle-gerentes',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
        acao: "ENTRADA",
        log: true
    }),
    success: function(resp){
        for(x in resp.data){
            if (resp.login == "ADM"){
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/log/log-controle-gerente/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }else{
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/tec/log/log-controle-gerente/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }
           dataresp = {
            acao: resp.data[x].acao,
            data: resp.data[x].dataHora,
            resp: resp.data[x].resp,
            cracha: resp.data[x].movGer.gerente.cracha,
            gerente: resp.data[x].movGer.gerente.nome.substring(0, 15),
            visualizar: visu
           }
           dadosLogsControleGer.push(dataresp)
        }
    }
});


$.ajax({
    url: '/lista-logs-controle-gerentes',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
       acao: "SAIDA",
       log: true
    }),
    success: function(resp){
        for(x in resp.data){
            if (resp.login == "ADM"){
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/log/log-controle-gerente/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }else{
                var visu = `<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/tec/log/log-controle-gerente/${resp.data[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`
            }
           dataresp = {
            acao: resp.data[x].acao,
            data: resp.data[x].dataHora,
            resp: resp.data[x].resp,
            cracha: resp.data[x].movGer.gerente.cracha,
            gerente: resp.data[x].movGer.gerente.nome.substring(0, 15),
            visualizar: visu
           }
           dadosLogsControleGer.push(dataresp)
        }
    }
});