// console.log("Sanity check!");

// fetch("/config/")
// .then((result) => { return result.json(); })
// .then((data) => {
//   // Initialize Stripe.js
//   const stripe = Stripe(data.publicKey);

//  document.querySelector("#submitBtn").addEventListener("click", () => {
//     console.log('hello');
//     // Get Checkout Session ID
//     fetch("/create-checkout-session/")
//     .then((result) => { return result.json(); })
//     .then((data) => {
//       console.log(data);
//       // Redirect to Stripe Checkout
//       return stripe.redirectToCheckout({sessionId: data.sessionId})
//     })
//     .then((res) => {
//       console.log(res);
//     });
//   });
// });
document.getElementById("checkout").addEventListener("click", event => {

  console.log("Sanity check!");
  fetch('/create-checkout-session/', {
    method: 'POST',
  })
  .then(function(response) {
    return response.json();
  })
  .then((data) => {
    var stripe = Stripe(data.publicKey);
    stripe.redirectToCheckout({ sessionId: data.sessionId });
  })
  .then(function(result) {
    // If `redirectToCheckout` fails due to a browser or network
    // error, you should display the localized error message to your
    // customer using `error.message`.
    if (result.error) {
      alert(result.error.message);
    }
  });
});
