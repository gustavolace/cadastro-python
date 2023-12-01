const corSamples = document.querySelectorAll(".cor-sample");
let hairColor

colorSelect(corSamples, hairColor)

function colorSelect(corSample, selectColor) {
    corSample.forEach((sample) => {
      sample.addEventListener("click", () => {
        selectColor = sample.getAttribute("data-cor");
        console.log(`Cor selecionada: ${selectColor}`);
      });
    });
}
