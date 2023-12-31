
const form = document.getElementById('commentForm');
const comment = document.getElementById('id_comment');
const csrf = document.getElementsByName('csrfmiddlewaretoken');
let user_id;
let post_id;
let URL;

function loadData(user, post, url) {
    user_id = parseInt(user);
    post_id = parseInt(post);
    url = url;
}

function handleSubmit(event) {
    //prevent from submit form
    event.preventDefault();
    // event.stopPropagation();

    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value;
    data['comment'] = comment.value;
    data['author'] = user_id;
    data['post'] = post_id;

    // Send Form Data

    // sendData(URL, data);
    console.log(data);
}

function sendData(url, data) {
    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        success: function (res) {
        console.log(res);
        }
    })
}

form.addEventListener('submit', handleSubmit);