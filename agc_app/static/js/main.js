$(document).ready(function () {

  // Show menu
  $('.navbar-toggle').click(function() {
    $(this).toggleClass('active');
    $('.panel').slideToggle( "slow", function() {});
  });

  // Scroll spee
  $('.nav__list, .intro, .start__btn').on('click','a', function (event) {
    event.preventDefault();
    var id  = $(this).attr('href'),
      top = $(id).offset().top;
      $('body,html').animate({scrollTop: top}, 800);
  });

  // Modal
  $('.open-modal').click(function(e) {
    e.preventDefault();
    $('.modal_request').fadeIn();
  });

  $('.modal__close').click(function() {
    $('.modal').fadeOut();
  });

  $(document).click(function(event) {
    if ($(event.target).closest('.open-modal').length 
      || $(event.target).closest('.modal__box').length ) return;
      $('.modal').fadeOut();
      event.stopPropagation();
  });

  // Maskedinput
  $(function($){
    $('.phone-mask').mask(('+7 ') + '(999) 999-99-99');
  });

  // Accardion
  var accordion = function() {
    var data = $('.accordion').attr('data-accordion');
    $('.accordion-header').on('click', function(){
      $(this).next('.accordion-body').not(':animated').slideToggle()
    });
    $('.accordion-header').click(function () {
      $(this).parent('.accordion li').toggleClass('active');
    });
  };
  accordion();

  // Material
  $('.details__link a').click(function(e) {
    e.preventDefault();
    $('.material').fadeIn();
    var ts = $(this).parents('.details__link').next('.material__text');
    var text = ts.html();
    $('.material__box').html(text);
  });

  $('.material__close, .back__link').click(function(e) {
    e.preventDefault();
    $('.material').fadeOut();
  });

  // Tabs
  $('.tabs__item').not(':first').hide();
  $('.tabs__name').click(function() {
    $('.tabs__name').removeClass('active').eq($(this).index()).addClass('active');
    $('.tabs__item').hide().eq($(this).index()).fadeIn()
  }).eq(0).addClass('active');

  // Swiper
  var mySwiper = new Swiper ('.swiper-container', {
    spaceBetween: 15,
    slidesPerView: 'auto',
    scrollbar: {
      el: '.swiper-scrollbar',
      hide: false,
      slidesPerView: 1,
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'fraction',
    },
    breakpoints: {
      480: {
        slidesPerView: 2,
        spaceBetween: 30,
      }
    }
  });

  var mySwiper1 = new Swiper ('.swiper-container1', {
    spaceBetween: 10,
    slidesPerView: '3',
    scrollbar: {
      el: '.swiper-scrollbar',
      hide: false,
      slidesPerView: 1,
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'fraction',
    },
    breakpoints: {
      768: {
        slidesPerView: 4,
        spaceBetween: 30,
      },
      480: {
        slidesPerView: 4,
        spaceBetween: 15,
      }
    }
  })

});