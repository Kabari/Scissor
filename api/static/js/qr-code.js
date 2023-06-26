// Get the short URL and access token from the template
// const shortUrl = "{{ short_url }}";

const access_token = localStorage.getItem("access_token");
// Function to extract the short URL from the current page URL
const currentUrl = window.location.href;
const urlParts = currentUrl.split("/");
const shortUrl = urlParts[urlParts.length - 1];



// Make a GET request to fetch the QR code image
axios
  .get(`/url/qr-code/${shortUrl}`, {
    headers: {
      Authorization: `Bearer ${access_token}`,
    },
    responseType: "blob",
  })
  .then((response) => {
    // Create a URL object from the response data
    const qrCodeBlob = new Blob([response.data], { type: "image/png" });
    const qrCodeUrl = URL.createObjectURL(qrCodeBlob);

    // Display the QR code image
    const qrCodeImage = document.getElementById("qr-code-image");
    qrCodeImage.src = qrCodeUrl;
    qrCodeImage.alt = "QR Code";

    // Add event listener to the download button
    const downloadButton = document.getElementById("download-button");
    downloadButton.addEventListener("click", () => {
      // Create a temporary link element for downloading the QR code
      const downloadLink = document.createElement("a");
      downloadLink.href = qrCodeUrl;
      downloadLink.download = "qrcode.png";
      downloadLink.style.display = "none";

      // Append the link element to the document body
      document.body.appendChild(downloadLink);

      // Simulate a click event on the link element to trigger the download
      downloadLink.click();

      // Clean up the URL object and remove the link element after use
      URL.revokeObjectURL(qrCodeUrl);
      document.body.removeChild(downloadLink);
    });
  })
  .catch((error) => {
    console.error("Failed to fetch QR code image:", error);
  });
  // .then((response) => {
  //   //   const qrCodeImageUrl = response.data.qr_code_image;

  //   //   // Display the QR code image
  //   //   const qrCodeContainer = document.querySelector(".qr-code-container");
  //   //   qrCodeContainer.innerHTML = `<img src="${qrCodeImageUrl}" alt="QR Code">`;
  //   // })

  //   // Create a URL object from the response data
  //   const qrCodeBlob = new Blob([response.data], { type: "image/png" });
  //   const qrCodeUrl = URL.createObjectURL(qrCodeBlob);

  //   // Display the QR code image
  //   const qrCodeImage = document.getElementById("qr-code-image");
  //   qrCodeImage.src = qrCodeUrl;
  //   qrCodeImage.alt = "QR Code";

  //   // Create a temporary link element for downloading the QR code
  //   // const downloadLink = document.createElement("a");
  //   // downloadLink.href = qrCodeUrl;
  //   // downloadLink.download = "qrcode.png";
  //   // downloadLink.style.display = "none";

  //   // Append the link element to the document body
  //   // document.body.appendChild(downloadLink);

  //   // Simulate a click event on the link element to trigger the download
  //   // downloadLink.click();

  //   // Clean up the URL object and remove the link element after use
  //   // URL.revokeObjectURL(qrCodeUrl);
  //   // document.body.removeChild(downloadLink);
  // })

  // .catch((error) => {
  //   console.error("Failed to fetch QR code image:", error);
  // });

// const access_token = localStorage.getItem("access_token");

// // Function to extract the short URL from the current page URL
// function getShortUrlFromCurrentPageUrl() {
//   const currentUrl = window.location.href;
//   const urlParts = currentUrl.split("/");
//   const shortUrl = urlParts[urlParts.length - 2];
//   return shortUrl;
// }

// // Function to fetch the QR code image URL from the server
// function fetchQRCodeImageUrl(shortUrl) {
//   // Set the API endpoint URL for fetching the QR code image
//   const apiUrl = `/url/${shortUrl}/qr-code`;

//   // Send a GET request to the API endpoint
//   return axios
//     .get(apiUrl, {
//       headers: {
//         Authorization: `Bearer ${access_token}`, // Replace with your JWT access token
//       },
//     })
//     .then((response) => {
//       // Return the QR code image URL from the response
//       return response.data.qr_code_image_url;
//     })
//     .catch((error) => {
//       console.error("Failed to fetch QR code image URL:", error);
//       throw error;
//     });
// }

// // Function to display the QR code image on the page
// function displayQRCodeImage(qrCodeImageUrl) {
//   // Get the QR code image element
//   const qrCodeImage = document.getElementById("qr-code-image");

//   // Set the src attribute of the QR code image element
//   qrCodeImage.src = qrCodeImageUrl;
// }

// // When the page is loaded
// window.addEventListener("load", function () {
//   // Get the short URL from the current page URL
//   const shortUrl = getShortUrlFromCurrentPageUrl();

//   // Fetch the QR code image URL from the server
//   fetchQRCodeImageUrl(shortUrl)
//     .then((qrCodeImageUrl) => {
//       // Display the QR code image on the page
//       displayQRCodeImage(qrCodeImageUrl);
//     })
//     .catch((error) => {
//       console.error("Failed to load QR code:", error);
//     });
// });
