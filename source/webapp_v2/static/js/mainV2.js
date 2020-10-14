function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
let csrftoken = getCookie('csrftoken');

async function makeRequest(url, method='GET',data={}) {
    let headers = {'Content-Type':'application/json',
    'X-CSRFToken': getCookie('csrftoken')
    }
    let response = await fetch(url, {method,headers:headers,body:JSON.stringify(data)});

    if (response.ok) {  // нормальный ответ
        console.log(response)
        return await response.json();

    } else {            // ошибка
        console.log(response)
        let error = new Error();
        error.response = response;
        throw error;
    }
}

// answer = makeRequest('http://localhost:8000/api/v1/multiply/',method = "POST", data = {"A":5,"B":4})
let buttons = document.querySelectorAll('button')
for (let button of buttons) {
    button.addEventListener('click', async function(event){
        try {
            let answer = await makeRequest('http://localhost:8000/api/v1/'+event.target.id+'/',method = "POST",
        data = {"A":document.getElementById('A').value,"B":document.getElementById('B').value})
            document.getElementById('text').value = answer.answer
        } catch (e) {
            let er = await e.response.json()
            document.getElementById('text').value = er.error
        }
    })
}
