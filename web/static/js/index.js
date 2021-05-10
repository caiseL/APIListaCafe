var flkty = new Flickity(".main-gallery", {
  // options
  cellAlign: "left",
  contain: true,
  pageDots: false,
  wrapAround: true,
});

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight) {
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}

/* 
A
*/

const form = document.getElementById("formulario_receta");

form.addEventListener("submit", async function (e) {
  e.preventDefault();
  const formData = new FormData(form).entries();
  const response = await fetch(
    "https://lista-cafes-api.herokuapp.com/recetas/agregar/?format=json",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(Object.fromEntries(formData)),
    }
  );
  console.log(response);

  const result = await response.json();
  console.log(result);
});
