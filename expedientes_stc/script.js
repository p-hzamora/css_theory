const d = document;


function fill_table_template(expediente, banco, coordinador, estado){
    const $temp = d.querySelector("template-body-exp-table").content;
    const $fragment = d.createDocumentFragment();

    $temp.querySelector(".expediente").settAt
    $temp.querySelector(".banco").settAt
    $temp.querySelector(".coordinador").settAt
    $temp.querySelector(".estado").settAt

    expediente
    banco
    coordinador
    estado

}


const response=[
    {
        expediente: "12340132401",
        banco: "BBVA",
        coordinador: "Pablo",
        estado: "Archivado"
    },
    {
        expediente: "12340132401",
        banco: "caixa",
        coordinador: "Marina",
        estado: "Cerrado"
    },
    {
        expediente: "12340132401",
        banco: "BBVA",
        coordinador: "Pablo",
        estado: "Abierto"
    },
]


fill_table_template();