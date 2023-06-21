// Add this code to your "shorten.js" file or within a <script> tag in your HTML

const urlCard = document.querySelector(".url-card");
urlCard.style.display = "none";

// Function to update the URL card with the returned data and show it
function updateUrlCard(data) {
  const longUrl = document.querySelector(".url-card .url-card-item .value");
  const shortUrl = document.querySelector(".shortened-url");
  const date = document.querySelector(".url-card .date");

  longUrl.textContent = data.long_url;
  shortUrl.textContent = data.short_url;
  date.textContent = formatDate(data.created_at); // You can customize the format of the date here

  // Show the URL card
  const urlCard = document.querySelector(".url-card");
  urlCard.style.display = "block";
}

// Function to handle the "Shorten" button click
function handleShortenButtonClick() {
  const longUrlInput = document.getElementById("long-url");
  const longUrl = longUrlInput.value;
  const access_token = localStorage.getItem("access_token");
  console.log(longUrl);
  // Make a POST request to the '/create' endpoint
  axios
    .post(
      "/url/create",
      { long_url: longUrl },
      {
        headers: {
          Authorization: `Bearer ${access_token}`
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

// Hide the URL card by default

// Function to show the URL card when the "Shorten" button is clicked
// function showUrlCard() {
//   urlCard.style.display = "block";
// }

// Attach the click event listener to the "Shorten" button
// const shortenBtn = document.getElementById("shorten-btn");
// shortenBtn.addEventListener("click", showUrlCard);















// axios
//   .get("/url/urls", {
//     headers: {
//       Authorization: "Bearer your-access-token", // Replace with your JWT access token
//     },
//   })
//   .then((response) => {
//     const urls = response.data;

//     // Get the link list container
//     const linkList = document.querySelector(".link-list");

//     // Loop through the URLs and create link items
//     urls.forEach((url) => {
//       // Create a link item
//       const linkItem = document.createElement("div");
//       linkItem.classList.add("link-item");

//       // Create the link content
//       const linkContent = document.createElement("div");
//       linkContent.classList.add("link-content");

//       // Create the original URL element
//       const originalUrl = document.createElement("div");
//       originalUrl.classList.add("link-original-url");
//       originalUrl.textContent = `Original URL: ${url.original_url}`;
//       linkContent.appendChild(originalUrl);

//       // Create the short URL element
//       const shortUrl = document.createElement("div");
//       shortUrl.classList.add("link-short-url");
//       const shortUrlLink = document.createElement("a");
//       shortUrlLink.href = url.short_url;
//       shortUrlLink.target = "_blank";
//       shortUrlLink.rel = "noopener noreferrer";
//       shortUrlLink.textContent = `Short URL: ${url.short_url}`;
//       shortUrl.appendChild(shortUrlLink);
//       linkContent.appendChild(shortUrl);

//       // Create the date element
//       const date = document.createElement("div");
//       date.classList.add("link-date");
//       date.textContent = `Date: ${url.date}`;
//       linkContent.appendChild(date);

//       // Append the link content to the link item
//       linkItem.appendChild(linkContent);

//       // Create the link actions
//       const linkActions = document.createElement("div");
//       linkActions.classList.add("link-actions");

//       // Create the copy button
//       const copyButton = document.createElement("button");
//       copyButton.classList.add("copy-button");
//       copyButton.textContent = "Copy";
//       copyButton.addEventListener("click", () => {
//         // Copy the short URL to the clipboard
//         navigator.clipboard
//           .writeText(url.short_url)
//           .then(() => {
//             alert("Short URL copied to clipboard!");
//           })
//           .catch((error) => {
//             console.error("Failed to copy short URL:", error);
//           });
//       });
//       linkActions.appendChild(copyButton);

//       // Create the other buttons (Edit, Add Alias, Track Performance, Categorize)
//       const buttons = [
//         "edit-link",
//         "add-alias",
//         "track-performance",
//         "categorize-link",
//       ];
//       buttons.forEach((buttonClass) => {
//         const button = document.createElement("button");
//         button.classList.add(buttonClass);
//         button.textContent = buttonClass.replace("-", " ");
//         linkActions.appendChild(button);
//       });

//       // Append the link actions to the link item
//       linkItem.appendChild(linkActions);

//       // Append the link item to the link list
//       linkList.appendChild(linkItem);
//     });
//   })
//   .catch((error) => {
//     console.error("Failed to fetch URL data:", error);
//   });