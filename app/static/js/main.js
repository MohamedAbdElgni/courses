var swiper1 = new Swiper(".swiperpopulartopics", {
  spaceBetween: 6,
    grid:{
        rows: 2,
      },
     breakpoints:{
    600: {
      slidesPerView: 2,
      grid:{
        rows: 2,
      },
    },
    968: {
      slidesPerView: 5,
      grid:{
        rows: 2,
      },
    },
     },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    
    });
