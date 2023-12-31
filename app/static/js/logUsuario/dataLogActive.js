var dadosLogUserActive = []

$.ajax({
    url: '/lista-logs-usuario',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
       acao: "ACTIVE"
    }),
    success: function(resp){
        console.log(resp)
        for(x in resp){
           dataresp = {
            acao: resp[x].acao,
            data: resp[x].dataHora,
            resp: resp[x].resp,
            usuario: resp[x].usuario.usuario,
            visualizar: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/log/log-manter-usuario/${resp[x].id}" class="btn btn-primary btn-sm" title="VIZUALIZAR"><i class="fa-regular fa-eye"></i></a></div>`)
           }
           dadosLogUserActive.push(dataresp)
        }
    }
});


var colunasLogUserActive = [
    {
        id: 'acao',
        name: 'Ação',
        width: '120px'
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
        id: 'usuario',
        name: "Usuário"
    },
    {
        id: 'visualizar',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Visualizar</span>")
    }
]