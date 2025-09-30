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
  // تعريف البائع الحالي
  let currentVendorId = document.querySelector('.vendor-id')?.textContent.trim();

  // جلب السلة من التخزين
  let arrayProduct = JSON.parse(localStorage.getItem('arrayProduct')) || [];

  // ✅ تحقق إذا كانت السلة تخص بائعًا آخر
  if (arrayProduct.length > 0 && arrayProduct[0].vId !== currentVendorId) {
    localStorage.removeItem('arrayProduct');
    arrayProduct = [];
    location.reload(); // لإفراغ الصفحة من منتجات البائع الآخر
    return;
  }



  
    
  // navigator.geolocation.getCurrentPosition((pos) =>{
  //   let lng = pos.coords.longitude
  //   let lat = pos.coords.latitude
  
  
  //   fetch(`${window.location.origin}{% url 'cardorder' vendor.vid %}?product={{ product.vendor }}`, {
  //     method: 'POST',
  //     headers: {
  //       "Content-Type": "application/json",
  //       "X-CSRFToken": "{{ csrf_token }}"
  //     },
  //     body: JSON.stringify({ lng, lat })
  //   })
  //   .then(res => res.text())
  //   .then(data =>{
  //     console.log("📌 الرد من السيرفر:", data)
  //   })
  // })

  // end location customer


  // تعريف العناصر
let nameOfProduct = document.querySelectorAll('.name-of-product');
let productPid = document.querySelectorAll('.product-pid');
let vendorId = document.querySelectorAll('.vendor-id');
let categoryOfProduct = document.querySelectorAll('.category-of-product');
let priceInProItem = document.querySelectorAll('.price-in-pro-item');
let quantityOneProduct = document.querySelectorAll('.quantity-one-product');
let btnAddCard = document.querySelectorAll('.btn-add-card');
let listGroup = document.querySelector('.list-group');
let alerts = document.querySelector('.alerts');

// رسم المنتجات من التخزين
arrayProduct.forEach((storedProduct) => {
  let i = Array.from(productPid).findIndex(el => el.textContent.trim() === storedProduct.pid);
  if (i !== -1) createItem(i);
});


for (let i = 0; i < btnAddCard.length; i++) {
  btnAddCard[i].addEventListener('click', function () {
    let productName = nameOfProduct[i].textContent.trim();
    let pid = productPid[i].textContent.trim();
    let vId = vendorId[i].textContent.trim();
    let qun = quantityOneProduct[i].value;
    let prices = parseFloat(priceInProItem[i].textContent.trim()) * parseInt(qun);

    // دالة لإضافة المنتج إلى السلة
    function addProduct(lng, lat) {
      let productData = { productName, prices, pid, vId, qun, lng, lat };
      arrayProduct.push(productData);
      createItem(i);
      localStorage.setItem("arrayProduct", JSON.stringify(arrayProduct));

      // رسالة نجاح
      document.querySelector(".alerts p").innerHTML = "Product is add to cart";
      alerts.style.visibility = "visible";
      document.querySelector(".alerts").style.background = "#ccff33";
      setTimeout(() => { alerts.style.visibility = "hidden" }, 2000);
    }

    // تحقق إذا المنتج موجود بالفعل
    if (!arrayProduct.some(item => item.pid === pid)) {
      
      // تحقق إذا سبق أن تم رفض الموقع
      let denied = localStorage.getItem('geolocationDenied');

      navigator.geolocation.getCurrentPosition(
        (pos) => {
          localStorage.removeItem('geolocationDenied'); // تم السماح
          addProduct(pos.coords.longitude, pos.coords.latitude);
        },
        (err) => {
          // المستخدم رفض الوصول
          localStorage.setItem('geolocationDenied', 'true');
          addProduct(null, null); // أضف المنتج بدون موقع
          alert("يرجى السماح بالوصول للموقع إذا أردت استخدام ميزة الموقع.");
        }
      );

    } else {
      // المنتج موجود بالفعل
      document.querySelector(".alerts p").innerHTML = "Product already in cart";
      alerts.style.visibility = "visible";
      document.querySelector(".alerts").style.background = "#ffcdd2";
      setTimeout(() => { alerts.style.visibility = "hidden" }, 2000);
    }
  });
}




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
