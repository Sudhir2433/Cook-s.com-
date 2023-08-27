

// // new code


// document.addEventListener("DOMContentLoaded", function() {
//   const quantityElement = document.querySelector('.product-quantity');
//   const incrementButton = document.querySelector('.increment-button');
//   const decrementButton = document.querySelector('.decrement-button');
//   const priceElement = document.querySelector('.product-price');
//   const bookNowButton = document.querySelector('.book-now-button');

//   const initialPrice = parseFloat(priceElement.getAttribute('data-initial-price'));

//   let quantity = 1;
//   let totalPrice = initialPrice;

//   function updateUI() {
//     quantityElement.textContent = quantity;
//     priceElement.textContent = `Rs:${totalPrice * quantity}`;
//   }

//   incrementButton.addEventListener('click', function() {
//     quantity++;
//     totalPrice = initialPrice;
//     updateUI();
//   });

//   decrementButton.addEventListener('click', function() {
//     if (quantity > 1) {
//       quantity--;
//       totalPrice = initialPrice;
//       updateUI();
//     }
//   });

//   bookNowButton.addEventListener('click', function() {
//     // Your code for handling the "Book Now" button click
//     // You can use AJAX to send the data to the backend if needed
//   });

//   // Initial UI update
//   updateUI();
// });
