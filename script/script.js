/*
Author: Cruz De Los Santos
Date: 11/19/2025
file: scripts.js
*/

/* SEOUL AND CONTACT PAGE INTERACTIONS */


let slideIndex = 0;
showSlides();

function showSlides() {
  let slides = document.getElementsByClassName("mySlides");
	if (slides.length === 0) return;
	
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) { slideIndex = 1 }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 4000); // Cambia cada 4 segundos
}


const faders = document.querySelectorAll('.fade-in');

function checkFade() {
  const triggerBottom = window.innerHeight * 0.9;
  faders.forEach(fader => {
    const boxTop = fader.getBoundingClientRect().top;
    if (boxTop < triggerBottom) {
      fader.classList.add('visible');
    } else {
      fader.classList.remove('visible');
    }
  });
}

window.addEventListener('scroll', checkFade);
window.addEventListener('load', checkFade);









/* HAMBURGER MENU */
const menuBtn = document.querySelector('.menu-btn');
const nav = document.querySelector('nav');

menuBtn.addEventListener('click', () => {
  menuBtn.classList.toggle('active');
  nav.classList.toggle('active');
});





 // SPLASH SCREEN LOGIC
document.addEventListener("DOMContentLoaded", () => {
  const splash = document.getElementById("splash-screen");

  // If user already entered once, skip splash
  if (localStorage.getItem("enteredOnce") === "yes") {
    splash.style.display = "none";
    return;
  }

  // If user clicks, hide splash and save preference
  splash.addEventListener("click", () => {
    splash.style.display = "none";
    localStorage.setItem("enteredOnce", "yes");
  });
});
