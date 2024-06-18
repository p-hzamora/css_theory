function showSpinner() {
    const spinner = document.createElement('div');
    spinner.classList.add('spinner');
        document.body.appendChild(spinner);
}

function hideSpinner() {
    const spinner = document.querySelector('.spinner');
    
    if (spinner) {
        spinner.classList.remove("spinner");
    }
}


showSpinner();
