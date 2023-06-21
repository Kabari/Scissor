// Login form event listener
const loginForm = document.getElementById("login-form");
loginForm.addEventListener("submit", async (event) => {
  event.preventDefault(); // Prevent the default form submission

  // Get the form inputs
  const emailInput = document.getElementById("email");
  const passwordInput = document.getElementById("password");

  // Create the login data object
  const loginData = {
    email: emailInput.value,
    password: passwordInput.value,
  };

  // Send the login request using Axios
  try {
    const response = await axios.post("/auth/login", loginData);
    const { access_token, refresh_token } = response.data;
    // Storing tokens in local storage
    localStorage.setItem("access_token", access_token);
    localStorage.setItem("refresh_token", refresh_token);
    // Redirecting to the dashboard page
    window.location.href = "/dashboard";
  } catch (error) {
    console.error("Login failed:", error);
    // Handle error: Display an error message or perform any other actions
  }
});

// // document.addEventListener("DOMContentLoaded", () => {
// const loginButton = document.getElementById("login-button");
// loginButton.addEventListener("click", async (event) => {
//   // alert("login button clicked");
//   event.preventDefault(); // Prevent the default form submission

//   const email = document.getElementById("email").value;
//   const password = document.getElementById("password").value;

//   console.log(email, password);
//   try {
//     const response = await axios.post("/auth/login", {
//       email: email.value,
//       password: password.value,
//     });

//     // Assuming the response contains access_token and refresh_token
//     const { access_token, refresh_token } = response.data;

//     // Storing tokens in local storage
//     localStorage.setItem("access_token", access_token);
//     localStorage.setItem("refresh_token", refresh_token);

//     // Redirecting to the dashboard page
//     window.location.href = "/dashboard";
//   } catch (error) {
//     console.error("Login failed:", error);
//     // Handle error: Display an error message or perform any other actions
//   }
// });
// // });
