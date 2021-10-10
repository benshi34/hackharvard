console.log('Hello World')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click',()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')

    modalBtn.innerHTML = `
        <div class="h5 mb-3">Are you sure you want to begin "<b>${name}</b>"
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
}))