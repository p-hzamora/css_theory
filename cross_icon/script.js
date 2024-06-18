const d = document;

(function(){
    const $btn_icon = d.querySelector(".frame");
    $btn_icon.addEventListener("click",()=>{
        $btn_icon.classList.toggle("active")
    const $div = d.querySelector(".menu-icon").querySelectorAll("div");
    $div.forEach(el => {
        el.classList.toggle("no-animation")
    });
    })

})();
