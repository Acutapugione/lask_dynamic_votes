// onclick="alert(document.getElementById('inputGroupSelect01').getAttribute('value'))
// document.querySelector("#inputGroupSelect02")
const votes = document.querySelectorAll("select.vote")

votes.forEach(vote => {
    vote.addEventListener("click", (e => {
        e.preventDefault()
        const selected_index = e.target.selectedIndex
        const selected_item = e.target.options[selected_index]
        
        // alert(`${e.target.getAttribute('id')}, ${selected_item.value}`)
        // fetch() {{url_for('vote_result')}}

        const data = new URLSearchParams();
        data.append('question_id', e.target.getAttribute('id'));
        data.append('option_id', selected_item.value);
        fetch("/vote/result/",{
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: data
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error(error));
        // {
        //     question_id: e.target.getAttribute('id')
        //     option_id:selected_item.value
        // }
    }));
});