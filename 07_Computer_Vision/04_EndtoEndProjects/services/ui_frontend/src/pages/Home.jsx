import React from "react";
import { Helmet } from "react-helmet-async";

const Home = () => {
  return (
    <>
      <Helmet>
        <title>🍕 Toukh Pizza | Best Pizza in Qalyubia, Egypt</title>
        <meta
          name="description"
          content="Order the most delicious pizza in Toukh, Qalyubia! Authentic Egyptian-Italian taste, fresh ingredients, fast delivery, and unbeatable flavors."
        />
        <meta
          name="keywords"
          content="Pizza Toukh, Toukh Pizza Store, Best Pizza Egypt, Pizza Qalyubia, بيتزا طوخ, بيتزا القليوبية, Toukh food delivery"
        />
        
        {/* Open Graph / Facebook */}
        <meta property="og:title" content="Toukh Pizza | Most Popular Pizza in Qalyubia" />
        <meta
          property="og:description"
          content="Craving pizza in Toukh? Enjoy hot, fresh, and flavorful pizzas delivered across Qalyubia."
        />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://pizza-store-4fcd5.web.app/" />
        <meta property="og:image" content="https://pizza-store-4fcd5.web.app/pizza-banner.jpg" />
        <meta property="og:locale" content="en_EG" />
        <meta property="og:site_name" content="Toukh Pizza Store" />

        {/* Twitter Card */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Toukh Pizza | Best Pizza in Qalyubia, Egypt" />
        <meta
          name="twitter:description"
          content="Try the most loved pizza in Toukh with authentic taste and fast delivery. Order now!"
        />
        <meta name="twitter:image" content="https://pizza-store-4fcd5.web.app/pizza-banner.jpg" />
      </Helmet>

      <div className="text-center text-2xl md:text-3xl font-bold text-red-600 mt-12">
        🍕 Welcome to Toukh's #1 Pizza Destination!
      </div>
      <p className="text-center text-gray-700 dark:text-gray-300 mt-4 px-4 max-w-2xl mx-auto text-lg">
        Freshly made pizza using the finest ingredients. Order now and enjoy a delicious experience with speedy delivery across Toukh and Qalyubia.
      </p>
    </>
  );
};

export default Home;









