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

  // init Chocolat light box
	var initChocolat = function() {
		Chocolat(document.querySelectorAll('.image-link'), {
		  imageSize: 'contain',
		  loop: true,
		})
	}

  var initSwiper = function() {
    
    // swiper slider home 2
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
        0: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        991: {
          slidesPerView: 5,
        },
        1500: {
          slidesPerView: 8,
        },
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
        0: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 2,
        },
        991: {
          slidesPerView: 3,
        },
        1500: {
          slidesPerView: 4,
        },
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
        0: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 3,
        },
        991: {
          slidesPerView: 4,
        },
        1500: {
          slidesPerView: 5,
        },
      }
    });

    // product single page
    var thumb_slider = new Swiper(".product-thumbnail-slider", {
      slidesPerView: 5,
      spaceBetween: 20,
      // autoplay: true,
      direction: "vertical",
      breakpoints: {
        0: {
          direction: "horizontal"
        },
        992: {
          direction: "vertical"
        },
      },
    });

    var large_slider = new Swiper(".product-large-slider", {
      slidesPerView: 1,
      // autoplay: true,
      spaceBetween: 0,
      effect: 'fade',
      thumbs: {
        swiper: thumb_slider,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });
  }

  // Animate Texts
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

  // input spinner
  var initProductQty = function(){

    $('.product-qty').each(function(){
      var $el_product = $(this);
      var quantity = 0;
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

  // init jarallax parallax
  var initJarallax = function() {
    jarallax(document.querySelectorAll(".jarallax"));

    jarallax(document.querySelectorAll(".jarallax-keep-img"), {
      keepImg: true,
    });
  }

  // document ready
  $(document).ready(function() {
    
    initPreloader();
    initTextFx();
    initSwiper();
    initProductQty();
    initJarallax();
    initChocolat();

  }); // End of a document



  // slider
  $(document).ready(function() {
    const $app = $('.app');
    const $img = $('.app__img');
    const $pageNav1 = $('.pages__item--1');
    const $pageNav2 = $('.pages__item--2');
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
      setTimeout(function() {
        animation = false;
      }, 3000)
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
  
    setTimeout(function() {
      $app.addClass('initial');
    }, 1500);
  
    setTimeout(function() {
      animation = false;
    }, 4500);
    
    $(document).on('mousewheel DOMMouseScroll', function(e) {
      var delta = e.originalEvent.wheelDelta;
      if (animation) return;
      if (delta > 0 || e.originalEvent.detail < 0) {
        navigateUp();
      } else {
        navigateDown();
      }
    });
  
    $(document).on("click", ".pages__item:not(.page__item-active)", function() {
      if (animation) return;
      let target = +$(this).attr('data-target');
      pagination(curSlide, target);
      curSlide = target;
    });
   });

})(jQuery);

// normel JS


document.addEventListener('DOMContentLoaded', function () {
  // --- 1. تعريف البائع والسلة ---
  let currentVendorId = document.querySelector('.vendor-id')?.textContent.trim();
  let arrayProduct = JSON.parse(localStorage.getItem('arrayProduct')) || [];

  if (arrayProduct.length > 0 && currentVendorId && arrayProduct[0].vId !== currentVendorId) {
    localStorage.removeItem('arrayProduct');
    arrayProduct = [];
    location.reload();
    return;
  }

  // --- 2. رسم المنتجات من التخزين عند التحميل ---
  // ملاحظة: قمت بتعديل هذه الجزئية لتعمل بالـ PID بدلاً من الـ index فقط
  arrayProduct.forEach((storedProduct) => {
    renderStoredItem(storedProduct);
  });

  // --- 3. الحدث الرئيسي (إضافة منتج) باستخدام Event Delegation ---
  // هذه الطريقة تضمن عمل الزر حتى لو تغير الـ HTML أو كان المنتج داخل Loop مختلف
  document.addEventListener('click', function (e) {
    if (e.target.closest('.btn-add-card')) {
      e.preventDefault();
      
      // العثور على حاوية المنتج الأقرب (الـ Card)
      let productCard = e.target.closest('.product-item');
      
      // جلب البيانات بدقة من داخل الكارد نفسه وليس عبر Index عام
      let productName = productCard.querySelector('.name-of-product')?.textContent.trim();
      let pid = productCard.querySelector('.product-pid')?.textContent.trim();
      let vId = productCard.querySelector('.vendor-id')?.textContent.trim();
      let qunInput = productCard.querySelector('.quantity-one-product');
      let qun = qunInput ? qunInput.value : 1;
      let priceText = productCard.querySelector('.price-in-pro-item')?.textContent.trim();
      let unitPrice = parseFloat(priceText);
      let totalPrice = unitPrice * parseInt(qun);

      // ✅ فحص الأخطاء قبل الإضافة (يمنع IntegrityError)
      if (!vId || vId === "undefined") {
        console.error("خطأ: معرف البائع مفقود في الـ HTML");
        return;
      }
      if (!pid) {
        console.error("خطأ: معرف المنتج (PID) مفقود");
        return;
      }

      // تحقق من تكرار المنتج
      if (arrayProduct.some(item => item.pid === pid)) {
        showAlert("⚠️ المنتج موجود مسبقا", "#ffcdd2");
        return;
      }

      // دالة الإضافة الفعلية
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
        
        renderStoredItem(productData); // إضافة للعرض
        showAlert("🛒 تم إضافة المنتج", "#ccff33");
      };

      // الكشف عن الـ WebView (فيسبوك/انستغرام)
      const ua = navigator.userAgent || navigator.vendor || window.opera;
      const isInWebView = /FBAN|FBAV|Instagram|FB_IAB|wv/.test(ua);

      if (isInWebView) {
        addProduct();
        document.getElementById('webviewBanner')?.style.setProperty('display', 'block');
      } else if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (pos) => addProduct(pos.coords.longitude, pos.coords.latitude),
          () => showAlert("⚠️ يرجى فتح الموقع لإضافة المنتجات", "#ffcdd2")
        );
      } else {
        addProduct(); // إضافة بدون موقع إذا كان المتصفح لا يدعم
      }
    }
  });

  // --- 4. دالة رسم العنصر في القائمة ---
  function renderStoredItem(item) {
    let listGroup = document.querySelector('.list-group');
    if(!listGroup) return;

    let li = document.createElement('li');
    li.className = 'list-group-item d-flex justify-content-between lh-sm list-group-item-card';
    li.innerHTML = `
      <div>
        <h6 class="my-0">${item.productName}</h6>
        <small class="text-body-secondary">${item.category || ""}</small>
      </div>
      <h4 class="text-body-secondary price-for-one" style="margin-top: 6px;">${item.prices}</h4>
      <p style="margin-top:8px;">x${item.qun}</p>
      <button class="btn btn-danger delete-item-pro" type="button" data-pid="${item.pid}">
        <i class="bi bi-trash"></i>
      </button>
    `;

    listGroup.appendChild(li);
    updateTotalPrice();
    updateCount();

    // حذف المنتج
    li.querySelector('.delete-item-pro').addEventListener('click', function () {
      li.remove();
      arrayProduct = arrayProduct.filter(p => p.pid !== item.pid);
      localStorage.setItem("arrayProduct", JSON.stringify(arrayProduct));
      updateTotalPrice();
      updateCount();
    });
  }

  // --- 5. تحديث الأرقام ---
  function updateTotalPrice() {
    let total = arrayProduct.reduce((sum, item) => sum + parseFloat(item.prices), 0);
    let totalElement = document.querySelector('.totals-price');
    if(totalElement) totalElement.innerHTML = total + ' Dz';
  }

  function updateCount() {
    let count = arrayProduct.length;
    document.querySelectorAll('.badge, .count-for-card-icon').forEach(el => {
      el.innerHTML = count;
    });
  }

  // دالة الرسائل التنبيهية
  function showAlert(message, bg) {
    const alertBox = document.querySelector(".alerts");
    if(!alertBox) return;
    alertBox.querySelector("p").textContent = message;
    alertBox.style.background = bg;
    alertBox.style.visibility = "visible";
    setTimeout(() => { alertBox.style.visibility = "hidden"; }, 2000);
  }

  // --- باقي الكود الخاص بالبحث والسكرول (يعمل كما هو) ---
  

  function createItem(i) {
    let productName = nameOfProduct[i].textContent.trim();
    let unitPrice = parseFloat(priceInProItem[i].innerHTML);
    let quantity = parseInt(quantityOneProduct[i].value) || 1;
    let totalPriceOne = unitPrice * quantity;

    let li = document.createElement('li');
    li.className = 'list-group-item d-flex justify-content-between lh-sm list-group-item-card';
    li.innerHTML = `
      <div>
        <h6 class="my-0 name-of-product">${productName}</h6>
        <small class="text-body-secondary category-of-product">${categoryOfProduct[i].innerText.trim()}</small>
      </div>
      <h4 class="text-body-secondary price-in-pro-item price-for-one" style="margin-top: 6px;">${totalPriceOne}</h4>
      <p style="margin-top:8px;">x${quantity}</p>
      <button class="btn btn-danger delete-item-pro" type="button">
        <i class="bi bi-trash"></i> Delete
      </button>

    `;

    listGroup.appendChild(li);
    updateTotalPrice();
    updateCount();

    li.querySelector('.delete-item-pro').addEventListener('click', function () {
      listGroup.removeChild(li);
      let index = arrayProduct.findIndex(item => item.productName === productName);
      if (index !== -1) arrayProduct.splice(index, 1);
      localStorage.setItem("arrayProduct", JSON.stringify(arrayProduct));
      updateTotalPrice();
      updateCount();
    });
  }

  function updateTotalPrice() {
    let total = 0;
    document.querySelectorAll('.price-for-one').forEach(item => {
      total += parseFloat(item.innerHTML);
    });
    document.querySelector('.totals-price').innerHTML = total + ' Dz';
  }

  function updateCount() {
    let count = arrayProduct.length;
    document.querySelector('.badge').innerHTML = count;
    document.querySelector('.count-for-card-icon').innerHTML = count;
  }




  
let  value_search = document.querySelectorAll('.value_search')
let  search_product = document.querySelector('.search_product')
for (let i = 0; i < value_search.length; i++) {
  value_search[i].addEventListener('click' , function () {
    search_product.value= value_search[i].textContent
    if (window.innerWidth < 768) {
      document.querySelector('.hidd-open').classList.add('show')
      
    }
  window.scrollTo({
    top:0,
  })
  
})
}



let most_search_scroll = document.querySelector('.most_search_scroll');
let section_most = document.querySelector('.section_most');

if (most_search_scroll && section_most) {
  most_search_scroll.addEventListener("click", function () {
    section_most.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    });
  });
}


  
  let close_session_card = document.querySelector('.close-session-card')
  close_session_card.addEventListener('click' , function () {
    document.querySelector('.hidd-open').classList.remove('show')
  })
  

  let btn_start = document.querySelectorAll('.btn-start')
  let product_tabs = document.querySelector('.product-tabs')
  for (let i = 0; i < btn_start.length; i++) {
    btn_start[i].addEventListener('click' , function () {
      product_tabs.scrollIntoView({
        behavior: 'smooth', 
        block: 'start'
      })
      
    })
  }

  window.addEventListener("pageshow", function (event) {
    if (event.persisted || performance.getEntriesByType("navigation")[0].type === "back_forward") {
      
      let referrer = document.referrer; 
      if (referrer.includes("/product_category/")) { 
        window.location.reload();
      }
    }
  });

  
})
