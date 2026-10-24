const cartForm = document.getElementById('add-to-cart-form');
const cartButton = document.getElementById('add-to-cart-btn');

if (cartForm && cartButton) {
    cartForm.addEventListener('submit', async function (event) {
        event.preventDefault();

        const originalText = cartButton.textContent;

        cartButton.disabled = true;
        cartButton.textContent = 'Adding...';

        try {
            const response = await fetch(cartForm.action, {
                method: 'POST',
                body: new FormData(cartForm)
            });

            const data = await response.json();

            if (response.ok && data.success) {
                cartButton.textContent = '✓ Added to Cart';
            } else {
                alert(data.message || 'Unable to add this item to your cart.');
                cartButton.textContent = originalText;
            }

        } catch (error) {
            alert('Something went wrong. Please try again.');
            cartButton.textContent = originalText;

        } finally {
            cartButton.disabled = false;
        }
    });
}