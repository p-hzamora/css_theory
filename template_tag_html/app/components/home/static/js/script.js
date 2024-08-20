import { TableGenerator } from "js/createTable.js";

const d = document;


d.addEventListener("DOMContentLoaded",function(){
    loadstaffList();
})


function loadstaffList(){
    fetch("/staffs/",{method:"GET"}).then(response=>response.json()).then(data=>{
        const table = new TableGenerator(data);
        table.render("content");
    })
    .catch(error=>console.error("error to create table", error))
}

function loadCityList(){
    fetch("/staffs/",{method:"GET"}).then(response=>response.json()).then(data=>{
        const table = new TableGenerator(data);
        table.render("content");
    })
    .catch(error=>console.error("error to create table", error))
}

function loadAddressList(){
    fetch("/staffs/",{method:"GET"}).then(response=>response.json()).then(data=>{
        const table = new TableGenerator(data);
        table.render("content");
    })
    .catch(error=>console.error("error to create table", error))
}