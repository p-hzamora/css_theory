const d = document;
const $sidebar = d.querySelector(".sidebar");

function showSidebar(){
    $sidebar.style.display = "flex";
}

function closeSidebar(){
    $sidebar.style.display = "none";
}

const $btn = d.querySelector(".sidebar-btn");
const $close_btn = d.querySelector(".close-btn-sidebar");

$btn.addEventListener("click",showSidebar);
$close_btn.addEventListener("click",closeSidebar);
