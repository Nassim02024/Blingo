// card order 
document.addEventListener('DOMContentLoaded', function () {

  let checking = document.querySelector('.checking')
  let names = document.querySelectorAll('.name-of-product')
  let prices = document.querySelectorAll('.price')

  // get data from local storage
  let arrayProduct = JSON.parse(localStorage.getItem('arrayProduct')) || [];

  arrayProduct.forEach(element => {
    let productName = element.productName
    let productPrice = element.prices
    let productPid = element.pid
    let vendorVid = element.vid
    let qun = element.qun


    
  
    
    let html =`
    <div style="display: flex; width: 100%; justify-content: space-around;"> 
      <div class="text-muted"  >
      <h6>name </h6>
        <p style="display:none;" >${vendorVid}</p>
        <p style="display:none;" > ${productPid}</p>
        
          <span class="text-dark">
          <p>${productName}</p>
        </span>
      </div>
      
      <div class="text-muted" >
        <h6>Color </h6>
        <span class=" text-dark">
        <p></p>
      </span>
      </div>

      <div class="text-muted" >
        <h6>quantity </h6>
        <span class=" text-dark">
          <p>${qun}</p>
        </span>
      </div>

      <div class="text-muted" >
        <h6>price </h6>
        <span class=" text-dark">
          <p class='price_one_product'>${productPrice}</p>
        </span>
      </div>

      <input class="inputeProductName" type="hidden" name="productName[]" value="${productName}" />
      <input class="inputPrice" type="hidden" name="price[]" value="${productPrice}" />
      <input class="input-product-id" type="hidden"  name="product_id[]" value="${productPid}" />
      <input class="input-vendor-id" type="hidden"  name="vendor_id[]" value="${vendorVid}" />
      <input class="qun" type="hidden"  name="qun[]" value="${qun}" />

    </div>
    <hr style="height:20px" />
    `
    //  document.querySelectorAll('.vendor-id') = vendorVid
    //  document.querySelectorAll('.product-id')  = productPid
    checking.innerHTML += html

    

  
  


    

    // function ordernow() {
    //   // let productElement = this.closest(".checking");
    //   // let productId = productElement.dataset.productId;
    //   // console.log(productId);

    //   let nameInputs = document.querySelectorAll('.inputeProductName')
    //   let priceInputs = document.querySelectorAll('.inputPrice')
    //   let inputProductId = document.querySelectorAll('.input-product-id')
    //   let inputvendorId = document.querySelectorAll('.input-vendor-id')
    
    //   for (let i = 0; i < productName.length; i++) {
    //     nameInputs[i].value = productName[i].innerText;
    //     priceInputs[i].value = productPrice[i].innerText;
    //     inputProductId[i].value = productPid[i].innerText;
    //     inputvendorId[i].value = productPid[i].innerText;
        
        
    //   }}
  });

  let price_one_product = document.querySelectorAll('.price_one_product')

let summary_order_tolal = document.querySelector('.summary_order_tolal')
let summary_Delivery_service = document.querySelector('.summary_Delivery_service')
let summary_order_all = document.querySelector('.summary_order_all')

let total = 0
price_one_product.forEach(element => {
  total += parseInt(element.innerText)
});

let deliveryPrice = 100.00;

if (summary_order_tolal) {
  summary_order_tolal.innerText = total + ' Dz';
} else {
  console.warn("⚠️" + " summary_order_tolal is not defined");
}

summary_Delivery_service.innerText = deliveryPrice + ' Dz';
summary_order_all.innerText = (total + deliveryPrice) + ' Dz';

})