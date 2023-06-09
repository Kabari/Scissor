document.addEventListener("DOMContentLoaded", function () {
  const access_token = localStorage.getItem("access_token");

  const currentUrl = window.location.href;
  const urlParts = currentUrl.split("/");
  const shortCode = urlParts[urlParts.length - 1];

  // Make a request to the analytics endpoint
  axios
    .get(`/url/analytics/${shortCode}`, {
      headers: {
        Authorization: `Bearer ${access_token}`, // Replace with your JWT access token
      },
    })
    .then((response) => {
      // Render the response in the HTML
      const clickData = response.data.clicks;
      console.log("Click data:", clickData);

      // Use the analyticsData to update your HTML elements accordingly

      const shortCodeSpan = document.getElementById("short_code");
      shortCodeSpan.textContent = shortCode;

      // Get the table body element
      const tableBody = document.getElementById("clicks-table-body");

      // Clear existing table rows
      tableBody.innerHTML = "";

      // Loop through the click data and create table rows
      clickData.forEach((click) => {
        // Create a new row
        const row = document.createElement("tr");

        // Create cells for each column
        const clickIdCell = document.createElement("td");
        clickIdCell.textContent = click.id;
        row.appendChild(clickIdCell);

        const ipAddressCell = document.createElement("td");
        ipAddressCell.textContent = click.ip_address;
        row.appendChild(ipAddressCell);
        
                const referrerCell = document.createElement("td");
                referrerCell.textContent = click.referrer;
                row.appendChild(referrerCell);

        const timestampCell = document.createElement("td");
        timestampCell.textContent = click.timestamp;
        row.appendChild(timestampCell);

        const userAgentCell = document.createElement("td");
        userAgentCell.textContent = click.user_agent;
        row.appendChild(userAgentCell);


        // Append the row to the table body
        tableBody.appendChild(row);
      });
    })
    .catch((error) => {
      console.error("Error retrieving analytics:", error);
    });
});

