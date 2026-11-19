import { useEffect, useState } from "react";
import menuFallback from "../data/menuData";
import { apiRequest } from "../lib/api";

import {
  FaCoffee,
  FaShoppingBag,
  FaPlus,
  FaStar,
} from "react-icons/fa";

function Menu({ addToCart }) {
  // =========================================
  // MENU ITEMS
  // =========================================

  const [menuItems, setMenuItems] = useState(menuFallback);
  const [menuLoadError, setMenuLoadError] = useState(false);

  useEffect(() => {
    apiRequest("/menu/")
      .then((items) => { if (Array.isArray(items) && items.length) setMenuItems(items); })
      .catch(() => setMenuLoadError(true));
  }, []);



  // =========================================
  // CATEGORY STATE
  // =========================================

  const [activeCategory, setActiveCategory] =
    useState("All");


  // =========================================
  // CATEGORY LIST
  // =========================================

  const categories = [
    "All",
    "Coffee",
    "Fast Food",
    "Desserts",
    "Beverages",
    "Special Dishes",
  ];


  // =========================================
  // FILTER MENU ITEMS
  // =========================================

  const filteredItems =
    activeCategory === "All"
      ? menuItems
      : menuItems.filter(
          (item) =>
            item.category === activeCategory
        );


  return (
    <section
      id="menu"
      className="menu-section"
    >

      <div className="container">

        {/* =================================
            SECTION HEADER
        ================================= */}

        <div className="section-heading text-center">

          <div className="section-label">
            <FaCoffee />
            OUR MENU
          </div>

          <h2>
            Made with love,
            <span> served with soul.</span>
          </h2>

          <p>
            From your first morning coffee to
            your favourite evening treat,
            there's always something waiting
            for you at Okali's Cafe.
          </p>

        </div>


        {/* =================================
            MENU FILTER BUTTONS
        ================================= */}

        <div className="menu-categories">

          {categories.map((category) => (

            <button
              key={category}
              className={`menu-category ${
                activeCategory === category
                  ? "active"
                  : ""
              }`}
              onClick={() =>
                setActiveCategory(category)
              }
            >

              {category}

            </button>

          ))}

        </div>


        {/* =================================
            MENU GRID
        ================================= */}

        {menuLoadError && <p className="text-center small text-muted mb-3">Showing the local menu while the server is offline.</p>}

        <div className="row g-4">

          {filteredItems.map((item) => (

            <div
              className="col-lg-4 col-md-6"
              key={item.id}
            >

              <div className="menu-card">

                {/* Image */}

                <div className="menu-card-image">

                  <img
                    src={item.image}
                    alt={item.name}
                    loading="lazy"
                  />

                  {item.popular && (
                    <span className="menu-popular">
                      <FaStar />
                      Popular
                    </span>
                  )}

                  <span className="menu-category-badge">
                    {item.category}
                  </span>

                </div>


                {/* Content */}

                <div className="menu-card-content">

                  <div className="menu-card-top">

                    <div>

                      <h3>
                        {item.name}
                      </h3>

                      <div className="menu-rating">

                        <FaStar />

                        <span>
                          {item.rating}
                        </span>

                      </div>

                    </div>

                    <span className="menu-price">
                      ₹{item.price}
                    </span>

                  </div>


                  <p>
                    {item.description}
                  </p>


                  {/* Add To Cart */}

                  <button
                    className="add-to-cart-btn"
                    onClick={() =>
                      addToCart(item)
                    }
                  >

                    <span>
                      <FaPlus />
                    </span>

                    Add to Order

                    <FaShoppingBag />

                  </button>

                </div>

              </div>

            </div>

          ))}

        </div>


        {/* =================================
            NO ITEMS MESSAGE
        ================================= */}

        {filteredItems.length === 0 && (

          <div className="menu-empty">

            <FaCoffee />

            <h3>
              Nothing here yet
            </h3>

            <p>
              Please choose another category.
            </p>

          </div>

        )}


        {/* =================================
            BOTTOM CTA
        ================================= */}

        <div className="menu-bottom-cta">

          <div>

            <FaCoffee />

            <span>
              More delicious moments await
            </span>

          </div>

          <a href="#reservation">
            Reserve a Table
          </a>

        </div>

      </div>

    </section>
  );
}

export default Menu;