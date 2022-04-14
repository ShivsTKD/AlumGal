const aside = document.getElementById('aside');
const mq = window.matchMedia('(max-width: 600px)');

function asideDisplay(){
  if (!mq.matches && aside.offsetWidth === 0){
    aside.style.maxWidth = "15em";
    aside.style.visibility = "visible";
    aside.style.transition = "all 500ms ease";
    aside.style.width = "15em";
  }
  else if (mq.matches && aside.offsetWidth === 0){
    aside.style.maxWidth = "100vw";
    aside.style.visibility = "visible";
    aside.style.transition = "all 500ms ease";
    aside.style.width = "100vw";
  }
  else {
    aside.style.maxWidth = "0";
  }
}

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