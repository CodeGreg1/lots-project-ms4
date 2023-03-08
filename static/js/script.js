function SendMail() {
    var params = {
        from_name : document.getElementById("name").value,
        email_id : document.getElementById("email").value,
        message : document.getElementById("message").value,
    }
    emailjs.send("service_nr7grav", "template_f97dyp9", params).then(function (res) {
        alert("Success! Message sent!")
    })
}