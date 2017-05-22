

// google map
var map = '';
var center;

function initialize() {
    markLocation = new google.maps.LatLng(51.993491, 4.386561);

    var mapOptions = {
        zoom: 14,
        center: markLocation,
        scrollwheel: false
    };


    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
    markerOptions = {
        //label: "hello",
        map: map,
        position: markLocation,
        title: "Surge-on",
    }
    marker = new google.maps.Marker(markerOptions);

    google.maps.event.addDomListener(map, 'idle', function () {
        calculateCenter();
    });

    google.maps.event.addDomListener(window, 'resize', function () {
        map.setCenter(center);
    });
}

function calculateCenter() {
    center = map.getCenter();
}

function loadGoogleMap() {
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&' + 'callback=initialize';
    document.body.appendChild(script);
}
/* jQuery Pre loader
  -----------------------------------------------*/
$(window).load(function(){
    $('.preloader').fadeOut(1000); // set duration in brackets    
});


/* Magnific Popup
-----------------------------------------------*/
$(document).ready(function() {
    $('.popup-youtube').magnificPopup({
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
         fixedContentPos: false,
    });
});


/* Istope Portfolio
-----------------------------------------------*/
jQuery(document).ready(function($){

  if ( $('.iso-box-wrapper').length > 0 ) { 

      var $container  = $('.iso-box-wrapper'), 
        $imgs     = $('.iso-box img');

      $container.imagesLoaded(function () {

        $container.isotope({
        layoutMode: 'fitRows',
        itemSelector: '.iso-box'
        });

        $imgs.load(function(){
          $container.isotope('reLayout');
        })

      });

      //filter items on button click

      $('.filter-wrapper li a').click(function(){

          var $this = $(this), filterValue = $this.attr('data-filter');

      $container.isotope({ 
        filter: filterValue,
        animationOptions: { 
            duration: 750, 
            easing: 'linear', 
            queue: false, 
        }                
      });             

      // don't proceed if already selected 

      if ( $this.hasClass('selected') ) { 
        return false; 
      }

      var filter_wrapper = $this.closest('.filter-wrapper');
      filter_wrapper.find('.selected').removeClass('selected');
      $this.addClass('selected');

        return false;
      }); 

  }

});


$(document).ready(function() {

  /* Hide mobile menu after clicking on a link
    -----------------------------------------------*/
    $('.navbar-collapse a').click(function(){
        $(".navbar-collapse").collapse('hide');
    });


  /*  smoothscroll
  ----------------------------------------------*/
   $(function() {
        $('#home a, .navbar-default a').bind('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - 49
            }, 1000);
            event.preventDefault();
        });
    });
  


  /* home slideshow section
  -----------------------------------------------*/
  $(function(){
    jQuery(document).ready(function() {
    $('#home').backstretch([
       "static/images/home-bg-slideshow1.jpg", 
       "static/images/home-bg-slideshow2.jpg",
       "static/images/home-bg-slideshow3.jpg",
        ],  {duration: 2000, fade: 750});
    });
  })


   /* Flexslider
    -----------------------------------------------*/
    $(window).load(function() {
      $('.flexslider').flexslider({
         animation: "slide"
      });

    });
  

  /* Parallax section
    -----------------------------------------------*/
  function initParallax() {
    $('#about').parallax("100%", 0.1);
    $('#feature').parallax("100%", 0.3);
    $('#about').parallax("100%", 0.1);
    $('#video').parallax("100%", 0.2);
    $('#menu').parallax("100%", 0.3);
    $('#team').parallax("100%", 0.3);
    $('#gallery').parallax("100%", 0.1);
    $('#contact').parallax("100%", 0.2);
  }
  initParallax();


  /* Nivo lightbox
    -----------------------------------------------*/
  $('#gallery .col-md-4 a').nivoLightbox({
        effect: 'fadeScale',
    });


  /* wow
  -------------------------------*/
  new WOW({ mobile: false }).init();
  loadGoogleMap();
  });

