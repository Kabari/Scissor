// // // Get the URL parameters from the query string
// // const params = new URLSearchParams(window.location.search);
// // const shortUrl = params.get("short_url").value;

// // // Set the short URL in the HTML
// // document.getElementById("short-url").textContent = shortUrl;

// const access_token = localStorage.getItem("access_token");

// !!!!!!!!!!!!!!!!!!!!!!!!

document.addEventListener("DOMContentLoaded", function () {
  const access_token = localStorage.getItem("access_token");

  // Make a GET request to fetch the click data
  const urlParams = new URLSearchParams(window.location.search);
  const shortUrl = urlParams.get("shortURL");

  // Fetch the click information using Axios

  axios
    .get(`/url/analytics/${shortUrl}`, {
      headers: {
        Authorization: `Bearer ${access_token}`, // Replace with your JWT access token
      },
    })
    .then((response) => {
      const clickData = response.data;
      console.log("Click data:", clickData);

      // Get the table body element
      const tableBody = document.getElementById("clicks-table-body");

      // Loop through the click data and create table rows
      clickData.forEach((click) => {
        // Create a new row
        const row = document.createElement("tr");

        // Create cells for each column
        const clickIdCell = document.createElement("td");
        clickIdCell.textContent = click.click_id;
        row.appendChild(clickIdCell);

        const timestampCell = document.createElement("td");
        timestampCell.textContent = click.timestamp;
        row.appendChild(timestampCell);

        const referrerCell = document.createElement("td");
        referrerCell.textContent = click.referrer;
        row.appendChild(referrerCell);

        const userAgentCell = document.createElement("td");
        userAgentCell.textContent = click.user_agent;
        row.appendChild(userAgentCell);

        const ipAddressCell = document.createElement("td");
        ipAddressCell.textContent = click.ip_address;
        row.appendChild(ipAddressCell);

        // Append the row to the table body
        tableBody.appendChild(row);
      });

      // Generate chart data
      const chartLabels = clickData.map((click) => click.timestamp);
      const chartData = clickData.map((click) => click.click_id);

      // Get the chart canvas element
      const chartCanvas = document.getElementById("chart");

      // Create the chart
      const chart = new Chart(chartCanvas, {
        type: "bar", // Use bar chart type
        data: {
          labels: chartLabels,
          datasets: [
            {
              label: "Click ID",
              data: chartData,
              backgroundColor: "rgba(54, 162, 235, 0.5)",
              borderColor: "rgba(54, 162, 235, 1)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    })
    .catch((error) => {
      console.error("Failed to fetch click data:", error);
    });

  // !!!!!!!!!!!!!!!!!!!!!!
});