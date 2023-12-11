const form = document.getElementById("charForm");


form.addEventListener("submit", function (event) {
event.preventDefault()
  const formData = new FormData(this);
  const url = window.location.href;
  const url_spit = url.split("/"); 
  const id = url_spit[url_spit.length - 1]; 

  fetch(`/register/newchar/${id}`, {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      const message = data.message;
      alert(message);
      return message;
    })
    .then((message) => {
      window.location.href = `/charlist/${id}`;
    })
    .catch((error) => {
      console.error("Erro:", error);
    });
})