function ShowPassword(){
    inputPassword = document.getElementById('password');
    buttonEye = document.getElementById('showpassword');

    if(inputPassword.type === 'password'){
        inputPassword.setAttribute('type', 'text');
        buttonEye.setAttribute('src', '../static/img/closed.png');
    }
    else{
        inputPassword.setAttribute('type', 'password');
        buttonEye.setAttribute('src', '../static/img/open.png');
    }
}