// CART FUNCTION

let cartCount = 0;

const cartButtons =
document.querySelectorAll(".add-cart");

const cartDisplay =
document.getElementById("cart-count");

cartButtons.forEach((button) => {

  button.addEventListener("click", () => {

    cartCount++;

    cartDisplay.innerText = cartCount;

    button.innerText = "Added";

    button.style.background = "green";

    setTimeout(() => {

      button.innerText = "Add to Cart";

      button.style.background = "#ff9900";

    },1000);

  });

});

// SEARCH FUNCTION

const searchInput =
document.querySelector(".search-box input");

searchInput.addEventListener("keyup", () => {

  const value =
  searchInput.value.toLowerCase();

  const products =
  document.querySelectorAll(".product-card");

  products.forEach((product) => {

    const name =
    product.querySelector("h3")
    .innerText.toLowerCase();

    if(name.includes(value)){

      product.style.display = "block";

    }

    else{

      product.style.display = "none";

    }

  });

});

// PRODUCT CLICK

const productCards =
document.querySelectorAll(".product-card");

productCards.forEach((card) => {

  card.addEventListener("click", () => {

    const productName =
    card.querySelector("h3").innerText;

    console.log(productName);

  });

});

// HERO BUTTON

document.querySelector(".hero button")
.addEventListener("click", () => {

  alert("Welcome To Amazon Sale");

});

// DEAL BUTTON

document.getElementById("deal-btn")
.addEventListener("click", () => {

  alert("Deal Activated");

});

// NEWSLETTER

document.getElementById("subscribe-btn")
.addEventListener("click", () => {

  const email =
  document.querySelector(".newsletter input").value;

  if(email === ""){

    alert("Please Enter Email");

  }

  else{

    alert("Subscribed Successfully");

  }

});