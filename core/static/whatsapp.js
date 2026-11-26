const BUSINESS_NUMBER = "2349019279152"; 

function sendToWhatsApp(text) {
  const url = "https://wa.me/" + BUSINESS_NUMBER + "?text=" + encodeURIComponent(text);
  window.open(url, "_blank");
}

document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("message").value;

  sendToWhatsApp(
    "Hello Deboss, my name is " + name + ".\n" +
    "Email: " + email + "\n\n" + message
  );
});