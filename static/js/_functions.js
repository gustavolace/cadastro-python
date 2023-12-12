import { colors, colorKey } from "./color-link-select.js";

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

export function sendChar(form, fetch_route, fetch_id, charlist_id) {
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(this);

    fetch(`${fetch_route}/${fetch_id}`, {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        const message = data.message;
        alert(message);
        return message;
      })
      .then((message) => {
        window.location.href = `/charlist/${charlist_id}`;
      })
      .catch((error) => {
        console.error("Erro:", error);
      });
  });
}

export function getID(){
  const url = window.location.href;
  const url_spit = url.split("/");
  const id = url_spit[url_spit.length - 1];
  return id
} 