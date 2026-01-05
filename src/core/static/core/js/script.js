(function($) {
  "use strict";

  var initPreloader = function() {
    $(document).ready(function($) {
    var Body = $('body');
        Body.addClass('preloader-site');
    });
    $(window).load(function() {
        $('.preloader-wrapper').fadeOut();
        $('body').removeClass('preloader-site');
    });
  }

  var initChocolat = function() {
    Chocolat(document.querySelectorAll('.image-link'), {
      imageSize: 'contain',
      loop: true,
    })
  }

  var initSwiper = function() {
    $('.slideshow').each(function(){
      var space = $(this).attr('data-space') ? $(this).attr('data-space') : 0 ;
      var col = $(this).attr('data-col');
      if ( typeof col == "undefined" || !col) {
        col = 1;
      }

      var swiper = new Swiper(".slideshow", {
        slidesPerView: col,
        spaceBetween: space,
        speed: 1000,
        loop: true,
        navigation: {
          nextEl: '.icon-arrow-right',
          prevEl: '.icon-arrow-left',
        },
        pagination: {
          el: ".slideshow-swiper-pagination",
          clickable: true,
        },
      });
    });

    var category_swiper = new Swiper(".category-carousel", {
      slidesPerView: 8,
      spaceBetween: 30,
      speed: 500,
      navigation: {
        nextEl: ".category-carousel-next",
        prevEl: ".category-carousel-prev",
      },
      breakpoints: {
        0: { slidesPerView: 2 },
        768: { slidesPerView: 3 },
        991: { slidesPerView: 5 },
        1500: { slidesPerView: 8 },
      }
    });

    var brand_swiper = new Swiper(".brand-carousel", {
      slidesPerView: 4,
      spaceBetween: 30,
      speed: 500,
      navigation: {
        nextEl: ".brand-carousel-next",
        prevEl: ".brand-carousel-prev",
      },
      breakpoints: {
        0: { slidesPerView: 2 },
        768: { slidesPerView: 2 },
        991: { slidesPerView: 3 },
        1500: { slidesPerView: 4 },
      }
    });

    var products_swiper = new Swiper(".products-carousel", {
      slidesPerView: 5,
      spaceBetween: 30,
      speed: 500,
      navigation: {
        nextEl: ".products-carousel-next",
        prevEl: ".products-carousel-prev",
      },
      breakpoints: {
        0: { slidesPerView: 1 },
        768: { slidesPerView: 3 },
        991: { slidesPerView: 4 },
        1500: { slidesPerView: 5 },
      }
    });

    var thumb_slider = new Swiper(".product-thumbnail-slider", {
      slidesPerView: 5,
      spaceBetween: 20,
      direction: "vertical",
      breakpoints: {
        0: { direction: "horizontal" },
        992: { direction: "vertical" },
      },
    });

    var large_slider = new Swiper(".product-large-slider", {
      slidesPerView: 1,
      spaceBetween: 0,
      effect: 'fade',
      thumbs: { swiper: thumb_slider },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });
  }

  var initTextFx = function () {
    $('.txt-fx').each(function () {
      var newstr = '';
      var count = 0;
      var delay = 100;
      var stagger = 10;
      var words = this.textContent.split(/\s/);
      var arrWords = new Array();
      
      $.each( words, function( key, value ) {
        newstr = '<span class="word">';
        for ( var i = 0, l = value.length; i < l; i++ ) {
          newstr += "<span class='letter' style='transition-delay:"+ ( delay + stagger * count ) +"ms;'>"+ value[ i ] +"</span>";
          count++;
        }
        newstr += '</span>';
        arrWords.push(newstr);
        count++;
      });
      this.innerHTML = arrWords.join("<span class='letter' style='transition-delay:"+ delay +"ms;'>&nbsp;</span>");
    });
  }

  var initProductQty = function(){
    $('.product-qty').each(function(){
      var $el_product = $(this);
      $el_product.find('.quantity-right-plus').click(function(e){
        e.preventDefault();
        var quantity = parseInt($el_product.find('.quantity').val());
        $el_product.find('.quantity').val(quantity + 1);
      });
      $el_product.find('.quantity-left-minus').click(function(e){
          e.preventDefault();
          var quantity = parseInt($el_product.find('.quantity').val());
          if(quantity>0){
            $el_product.find('.quantity').val(quantity - 1);
          }
      });
    });
  }

  var initJarallax = function() {
    jarallax(document.querySelectorAll(".jarallax"));
    jarallax(document.querySelectorAll(".jarallax-keep-img"), { keepImg: true });
  }

  $(document).ready(function() {
    initPreloader();
    initTextFx();
    initSwiper();
    initProductQty();
    initJarallax();
    initChocolat();
  });

  $(document).ready(function() {
    const $app = $('.app');
    let animation = true;
    let curSlide = 1;
    let scrolledUp, nextSlide;
    
    let pagination = function(slide, target) {
      animation = true;
      if (target === undefined) {
        nextSlide = scrolledUp ? slide - 1 : slide + 1;
      } else {
        nextSlide = target;
      }
      $('.pages__item--' + nextSlide).addClass('page__item-active');
      $('.pages__item--' + slide).removeClass('page__item-active');
      $app.toggleClass('active');
      setTimeout(function() { animation = false; }, 3000)
    }
    
    let navigateDown = function() {
      if (curSlide > 1) return;
      scrolledUp = false;
      pagination(curSlide);
      curSlide++;
    }
  
    let navigateUp = function() {
      if (curSlide === 1) return;
      scrolledUp = true;
      pagination(curSlide);
      curSlide--;
    }
  
    setTimeout(function() { $app.addClass('initial'); }, 1500);
    setTimeout(function() { animation = false; }, 4500);
    
    $(document).on('mousewheel DOMMouseScroll', function(e) {
      var delta = e.originalEvent.wheelDelta;
      if (animation) return;
      if (delta > 0 || e.originalEvent.detail < 0) { navigateUp(); } else { navigateDown(); }
    });
  
    $(document).on("click", ".pages__item:not(.page__item-active)", function() {
      if (animation) return;
      let target = +$(this).attr('data-target');
      pagination(curSlide, target);
      curSlide = target;
    });
  });

})(jQuery);

// --- Normal JS (Vanila JS) ---

// =====================================================================
// كود الجافاسكريبت الرئيسي للسلة (CARD_ORDER.JS) - النسخة الأخيرة
// =====================================================================

// ✅ 1. تعريف arrayProduct كمتغير عام هنا (متاح لجميع الدوال)
let arrayProduct = JSON.parse(localStorage.getItem('arrayProduct')) || [];

// ✅ مُحدِّد آمن لقائمة المنتجات (يجب أن يكون هذا ID في HTML)
const PRODUCTS_CONTAINER_SELECTOR = '#products-list-container'; 

// ------------------------------------------------
// 2. الدوال المساعدة: الرسم والتحديث والتنبيهات (معرّفة عالمياً)
// ------------------------------------------------

/**
 * دالة تحديث السعر الإجمالي
 */
function updateTotalPrice() {
    let total = arrayProduct.reduce((sum, item) => sum + parseFloat(item.prices), 0);
    
    // ✅ نبحث فقط عن الكلاس .totals-price في أي مكان
    let totalElement = document.querySelector('.totals-price'); 
    
    if (totalElement) {
        totalElement.innerHTML = total  + ' Dz';
        console.log("تم العثور على العنصر وتحديث الإجمالي بنجاح:", total);
    } else {
        console.error("العنصر الذي يحمل الكلاس '.totals-price' لم يتم العثور عليه. (تحقق من HTML)");
    }
}

/**
 * دالة تحديث عداد المنتجات في السلة
 */
function updateCount() {
    let count = arrayProduct.length;
    document.querySelectorAll('.badge, .count-for-card-icon').forEach(el => {
        el.innerHTML = count;
    });
}

/**
 * دالة إظهار التنبيهات المؤقتة
 */
function showAlert(message, bg) {
    const alertBox = document.querySelector(".alerts");
    if (!alertBox) return;
    alertBox.querySelector("p").textContent = message;
    alertBox.style.background = bg;
    alertBox.style.visibility = "visible";
    setTimeout(() => { alertBox.style.visibility = "hidden"; }, 2000);
}

/**
 * دالة رسم عنصر منتج واحد في قائمة السلة
 */
function renderStoredItem(item) {
    // ✅ استخدام ID آمن للرسم
    let listGroup = document.querySelector(PRODUCTS_CONTAINER_SELECTOR); 
    if (!listGroup) return;

    let li = document.createElement('li');
    li.className = 'list-group-item d-flex align-items-center justify-content-between lh-sm list-group-item-card';
    li.innerHTML = `
        <div>
            <h6 class="my-0" style="font-size: 12px;">${item.productName}</h6>
            <small class="text-body-secondary" style="font-size: 10px;">${item.category || ""}</small>
        </div>
<div style="display: flex; justify-content: center; align-items: center; "> 
            <p style="font-size: 8px; margin-right: 2px; margin-bottom: 0;">Dz</p>
            <h4 class="text-body-secondary price-for-one" style="margin-top: 6px; font-size: 14px; margin-bottom: 0;">${item.prices}</h4>
        </div>
        <p style="font-size: 8px;margin-right: 10px; margin-bottom: 0;padding:5px;">x${item.qun}</p>

        <button class="btn btn-danger delete-item-pro" style="height: fit-content;" type="button" data-pid="${item.pid}">
            <i class="bi bi-trash"></i>
        </button>
    `;

    listGroup.appendChild(li);
    
    // إضافة معالج حدث الحذف
    li.querySelector('.delete-item-pro').addEventListener('click', function () {
        arrayProduct = arrayProduct.filter(p => p.pid !== item.pid);
        localStorage.setItem("arrayProduct", JSON.stringify(arrayProduct));
        initializeCartDisplay();
    });
}


// =====================================================================
// الدالة الموحدة للرسم والتحديث (معرّفة عالمياً)
// =====================================================================
const initializeCartDisplay = () => {
    arrayProduct = JSON.parse(localStorage.getItem('arrayProduct')) || [];

    // 2. تحديث قائمة المنتجات (الرسم)
    const listGroup = document.querySelector(PRODUCTS_CONTAINER_SELECTOR); 
    if (listGroup) {
        listGroup.innerHTML = ''; 
        arrayProduct.forEach(productData => {
             renderStoredItem(productData);
        });
    }

    // 3. تحديث الإجماليات والعدادات
    updateTotalPrice(); 
    updateCount();

    // 4. تحديث حالة الأزرار (إذا كانت موجودة)
    if (typeof updateCartUIStatus === 'function') {
        updateCartUIStatus();
    }
};

// ------------------------------------------------
// 3. منطق DOMContentLoaded (التحميل والإضافة) - مرة واحدة فقط
// ------------------------------------------------
document.addEventListener('DOMContentLoaded', function () {
    let currentVendorId = document.querySelector('.vendor-id')?.textContent.trim();
    
    // --- 1. منطق قيد البائع: مسح السلة عند الخروج أو التغيير ---
    if (arrayProduct.length > 0) {
        let storedVendorId = arrayProduct[0].vId;
        
        if (currentVendorId && currentVendorId !== storedVendorId) {
            localStorage.removeItem('arrayProduct');
            arrayProduct = [];
            console.log("تم مسح السلة: دخول متجر بائع آخر");
        } 
        else if (!currentVendorId) {
            localStorage.removeItem('arrayProduct');
            arrayProduct = [];
            console.log("تم مسح السلة: الخروج للصفحة الرئيسية");
        }
    }

    if (currentVendorId) {
        sessionStorage.setItem('activeVendorSession', currentVendorId);
    }

    // ✅ استدعاء الدالة الموحدة للرسم عند التحميل العادي
    initializeCartDisplay(); 
    
    // --- 2. إضافة منتج جديد (معالج النقر) ---
    document.addEventListener('click', function (e) {
        if (e.target.closest('.btn-add-card')) {
            e.preventDefault();
            
            let productCard = e.target.closest('.product-item');
            let productName = productCard.querySelector('.name-of-product')?.textContent.trim();
            let pid = productCard.querySelector('.product-pid')?.textContent.trim();
            let vId = productCard.querySelector('.vendor-id')?.textContent.trim();
            let qunInput = productCard.querySelector('.quantity-one-product');
            let qun = qunInput ? qunInput.value : 1;
            let priceText = productCard.querySelector('.price-in-pro-item')?.textContent.trim();
            
            let cleanedPrice = priceText
    .replace('Dz', '')    // إزالة رمز العملة أولاً
    .replace(/[^\d,]/g, '') // إزالة أي رموز أخرى غير الأرقام أو الفاصلة
    .replace(',', '.');   // استبدال الفاصلة (,) بالنقطة (.) قبل التحويل

let unitPrice = parseFloat(cleanedPrice) || 0;
            let totalPrice = unitPrice * parseInt(qun); 

            if (!vId || vId === "undefined") {
                console.error("معرف البائع مفقود");
                return;
            }

            if (arrayProduct.some(item => String(item.pid) === pid)) {
                showAlert("⚠️ المنتج موجود مسبقا", "#ffcdd2");
                return;
            }
            
            if (arrayProduct.length > 0 && arrayProduct[0].vId !== vId) {
                showAlert("⚠️ لا يمكن إضافة منتجات من بائعين مختلفين", "#ffcdd2");
                return;
            }


            const addProduct = (lng = null, lat = null) => {
                let productData = { 
                    productName, 
                    prices: totalPrice, 
                    pid, 
                    vId, 
                    qun, 
                    lng, 
                    lat,
                    category: productCard.querySelector('.category-of-product')?.textContent.trim() || ""
                };
                
                arrayProduct.push(productData);
                localStorage.setItem("arrayProduct", JSON.stringify(arrayProduct));
                
                initializeCartDisplay(); 
                
                showAlert("🛒 تم إضافة المنتج", "#ccff33");
            };

            const ua = navigator.userAgent || navigator.vendor || window.opera;
            const isInWebView = /FBAN|FBAV|Instagram|FB_IAB|wv/.test(ua);

            if (isInWebView) {
                addProduct();
                document.getElementById('webviewBanner')?.style.setProperty('display', 'block');
            } else if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (pos) => addProduct(pos.coords.longitude, pos.coords.latitude),
                    () => {
                        showAlert("⚠️ تعذر تحديد الموقع، تتم الإضافة بدون إحداثيات", "#ffcdd2");
                        addProduct();
                    } 
                );
            } else {
                addProduct();
            }
        }
    });

    // --- 3. البحث والتنقل (الموجود مسبقاً) ---
    let value_search = document.querySelectorAll('.value_search');
    let search_product = document.querySelector('.search_product');
    value_search.forEach(btn => {
      btn.addEventListener('click', function () {
        search_product.value = btn.textContent;
        if (window.innerWidth < 768) {
          document.querySelector('.hidd-open')?.classList.add('show');
        }
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    });

    let most_search_scroll = document.querySelector('.most_search_scroll');
    let section_most = document.querySelector('.section_most');
    if (most_search_scroll && section_most) {
      most_search_scroll.addEventListener("click", () => {
        section_most.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    }

    document.querySelector('.close-session-card')?.addEventListener('click', () => {
      document.querySelector('.hidd-open')?.classList.remove('show');
    });

    document.querySelectorAll('.btn-start').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelector('.product-tabs')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
});

// =====================================================================
// معالجة الانتقال بالصفحات (BFcache)
// =====================================================================
window.addEventListener("pageshow", function (event) {
    if (event.persisted || (performance.getEntriesByType("navigation").length > 0 && performance.getEntriesByType("navigation")[0].type === "back_forward")) {
        console.log("BFcache detected. Re-initializing cart display.");
        initializeCartDisplay(); 
    }
});