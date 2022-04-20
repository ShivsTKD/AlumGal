const aside = document.getElementById('aside');
const mq = window.matchMedia('(max-width: 896px)');

function asideDisplay(){
  if (!mq.matches && aside.offsetWidth === 0){
    aside.style.maxWidth = "20em";
    aside.style.visibility = "visible";
    aside.style.transition = "all 500ms ease";
    aside.style.width = "20em";
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

function removeFlash(element){
    element.style.display = "none";
}

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

let numUsers = 0;

async function loadMoreUsers(){
  numUsers += 25;
  let result = document.getElementById("resultListing");
  let html = "";
  let response = await fetch(`/loadusers/${numUsers}`);
  let users = await response.json();
  for (let user of users){
    html += `
      <a href="/profile/${user.pid}" class="card">
        <img class="responsive-img" src="/static/Userpics/Zachary Bowen.jpg" alt="${user.first_name} ${user.last_name}">
        <div>
          <span>Name:      ${user.first_name} ${user.last_name}</span>
          <span>Grad Year: ${user.graduation_year}</span>
        </div>
      </a>
    `;
  }
  result.innerHTML += html;
}

function loadMoreResults(){
  numUsers += 25;
  let result = document.getElementById("resultListing");
  let html = "";
  for (let i = numUsers; i < (numUsers + 25); i++){
    html += `
      <a href="/profile/${arguments[0][i].pid}" class="card">
        <img class="responsive-img" src="/static/Userpics/Zachary Bowen.jpg" alt="${arguments[0][i].first_name} ${arguments[0][i].last_name}">
        <div>
          <span>Name:      ${arguments[0][i].first_name} ${arguments[0][i].last_name}</span>
          <span>Grad Year: ${arguments[0][i].graduation_year}</span>
        </div>
      </a>
    `;
  }
  if (numUsers - 25 > arguments[0].length){
    for (let i = numUsers - 25; i < arguments[0].length; i++){
      html += `
        <a href="/profile/${arguments[0][i].pid}" class="card">
          <img class="responsive-img" src="/static/Userpics/Zachary Bowen.jpg" alt="${arguments[0][i].first_name} ${arguments[0][i].last_name}">
          <div>
            <span>Name:      ${arguments[0][i].first_name} ${arguments[0][i].last_name}</span>
            <span>Grad Year: ${arguments[0][i].graduation_year}</span>
          </div>
        </a>
      `;
    }
  }
  result.innerHTML += html;
}