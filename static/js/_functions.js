export function fetchCharacterImages(hairColor, skinColor) {
  return fetch("/img")

    .then((res) => res.json())
    .then((links) => {

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
  divImg.src = link
}

export function hrefChange(tag, number, route) {
  document
    .getElementsByTagName(tag)[number]
    .addEventListener("click", () => {
      window.location.href = route;
    });
}
