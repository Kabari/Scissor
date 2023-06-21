// Signup form event listener
const signupForm = document.getElementById("signup-form");
signupForm.addEventListener("submit", async (event) => {
  event.preventDefault(); // Prevent the default form submission

  // Get the form inputs
  const firstNameInput = document.getElementById("firstName");
  const lastNameInput = document.getElementById("lastName");
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");
  const confirmPasswordInput = document.getElementById("confirmPassword");

  // Create the signup data object
  const signupData = {
    first_name: firstNameInput.value,
    last_name: lastNameInput.value,
    email: emailInput.value,
    password: passwordInput.value,
    confirm_password: confirmPasswordInput.value,
  };

  // Send the signup request using Axios
  try {
    const response = await axios.post("/auth/signup", signupData);
    if (response.status === 201) {
      // Registration successful, redirect to login page
      window.location.href = "/login";
    } else {
      // Registration failed, handle error
      console.log("Registration Error:", response.data.message);
    }
  } catch (error) {
    console.log("Request Error:", error);
  }
});

// const signupButton = document.getElementById("signup-button");
// signupButton.addEventListener("click", async (event) => {
//   event.preventDefault(); // Prevent the default form submission

//   // Get the form inputs
//   const firstNameInput = document.getElementById("firstName");
//   const lastNameInput = document.getElementById("lastName");
//   const emailInput = document.getElementById("email");
//   const passwordInput = document.getElementById("password");
//   const confirmPasswordInput = document.getElementById("confirmPassword");

//   // Create the signup data object
//   const signupData = {
//     first_name: firstNameInput.value,
//     last_name: lastNameInput.value,
//     email: emailInput.value,
//     password: passwordInput.value,
//     confirm_password: confirmPasswordInput.value,
//   };

//   // Send the signup request using Axios
//   try {
//     const response = await axios.post("/auth/signup", signupData);
//     if (response.status === 201) {
//       // Registration successful, redirect to login page
//       window.location.href = "/login";
//     } else {
//       // Registration failed, handle error
//       console.log("Registration Error:", response.data.message);
//     }
//   } catch (error) {
//     console.log("Request Error:", error);
//   }
// });





// // Function to handle the "Link History" button click event
// function handleLinkHistoryButtonClick() {
//   // Make a GET request to fetch the URL data
//   const access_token = localStorage.getItem("access_token");
//   axios
//     .get("/urls", {
//       headers: {
//         Authorization: `Bearer ${access_token}`,
//       },
//     })
//     .then((response) => {
//       const urls = response.data;

//       // Get the link list container
//       const linkList = document.querySelector(".link-list");

//       // Clear the existing link items
//       linkList.innerHTML = "";

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
//         originalUrl.textContent = `Original URL: ${url.original_url}`;
//         linkContent.appendChild(originalUrl);

//         // Create the short URL element
//         const shortUrl = document.createElement("div");
//         shortUrl.classList.add("link-short-url");
//         const shortUrlLink = document.createElement("a");
//         shortUrlLink.href = url.short_url;
//         shortUrlLink.target = "_blank";
//         shortUrlLink.rel = "noopener noreferrer";
//         shortUrlLink.textContent = `${url.short_url}`;
//         shortUrl.appendChild(shortUrlLink);
//         linkContent.appendChild(shortUrl);

//         // Create the date element
//         const date = document.createElement("div");
//         date.classList.add("link-date");
//         date.textContent = `Date: ${formatDate(url.date)}`;
//         linkContent.appendChild(date);

//         // Append the link content to the link item
//         linkItem.appendChild(linkContent);

//         // Append the link item to the link list
//         linkList.appendChild(linkItem);
//       });
//     })
//     .catch((error) => {
//       console.error("Failed to fetch URL data:", error);
//     });
// }

// // Get the "Link History" button element
// const linkHistoryButton = document.getElementById("link-history-button");

// // Add the click event handler
// linkHistoryButton.addEventListener("click", handleLinkHistoryButtonClick);
