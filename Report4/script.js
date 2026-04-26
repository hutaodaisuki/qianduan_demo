function validateRegister() {
    let isValid = true;
    
    document.querySelectorAll('.error-msg').forEach(el => el.textContent = '');
    
    const username = document.getElementById('username').value.trim();
    if (username === '') {
        document.getElementById('usernameError').textContent = '用户名不能为空';
        isValid = false;
    } else if (username.length < 2 || username.length > 15) {
        document.getElementById('usernameError').textContent = '用户名长度应在2-15个字符之间';
        isValid = false;
    } else if (!/^[a-zA-Z0-9_\u4e00-\u9fa5]+$/.test(username)) {
        document.getElementById('usernameError').textContent = '用户名只能包含字母、数字、下划线和中文';
        isValid = false;
    }
    
    const password = document.getElementById('password').value;
    if (password === '') {
        document.getElementById('passwordError').textContent = '密码不能为空';
        isValid = false;
    } else if (password.length < 6) {
        document.getElementById('passwordError').textContent = '密码长度不能少于6个字符';
        isValid = false;
    } else if (!/(?=.*[a-zA-Z])(?=.*[0-9])/.test(password)) {
        document.getElementById('passwordError').textContent = '密码必须包含字母和数字';
        isValid = false;
    }
    
    const confirmPassword = document.getElementById('confirmPassword').value;
    if (confirmPassword === '') {
        document.getElementById('confirmPasswordError').textContent = '请确认密码';
        isValid = false;
    } else if (confirmPassword !== password) {
        document.getElementById('confirmPasswordError').textContent = '两次输入的密码不一致';
        isValid = false;
    }
    
    const email = document.getElementById('email').value.trim();
    if (email === '') {
        document.getElementById('emailError').textContent = '邮箱不能为空';
        isValid = false;
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        document.getElementById('emailError').textContent = '请输入有效的邮箱地址';
        isValid = false;
    }
    
    const phone = document.getElementById('phone').value.trim();
    if (phone === '') {
        document.getElementById('phoneError').textContent = '联系电话不能为空';
        isValid = false;
    } else if (!/^1[3-9]\d{9}$/.test(phone)) {
        document.getElementById('phoneError').textContent = '请输入有效的11位手机号';
        isValid = false;
    }
    
    const securityQuestion = document.getElementById('securityQuestion').value;
    if (securityQuestion === '') {
        document.getElementById('questionError').textContent = '请选择密码问题';
        isValid = false;
    }
    
    const questionAnswer = document.getElementById('questionAnswer').value.trim();
    if (questionAnswer === '') {
        document.getElementById('answerError').textContent = '请输入问题答案';
        isValid = false;
    }
    
    const occupation = document.getElementById('occupation').value;
    if (occupation === '') {
        document.getElementById('occupationError').textContent = '请选择职业';
        isValid = false;
    }
    
    if (isValid) {
        alert('注册成功！');
        window.location.href = 'login.html';
    }
    
    return false;
}

function validateLogin() {
    let isValid = true;
    
    document.querySelectorAll('.error-msg').forEach(el => el.textContent = '');
    
    const username = document.getElementById('loginUsername').value.trim();
    if (username === '') {
        document.getElementById('loginUsernameError').textContent = '用户名不能为空';
        isValid = false;
    } else if (username.length < 2 || username.length > 15) {
        document.getElementById('loginUsernameError').textContent = '用户名长度应在2-15个字符之间';
        isValid = false;
    }
    
    const password = document.getElementById('loginPassword').value;
    if (password === '') {
        document.getElementById('loginPasswordError').textContent = '密码不能为空';
        isValid = false;
    } else if (password.length < 6) {
        document.getElementById('loginPasswordError').textContent = '密码长度不能少于6个字符';
        isValid = false;
    }
    
    if (isValid) {
        alert('登录成功！');
    }
    
    return false;
}