function carregarLogin() {
  fetch("/login")
    .then((response) => response.text())
    .then((html) => {
      document.getElementById("secaoLogin").innerHTML = html;
    })
    .catch((error) => {
      console.error("Ocorreu um erro ao carregar o HTML de login:", error);
    });
}
