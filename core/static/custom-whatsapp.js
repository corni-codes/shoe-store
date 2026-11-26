const CUSTOM_BUSINESS_NUMBER = "2349019279152";

document.getElementById("customForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const item = document.getElementById("categorie").value.trim();
  const color = document.getElementById("color").value.trim();
  const unit = document.getElementById("unit").value.trim();
  const description = document.getElementById("descriptions").value.trim();

  let message = "Hello Deboss, I'd like a custom order.\n\n";
  message += "Name: " + name + "\n";
  if (email) message += "Email: " + email + "\n";
  if (item) message += "Item: " + item + "\n";
  if (color) message += "Colour: " + color + "\n";
  if (unit) message += "Quantity: " + unit + "\n";
  message += "\nDesign idea:\n" + description;

  const url = "https://wa.me/" + CUSTOM_BUSINESS_NUMBER + "?text=" + encodeURIComponent(message);
  window.open(url, "_blank");
});