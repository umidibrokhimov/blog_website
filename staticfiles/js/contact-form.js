let form = document.querySelector('#contact .contactt-form');

form.addEventListener('submit', (e)=> {
    e.preventDefault()
    
    username = form.querySelector('#name')
    email = form.querySelector('#email')
    subject = form.querySelector('#subject')
    text = form.querySelector('#text')
    
    let my_text = `Yangi user: %0A - Username: ${username.value} %0A - Useremail: ${email.value} %0A - User Subject: ${subject.value} %0A - User Text: ${text.value}`
    
    let token = '5364201856:AAG9P3GruT17uqf0YEOsCC52vI1SapIuwSo';
    let chat_id = -1001640322912
    
    let url = `https://api.telegram.org/bot${token}/sendMessage?chat_id=${chat_id}&text=${my_text}`
    
    let api = new XMLHttpRequest()
    api.open("GET", url, true)
    api.send()
    
    username.value = ''
    email.value = ''
    subject.value = ''
    text.value = ''
    
    let alertSucces = form.querySelector('#succes-alert')
    alertSucces.classList.remove('d-none')
    
    setTimeout(() => {
        alertSucces.classList.add('d-none')
    }, 3000)
})