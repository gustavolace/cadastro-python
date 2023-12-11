document.querySelectorAll(".personagem").forEach( (item) => {
  item.addEventListener("click", () => {
    let charId = item.getAttribute("data-charid");
    window.location.href = `/char/${charId}`;
  });
});

document
  .getElementById("criar-personagem")
  .addEventListener("click", function () {
    let userId = this.getAttribute("data-user-id");
    window.location.href = `/newchar/${userId}`;
  });

let fasfatimes = document.querySelectorAll(".fas.fa-times");
fasfatimes.forEach(element => {
  element.addEventListener('click', function (event) {
    event.stopPropagation();
    let charid = this.getAttribute("data-char-id");
    if(confirm(`Tem certeza de que deseja excluir?`)) {
      fetch(`/delete/${charid}`, {
        method: "POST",
      })
        .then((response) => response.json())
        .then((data) => {
          const message = data.message;
          alert(message);
          return message
        })
        .then((message) => {
          location.reload()
        })
    }
  })
})