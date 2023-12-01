const corSamples = document.querySelectorAll(".cor-sample");
const skinSamples = document.querySelectorAll(".skin-sample");

let hairColor;
let skinColor;

colorSelect(corSamples, "hair");
colorSelect(skinSamples, "skin");

function colorSelect(color, type) {
  color.forEach((sample) => {
    sample.addEventListener("click", () => {
      let selectColor = sample.getAttribute("data-cor");
      console.log(`Cor selecionada para ${type}: ${selectColor}`);

      if (type === "hair") {
        hairColor = selectColor;
      } else if (type === "skin") {
        skinColor = selectColor;
      }
      let divImg = document.querySelector(".character-image");
      const defaultHairColor = hairColor || "yellow";
      const defaultSkinColor = skinColor || "bege";
      divImg.innerHTML = `
  <img src="/static/img/${defaultHairColor}-${defaultSkinColor}.png" alt="Imagem do personagem">
    `;
    });
  });
}
