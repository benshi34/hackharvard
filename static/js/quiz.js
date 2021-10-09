console.log('hello world quiz')
const url = window.location.href

const quizBox = document.getElementById("quiz-box")
let data

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        //console.log(response)
        data = response.data
        data.forEach(el => {
            for(const [questions,answers] of Object.entries(el)){
                quizBox.innerHTML += 
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                    </hr>
                
            } 
        });
    },
    error: function(error){
        console.log(error)
    }
})