document.addEventListener('DOMContentLoaded', function () {

    const checking = document.querySelector('.checking');
    const form = document.querySelector('form');
    
    // 1. جلب البيانات من local storage
    let arrayProduct = JSON.parse(localStorage.getItem('arrayProduct')) || [];
    let totalProductsPrice = 0;

    // تنظيف المحتوى قبل البدء
    if (checking) {
        checking.innerHTML = ""; 
    }

    if (arrayProduct.length > 0) {
        // نأخذ الإحداثيات من أول منتج في السلة كإحداثيات عامة للطلب
        const commonLng = arrayProduct[0].lng || "";
        const commonLat = arrayProduct[0].lat || "";

        arrayProduct.forEach(element => {
            let productName = element.productName || "منتج غير مسمى";
            let productPrice = parseFloat(element.prices) || 0;
            let productPid = element.pid || "";
            
            // ملاحظة: تأكد أن صفحة المنتج تخزن 'vid' بشكل صحيح
            let vendorVid = element.vid || ""; 
            let qun = parseInt(element.qun) || 1;

            totalProductsPrice += (productPrice);

            let html = `
            <div class="product-item" style="display: flex; width: 100%; justify-content: space-around; align-items: center; margin-bottom: 10px;"> 
              <div class="text-muted">
                <h6 style="font-size: 12px;">المنتج</h6>
                <p class="text-dark" style="font-weight: bold;">${productName}</p>
              </div>
              
              <div class="text-muted">
                <h6 style="font-size: 12px;">الكمية</h6>
                <p class="text-dark">${qun}</p>
              </div>

              <div class="text-muted">
                <h6 style="font-size: 12px;">السعر</h6>
                <p class="text-dark price_one_product">${productPrice} د.ج</p>
              </div>

              <input type="hidden" name="productName[]" value="${productName}" />
              <input type="hidden" name="price[]" value="${productPrice}" />
              <input type="hidden" name="product_id[]" value="${productPid}" />
              <input type="hidden" name="vendor_id[]" value="${vendorVid}" />
              <input type="hidden" name="qun[]" value="${qun}" />
            </div>
            <hr />
            `;
            checking.innerHTML += html;
        });

        // إدراج الإحداثيات مرة واحدة فقط للطلب بالكامل
        let locationHtml = `
            <input type="hidden" name="lng" value="${commonLng}" />
            <input type="hidden" name="lat" value="${commonLat}" />
        `;
        checking.innerHTML += locationHtml;

    } else {
        if (checking) checking.innerHTML = "<p class='alert alert-warning text-center'>سلة التسوق فارغة</p>";
    }

    // 2. إعدادات حساب التوصيل والإجمالي
    const select = document.querySelector('.country');
    const summary_Delivery_service = document.querySelector('.summary_Delivery_service');
    const summary_order_tolal = document.querySelector('.summary_order_tolal');
    const summary_order_all = document.querySelector('.summary_order_all');
    const end_Delivery_service = document.querySelector('.end_Delivery_service');

    // إنشاء حقل مخفي لسعر التوصيل ليتم إرساله للـ Django إذا لم يكن موجوداً
    let hiddenInput = document.querySelector('input[name="send_delivry_service"]');
    if (!hiddenInput && form) {
        hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = 'send_delivry_service';
        form.appendChild(hiddenInput);
    }

    const deliveryPrices = {
        'الزاوية العابدية': 100, 'تبسبست': 100, 'حي الرمال': 200, 'حي المستقبل': 150,
        'دراع البارود': 250, 'حي 360 مسكن': 200, 'حي 450 مسكن': 200, 'حي 700 مسكن': 200,
        'حي 300 مسكن': 200, 'حي الأمل': 200, 'حي الفتح': 200, 'حي النصر': 200,
        'حي السلام': 200, 'حي القدس': 200, 'حي النسيم': 200, 'حي الواحات': 200,
        'حي الورود': 200, 'النزلة': 200, 'لبدوع': 200, 'تماسين': 350,
        'لمقارين': 250, 'بلدة عمر': 300, 'مقر': 350, 'بلدة سيدي سليمان': 300, 'القوق': 400
    };

    // وظيفة تحديث الأسعار
    function updateTotals() {
        const selectedValue = select ? select.value : "";
        const deliveryPrice = deliveryPrices[selectedValue] || 0;

        if (summary_order_tolal) summary_order_tolal.innerText = totalProductsPrice + ' د.ج';
        if (summary_Delivery_service) summary_Delivery_service.innerText = deliveryPrice + ' د.ج';
        if (summary_order_all) summary_order_all.innerText = (totalProductsPrice + deliveryPrice) + ' د.ج';
        if (end_Delivery_service) end_Delivery_service.innerText = deliveryPrice + ' د.ج';

        if (hiddenInput) hiddenInput.value = deliveryPrice;
    }

    if (select) {
        select.addEventListener('change', updateTotals);
        // تنفيذ التغيير مرة واحدة عند التحميل الابتدائي لتحديد سعر أول منطقة مختارة
        updateTotals();
    }
});