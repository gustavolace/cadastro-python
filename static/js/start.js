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

      let span = document.querySelector(".close")
      span.addEventListener("click", () => {
        modalContainer.remove()
      })
    })

    window.addEventListener("click", (event) => {
      let logindiv = document.querySelector(".modal")
  
      if (event.target === modalContainer || event.target === logindiv) {
        modalContainer.remove()
      }
    });
  }
