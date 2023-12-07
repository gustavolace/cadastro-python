import { colors, colorKey } from "./char.js";

export function fetchCharacterImages(hairColor, skinColor) {
  return fetch("/img")
    .then((res) => res.json())
    .then((links) => {
      skinColor = skinColor ?? colorKey.skinColor;
      hairColor = hairColor ?? colorKey.hairColor;

      const defaultHairColor = hairColor || "yellow";
      const defaultSkinColor = skinColor || "bege";
      let linkColor = defaultHairColor + "_" + defaultSkinColor;

      return links[linkColor];
    })
    .catch((e) => {
      console.error("Erro ao buscar imagens:", e);
      return null;
    });
}

export function applyImageToCharacter(link, divImg) {
  divImg.src = link;
}

export function hrefChange(tag, number, route) {
  document.getElementsByTagName(tag)[number].addEventListener("click", () => {
    window.location.href = route;
  });
}

export function handleColorSelection(
  selectedColor,
  type,
  characterImageElement
) {
  if (type === "hair") {
    colors.hairColor = selectedColor;
  } else if (type === "skin") {
    colors.skinColor = selectedColor;
  }
  fetchCharacterImages(colors.hairColor, colors.skinColor).then((imageLink) => {
    applyImageToCharacter(imageLink, characterImageElement);
  });
}
