// 网页的 JavaScript 部分
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // 阻止表单默认提交行为

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // 发送登录请求到服务器
    fetch("/sign_in/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // 登录成功，进行页面跳转
            window.location.href = "index.html";
        } else {
            // 登录失败，显示错误提示
            alert(data.error);
        }
    })
    .catch(error => {
        // 发生错误，显示通用错误提示
        alert("An error occurred. Please try again later.");
        console.error(error);
    });
});
