document.addEventListener("DOMContentLoaded", function () {
  const access_token = localStorage.getItem("access_token");

  // Make a request to the dashboard stats endpoint
  axios
    .get("/url/dashboard", {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    })
    .then((response) => {
      // Retrieve the data from the response
      const { total_urls, total_clicks } = response.data;

      // Update the HTML elements with the retrieved data
      const userFirstNameElement = document.getElementById("user-first_name");
      userFirstNameElement.textContent = response.data.first_name;

      // Update the HTML elements with the retrieved data
      const totalLinksElement = document.getElementById("total-links");
      totalLinksElement.textContent = total_urls;

      const totalClicksElement = document.getElementById("total-clicks");
      totalClicksElement.textContent = total_clicks;
    })
    .catch((error) => {
      console.error("Error retrieving dashboard stats:", error);
    });
});
