import {
  fetchCharacterImages,
  applyImageToCharacter,
} from "./_functions.js";

const corSamples = document.querySelectorAll(".cor-sample");
const skinSamples = document.querySelectorAll(".skin-sample");
let characterImageElement = document.querySelector(".character-image img");

selectColor(corSamples, "hair");
selectColor(skinSamples, "skin");

let hairColor;
let skinColor;

 function selectColor(colorSamples, type) {
  let selectedColor;
  colorSamples.forEach((sample) => {
    sample.addEventListener("click", () => {
      selectedColor = sample.getAttribute("data-cor");
      if (type === "hair") {
        hairColor = selectedColor;
      } else if (type === "skin") {
        skinColor = selectedColor;
      }


      fetchCharacterImages(hairColor, skinColor).then((imageLink) => {
        if (imageLink) {
          applyImageToCharacter(imageLink, characterImageElement);
        }
      });
    });
  });
}
