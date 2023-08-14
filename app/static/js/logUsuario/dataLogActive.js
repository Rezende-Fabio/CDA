var dadosLogUserActive = []

$.ajax({
    url: '/lista-logs-usuario',
    type: 'POST',
    async: false,
    dataType: 'json',
    contentType: 'application/json',
    data:JSON.stringify({
       tipo: "ACTIVE"
    }),
    success: function(resp){
        console.log(resp)
        for(x in resp){
           dataresp = {
            acao: resp[x].acao,
            data: resp[x].dataHora,
            resp: resp[x].resp,
            usuario: resp[x].usuario.us_usuario,
            visualizar: gridjs.html(`<div style="width: 100%;display: flex;align-items: center;text-align: center;justify-content: center;"><a href="/admin/controle-chave/incluir-devolucao/${resp[x].id}" class="btn btn-primary btn-sm"><i class="fa-regular fa-eye"></i></a></div>`)
           }
           dadosLogUserActive.push(dataresp)
        }
    }
});


var colunasLogUserActive = [
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
        id: 'usuario',
        name: "Usuário"
    },
    {
        id: 'visualizar',
        name: gridjs.html("<span style='display:flex; text-align: center; justify-content: center;align-items: center;'>Visualizar</span>")
    }
]