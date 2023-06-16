// // --- Admin Product Management Btns ---
// const addProductBtn = document.querySelector("#add-product-menu");
// const removeProductBtn = document.querySelector("#remove-product-menu");

// // Admin Management Containers
// const addContainer = document.querySelector(".add-container");
// const removeContainer = document.querySelector(".remove-container");

// // Admin Side URL
// const adminSRC = /admin-side.html";

// // --- Admin Side ---
// if (adminSRC === window.location.href) {
//   console.log("admin side");
//   // Admin Management Btns
//   addProductBtn.addEventListener("click", () => {
//     addContainer.classList.toggle("show-container");
//     removeContainer.classList.remove("show-container");
//   });

//   // Admin Management Btns
//   removeProductBtn.addEventListener("click", () => {
//     removeContainer.classList.toggle("show-container");
//     addContainer.classList.remove("show-container");
//   });
// }



// var removeButton = document.getElementById('remove-product-menu');
// var removeSection = document.getElementById('remove_from_menu');
// console.log("REgistered")
// removeButton.addEventListener("click", function() {
//     console.log("clicked")
//     if (removeSection.style.display === 'none') {
//         removeSection.style.display = 'block';
//     } else {
//         removeSection.style.display = 'none';
//     }
//   });

var addButton = document.getElementById('add-product-menu');
var addSection = document.getElementById('add_to_menu');
console.log("Registered")
addButton.addEventListener("click", function() {
    console.log("Clicked")
    if (addSection.style.display === 'none') {
        addSection.style.display = 'block';
    } else {
        addSection.style.display = 'none';
    }
});

// Function to send an AJAX request to add a product
function addProduct(product, category, price) {
    // Create an XMLHttpRequest object
    var xhr = new XMLHttpRequest();
  
    // Configure the request
    xhr.open("POST", "/add_product", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  
    // Define the request parameters
    var params = "product=" + encodeURIComponent(product) + "&category=" + encodeURIComponent(category) + "&price=" + encodeURIComponent(price);
  
    // Send the request
    xhr.send(params);
  
    // Handle the response
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log(response.message);
        } else {
            console.log("Failed to add product to menu");
        }
    };
}

// // Example usage
// var product = "New Product";
// var category = "Food";
// var price = 10.99;

addProduct(product, category, price);


// var addButton = document.getElementById('add-product-menu');
// var addSection = document.getElementById('add_to_menu');
// console.log("REgistered")
// console.log("Registered")
// addButton.addEventListener("click", function() {
//     console.log("clicked")
//     console.log("Clicked")
//     if (addSection.style.display === 'none') {
//         addSection.style.display = 'block';
//     } else {
//         addSection.style.display = 'none';
//     }
//   });

// var removeButton = document.getElementById('remove-product-menu');
// var removeSection = document.getElementById('remove_from_menu');
// console.log("REgistered")
// removeButton.addEventListener("click", function() {
//     console.log("clicked")
//     if (removeSection.style.display === 'none') {
//         removeSection.style.display = 'block';
//     } else {
//         removeSection.style.display = 'none';
//     }
//   });
// });
