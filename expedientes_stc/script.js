const d = document;

function read_response_and_fill_exp_list(){

    const $exp_container = d.querySelector(".exp-container");
    const $fragment = d.createDocumentFragment();


    function fill_exp_list({expediente, banco, coordinador, estado}){
        const $temp = d.getElementById("template-li-exp").content;

        $temp.querySelector(".expediente").textContent = expediente;
        $temp.querySelector(".banco").textContent = banco;
        $temp.querySelector(".coordinador").textContent = coordinador;
        $temp.querySelector(".estado").textContent = estado;

        const clone = d.importNode($temp,true);
        $fragment.appendChild(clone);

    }

    const response_pendientes=[
        {
            expediente: "qwertyui",
            banco: "otro BBVA",
            coordinador: "Pablo",
            estado: "En progreso"
        },
        {
            expediente: "1o2iu3yt",
            banco: "caixa",
            coordinador: "Marina",
            estado: "Aperturando"
        },
        {
            expediente: "xcvbnkjhgfds",
            banco: "BBVA",
            coordinador: "Pablo",
            estado: "Abierto"
        },
    ]
    const response_archivados=[
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
    const response_cerrados=[
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



    response_pendientes.forEach(e=>{
        fill_exp_list(e);
    });

    $exp_container.appendChild($fragment);

}


d.addEventListener("DOMContentLoaded",()=>{
    const $estados = d.querySelectorAll(".estados .estado")
    $estados.forEach(e=>{
        e.addEventListener("click",function(){
            $estados.forEach(e=>{
                e.classList.remove("active")
            })
            this.classList.add("active")
        })
    })
})


read_response_and_fill_exp_list()