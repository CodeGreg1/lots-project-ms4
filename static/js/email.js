const btn = document.getElementById('buttonsm');
// Below is the code to send emails using emailJS
function sendReset() {
  btn.value = 'Send Email';
}

document.getElementById('form').addEventListener('submit', function(event) {
   event.preventDefault();

   btn.value = 'Sending...';

   const serviceID = 'default_service';
   const templateID = 'template_f97dyp9';

   emailjs.sendForm(serviceID, templateID, this)
    .then(() => {
      btn.value = 'Sent!'
      setTimeout(sendReset, 5000)
    }, (err) => {
      btn.value = 'Send Email';
      alert(JSON.stringify(err));
    });
});
