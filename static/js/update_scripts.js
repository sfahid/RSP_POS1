// scripts.js

$(document).ready(function () {
    // Fetch product data via Ajax (you can use Django views for this)
    // Populate the product table dynamically

    // Example: Handle inline editing
    $('#productTable').on('click', '.edit-btn', function () {
        const row = $(this).closest('tr');
        const productId = row.data('product-id');
        const productName = row.find('.product-name').text();
        const productDescription = row.find('.product-description').text();
        const productPrice = row.find('.product-price').text();

        // Show input fields for editing
        // Handle save/update logic via Ajax
    });
});
