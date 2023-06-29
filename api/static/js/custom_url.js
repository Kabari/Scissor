const access_token = localStorage.getItem("access_token");
document.addEventListener("DOMContentLoaded", function () {
  // Function to extract the short URL from the current page URL
  const currentUrl = window.location.href;
  const urlParts = currentUrl.split("/");
  const shortCode = urlParts[urlParts.length - 1];

  //   // Retrieve the HTML elements
  //   const longUrlElement = document.getElementById("long-url");
  //   const shortUrlElement = document.getElementById("short-url");
  const customDomainInput = document.getElementById("custom-domain-input");
  const customUrlButton = document.getElementById("custom-url-button");
  const customUrlElement = document.getElementById("custom-url");

  // Display the long URL and short URL on the page
  //   longUrlElement.textContent = "Long URL: " + url.long_url;
  //   shortUrlElement.textContent = "Short URL: " + url.short_url;

  // Event listener for the "Generate Custom URL" button
  customUrlButton.addEventListener("click", function () {
    const customDomain = customDomainInput.value;

    // Make a request to the server to update the custom domain
    axios
      .patch(
        `/url/custom/${shortCode}`,
        { custom_domain: customDomain },
        {
          headers: {
            Authorization: `Bearer ${access_token}`,
          },
        }
      )
      .then(function (response) {
        const updatedUrl = response.data;

        // Display the updated custom URL on the page
        customUrlElement.textContent = "Custom URL: " + updatedUrl.custom_url;
      })
      .catch(function (error) {
        console.error("Error updating custom URL:", error);
      });
  });
});
