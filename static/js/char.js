import {
  handleColorSelection,
} from "./_functions.js";

export const colors = {
  hairColor: null,
  skinColor: null,
};

const corSamples = document.querySelectorAll(".cor-sample");
const skinSamples = document.querySelectorAll(".skin-sample");
let characterImageElement = document.querySelector(".character-image img");

/* document.addEventListener("DOMContentLoaded", () => {
  let skinRadios = document.querySelectorAll(
    'input[type="radio"][name=skinColor]'
  );
  let hairRadios = document.querySelectorAll(
    'input[type="radio"][name=corCabelo]'
  );
  eachRadio(skinRadios, "skin");
  eachRadio(hairRadios, "hair");



  function eachRadio(radio, type) {
    radio.forEach(function (radio) {
      let spanColor = radio.nextElementSibling.getAttribute("data-cor");
      if (radio.checked) {
        handleColorSelection(spanColor, type, characterImageElement);
      }
    });
  }
});
 */

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
