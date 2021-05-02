let url = "http://127.0.0.1:8000/api";

let table = document.querySelector("table");

function generateTableHead(table, data) {
  let thead = table.createTHead();
  let row = thead.insertRow();
  for (let key in data) {
    let th = document.createElement("th");
    let text = document.createTextNode(key);
    th.appendChild(text);
    row.appendChild(th);
  }
}

function generateTable(table, products) {
  for (let product of products) {
    let row = table.insertRow();
    for (key in product) {
      let cell = row.insertCell();
      let _child = null;
      if (key === "image") {
        _child = document.createElement("img");
        _child.classList.add("image");
        _child.src = product[key];
      } else {
        _child = document.createTextNode(product[key]);
      }
      cell.appendChild(_child);
    }
  }
}

function fetchAndCreate() {
  fetch(`${url}/product/`)
    .then((response) => response.json())
    .then((products) => {
      generateTableHead(table, products[0]);
      generateTable(table, products);
    })
    .catch((e) => console.log(e));
}
