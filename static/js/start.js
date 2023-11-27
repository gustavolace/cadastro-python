function openModal() {
  let modalContent = document.getElementById("modalContent");
  let modalContainer = document.createElement("div");
  modalContainer.classList.add("modal-container");

  fetch("/signin")
    .then((response) => response.text())
    .then((html) => {
      modalContainer.innerHTML = html;
      modalContent.appendChild(modalContainer);
      modalContent.style.display = "block";
    })
    .catch((error) => console.error("Erro ao carregar o modal:", error));
}

function closeModal() {
  let modalContent = document.getElementById("modalContent");
  modalContent.innerHTML = "";
  modalContent.style.display = "none";
}

document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
  });
