// Make a GET request to fetch the URL data
const linkList = document.querySelector(".link-list");
linkList.textContent = "";

const access_token = localStorage.getItem("access_token");
axios
  .get("/url/urls", {
    headers: {
      Authorization: `Bearer ${access_token}`, // Replace with your JWT access token
    },
  })
  .then((response) => {
    const urls = response.data;

    // Get the link list container
    const linkList = document.querySelector(".link-list");

    // Loop through the URLs and create link items
    urls.forEach((url) => {
      // Create a link item
      const linkItem = document.createElement("div");
      linkItem.classList.add("link-item");

      // Create the link content
      const linkContent = document.createElement("div");
      linkContent.classList.add("link-content");

      // Create the original URL element
      const originalUrl = document.createElement("div");
      originalUrl.classList.add("link-original-url");
      originalUrl.textContent = `Original URL: ${url.long_url}`;
      linkContent.appendChild(originalUrl);

      // Create the short CODE element
      const shortCode = document.createElement("div");
      shortCode.classList.add("link-short-code");
      const shortCodeLink = document.createElement("a");
      shortCodeLink.href = url.short_code;
      shortCodeLink.target = "_blank";
      shortCodeLink.rel = "noopener noreferrer";
      shortCodeLink.textContent = `Short Code: ${url.short_code}`;
      shortCode.appendChild(shortCodeLink);
      linkContent.appendChild(shortCode);

      // Create the short Url element
      const shortUrl = document.createElement("div");
      shortUrl.classList.add("link-short-url");
      const shortUrlLink = document.createElement("a");
      shortUrlLink.href = url.short_url;
      shortUrlLink.target = "_blank";
      shortUrlLink.rel = "noopener noreferrer";
      shortUrlLink.textContent = `Short Url: ${url.short_url}`;
      shortUrl.appendChild(shortUrlLink);
      linkContent.appendChild(shortUrl);

      // Create the custom Url element
      const customUrl = document.createElement("div");
      customUrl.classList.add("link-custom-url");
      const customUrlLink = document.createElement("a");
      customUrlLink.href = url.custom_url;
      customUrlLink.target = "_blank";
      customUrlLink.rel = "noopener noreferrer";
      customUrlLink.textContent = `custom Url: ${url.custom_url}`;
      customUrl.appendChild(customUrlLink);
      linkContent.appendChild(customUrl);

      // Create the date element
      const date = document.createElement("div");
      date.classList.add("link-date");
      date.textContent = `Date: ${formatDate(url.created_at)}`;
      linkContent.appendChild(date);

      // Append the link content to the link item
      linkItem.appendChild(linkContent);

      // Create the link actions
      const linkActions = document.createElement("div");
      linkActions.classList.add("link-actions");

      // Create the copy button
      const copyButton = document.createElement("button");
      copyButton.classList.add("copy-button");
      copyButton.textContent = "Copy";
      copyButton.addEventListener("click", () => {
        // Copy the short URL to the clipboard
        navigator.clipboard
          .writeText(url.short_url)
          .then(() => {
            alert("Short URL copied to clipboard!");
          })
          .catch((error) => {
            console.error("Failed to copy short URL:", error);
          });
      });
      linkActions.appendChild(copyButton);

      const trackPerformanceButton = document.createElement("button");
      trackPerformanceButton.classList.add("analytics-button");
      trackPerformanceButton.textContent = "Track Performance";
      linkActions.appendChild(trackPerformanceButton);
      trackPerformanceButton.addEventListener("click", () => {
        const shortCode = url.short_code;
        // window.open(`/url/analytics/${shortUrl}`, "_blank");
        window.location.href = `/analytics/${shortCode}`;
        // window.location.href = `/analytics?shortURL=${encodeURIComponent(shortUrl)}`;
      });

      // Create the QR code button
      const qrCodeButton = document.createElement("button");
      qrCodeButton.classList.add("qr-code-button");
      qrCodeButton.textContent = "QR Code";
      qrCodeButton.addEventListener("click", () => {
        const shortCode = url.short_code;
        // Open the QR code page for the selected URL
        // window.open(
        //   `/url/${encodeURIComponent(url.short_url)}/qr-code`,
        //   "_blank"
        // );
        window.location.href = `/qr-code/${shortCode}`;
      });

      linkActions.appendChild(qrCodeButton);

      // Create the Add Alias button
      const addAliasButton = document.createElement("button");
      addAliasButton.classList.add("add-alias");
      addAliasButton.textContent = "Add Alias";
      addAliasButton.addEventListener("click", () => {
        const shortCode = url.short_code;
        // Redirect to the custom URL page
        window.location.href = `/custom_url/${shortCode}`;
      });
      linkActions.appendChild(addAliasButton);

      // Create the other buttons (Edit, Add Alias, Track Performance, Categorize)
      // const buttons = [
      //   "edit-link",
      //   // "add-alias",
      //   // "track-performance",
      //   // "categorize-link",
      // ];
      // buttons.forEach((buttonClass) => {
      //   const button = document.createElement("button");
      //   button.classList.add(buttonClass);
      //   button.textContent = buttonClass.replace("-", " ");
      //   linkActions.appendChild(button);
      // });

      // Append the link actions to the link item
      linkItem.appendChild(linkActions);

      // Append the link item to the link list
      linkList.appendChild(linkItem);
    });
  })
  .catch((error) => {
    console.error("Failed to fetch URL data:", error);
  });

// Function to format the date
function formatDate(dateString) {
  const options = { year: "numeric", month: "long", day: "numeric" };
  const date = new Date(dateString);
  return date.toLocaleDateString(undefined, options);
}
// !!!!!!!!!!!!!!!!!!!!!!!!!!
