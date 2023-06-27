// Add this code to your "shorten.js" file or within a <script> tag in your HTML
const access_token = localStorage.getItem("access_token");

// const urlCard = document.querySelector(".url-card");
// urlCard.style.display = "none";

// Function to update the URL card with the returned data and show it
function updateUrlCard(data) {
  const longUrl = document.querySelector(".url-card .url-card-item .value");
  // const shortCode = document.querySelector(".shortened-code");
  const shortUrl = document.querySelector(".shortened-url");
  // const date = document.querySelector(".url-card .date");

  // longUrl.textContent = data.long_url;
  // shortCode.textContent = data.short_code;
  shortUrl.textContent = data.short_url;
  // date.textContent = formatDate(data.created_at); // You can customize the format of the date here

  // Show the URL card
  // const urlCard = document.querySelector(".url-card");
  // urlCard.style.display = "block";
}

// Function to handle the "Shorten" button click
function handleShortenButtonClick() {
  const longUrlInput = document.getElementById("long-url");
  const longUrl = longUrlInput.value;
  console.log(longUrl);
  // Make a POST request to the '/create' endpoint
  axios
    .post(
      "/url/create",
      { long_url: longUrl },
      {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      }
    )
    .then((response) => {
      const data = response.data;
      updateUrlCard(data);
    })
    .catch((error) => {
      console.error(error);
    });
}

// Attach the click event listener to the "Shorten" button
const shortenBtn = document.getElementById("shorten-btn");
shortenBtn.addEventListener("click", handleShortenButtonClick);

// Function to format the date in a desired format
function formatDate(dateString) {
  const options = { year: "numeric", month: "long", day: "numeric" };
  const date = new Date(dateString);
  return date.toLocaleDateString(undefined, options);
}


