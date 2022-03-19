
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

main();
M.AutoInit();

let password = document.querySelector("#password");
let confirm_password = document.querySelector("#confirm_password");

function validatePassword(){
    confirm_password.classList.add('invalid');
    if(password.value == confirm_password.value) {
        confirm_password.classList.remove('invalid');
        confirm_password.classList.add('valid');
        confirm_password.setCustomValidity('');
    }   
    else {
        confirm_password.setCustomValidity('Passwords Must Match');
    }     
}

function E_Tab(){
    M.Tabs.getInstance(document.querySelector('.tabs')).select('education-info');
    setTimeout(() => {
        history.replaceState('', document.title, window.location.origin + window.location.pathname + window.location.search)
    }, 5);
}

function S_Tab(){
    M.Tabs.getInstance(document.querySelector('.tabs')).select('social-info');
    setTimeout(() => {
        history.replaceState('', document.title, window.location.origin + window.location.pathname + window.location.search)
    }, 5);
}