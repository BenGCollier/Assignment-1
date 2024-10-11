const siteUrl = '//127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250;
const minHeight = 250;

// load CSS
var head = document.getElementsByTagName('head')[0];  // Get HTML head element
var link = document.createElement('link'); // Create new link Element
link.rel = 'stylesheet'; // set the attributes for link element
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random()*9999999999999999);
head.appendChild(link);  // Append link element to HTML head

// load HTML
var body = document.getElementsByTagName('body')[0];
boxHtml = `
  <div id="bookmarklet">
    <a href="#" id="close">&times;</a>
    <h1>Select an image to bookmark:</h1>
    <div class="recipe_images"></div>
  </div>`;
body.innerHTML += boxHtml;

function bookmarkletLaunch() {
  bookmarklet = document.getElementById('bookmarklet');
  var recipe_imagesFound = bookmarklet.querySelector('.images');

  // clear recipe_images found
  recipe_imagesFound.innerHTML = '';
  // display bookmarklet
  bookmarklet.style.display = 'block';

  // close event
  bookmarklet.querySelector('#close')
             .addEventListener('click', function(){
    bookmarklet.style.display = 'none'
  });

  // find recipe_images in the DOM with the minimum dimensions
  recipe_images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]');
  recipe_images.forEach(recipe_image => {
    if(recipe_image.naturalWidth >= minWidth
       && recipe_image.naturalHeight >= minHeight)
    {
      var recipe_imageFound = document.createElement('img');
      recipe_imageFound.src = recipe_image.src;
      recipe_imagesFound.append(recipe_imageFound);
    }
  })

  // select recipe_image event
  recipe_imagesFound.querySelectorAll('img').forEach(recipe_image => {
    recipe_image.addEventListener('click', function(event){
        recipe_imageSelected = event.target;
      bookmarklet.style.display = 'none';
      window.open(siteUrl + 'recipe_images/create/?url='
                  + encodeURIComponent(recipe_imageSelected.src)
                  + '&title='
                  + encodeURIComponent(document.title),
                  '_blank');
    })
  })
}

// launch the bookmkarklet
bookmarkletLaunch();