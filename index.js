$(function(){

    new WOW().init();

    console.log($('.aboutus').offset().top);
    
    $('.logovamenu ul li:nth-child(2) a').on('click',function(event){
        event.preventDefault();

        $('html,body').animate({ scrollTop: $('.aboutus').offset().top},1000);
    });
    $('.logovamenu ul li:nth-child(3) a').on('click',function(event){
        event.preventDefault();

        $('html,body').animate({ scrollTop: $('.contact').offset().top},1000);
    });
});