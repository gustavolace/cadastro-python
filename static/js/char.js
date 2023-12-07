import {
  handleColorSelection,
} from "./_functions.js";

export const colors = {
  hairColor: null,
  skinColor: null,
};
const characterImage = document.querySelector(".character-image img");
export const colorKey = {
  hairColor: characterImage.getAttribute("data-hair"),
  skinColor: characterImage.getAttribute("data-skin")
}


const corSamples = document.querySelectorAll(".cor-sample");
const skinSamples = document.querySelectorAll(".skin-sample");
let characterImageElement = document.querySelector(".character-image img");

selectColor(corSamples, "hair");
selectColor(skinSamples, "skin");

function selectColor(colorSamples, type) {
  colorSamples.forEach((sample) => {
    let selectedColor = sample.getAttribute("data-cor");
    sample.addEventListener("click", () => {
      handleColorSelection(selectedColor, type, characterImageElement);
    });
  });
}
