// // // Create the track performance button
// const performanceButton = document.getElementById("analytics-button");
// // performanceButton.classList.add("analytics-button");
// // performanceButton.textContent = "Track Performance";
// performanceButton.addEventListener("click", () => {
//   // Open the analytics page for the selected URL
//   alert("I am here");
//   console.log("commandant called!!!");
//   window.open(`/url/${url.short_url}/analytics`, "_blank");
// });

// Make a GET request to fetch the URL data
// const linkList = document.querySelector(".link-list");
// linkList.textContent = "";

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

      // Create the short URL element
      const shortUrl = document.createElement("div");
      shortUrl.classList.add("link-short-url");
      const shortUrlLink = document.createElement("a");
      shortUrlLink.href = url.short_url;
      shortUrlLink.target = "_blank";
      shortUrlLink.rel = "noopener noreferrer";
      shortUrlLink.textContent = `Short URL: ${url.short_url}`;
      shortUrl.appendChild(shortUrlLink);
      linkContent.appendChild(shortUrl);

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

      // Create the track performance button
      const trackPerformanceButton = document.createElement("button");
      trackPerformanceButton.classList.add("analytics-button");
      trackPerformanceButton.textContent = "Track Performance";
      linkActions.appendChild(trackPerformanceButton);
      trackPerformanceButton.addEventListener("click", () => {
        //
        // Open the analytics page for the selected URL
        window.open(
          `/analytics?shortURL=${encodeURIComponent(url.short_url)}`,
          "_blank"
        );
        // window.open(`/url/${encodeURIComponent(url.short_url)}/analytics`, "_blank");
        // console.log("commandant called!!!");
      });

      // Create the other buttons (Edit, Add Alias, Track Performance, Categorize)
      const buttons = [
        "edit-link",
        "add-alias",
        // "track-performance",
        "categorize-link",
      ];
      buttons.forEach((buttonClass) => {
        const button = document.createElement("button");
        button.classList.add(buttonClass);
        button.textContent = buttonClass.replace("-", " ");
        linkActions.appendChild(button);
      });

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
