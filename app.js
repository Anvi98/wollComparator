
fetch('./products.json')
.then(response => {
  return response.json();
})
.then(data => {
  const container = document.querySelector('.container');

  data.forEach(product => {
    console.log(product.name)
    const div = document.createElement('div');
    const img = document.createElement('img');
    const img_wrapper = document.createElement('div');
    const detail_wrapper = document.createElement('div');
    const nameProducts = document.createElement('h3');
    const price = document.createElement('h3');
    const delivery = document.createElement('p');
    const needle = document.createElement('p');
    const composition =  document.createElement('p');
    const button = document.createElement('button');

    div.classList.add('item');
    img.setAttribute('src', `${product.image}`);
    img.classList.add('img_item');
    img_wrapper.classList.add('img_wrapper');
    detail_wrapper.classList.add('details');
    nameProducts.innerText = product.name;
    nameProducts.classList.add('name_item');
    price.innerText = product.price;
    price.classList.add('price');
    delivery.innerText = product.delivery
    delivery.classList.add('delivery');
    needle.innerText = `NeedleSize: ${product.needleSize}`;
    needle.classList.add('needle');
    composition.innerText = product.composition;
    composition.classList.add('composition');
    button.innerText = 'Buy';

    img_wrapper.appendChild(img);
    div.appendChild(img_wrapper);
    detail_wrapper.appendChild(nameProducts);
    detail_wrapper.appendChild(price);
    detail_wrapper.appendChild(delivery);
    detail_wrapper.appendChild(needle);
    detail_wrapper.appendChild(composition);
    detail_wrapper.appendChild(button);
    div.appendChild(detail_wrapper);

    container.appendChild(div)
  });
  console.log(data);
}).catch(err => {
  // Do something for an error here
});