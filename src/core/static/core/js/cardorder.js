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
    let lng = element.lng
    let lat = element.lat
    console.log(lng)
  
    
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
      <input class="lng" type="hidden"  name="lng" value="${lng}" />
      <input class="lat" type="hidden"  name="lat" value="${lat}" />
    

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



let total = 0
price_one_product.forEach(element => {
  total += parseInt(element.innerText)
}); 


const select = document.querySelector('.country');
const summary_Delivery_service = document.querySelector('.summary_Delivery_service');
const summary_order_tolal = document.querySelector('.summary_order_tolal');
const summary_order_all = document.querySelector('.summary_order_all');
const end_Delivery_service = document.querySelector('.end_Delivery_service');
const form = document.querySelector('form');

let hiddenInput = document.createElement('input');
hiddenInput.type = 'hidden';
hiddenInput.name = 'send_delivry_service';
form.appendChild(hiddenInput);


const deliveryPrices = {
  'الزاوية العابدية': 100,
  'تبسبست': 100,
  'حي الرمال': 200,
  'حي المستقبل': 150,
  'دراع البارود': 250,
  'حي 360 مسكن': 200,
  'حي 450 مسكن': 200,
  'حي 700 مسكن': 200,
  'حي 300 مسكن': 200,
  'حي الأمل': 200,
  'حي الفتح': 200,
  'حي النصر': 200,
  'حي السلام': 200,
  'حي القدس': 200,
  'حي النسيم': 200,
  'حي الواحات': 200,
  'حي الورود': 200,
  'النزلة': 200,
  'لبدوع': 200,
  'تماسين': 350,
  'لمقارين': 250,
  'بلدة عمر': 300,
  'مقر': 350,
  'بلدة سيدي سليمان': 300,
  'القوق': 400
};

select.addEventListener('change', () => {
  const selectedValue = select.value;
  const deliveryPrice = deliveryPrices[selectedValue] || 0;

  summary_order_tolal.innerText = total + ' Dz';
  summary_Delivery_service.innerText = deliveryPrice + ' Dz';
  summary_order_all.innerText = (total + deliveryPrice) + ' Dz';
  end_Delivery_service.innerText = deliveryPrice + ' Dz'; // ✅ تم التعديل

  hiddenInput.value = deliveryPrice;

  console.log("🚚 تم تحديث سعر التوصيل:", deliveryPrice);
});

})