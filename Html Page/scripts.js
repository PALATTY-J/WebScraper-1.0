let addLinkButton = document.querySelector("#addLink");
let inputUrl = document.querySelector("#inputUrl");
let listContainer = document.querySelector("#listContainer");
listArray = [];

addLinkButton.addEventListener("click", () => {
  ipValue = inputUrl.value.toString();
  tagScript = `<div style="display: flex;
justify-content: center; border: 1px solid;border-radius: 10px;padding: 1rem;margin-bottom: 1rem;">
<div style="align-self: center; padding: .5rem;padding-right: 2rem;">
    <span>${ipValue}</span>
</div>
<div style="padding-right: 1rem;">
    <button onclick="deleteFromArray('${ipValue}')"><span class="material-icons">
        delete
    </span></button>
</div>
<a style="display: block;text-decoration: none;" target="__blank" href="${ipValue}">
                <button><span class="material-icons">
                        link
                    </span></button>
            </a>  
</div>`;
  listContainer.innerHTML += tagScript;
  inputUrl.value = "";
  listArray.push(ipValue);
});

deleteFromArray = (value) => {
  listArray.splice(listArray.indexOf(value.toString()), 1);
  innerText = ``;
  listContainer.innerHTML = "";
  listArray.forEach((value) => {
    tagScript = `<div style="display: flex;
justify-content: center; border: 1px solid;border-radius: 10px;padding: 1rem;margin-bottom: 1rem;">
<div style="align-self: center; padding: .5rem;padding-right: 2rem;">
    <span>${value}</span>
</div>
<div style="padding-right: 1rem;">
    <button onclick="deleteFromArray('${value}')"><span class="material-icons">
        delete
    </span></button>
</div>
<a style="display: block;text-decoration: none;" target="__blank" href="${ipValue}">
                <button><span class="material-icons">
                        link
                    </span></button>
            </a>  
</div>`;
    innerText += tagScript;
  });
  listContainer.innerHTML += innerText;
};

downloadCSV = () => {
  var hiddenElement = document.createElement("a");
  hiddenElement.href = "data:text/csv;charset=utf-8," + encodeURI(listArray.join(','));
  hiddenElement.target = "_blank";
  //provide the name for the CSV file to be downloaded
  hiddenElement.download = "Link List.csv";
  hiddenElement.click();
};
