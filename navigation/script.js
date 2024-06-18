const d = document;

const $a = d.querySelectorAll(".nav-menu-item");

function activeLink(){
    $a.forEach(item=>{
        item.classList.remove("active");
    })
    this.classList.add("active");

}
$a.forEach(item=>{
    item.addEventListener("click",activeLink)
})

