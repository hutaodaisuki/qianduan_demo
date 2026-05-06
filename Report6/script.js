// 标签切换功能
document.addEventListener('DOMContentLoaded', function() {
    // 登录注册页面的标签切换
    const tabs = document.querySelectorAll('.auth-tab');
    const forms = document.querySelectorAll('.auth-form');
    
    if (tabs.length > 0 && forms.length > 0) {
        tabs.forEach(tab => {
            tab.addEventListener('click', function() {
                const tabId = this.getAttribute('data-tab');
                
                // 移除所有标签的active类
                tabs.forEach(t => t.classList.remove('active'));
                // 添加当前标签的active类
                this.classList.add('active');
                
                // 隐藏所有表单
                forms.forEach(form => form.classList.remove('active'));
                // 显示当前表单
                document.getElementById(tabId + '-form').classList.add('active');
            });
        });
        
        // 登录表单验证
        const loginForm = document.getElementById('login-form');
        if (loginForm) {
            loginForm.addEventListener('submit', function(e) {
                e.preventDefault();
                const username = document.getElementById('login-username').value;
                const password = document.getElementById('login-password').value;
                
                if (!username) {
                    alert('请输入用户名');
                    return;
                }
                
                if (!password) {
                    alert('请输入密码');
                    return;
                }
                
                if (password.length < 6) {
                    alert('密码长度不能小于6位');
                    return;
                }
                
                alert('登录成功！');
            });
        }
        
        // 注册表单验证
        const registerForm = document.getElementById('register-form');
        if (registerForm) {
            registerForm.addEventListener('submit', function(e) {
                e.preventDefault();
                const username = document.getElementById('register-username').value;
                const phone = document.getElementById('register-phone').value;
                const password = document.getElementById('register-password').value;
                const confirmPassword = document.getElementById('register-confirm-password').value;
                
                if (!username) {
                    alert('请输入用户名');
                    return;
                }
                
                if (!phone) {
                    alert('请输入手机号');
                    return;
                }
                
                // 手机号格式验证
                const phoneRegex = /^1[3-9]\d{9}$/;
                if (!phoneRegex.test(phone)) {
                    alert('请输入正确的手机号格式');
                    return;
                }
                
                if (!password) {
                    alert('请输入密码');
                    return;
                }
                
                if (password.length < 6) {
                    alert('密码长度不能小于6位');
                    return;
                }
                
                if (password !== confirmPassword) {
                    alert('两次密码输入不一致');
                    return;
                }
                
                alert('注册成功！');
            });
        }
    }
});