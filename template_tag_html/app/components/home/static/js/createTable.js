const d = document;

export class TableGenerator{
    constructor(jsonArray){
        this.data = jsonArray;
        this.headers = Object.keys(jsonArray[0]);
    }

    generateTable(){
        const table = d.createElement("table");
        table.style.borderCollapse = "collapse";

        const thead = d.createElement("thead");
        const headerRow = d.createElement("tr");
        this.headers.forEach(el=>{
            const th = d.createElement("th");
            th.textContent = el;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.append(thead)

        const tbody =  d.createElement("tbody");
        this.data.forEach(row=>{
            const tr = d.createElement("tr");
            this.headers.forEach(col=>{
                const td = d.createElement("td");
                td.textContent= row[col]
                tr.appendChild(td);
            });
            tbody.appendChild(tr);
        });

        table.appendChild(tbody);

        return table
    }

    render(containerID){
        const $container = d.getElementById(containerID);
        if ($container){
            const table = this.generateTable();
            $container.appendChild(table);
        }else{
            console.error(`${containerID} does not found.`)
        }
    }
}
