let modalContainer;

function openModal(route) {
  if (modalContainer !== undefined) {
    modalContainer.remove();
  }

  let modalContent = document.getElementById("modalContent");
  modalContainer = document.createElement("div");
  modalContainer.classList.add("modal-container");

  fetch(route)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok.");
      }
      return response.text();
    })
    .then((html) => {
      modalContainer.innerHTML = html;
      modalContent.appendChild(modalContainer);
      modalContent.style.display = "block";

      let span = document.querySelector(".close");
      span.addEventListener("click", () => {
        modalContainer.remove();
      });
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
      alert("Houve um problema");
    });

  window.addEventListener("click", (event) => {
    let logindiv = document.querySelector(".modal");

    if (event.target === modalContainer || event.target === logindiv) {
      modalContainer.remove();
    }
  });
}

async function checkUsernameAvailability() {
  const username = document.getElementById('username').value

  const response = await fetch(`/username/${username}`)
  const data = await response.json()

  if(!data.available) {
    alert("Nome de usuário já está em uso.");
  }
}
