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
