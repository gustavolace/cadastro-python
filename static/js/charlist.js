function alerta(event) {
  event.stopPropagation();
  alert("hello world");
}

let liElements = document.querySelectorAll(".personagem");
liElements.forEach((char) => {
  char.addEventListener("click", () => {
    window.location.href = "/char";
  });
});
