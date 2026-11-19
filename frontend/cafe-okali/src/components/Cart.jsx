import { useState } from "react";
import { apiRequest } from "../lib/api";
import {
  FaShoppingBag,
  FaPlus,
  FaMinus,
  FaTrash,
  FaTimes,
  FaArrowRight,
  FaCoffee,
} from "react-icons/fa";

function Cart({ cartItems, setCartItems, isOpen, setIsOpen }) {
  const [checkout, setCheckout] = useState({ customer_name: "", phone: "", email: "", fulfillment: "delivery", delivery_address: "", notes: "" });
  const [checkoutError, setCheckoutError] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  // Increase quantity
  const increaseQuantity = (id) => {
    setCartItems((items) =>
      items.map((item) =>
        item.id === id
          ? { ...item, quantity: item.quantity + 1 }
          : item
      )
    );
  };

  // Decrease quantity
  const decreaseQuantity = (id) => {
    setCartItems((items) =>
      items
        .map((item) =>
          item.id === id
            ? { ...item, quantity: item.quantity - 1 }
            : item
        )
        .filter((item) => item.quantity > 0)
    );
  };

  // Remove item
  const removeItem = (id) => {
    setCartItems((items) =>
      items.filter((item) => item.id !== id)
    );
  };

  // Clear cart
  const clearCart = () => {
    setCartItems([]);
  };

  // Calculate subtotal
  const subtotal = cartItems.reduce(
    (total, item) =>
      total + item.price * item.quantity,
    0
  );

  // Delivery charge
  const deliveryCharge =
    cartItems.length > 0 && checkout.fulfillment === "delivery" ? 40 : 0;

  // Final total
  const total = subtotal + deliveryCharge;

  // Total items
  const totalItems = cartItems.reduce(
    (total, item) => total + item.quantity,
    0
  );

  const handleCheckoutChange = (event) => setCheckout((previous) => ({ ...previous, [event.target.name]: event.target.value }));
  const handleCheckoutSubmit = async (event) => {
    event.preventDefault();
    setCheckoutError("");
    setIsSubmitting(true);
    try {
      const result = await apiRequest("/orders/", {
        method: "POST",
        body: JSON.stringify({ ...checkout, items: cartItems.map((item) => ({ menu_item_id: item.id, quantity: item.quantity })) }),
      });
      window.alert(`Order received! Your order number is #${result.order.id}. Thank you for choosing Okali's Cafe.`);
      setCartItems([]);
      setCheckout({ customer_name: "", phone: "", email: "", fulfillment: "delivery", delivery_address: "", notes: "" });
      setIsOpen(false);
    } catch (error) {
      setCheckoutError(error.message || "We couldn't place your order. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };


  return (
    <>
      {/* Cart Overlay */}
      {isOpen && (
        <div
          className="cart-overlay"
          onClick={() => setIsOpen(false)}
        ></div>
      )}

      {/* Cart Sidebar */}
      <aside
        className={`cart-sidebar ${
          isOpen ? "cart-sidebar-open" : ""
        }`}
      >
        {/* Header */}
        <div className="cart-header">

          <div className="cart-title">

            <div className="cart-title-icon">
              <FaShoppingBag />
            </div>

            <div>
              <span>Your Order</span>

              <h3>
                Okali's Cafe
              </h3>
            </div>

          </div>

          <button
            className="cart-close"
            onClick={() => setIsOpen(false)}
            aria-label="Close cart"
          >
            <FaTimes />
          </button>

        </div>


        {/* Cart Content */}
        <div className="cart-content">

          {cartItems.length === 0 ? (

            /* Empty Cart */
            <div className="empty-cart">

              <div className="empty-cart-icon">
                <FaCoffee />
              </div>

              <h3>
                Your cart is empty
              </h3>

              <p>
                Looks like you haven't added
                anything yet.
              </p>

              <button
                onClick={() => setIsOpen(false)}
              >
                Explore Our Menu
              </button>

            </div>

          ) : (

            <>

              {/* Items Count */}
              <div className="cart-items-top">

                <span>
                  {totalItems}{" "}
                  {totalItems === 1
                    ? "item"
                    : "items"}{" "}
                  in your order
                </span>

                <button
                  onClick={clearCart}
                >
                  Clear All
                </button>

              </div>


              {/* Cart Items */}
              <div className="cart-items">

                {cartItems.map((item) => (

                  <div
                    className="cart-item"
                    key={item.id}
                  >

                    {/* Image */}
                    <div className="cart-item-image">

                      <img
                        src={item.image}
                        alt={item.name}
                      />

                    </div>


                    {/* Details */}
                    <div className="cart-item-details">

                      <h4>
                        {item.name}
                      </h4>

                      <p>
                        ₹{item.price}
                      </p>


                      {/* Quantity */}
                      <div className="cart-item-bottom">

                        <div className="quantity-control">

                          <button
                            onClick={() =>
                              decreaseQuantity(
                                item.id
                              )
                            }
                            aria-label="Decrease quantity"
                          >
                            <FaMinus />
                          </button>

                          <span>
                            {item.quantity}
                          </span>

                          <button
                            onClick={() =>
                              increaseQuantity(
                                item.id
                              )
                            }
                            aria-label="Increase quantity"
                          >
                            <FaPlus />
                          </button>

                        </div>


                        <strong>
                          ₹
                          {(
                            item.price *
                            item.quantity
                          ).toLocaleString(
                            "en-IN"
                          )}
                        </strong>

                      </div>

                    </div>


                    {/* Delete */}
                    <button
                      className="remove-cart-item"
                      onClick={() =>
                        removeItem(item.id)
                      }
                      aria-label={`Remove ${item.name}`}
                    >
                      <FaTrash />
                    </button>

                  </div>

                ))}

              </div>


              {/* Order Summary */}
              <div className="cart-summary">

                <h4>
                  Order Summary
                </h4>

                <div className="summary-row">

                  <span>
                    Subtotal
                  </span>

                  <strong>
                    ₹
                    {subtotal.toLocaleString(
                      "en-IN"
                    )}
                  </strong>

                </div>


                <div className="summary-row">

                  <span>
                    Delivery
                  </span>

                  <strong>
                    ₹
                    {deliveryCharge.toLocaleString(
                      "en-IN"
                    )}
                  </strong>

                </div>


                <div className="summary-divider"></div>


                <div className="summary-total">

                  <span>
                    Total
                  </span>

                  <strong>
                    ₹
                    {total.toLocaleString(
                      "en-IN"
                    )}
                  </strong>

                </div>


                {/* Customer details and server-backed checkout */}
                <form className="okali-checkout-form" onSubmit={handleCheckoutSubmit}>
                  <h5>Checkout Details</h5>
                  <label>Full name</label>
                  <input name="customer_name" value={checkout.customer_name} onChange={handleCheckoutChange} required minLength={3} placeholder="Your name" />
                  <label>Mobile number</label>
                  <input name="phone" value={checkout.phone} onChange={handleCheckoutChange} required inputMode="numeric" pattern="[6-9][0-9]{9}" maxLength={10} placeholder="10-digit phone number" />
                  <label>Email (optional)</label>
                  <input name="email" type="email" value={checkout.email} onChange={handleCheckoutChange} placeholder="Email address" />
                  <label>Order type</label>
                  <select name="fulfillment" value={checkout.fulfillment} onChange={handleCheckoutChange}>
                    <option value="delivery">Delivery (+ ₹40)</option>
                    <option value="pickup">Pickup (no delivery fee)</option>
                  </select>
                  {checkout.fulfillment === "delivery" && <><label>Delivery address</label><textarea name="delivery_address" value={checkout.delivery_address} onChange={handleCheckoutChange} required minLength={8} rows={2} placeholder="Full delivery address" /></>}
                  <label>Notes (optional)</label>
                  <textarea name="notes" value={checkout.notes} onChange={handleCheckoutChange} rows={2} placeholder="Any special instructions" />
                  {checkoutError && <p className="form-api-error" role="alert">{checkoutError}</p>}
                  <button className="checkout-button" type="submit" disabled={isSubmitting}>
                    {isSubmitting ? "Placing Order..." : "Place Order"} <FaArrowRight />
                  </button>
                </form>


                <p className="checkout-note">
                  <FaCoffee />
                  Freshly prepared with love at
                  Okali's Cafe.
                </p>

              </div>

            </>

          )}

        </div>

      </aside>
    </>
  );
}

export default Cart;