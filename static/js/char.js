import { colorKey } from "./color-link-select.js";
import { sendChar, getID } from "./_functions.js";

let skinRadios = document.querySelectorAll(
  'input[type="radio"][name="skinColor"]'
);
let hairRadios = document.querySelectorAll(
  'input[type="radio"][name="hairColor"]'
);
radio_check(skinRadios, colorKey.skinColor);
radio_check(hairRadios, colorKey.hairColor);

function radio_check(array, color) {
  array.forEach((radio) => {
    if (radio.value === color) {
      radio.checked = true;
    }
  });
}

const charid = getID()
const form = document.querySelector("form");
sendChar(form, "/char/update", charid, userid);
