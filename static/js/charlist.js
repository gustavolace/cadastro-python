document.querySelectorAll(".personagem").forEach( (item) => {
  item.addEventListener("click", () => {
    let charId = item.getAttribute("data-charid");
    window.location.href = `/char/${charId}`;
  });
});
