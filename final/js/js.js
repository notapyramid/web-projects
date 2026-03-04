const currentPage = window.parent.location.pathname;
const titleElement = document.getElementById('a');

if (titleElement) {
  if (currentPage.includes('gallery.html')) {
    titleElement.innerText = 'Our Members';
  } else if (currentPage.includes('about.html')) {
    titleElement.innerText = 'About Us';
  } else if (currentPage.includes('contact.html')) {  
    titleElement.innerText = 'Our Contact';
  } else if (currentPage.includes('help.html')) {
    titleElement.innerText = 'How do we stack up?';
  } else {
    titleElement.innerText = 'Lizard hq (seattle edition)';
  }
}