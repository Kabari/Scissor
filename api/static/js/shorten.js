// !!!!!!! Function to handle the "Logout" button click
function handleLogoutButtonClick() {
  const accessToken = localStorage.getItem("access_token");

  // Make a POST request to the '/logout' endpoint
  console.log("axios is working well");
  axios
    .post(
      "/auth/logout",
      {},
      {
        headers: {
          Authorization: `Bearer ${accessToken}`, // Include the access token in the Authorization header
        },
      }
    )
    .then((response) => {
      // Clear the access token from local storage
      localStorage.removeItem("access_token");

      // Redirect the user to the login page or perform any other action
      window.location.href = "/login"; // Replace "/login" with the appropriate login page URL
    })
    .catch((error) => {
      console.error(error);
    });
}

// Attach the click event listener to the "Logout" button
const logoutBtn = document.querySelector(".logout-btn");
logoutBtn.addEventListener("click", handleLogoutButtonClick);

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

//!!!! copy link to clipboard!!
function copyToClipboard() {
  // Get the shortened URL element
  var shortenedUrlElement = document.getElementById("shortened-url");

  // Create a temporary textarea element
  var textarea = document.createElement("textarea");
  textarea.value = shortenedUrlElement.textContent;
  document.body.appendChild(textarea);

  // Select the text within the textarea
  textarea.select();

  try {
    // Execute the copy command
    var successful = document.execCommand("copy");
    var message = successful ? "URL copied!" : "Copy failed!";
    alert(message);
  } catch (err) {
    console.error("Error copying URL: ", err);
  }

  // Clean up and remove the temporary textarea element
  document.body.removeChild(textarea);
}

var copyButton = document.getElementById("copy-btn");
copyButton.addEventListener("click", copyToClipboard);
