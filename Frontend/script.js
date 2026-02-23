async function LoginFunction(event) {
    event.preventDefault(); 
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const RequestOptions ={
        method: "POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    }
    try {
        const response = await fetch("http://127.0.0.1:8000/login",RequestOptions);
        const data = await response.json();
        if(response.ok){
            window.location.href='homepage.html';
        }else{
           console.error("Login failed:", data.detail);
           const ErrorDiv=document.getElementById("error-message");
           ErrorDiv.innerText=data.detail;
        }
    }
    catch(error){
        console.error("An error occurred:", error);
    }
}

async function SignupFunc(event) {
    event.preventDefault(); 
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm_password');
    if(password.value !== confirmPassword.value){
        const ErrorDiv=document.getElementById("error-message");
        ErrorDiv.innerText="Passwords do not match!";
        return;
    }else{
        try{
            const RequestOptions ={
                method: "POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body: JSON.stringify({
                    username: username.value,
                    password: password.value
                })
            }
            const response = await fetch("http://127.0.0.1:8000/register",RequestOptions);
            const data = await response.json()
            if(response.ok){
                window.location.href='homepage.html';
            }else{
                console.error("Registration failed:", data.detail);
                const ErrorDiv=document.getElementById("error-message");
                ErrorDiv.innerText=data.detail;
            }
        }
        catch(error){
            console.error("An error occurred:", error);
        }
    }
}