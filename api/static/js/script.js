// JavaScript code for the Landing Page

// Add click event listener to the "Get Started" button
// const getStartedButton = document.getElementById("get-started-button");
// getStartedButton.addEventListener("click", () => {
//   // Redirect to the Shorten URL Page
//   window.location.href = "/signup";
// });

// const signupLink = document.getElementById("signup-link");
// signupLink.addEventListener("click", () => {
//   console.log("heyo")
//   // Redirect to the Shorten URL Page
//   window.location.href = "/signup";
// });

// const loginLink = document.getElementById("login-link");
// loginLink.addEventListener("click", () => {
//   console.log("Na me")
//   // Redirect to the Shorten URL Page
//   window.location.href = "/login";
// });

// const logLink = document.getElementById("loger-link");
// logLink.addEventListener("click", () => {
//   console.log("Na me")
//   // Redirect to the Shorten URL Page
//   window.location.href = "/login";
// });

// const regLink = document.getElementById("reg-link");
// regLink.addEventListener("click", () => {
//   console.log("heyo")
//   // Redirect to the Shorten URL Page
//   window.location.href = "/signup";
// });

// // JavaScript code for the Shorten URL Page

// // Add click event listener to the "Shorten" button
// const shortenButton = document.getElementById("shorten-button");
// shortenButton.addEventListener("click", () => {
//   // Get the long URL input value
//   const longUrlInput = document.getElementById("long-url-input");
//   const longUrl = longUrlInput.value;

//   // TODO: Validate the long URL input value

//   // TODO: Send an API request to shorten the URL

//   // TODO: Handle the response and update the UI accordingly
// });

// // JavaScript code for the Link History Page

// // Add click event listener to the links in the table
// const linkTable = document.getElementById("link-table");
// linkTable.addEventListener("click", (event) => {
//   if (event.target.tagName === "A") {
//     // Get the clicked link URL
//     const clickedLinkUrl = event.target.href;

//     // TODO: Handle the clicked link URL (e.g., open it in a new tab)
//   }
// });

// // JavaScript code for the Analytics Page

// // Add click event listener to the "View Analytics" button
// const viewAnalyticsButton = document.getElementById("view-analytics-button");
// viewAnalyticsButton.addEventListener("click", () => {
//   // TODO: Send an API request to fetch the analytics data

//   // TODO: Handle the response and update the UI accordingly
// });

// // JavaScript code for the QR Code Page

// // Add event listener to generate QR code button
// const generateQRCodeButton = document.getElementById("generate-qrcode-button");
// generateQRCodeButton.addEventListener("click", () => {
//   // Get the current URL
//   const currentUrl = window.location.href;

//   // TODO: Send an API request to generate the QR code

//   // TODO: Handle the response and display the QR code
// });

// // JavaScript code for the Login Page

// // Add click event listener to the "Login" button
// const loginButton = document.getElementById("login-button");
// loginButton.addEventListener("click", () => {
//   // Get the username and password input values
//   const usernameInput = document.getElementById("username-input");
//   const passwordInput = document.getElementById("password-input");
//   const username = usernameInput.value;
//   const password = passwordInput.value;

//   // TODO: Validate the username and password inputs

//   // TODO: Send an API request to authenticate the user

//   // TODO: Handle the response and redirect to the appropriate page
// });

// // JavaScript code for the Registration Page

// // Add click event listener to the "Register" button
// const registerButton = document.getElementById("register-button");
// registerButton.addEventListener("click", () => {
//   // Get the registration form input values
//   const usernameInput = document.getElementById("username-input");
//   const passwordInput = document.getElementById("password-input");
//   const confirmPasswordInput = document.getElementById("confirm-password-input");
//   const emailInput = document.getElementById("email-input");
//   const username = usernameInput.value;
//   const password = passwordInput.value;
//   const confirmPassword = confirmPasswordInput.value;
//   const email = emailInput.value;

//   // TODO: Validate the registration form inputs

//   // TODO: Send an API request to register the user

//   // TODO: Handle the response and redirect to the appropriate page
// });

// // JavaScript code for the Error Page

// // Add click event listener to the "Go Back" button
// const goBackButton = document.getElementById("go-back-button");
// goBackButton.addEventListener("click", () => {
//   // Navigate back to the previous page
//   window.history.back();
// });

// // JavaScript code for the History Page

// // Retrieve the link history data from the API
// function fetchLinkHistory() {
//   // TODO: Send an API request to fetch the link history data

//   // TODO: Handle the response and update the UI accordingly
// }

// // Function to format the date and time
// function formatDateTime(dateString) {
//   // TODO: Implement the logic to format the date and time

//   return formattedDateTime;
// }

// // Function to render the link history table
// function renderLinkHistoryTable(data) {
//   const tableBody = document.getElementById("link-history-table-body");
//   tableBody.innerHTML = "";

//   // Iterate over the link history data and populate the table
//   data.forEach((link) => {
//     const row = document.createElement("tr");

//     const linkCell = document.createElement("td");
//     const linkAnchor = document.createElement("a");
//     linkAnchor.href = link.url;
//     linkAnchor.textContent = link.url;
//     linkCell.appendChild(linkAnchor);

//     const shortLinkCell = document.createElement("td");
//     shortLinkCell.textContent = link.shortUrl;

//     const dateTimeCell = document.createElement("td");
//     const formattedDateTime = formatDateTime(link.dateTime);
//     dateTimeCell.textContent = formattedDateTime;

//     row.appendChild(linkCell);
//     row.appendChild(shortLinkCell);
//     row.appendChild(dateTimeCell);

//     tableBody.appendChild(row);
//   });
// }

// // Fetch the link history when the page loads
// document.addEventListener("DOMContentLoaded", () => {
//   fetchLinkHistory();
// });

// // JavaScript code for the Analytics Page

// // Retrieve the analytics data from the API
// function fetchAnalyticsData() {
//   // TODO: Send an API request to fetch the analytics data

//   // TODO: Handle the response and update the UI accordingly
// }

// // Function to render the analytics chart
// function renderAnalyticsChart(data) {
//   // TODO: Implement the logic to render the analytics chart
// }

// // Fetch the analytics data when the page loads
// document.addEventListener("DOMContentLoaded", () => {
//   fetchAnalyticsData();
// });

// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!Register Endpoint

// // document

//! ?????? Signup form submission handler!!

//!!!! Login form submission handler
// // Assuming you have imported the Axios library

const shortenLink = document.getElementById("shorten-link");
shortenLink.addEventListener("click", () => {
  window.location.href = "/create";
});

// const openLink = document.getElementById("link-history-button");
// openLink.addEventListener("click", () => {
//   window.location.href = "/link-man";
// });


// Add this code to your script.js file or within a <script> tag in your HTML

// // Function to update the URL card with the returned data and show it
// function updateUrlCard(data) {
//   const urlCard = document.querySelector('.url-card');
//   const longUrl = document.querySelector('.url-card .long-url');
//   const shortUrl = document.querySelector('.url-card .short-url');
//   const date = document.querySelector('.url-card .date');

//   longUrl.textContent = data.long_url;
//   shortUrl.textContent = data.short_url;
//   date.textContent = formatDate(data.created_at); // You can customize the format of the date here
//   urlCard.style.display = 'block';
// }

// // Function to handle form submission
// function handleFormSubmit(event) {
//   event.preventDefault();

//   const longUrlInput = document.getElementById('long-url');
//   const longUrl = longUrlInput.value;

//   // Make a POST request to the '/create' endpoint
//   axios.post('/create', { long_url: longUrl })
//     .then(response => {
//       const data = response.data;
//       updateUrlCard(data);
//     })
//     .catch(error => {
//       console.error(error);
//     });
// }

// // Attach the form submission event listener
// const form = document.getElementById('shorten-url-form');
// form.addEventListener('submit', handleFormSubmit);

// // Function to format the date in a desired format
// function formatDate(dateString) {
//   const options = { year: 'numeric', month: 'long', day: 'numeric' };
//   const date = new Date(dateString);
//   return date.toLocaleDateString(undefined, options);
// }

// // Hide the URL card by default
// document.querySelector('.url-card').style.display = 'none';

// // Function to show the URL card when the "Shorten" button is clicked
// function showUrlCard() {
//   document.querySelector('.url-card').style.display = 'block';
// }

// // Attach the click event listener to the "Shorten" button
// const shortenBtn = document.getElementById('shorten-btn');
// shortenBtn.addEventListener('click', showUrlCard);

//!!!!!!! Function to handle the "Logout" button click
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
const logoutBtn = document.getElementById("logout-btn");
logoutBtn.addEventListener("click", handleLogoutButtonClick);

//!! Redirect to Original URL
function redirectToLongUrl(shortUrl) {
  axios
    .get(`http://127.0.0.1:5000/url/${shortUrl}`)
    .then((response) => {
      // Handle the redirect on the client-side
      window.location.href = response.request.responseURL;
    })
    .catch((error) => {
      console.error(error);
      // Handle error, e.g., display an error message to the user
    });
}



// !!
// !!!Make a GET request to fetch the URL data
// function handleLinkHistoryButtonClick() {
//   // Make a GET request to fetch the URL data
//   const access_token = localStorage.getItem("access_token");
//   axios
//     .get("/url/urls", {
//       headers: {
//         Authorization: `Bearer ${access_token}`, // Replace with your JWT access token
//       },
//     })
//     .then((response) => {
//       const urls = response.data;

//       // Get the link list container
//       const linkList = document.querySelector(".link-list");

//       // Loop through the URLs and create link items
//       urls.forEach((url) => {
//         // Create a link item
//         const linkItem = document.createElement("div");
//         linkItem.classList.add("link-item");

//         // Create the link content
//         const linkContent = document.createElement("div");
//         linkContent.classList.add("link-content");

//         // Create the original URL element
//         const originalUrl = document.createElement("div");
//         originalUrl.classList.add("link-original-url");
//         originalUrl.textContent = `Original URL: ${url.long_url}`;
//         linkContent.appendChild(originalUrl);

//         // Create the short URL element
//         const shortUrl = document.createElement("div");
//         shortUrl.classList.add("link-short-url");
//         const shortUrlLink = document.createElement("a");
//         shortUrlLink.href = url.short_url;
//         shortUrlLink.target = "_blank";
//         shortUrlLink.rel = "noopener noreferrer";
//         shortUrlLink.textContent = `Short URL: ${url.short_url}`;
//         shortUrl.appendChild(shortUrlLink);
//         linkContent.appendChild(shortUrl);

//         // Create the date element
//         const date = document.createElement("div");
//         date.classList.add("link-date");
//         date.textContent = `Date: ${url.created_at}`;
//         linkContent.appendChild(date);

//         // Append the link content to the link item
//         linkItem.appendChild(linkContent);

//         // Create the link actions
//         const linkActions = document.createElement("div");
//         linkActions.classList.add("link-actions");
        
//         // Create the copy button
//         const copyButton = document.createElement("button");
//         copyButton.classList.add("copy-button");
//         copyButton.textContent = "Copy";
//         copyButton.addEventListener("click", () => {
//           // Copy the short URL to the clipboard
//           navigator.clipboard
//           .writeText(url.short_url)
//           .then(() => {
//             alert("Short URL copied to clipboard!");
//           })
//           .catch((error) => {
//             console.error("Failed to copy short URL:", error);
//           });
//         });
//         linkActions.appendChild(copyButton);
        
//         // Create the other buttons (Edit, Add Alias, Track Performance, Categorize)
//         const buttons = [
//           "edit-link",
//           "add-alias",
//           "track-performance",
//           "categorize-link",
//         ];
//         buttons.forEach((buttonClass) => {
//           const button = document.createElement("button");
//           button.classList.add(buttonClass);
//           button.textContent = buttonClass.replace("-", " ");
//           linkActions.appendChild(button);
//         });

//         // Append the link actions to the link item
//         linkItem.appendChild(linkActions);

//         // Append the link item to the link list
//         linkList.appendChild(linkItem);
//       });
//     })
//     .catch((error) => {
//       console.error("Failed to fetch URL data:", error);
//     });
//     // window.location.href = "/link-man";
// }

// // Get the "Link History" button element
// const linkHistoryButton = document.getElementById("link-history-button");

// // Add the click event handler
// linkHistoryButton.addEventListener("click", handleLinkHistoryButtonClick);









// ////////////////////////////////////////////////////////////////!!!!!!




// function handleLinkHistoryButtonClick() {
//   // Redirect to the "link-man" page
//   window.location.href = "/link-man";

//   // Delay before making the API request
//   setTimeout(() => {
//     // Make a GET request to fetch the URL data
//     const access_token = localStorage.getItem("access_token");
//     axios
//       .get("/url/urls", {
//         headers: {
//           Authorization: `Bearer ${access_token}`, // Replace with your JWT access token
//         },
//       })
//       .then((response) => {
//         const urls = response.data;

//         // Get the link list container
//         const linkList = document.querySelector(".link-list");

//         // Loop through the URLs and create link items
//         urls.forEach((url) => {
//           // Create a link item
//           const linkItem = document.createElement("div");
//           linkItem.classList.add("link-item");

//           // ... Rest of the code to create link content, buttons, etc.
//           // Create the link content
//           const linkContent = document.createElement("div");
//           linkContent.classList.add("link-content");

//           // Create the original URL element
//           const originalUrl = document.createElement("div");
//           originalUrl.classList.add("link-original-url");
//           originalUrl.textContent = `Original URL: ${url.long_url}`;
//           linkContent.appendChild(originalUrl);

//           // Create the short URL element
//           const shortUrl = document.createElement("div");
//           shortUrl.classList.add("link-short-url");
//           const shortUrlLink = document.createElement("a");
//           shortUrlLink.href = url.short_url;
//           shortUrlLink.target = "_blank";
//           shortUrlLink.rel = "noopener noreferrer";
//           shortUrlLink.textContent = `Short URL: ${url.short_url}`;
//           shortUrl.appendChild(shortUrlLink);
//           linkContent.appendChild(shortUrl);

//           // Create the date element
//           const date = document.createElement("div");
//           date.classList.add("link-date");
//           date.textContent = `Date: ${url.created_at}`;
//           linkContent.appendChild(date);

//           // Append the link content to the link item
//           linkItem.appendChild(linkContent);

//           // Create the link actions
//           const linkActions = document.createElement("div");
//           linkActions.classList.add("link-actions");
        
//           // Create the copy button
//           const copyButton = document.createElement("button");
//           copyButton.classList.add("copy-button");
//           copyButton.textContent = "Copy";
//           copyButton.addEventListener("click", () => {
//             // Copy the short URL to the clipboard
//             navigator.clipboard
//             .writeText(url.short_url)
//             .then(() => {
//               alert("Short URL copied to clipboard!");
//             })
//             .catch((error) => {
//               console.error("Failed to copy short URL:", error);
//             });
//           });
//           linkActions.appendChild(copyButton);
        
//           // Create the other buttons (Edit, Add Alias, Track Performance, Categorize)
//           const buttons = [
//             "edit-link",
//             "add-alias",
//             "track-performance",
//             "categorize-link",
//           ];
//           buttons.forEach((buttonClass) => {
//             const button = document.createElement("button");
//             button.classList.add(buttonClass);
//             button.textContent = buttonClass.replace("-", " ");
//             linkActions.appendChild(button);
//           });

//           // Append the link actions to the link item
//           linkItem.appendChild(linkActions);



//           // Append the link item to the link list
//           linkList.appendChild(linkItem);
//         });
//       })
//       .catch((error) => {
//         console.error("Failed to fetch URL data:", error);
//       });
//   }, 1000); // Adjust the delay duration as needed
// }

// // Get the "Link History" button element
// const linkHistoryButton = document.getElementById("link-history-button");

// // Add the click event handler
// linkHistoryButton.addEventListener("click", handleLinkHistoryButtonClick);




const linkHistoryButton = document.getElementById("link-history-button");

// Add the click event handler
linkHistoryButton.addEventListener("click", () => {
  window.location.href = "/link-man";
});















// Retrieve data for pie chart
const pieChartData = {
  labels: ["Red", "Blue", "Yellow"],
  datasets: [
    {
      data: [10, 20, 30],
      backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
      hoverBackgroundColor: ["#FF6384", "#36A2EB", "#FFCE56"],
    },
  ],
};

// Create pie chart instance
const pieChartCtx = document.getElementById("pieChart").getContext("2d");
const pieChart = new Chart(pieChartCtx, {
  type: "pie",
  data: pieChartData,
  options: {
    responsive: true,
    maintainAspectRatio: false,
    // Configure other chart options as needed
  },
});

// Retrieve data for line graph
const lineGraphData = {
  labels: ["January", "February", "March", "April", "May", "June"],
  datasets: [
    {
      label: "Data",
      data: [12, 19, 3, 5, 2, 3],
      fill: false,
      borderColor: "#FF6384",
      backgroundColor: "#FF6384",
      tension: 0.1,
    },
  ],
};

// Create line graph instance
const lineGraphCtx = document.getElementById("lineGraph").getContext("2d");
const lineGraph = new Chart(lineGraphCtx, {
  type: "line",
  data: lineGraphData,
  options: {
    responsive: true,
    maintainAspectRatio: false,
    // Configure other chart options as needed
  },
});

// !!!!!!!!!!!!!!!!!!!!!
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
